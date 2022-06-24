import json
from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet


class SoftDeletionQuerySet(QuerySet):
    """
    Queryset to handle the bulk deletes that will bypass the 
    delete() method of objects ensuring our softdeletes 
    are always complied with.

    """

    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    """
    Manager for softDelete model, ensures that only files the user deems as not deleted
    are made visible to and can be manipulated by the user.

    """

    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    """
    An abstract model that will be inherited by all model to handle deletion of model 
    objects to prevent accidental perminent delete, all data will be deleted after 
    a speciied amount of time indicated to the user.

    """
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()

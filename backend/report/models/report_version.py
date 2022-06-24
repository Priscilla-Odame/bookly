from django.db import models
from app.models.Soft_deletion import SoftDeletionModel
from report.models.report import Report


class ReportVersion(SoftDeletionModel):
    
    def __str__(self) -> str:
        name = self.report.name
        last_modified = str(self.last_modified)
        if self.is_active:
            is_active = 'current'
        else:
            is_active = 'not current'
        return f'{name} - {is_active} - {last_modified}'

    last_modified = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    report = models.ForeignKey(
        Report,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )

    


from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ModelObjectField(serializers.Field):
    """
        This is used when doing bulk create/update. Since multiple instances share
        many of the same fk objects the objects are validated and queried first, then the request data
        is modified with the fk objects. This allows objects to be passed in to be validated.
    """

    def to_representation(self, value):
        return value.id

    def to_internal_value(self, data):
        return data


class CurrentProjectDefault(object):
    requires_context = True

    def __call__(self, serializer_field):
        try:
            self.user = serializer_field.context["request"].user

        except None:
            raise ValidationError("Created_by field empty")

        return self.user

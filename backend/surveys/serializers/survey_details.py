from rest_framework import serializers
from surveys.models.survey_details import SurveyDetails


class SurveyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyDetails
        fields = "__all__"
        read_only_fields = ('deleted_at',)

from rest_framework import serializers
from surveys.models.survey_progress import SurveyProgress


class SurveyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyProgress
        fields = "__all__"
        read_only_fields = ('deleted_at',)

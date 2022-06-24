from rest_framework import generics
from surveys.serializers.survey_progress import SurveyProgressSerializer
from surveys.models.survey_progress import SurveyProgress


class CreateSurveyProgressAPI(generics.CreateAPIView):
    serializer_class = SurveyProgressSerializer


class RetrieveSurveyProgressAPI(generics.RetrieveAPIView):
    serializer_class = SurveyProgressSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return SurveyProgress.objects.filter(user=user.id)


class UpdateSurveyProgressAPI(generics.UpdateAPIView):
    serializer_class = SurveyProgressSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return SurveyProgress.objects.filter(user=user.id)


class ListSurveyProgressAPI(generics.ListAPIView):
    serializer_class = SurveyProgressSerializer
    filterset_fields = ['user', 'survey', 'is_completed', 'is_current']

    def get_queryset(self):
        user = self.request.user
        return SurveyProgress.objects.filter(user=user.id)


class DestroySurveyProgressAPI(generics.DestroyAPIView):
    serializer_class = SurveyProgressSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return SurveyProgress.objects.filter(user=user.id)

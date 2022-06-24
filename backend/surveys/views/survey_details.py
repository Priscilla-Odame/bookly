from rest_framework import generics
from surveys.serializers.survey_details import SurveyDetailsSerializer
from surveys.models.survey_details import SurveyDetails
from projectapp.models.project import ProjectMember


class CreateSurveyDetailsAPI(generics.CreateAPIView):
    serializer_class = SurveyDetailsSerializer


class RetrieveSurveyDetailsAPI(generics.RetrieveAPIView):
    serializer_class = SurveyDetailsSerializer
    queryset = SurveyDetails.objects.all()
    lookup_field = 'id'


class UpdateSurveyDetailsAPI(generics.UpdateAPIView):
    serializer_class = SurveyDetailsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        project_ids = ProjectMember.objects.values('id').filter(user=user.id)
        return SurveyDetails.objects.filter(project__in=project_ids)


class ListSurveyDetailsAPI(generics.ListAPIView):
    serializer_class = SurveyDetailsSerializer
    filterset_fields = ['name', 'project']

    def get_queryset(self):
        user = self.request.user
        project_ids = ProjectMember.objects.values('id').filter(user=user.id)
        return SurveyDetails.objects.filter(project__in=project_ids)


class DestroySurveyDetailsAPI(generics.DestroyAPIView):
    serializer_class = SurveyDetailsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        project_ids = ProjectMember.objects.values('id').filter(user=user.id)
        return SurveyDetails.objects.filter(project__in=project_ids)

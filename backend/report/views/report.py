from rest_framework.response import Response
from report.serializers.report import ReportSerializer
from rest_framework import viewsets
from report.models import Report, ReportMemberVersion
from projectapp.models.project import ProjectMember


class ReportViewSet(viewsets.ModelViewSet):
    is_unread = None
    serializer_class = ReportSerializer

    def get_queryset(self,):
        projects = list()
        project_memberships = ProjectMember.objects.filter(user=self.request.user)
        for project_membership in project_memberships:
            projects.append(project_membership.project)
        return Report.objects.filter(project__in=projects)

    def get_unread_reports(self,):
        read_reports = ReportMemberVersion.objects.filter(member=self.request.user)
        versions = list()
        for read_report in read_reports:
            versions.append(read_report.report_version)
        results = self.get_queryset().exclude(reportversion__in=versions)
        return Response(ReportSerializer(results, many=True, context={'request': self.request}).data)

    def list(self, request, *args, **kwargs):
        for field in ('is_unread',):
            setattr(self, field, request.GET.get(field, None))
        if self.is_unread:
            return self.get_unread_reports()
        else:
            return super().list(request)
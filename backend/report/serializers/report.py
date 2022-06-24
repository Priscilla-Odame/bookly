from projectapp.models.project import Project
from rest_framework import serializers
from report.models.report import Report
from report.models.report_version import ReportVersion


class ReportSerializer(serializers.ModelSerializer):
    project = serializers.HyperlinkedRelatedField(
        view_name='retrieve_one_project',
        lookup_field='id',
        queryset=Project.objects.all()
    )
    class Meta:
        model = Report
        #fields = "__all__"
        exclude = ['deleted_at']


class ReportVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportVersion
        fields = "__all__"

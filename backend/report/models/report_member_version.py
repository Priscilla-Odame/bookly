from django.db import models
from app.models.Soft_deletion import SoftDeletionModel
from app.models.user import User
from .report_version import ReportVersion
from .report import Report


class ReportMemberVersion(SoftDeletionModel):

    def __str__(self):
        user_name = self.member.firstname+' '+self.member.othernames
        report_version = str(self.report_version)
        return f' {user_name} - {report_version} '

    member = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )

    report_version = models.ForeignKey(
        ReportVersion,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )


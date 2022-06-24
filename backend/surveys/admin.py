from django.contrib import admin

from app.admin_soft_deletion import SoftDeletionAdmin
from surveys.models.survey_details import SurveyDetails
from surveys.models.survey_progress import SurveyProgress 


class SurveyDetailsAdmin(SoftDeletionAdmin):
    list_display = ('id',
                    'name',
                    'description',
                    'question_count',
                    'published_at',
                    'survey_deadline',
                    'deleted_at',
                    'project'
                    )

class SurveyProgressAdmin(SoftDeletionAdmin):
    list_display = ('id',
                    'user',
                    'questions_completed',
                    'survey',
                    'is_completed',
                    'last_modified',
                    'is_current',
                    )

admin.site.register(SurveyDetails, SurveyDetailsAdmin)
admin.site.register(SurveyProgress, SurveyProgressAdmin)

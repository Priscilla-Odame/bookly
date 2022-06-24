from django.urls import path
from surveys.views.views import AllProjectSurveysAPI
from surveys.views.survey_details import CreateSurveyDetailsAPI, RetrieveSurveyDetailsAPI, UpdateSurveyDetailsAPI, ListSurveyDetailsAPI, DestroySurveyDetailsAPI
from surveys.views.survey_progress import CreateSurveyProgressAPI, RetrieveSurveyProgressAPI, UpdateSurveyProgressAPI, ListSurveyProgressAPI, DestroySurveyProgressAPI
urlpatterns = [

    # ----------------------------------survey details-------------------------------------#
    path(
        'project/all',
        AllProjectSurveysAPI.as_view(),
        name='all_project_surveys'
    ),

    path(
        'create',
        CreateSurveyDetailsAPI.as_view(),
        name='create_survey_details'
    ),

    path(
        '<id>',
        RetrieveSurveyDetailsAPI.as_view(),
        name='retrieve_survey_details'
    ),

    path(
        'update/<id>',
        UpdateSurveyDetailsAPI.as_view(),
        name='update_survey_details'
    ),

    path(
        '',
        ListSurveyDetailsAPI.as_view(),
        name='list_surveys'
    ),

    path(
        'remove/<id>',
        DestroySurveyDetailsAPI.as_view(),
        name='remove_survey'
    ),
    # -----------------------------------------------survey progress------------------------------#
    path(
        'progress/create',
        CreateSurveyProgressAPI.as_view(),
        name='create_survey_Progress'
    ),

    path(
        'progress/<id>',
        RetrieveSurveyProgressAPI.as_view(),
        name='retrieve_survey_Progress'
    ),

    path(
        'progress/update/<id>',
        UpdateSurveyProgressAPI.as_view(),
        name='update_survey_Progress'
    ),

    path(
        'progress/',
        ListSurveyProgressAPI.as_view(),
        name='list_surveys_Progress'
    ),

    path(
        'progress/remove/<id>',
        DestroySurveyProgressAPI.as_view(),
        name='remove_survey_Progress'
    ),

]

from django.urls import path, include
from app.views.user import RegisterAPI, LoginAPI, VerifyEmail, ValidateEmailView, ListAllCompanyMembersAPI
from app.views.default import APIRoot
from app.views.project_file_upload import CreateProjectFileUploadAPIBeta, CreateProjectFileUploadAPI, ListProjectFileUploadsAPI, RetrieveProjectFileUploadDetailsAPI, DeleteProjectUploadedFileAPI, UpdateProjectUploadedFileAPI
from app.views.company_file_upload import CreateCompanyFileUploadAPIBeta, CreateCompanyFileUploadAPI, ListCompanyFileUploadsAPI, RetrieveCompanyFileUploadDetailsAPI, DeleteCompanyUploadedFileAPI, UpdateCompanyUploadedFileAPI, CreateCompanyFileUploadView
from app.views.company import CreateCompanyAPI, UpdateCompanyAPI, RetrieveCompanyAPI, ListCompanyAPI, DeleteCompanyAPI, ListCompanyNamesAPI
from app.views.password_reset import PasswordTokenCheckAPI, RequestPasswordEmailReset, SetNewPasswordAPI
from projectapp.views.project_report import GetEmbeddedReportView
from app.views.oauth import OAuthAPI, CompanyWhitelistAPI
from app.views.company_directory_upload import CreateCompanyDirectoryUploadAPI
from app.views.dtale import data_profile_html, data_profile_json
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'createfile/upload', CreateCompanyFileUploadView, 'create-file-upload')

urlpatterns = [
    path('api/', include(router.urls)),
    path(
        '',
        APIRoot.as_view(),
        name='api_root'
    ),

    path(
        'api/user/login',
        LoginAPI.as_view(),
        name='login'
    ),

    path(
        'api/user/login/oauth',
        OAuthAPI.as_view(),
        name='oauth'
    ),

    path(
        'api/user/signup',
        RegisterAPI.as_view(),
        name='signup'
    ),

    path(
        'api/user/verify_email/<uidb64>/<token>',
        VerifyEmail.as_view(),
        name='verify_email'
    ),

    path(
        'api/email/',
        ValidateEmailView.as_view(),
        name='email'
    ),

    path
    (
        "api/fileupload/project/create/beta",
        CreateProjectFileUploadAPIBeta.as_view(),
        name='create_project_file_upload_beta'
    ),

    path
    (
        "api/fileupload/project/create",
        CreateProjectFileUploadAPI.as_view(),
        name='create_project_file_upload'
    ),

    path
    (
        "api/fileuploads/project/",
        ListProjectFileUploadsAPI.as_view(),
        name='list_project_file_uploads'
    ),

    path
    (
        "api/fileupload/project/<pk>",
        RetrieveProjectFileUploadDetailsAPI.as_view(),
        name='list_one_project_file_upload'
    ),

    path
    (
        "api/fileupload/update/project/<pk>",
        UpdateProjectUploadedFileAPI.as_view(),
        name='update_uploaded_project_file'
    ),

    path
    (
        "api/fileupload/delete/project/<pk>",
        DeleteProjectUploadedFileAPI.as_view(),
        name='delete_uploaded_project_file'
    ),

    path
    (
        "api/fileupload/create/beta",
        CreateCompanyFileUploadAPIBeta.as_view(),
        name='create_file_upload_beta'
    ),


    path
    (
        "api/fileupload/create",
        CreateCompanyFileUploadAPI.as_view(),
        name='create_file_upload'
    ),

    path
    (
        "api/fileuploads",
        ListCompanyFileUploadsAPI.as_view(),
        name='list_file_uploads'
    ),

    path
    (
        "api/fileupload/<pk>",
        RetrieveCompanyFileUploadDetailsAPI.as_view(),
        name='list_one_file_upload'
    ),

    path
    (
        "api/fileupload/update/<pk>",
        UpdateCompanyUploadedFileAPI.as_view(),
        name='update_uploaded_file'
    ),

    path
    (
        "api/fileupload/delete/<pk>",
        DeleteCompanyUploadedFileAPI.as_view(),
        name='delete_uploaded_file'
    ),

    path
    (
        "api/directory_upload/create",
        CreateCompanyDirectoryUploadAPI.as_view(),
        name='create_company_directory_upload'
    ),

    path
    (
        "api/company/create",
        CreateCompanyAPI.as_view(),
        name='create_company'
    ),

    path
    (
        "api/companies",
        ListCompanyAPI.as_view(),
        name='List_companies'
    ),

    path
    (
        "api/company/<company_id>",
        RetrieveCompanyAPI.as_view(),
        name='view_company'
    ),

    path
    (
        "api/company/<company_id>/update",
        UpdateCompanyAPI.as_view(),
        name='update_company'
    ),

    path
    (
        "api/company/<company_id>/delete",
        DeleteCompanyAPI.as_view(),
        name='delete_company'
    ),

    path
    (
        "api/companystaff",
        ListAllCompanyMembersAPI.as_view(),
        name='list_company_members'
    ),

    path
    (
        "api/companynames",
        ListCompanyNamesAPI.as_view(),
        name='list_all_company_names'
    ),

    path
    (
        'api/password-reset/<uidb64>/<token>',
        PasswordTokenCheckAPI.as_view(),
        name='password_reset_confirm'
    ),

    path
    (
        'api/request_password_reset',
        RequestPasswordEmailReset.as_view(),
        name='password_reset_request'
    ),

    path
    (
        "api/password_reset_complete",
        SetNewPasswordAPI.as_view(),
        name="complete_password_reset"
    ),

    path
    (
        "api/company_whitelist",
        CompanyWhitelistAPI.as_view(),
        name="company_whitelist"
    ),
    path('api/profile2json', data_profile_json, name='profile2json'),
    path('api/profile2html', data_profile_html, name='profile2html'),

]

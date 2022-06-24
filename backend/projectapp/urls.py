from django.urls import path
from app.views.default import APIRoot
from projectapp.views.project_dashboard import ListCreateProjectDashboardsAPI, ProjectDashboardAPI
from projectapp.views.project_member import ProjectMemberAPI, ProjectMemberRoleAPI, CreateProjectMemberAPI, UpdateProjectMemberAPI, MemberApproveRejectProject
from projectapp.views.project import CreateProjectAPI, ListProjectAPI, DeleteProjectAPI, UpdateProjectAPI, RetrieveProjectAPI
from projectapp.views.project_report import GetEmbeddedReportView
from projectapp.views.search import SearchResultsView, HomePageView
from projectapp.views.invites import PendingInvitationsView

urlpatterns = [
    path(
        '',
        APIRoot.as_view(),
        name='api_root'
    ),
    path(
        'api/project/create',
        CreateProjectAPI.as_view(),
        name='create_project'
    ),

    path(
        'api/projects',
        ListProjectAPI.as_view(),
        name='list_projects'
    ),

    path
    (
        'api/project/<id>',
        RetrieveProjectAPI.as_view(),
        name='retrieve_one_project'
    ),

    path
    (
        'api/project/<id>/update',
        UpdateProjectAPI.as_view(),
        name='update_project'
    ),

    path
    (
        'api/project/<id>/delete',
        DeleteProjectAPI.as_view(),
        name='delete_project'
    ),

    path
    (
        "api/dashboards/list_create_dashboards",
        ListCreateProjectDashboardsAPI.as_view(),
        name="list_create_dashboards"
    ),

    path
    (
        "api/dashboard/<id>",
        ProjectDashboardAPI.as_view(),
        name='get_post_delete_put_patch_project_dashboard_'
    ),

    path
    (
        "api/project/members/create",
        CreateProjectMemberAPI.as_view(),
        name='create_project_members'
    ),

    path
    (
        "api/project/<project_id>/members/update",
        UpdateProjectMemberAPI.as_view(),
        name='update_project_members'
    ),

    path
    (
        "api/project/member/<id>",
        ProjectMemberAPI.as_view(),
        name='get_delete_project_member'
    ),

    path
    (
        "api/create_project_member_role",
        ProjectMemberRoleAPI.as_view(),
        name='create_project_member_role'
    ),
   path
    (
        'api/search',
        SearchResultsView.as_view(),
        name='search_results'
    ),

    path
    (
        'api/typesearch',
        HomePageView.as_view(),
        name='home'
    ),
    
    path(
        'api/pending_invites',
        PendingInvitationsView.as_view(),
        name='all_pending_invites'
    ),
    path(
        'api/acceptinvite/<uidb64>/<token>/<id>',
        MemberApproveRejectProject.as_view(),
        name='acceptinvite'
    )
] 
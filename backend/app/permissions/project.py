from rest_framework.permissions import SAFE_METHODS, BasePermission


class ProjectPermission(BasePermission):
    """
    A permission class for the project member role
    """
    message = "You must be the owner of this object or an admin to perform this action"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHOD:
            return True

        projectMember = ProjectMember.objects.get(
            user=request.user, project=obj.project,)
        isAdmin = projectMember.project_member_role.is_admin

        return isAdmin

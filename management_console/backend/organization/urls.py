from rest_framework import routers
from django.urls import path, include
from organization.views import OrganizationStatusViewSet, ContactStatusViewSet, AdministratorViewSet,  AdministratorStatusViewSet, OrganizationViewSet, ContactViewSet, ContactRoleViewSet
from organization.views.staff import RetrieveAllStaffViewSet
from organization.views.profile import ProfileViewSet
from auths.views import LoginViewSet

router = routers.DefaultRouter()
router.register(r'administrator', AdministratorViewSet,'administrators')
router.register(r'administrator-status',  AdministratorStatusViewSet, 'administrator_status')
router.register(r'organization', OrganizationViewSet,'organizations')
router.register(r'contact', ContactViewSet, 'contacts')
router.register(r'contact-role', ContactRoleViewSet, 'contact_roles')
router.register(r'contact-status', ContactStatusViewSet, 'contact_status')
router.register(r'organization-status', OrganizationStatusViewSet, 'organization_status')
router.register(r'staff-members', RetrieveAllStaffViewSet, 'staff_members')
router.register(r'profile', ProfileViewSet, 'profile')
router.register(r'login', LoginViewSet, 'login')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api/login', LoginViewSet.as_view({'post':'create'}), name ='login')
# ]
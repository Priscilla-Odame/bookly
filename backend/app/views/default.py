from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics, permissions


class APIRoot(generics.GenericAPIView):
    """ Click on any of the links below to view the resources """

    def get(self, request):
        return Response({
            'Register endpoint': reverse('signup'),
            'Login endpoint': reverse('login'),
            'Create Project endpoint': reverse('create_project'),
            'List all projects endpoint': reverse('list_projects'),
            'Retrieve a specific project endpoint': reverse('retrieve_one_project', kwargs={'id': id}),
            'Update the details of a project endpoint': reverse('update_project', kwargs={'id': id}),
            'Delete a project endpoint': reverse('delete_project', kwargs={'id': id}),
            'Create one or more project members': reverse('create_project_members'),
            'Perform Get, Patch, Put and Delete operations on project members': reverse('get_delete_project_member', kwargs={'id': id}),
            'Create or list project dashboards endpoint': reverse('list_create_dashboards'),
            'Perform Get, Post, Put, Patch & Delete operations on project dashboard endpoint': "/api/dashboard/<id>",
            'Upload a file endpoint': reverse('create_file_upload'),
            'List all uploaded files endpoint': reverse('list_file_uploads'),
            'Read details of a uploaded file': reverse('list_one_file_upload', kwargs={'pk': id}),
            'Create a company': reverse('create_company'),
            'View specified company details': reverse('view_company', kwargs={'company_id': id}),
            'update a specified company details': reverse('update_company', kwargs={'company_id': id}),

        })

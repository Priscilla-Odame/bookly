from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from app.serializers.company import CompanySerializer, CompanyNamesSerializer
from app.models.company import Company


class CreateCompanyAPI(generics.CreateAPIView):
    """
    Endpoint to create a company
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = CompanySerializer
    queryset = Company.objects


class ListCompanyAPI(generics.ListAPIView):
    """
    Endpoint to list all companies
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = CompanySerializer
    queryset = Company.objects


class RetrieveCompanyAPI(generics.RetrieveAPIView):
    """
    Endpoint to view specified company details
    """
    serializer_class = CompanySerializer
    queryset = Company.objects
    lookup_field = 'company_id'


class UpdateCompanyAPI(generics.UpdateAPIView):
    """
    Endpoint to update specified company details
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = CompanySerializer
    queryset = Company.objects
    lookup_field = 'company_id'


class DeleteCompanyAPI(generics.DestroyAPIView):
    """
    Endpoint to delete specified company
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = CompanySerializer
    queryset = Company.objects
    lookup_field = 'company_id'


class ListCompanyNamesAPI(generics.GenericAPIView):
    """
    Endpoint to list all company names and Id

{
    "names": [
        "GetInnotized"
    ]
}
    """
    permission_classes = (permissions.AllowAny,)

    serializer_class = CompanyNamesSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)

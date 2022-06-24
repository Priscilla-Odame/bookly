from django.http import HttpResponse
from rest_framework.views import APIView
import json
from rest_framework.response import Response


class AllProjectSurveysAPI(APIView):

    def get(self, request):
        dummy_data = [
            {
                "id": "1",
                "name": "Telefonica - Survey 1",
                "description": "Description of Telefonica - Survey 1",
                "project": "http://localhost:8000/projects/api/project/1",
                "completion_deadline": "15-03-2021 9:30 am",
                "completion_status" : "50%"
            },
            {
                "id": "2",
                "name": "Telefonica - Survey 2",
                "description": "Description of Telefonica - Survey 2",
                "project": "http://localhost:8000/projects/api/project/1",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "30%"
            },
            {
                "id": "3",
                "name": "Telefonica - Survey 3",
                "description": "Description Of Telefonica - Survey 3",
                "project": "http://localhost:8000/projects/api/project/1",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "20%"
            },
            {
                "id": "4",
                "name": "Telefonica - Survey 4",
                "description": "Description of Telefonica - Survey 4",
                "project": "http://localhost:8000/projects/api/project/1",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "10%"
            },
            {
                "id": "5",
                "name": "Lafarge - Survey 1",
                "description": "Description of Lafarge - Survey 1",
                "project": "http://localhost:8000/projects/api/project/2",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "60%"
            },
            {
                "id": "6",
                "name": "Lafarge - Survey 2",
                "description": "Description of Lafarge - Survey 2",
                "project": "http://localhost:8000/projects/api/project/2",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "30%"
            },
            {
                "id": "7",
                "name": "Lafarge - Survey 3",
                "description": "Description of Lafarge - Survey 3",
                "project": "http://localhost:8000/projects/api/project/2",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "25%"
            },
            {
                "id": "8",
                "name": "TKE - Survey 1",
                "description": "Description of TKE - Survey 1",
                "project": "http://localhost:8000/projects/api/project/3",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "90%"
            },
            {
                "id": "9",
                "name": "TKE - Survey 2",
                "description": "Description Of TKE - Survey 2",
                "project": "http://localhost:8000/projects/api/project/3",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "10%"
            },
            {
                "id": "10",
                "name": "TKE - Survey 3",
                "description": "Description Of TKE - Survey 3",
                "project": "http://localhost:8000/projects/api/project/3",
                "completion_deadline": "21-03-2021 05:00 pm",
                "completion_status" : "30%"
            }
        ]
        return Response(dummy_data)

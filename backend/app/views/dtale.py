import os
import pandas as pd
from pandas_profiling import ProfileReport
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view


@api_view(['GET'])
def data_profile_json(request):
    """
    Return a JSON object with the data profile of the dataset provided in the request dataset can be in only excel or csv format.
    """
    fileurl = os.path.join(os.path.abspath(os.curdir), 'mediafiles/File/salary.csv')
    # url = os.path.dirname(__file__)
    # url = 'https://raw.githubusercontent.com/werowe/logisticRegressionBestModel/master/ct1.json'
    data = pd.read_csv(fileurl, sep=',', encoding='utf-8')
    profile = ProfileReport(data, title="PushInsight Data Profiling Report")
    return HttpResponse(profile.to_json(), content_type="application/json")


@api_view(['GET'])
def data_profile_html(request):
    """
    Return a HTML object with the data profile of the dataset provided in the request, dataset can be in only excel or csv format.
    """
    fileurl = os.path.join(os.path.abspath(os.curdir), 'mediafiles/File/salary.csv')
    # url = 'https://raw.githubusercontent.com/werowe/logisticRegressionBestModel/master/ct1.json'
    # data = pd.read_csv("/pushInsights_dev/app/views/salary.csv", sep=',', encoding='utf-8')
    profile = ProfileReport(fileurl, title="PushInsight Data Profiling Report")
    return HttpResponse(profile.to_html(), content_type="text/html")











# from dtale.views import startup
# def index(request):
#     return HttpResponse("""
#         <h1>Django/Flask Hybrid</h1>
#         <span>Generate sample dataframe in D-Tale by clicking this </span><a href="/create-df">link</a>
#     """)


# def create_df(request):
#     df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6]))
#     instance = startup(data=df, ignore_duplicate=True)

#     resp = redirect(f"/pidata/dtale/main/{instance._data_id}")
#     return resp

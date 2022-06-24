import app.services.pbiembedservice as emb_report
from rest_framework.response import Response
from rest_framework import generics


class GetEmbeddedReportView(generics.RetrieveAPIView):

    def get(self, request):
        report_id = 'c97456ee-23ed-4837-8622-c192b21c5eee'
        workspace_id = '04b92991-8c5a-4138-9e4f-32a33b2fb791'
        response = emb_report.get_embed_params_for_single_report(
            workspace_id, report_id)

        return Response(response)

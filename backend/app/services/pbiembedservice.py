# from services.aadservice import AadService
# from models.reportconfig import ReportConfig
# from models.embedtoken import EmbedToken
# from models.embedconfig import EmbedConfig
# from models.embedtokenrequestbody import EmbedTokenRequestBody
from app.utils import Utils
import requests
import msal
import json


def get_embed_params_for_single_report(workspace_id, report_id, additional_dataset_id=None):
    '''Get embed params for a report and a workspace

    Args:
        workspace_id (str): Workspace Id
        report_id (str): Report Id
        additional_dataset_id (str, optional): Dataset Id different than the one bound to the report. Defaults to None.

    Returns:
        EmbedConfig: Embed token and Embed URL
    '''
    report_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/reports/{report_id}'
    api_response = requests.get(report_url, headers=get_request_header())

    if api_response.status_code != 200:
        raise Exception(
            f'Error while retrieving Embed URL\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')
    # if api_response.status_code != 200:
    #     raise Exception(
    #         f'Error while retrieving Embed URL\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')

    api_response = json.loads(api_response.text)
    report_config_params = dict()
    report_config_params.update([('reportId', api_response['id'])])
    report_config_params.update([('reportName', api_response['name'])])
    report_config_params.update([('embedUrl', api_response['embedUrl'])])
    report_config_params.update([('datasetId', None)])
    report_config = list()
    report_config.append(report_config_params)
    dataset_ids = [api_response['datasetId']]
    if additional_dataset_id is not None:
        dataset_ids.append(additional_dataset_id)
    embed_token = get_embed_token_for_single_report_single_workspace(
        report_id, dataset_ids, workspace_id)
    embed_config = {
        'token_id': embed_token['tokenId'],
        'access_token': embed_token['token'],
        'token_expiry': embed_token['expiration'],
        'report_config': report_config
    }
    return embed_config


def get_embed_token_for_single_report_single_workspace(report_id, dataset_ids, target_workspace_id=None):
    '''Get Embed token for single report, multiple datasets, and an optional target workspace

    Args:
        report_id (str): Report Id
        dataset_ids (list): Dataset Ids
        target_workspace_id (str, optional): Workspace Id. Defaults to None.

    Returns:
        EmbedToken: Embed token
    '''
    request_body = dict()
    request_body.update(
        [('datasets', list()), ('reports', list()), ('targetWorkspaces', list())])
    for dataset_id in dataset_ids:
        request_body['datasets'].append({'id': dataset_id})
    request_body['reports'].append({'id': report_id})
    if target_workspace_id is not None:
        request_body['targetWorkspaces'].append({'id': target_workspace_id})
    embed_token_api = 'https://api.powerbi.com/v1.0/myorg/GenerateToken'
    api_response = requests.post(embed_token_api, data=json.dumps(
        request_body), headers=get_request_header())

    if api_response.status_code != 200:
        raise Exception(
            f'Error while retrieving Embed token\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')
    # if api_response.status_code != 200:
    #     raise Exception(
    #         f'Error while retrieving Embed URL\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')
    return json.loads(api_response.text)


def get_request_header():
    '''Get Power BI API request header

    Returns:
        Dict: Request header
    '''
    return {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + get_access_token()}


def get_access_token():
    '''Generates and returns Access token

    Returns:
        string: Access token
    '''
    client_id = '8e0afafc-4089-4e02-9cd1-66974f97cba9'
    tenant_id = '501c5854-0570-4876-8793-fa427b522557'
    client_secret = 'JYdC5x1hh63MaWT6jjeD2.~G9__fZ6HtwW'
    authority = 'https://login.microsoftonline.com/organizations'
    authority = authority.replace('organizations', tenant_id)
    scope = ['https://analysis.windows.net/powerbi/api/.default']
    clientapp = msal.ConfidentialClientApplication(
        client_id, client_credential=client_secret, authority=authority)
    response = clientapp.acquire_token_for_client(scopes=scope)
    try:
        return response['access_token']
    except KeyError:
        raise Exception(response['error_description'])
    except Exception as ex:
        raise Exception('Error retrieving Access token\n' + str(ex))


# class PbiEmbedService:

#     def get_embed_params_for_single_report(self, workspace_id, report_id, additional_dataset_id=None):
#         '''Get embed params for a report and a workspace
#         Args:
#             workspace_id (str): Workspace Id
#             report_id (str): Report Id
#             additional_dataset_id (str, optional): Dataset Id different than the one bound to the report. Defaults to None.
#         Returns:
#             EmbedConfig: Embed token and Embed URL
#         '''

#         report_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/reports/{report_id}'
#         api_response = requests.get(
#             report_url, headers=self.get_request_header())

        # if api_response.status_code != 200:
        #     Utils.custom_exception_handler(api_response.status_code,
        #                                    description=f'Error while retrieving Embed URL\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')
#             # abort(api_response.status_code,
#             #       description=f'Error while retrieving Embed URL\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')

#         api_response = json.loads(api_response.text)
#         report = ReportConfig(
#             api_response['id'], api_response['name'], api_response['embedUrl'])
#         dataset_ids = [api_response['datasetId']]

#         # Append additional dataset to the list to achieve dynamic binding later
#         if additional_dataset_id is not None:
#             dataset_ids.append(additional_dataset_id)

#         embed_token = self.get_embed_token_for_single_report_single_workspace(
#             report_id, dataset_ids, workspace_id)
#         embed_config = EmbedConfig(
#             embed_token.tokenId, embed_token.token, embed_token.tokenExpiry, [report.__dict__])
#         return json.dumps(embed_config.__dict__)

#     def get_embed_params_for_multiple_reports(self, workspace_id, report_ids, additional_dataset_ids=None):
#         '''Get embed params for multiple reports for a single workspace
#         Args:
#             workspace_id (str): Workspace Id
#             report_ids (list): Report Ids
#             additional_dataset_ids (list, optional): Dataset Ids which are different than the ones bound to the reports. Defaults to None.
#         Returns:
#             EmbedConfig: Embed token and Embed URLs
#         '''

#         # Note: This method is an example and is not consumed in this sample app

#         dataset_ids = []

#         # To store multiple report info
#         reports = []

#         for report_id in report_ids:
#             report_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/reports/{report_id}'
#             api_response = requests.get(
#                 report_url, headers=self.get_request_header())

#             if api_response.status_code != 200:
#                 Utils.custom_exception_handler(api_response.status_code,
#                                                description=f'Error while retrieving Embed URL\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')

#             api_response = json.loads(api_response.text)
#             report_config = ReportConfig(
#                 api_response['id'], api_response['name'], api_response['embedUrl'])
#             reports.append(report_config.__dict__)
#             dataset_ids.append(api_response['datasetId'])

#         # Append additional dataset to the list to achieve dynamic binding later
#         if additional_dataset_ids is not None:
#             dataset_ids.extend(additional_dataset_ids)

#         embed_token = self.get_embed_token_for_multiple_reports_single_workspace(
#             report_ids, dataset_ids, workspace_id)
#         embed_config = EmbedConfig(
#             embed_token.tokenId, embed_token.token, embed_token.tokenExpiry, reports)
#         return json.dumps(embed_config.__dict__)

#     def get_embed_token_for_single_report_single_workspace(self, report_id, dataset_ids, target_workspace_id=None):
#         '''Get Embed token for single report, multiple datasets, and an optional target workspace
#         Args:
#             report_id (str): Report Id
#             dataset_ids (list): Dataset Ids
#             target_workspace_id (str, optional): Workspace Id. Defaults to None.
#         Returns:
#             EmbedToken: Embed token
#         '''

#         request_body = EmbedTokenRequestBody()

#         for dataset_id in dataset_ids:
#             request_body.datasets.append({'id': dataset_id})

#         request_body.reports.append({'id': report_id})

#         if target_workspace_id is not None:
#             request_body.targetWorkspaces.append({'id': target_workspace_id})

#         # Generate Embed token for multiple workspaces, datasets, and reports. Refer https://aka.ms/MultiResourceEmbedToken
#         embed_token_api = 'https://api.powerbi.com/v1.0/myorg/GenerateToken'
#         api_response = requests.post(embed_token_api, data=json.dumps(
#             request_body.__dict__), headers=self.get_request_header())

        # if api_response.status_code != 200:
        #     Utils.custom_exception_handler(api_response.status_code,
        #                                    description=f'Error while retrieving Embed token\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')

#         api_response = json.loads(api_response.text)
#         embed_token = EmbedToken(
#             api_response['tokenId'], api_response['token'], api_response['expiration'])
#         return embed_token

#     def get_embed_token_for_multiple_reports_single_workspace(self, report_ids, dataset_ids, target_workspace_id=None):
#         '''Get Embed token for multiple reports, multiple dataset, and an optional target workspace
#         Args:
#             report_ids (list): Report Ids
#             dataset_ids (list): Dataset Ids
#             target_workspace_id (str, optional): Workspace Id. Defaults to None.
#         Returns:
#             EmbedToken: Embed token
#         '''

#         # Note: This method is an example and is not consumed in this sample app

#         request_body = EmbedTokenRequestBody()

#         for dataset_id in dataset_ids:
#             request_body.datasets.append({'id': dataset_id})

#         for report_id in report_ids:
#             request_body.reports.append({'id': report_id})

#         if target_workspace_id is not None:
#             request_body.targetWorkspaces.append({'id': target_workspace_id})

#         # Generate Embed token for multiple workspaces, datasets, and reports. Refer https://aka.ms/MultiResourceEmbedToken
#         embed_token_api = 'https://api.powerbi.com/v1.0/myorg/GenerateToken'
#         api_response = requests.post(embed_token_api, data=json.dumps(
#             request_body.__dict__), headers=self.get_request_header())

#         if api_response.status_code != 200:
#             Utils.custom_exception_handler(api_response.status_code,
#                                            description=f'Error while retrieving Embed token\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')

#         api_response = json.loads(api_response.text)
#         embed_token = EmbedToken(
#             api_response['tokenId'], api_response['token'], api_response['expiration'])
#         return embed_token

#     def get_embed_token_for_multiple_reports_multiple_workspaces(self, report_ids, dataset_ids, target_workspace_ids=None):
#         '''Get Embed token for multiple reports, multiple datasets, and optional target workspaces
#         Args:
#             report_ids (list): Report Ids
#             dataset_ids (list): Dataset Ids
#             target_workspace_ids (list, optional): Workspace Ids. Defaults to None.
#         Returns:
#             EmbedToken: Embed token
#         '''

#         # Note: This method is an example and is not consumed in this sample app

#         request_body = EmbedTokenRequestBody()

#         for dataset_id in dataset_ids:
#             request_body.datasets.append({'id': dataset_id})

#         for report_id in report_ids:
#             request_body.reports.append({'id': report_id})

#         if target_workspace_ids is not None:
#             for target_workspace_id in target_workspace_ids:
#                 request_body.targetWorkspaces.append(
#                     {'id': target_workspace_id})

#         # Generate Embed token for multiple workspaces, datasets, and reports. Refer https://aka.ms/MultiResourceEmbedToken
#         embed_token_api = 'https://api.powerbi.com/v1.0/myorg/GenerateToken'
#         api_response = requests.post(embed_token_api, data=json.dumps(
#             request_body.__dict__), headers=self.get_request_header())

#         if api_response.status_code != 200:
#             Utils.custom_exception_handler(api_response.status_code,
#                                            description=f'Error while retrieving Embed token\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')

#         api_response = json.loads(api_response.text)
#         embed_token = EmbedToken(
#             api_response['tokenId'], api_response['token'], api_response['expiration'])
#         return embed_token

#     def get_request_header(self):
#         '''Get Power BI API request header
#         Returns:
#             Dict: Request header
#         '''

#         return {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + AadService.get_access_token()}

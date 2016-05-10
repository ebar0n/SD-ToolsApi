import requests
from requests.auth import HTTPBasicAuth
import json


class TogglClientApi:

    api_token = None
    api_base_url = 'https://www.toggl.com/api/v8/'
    headers = {'content-type': 'application/json'}

    def __init__(self, api_token=None, workspace=None):
        self.api_token = api_token
        self.workspace = workspace

    def create_project(self, name):
        url = self.api_base_url + 'projects'
        params = {
            "project":{
                "name":name,
                "wid":self.workspace,
                "is_private":False
            }
        }
        response = requests.post(
            url,
            headers=self.headers,
            data=json.dumps(params),
            auth=HTTPBasicAuth(self.api_token, 'api_token')
        )
        return response

    def get_workspace_projects(self):
        url = self.api_base_url + 'workspaces/{}/projects'.format(self.workspace)
        response = requests.get(
            url,
            headers=self.headers,
            auth=HTTPBasicAuth(self.api_token, 'api_token')
        )
        return response







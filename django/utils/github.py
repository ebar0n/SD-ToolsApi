import requests


class GithubClientApi:

    access_token = None
    api_base_url = 'https://api.github.com/user/'
    headers = {'content-type': 'application/json'}

    def __init__(self, access_token=None):
        self.access_token = access_token

    def get_repos(self):
        url = self.api_base_url + 'repos'
        params = {
            'access_token': self.access_token
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response

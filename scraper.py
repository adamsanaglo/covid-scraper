import requests
import json

API_KEY = "get_ur_own"
PROJECT_TOKEN = "get_ur_own"
RUN_TOKEN = "get_ur_own"


class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {"api key": self.api_key}
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
                                params={"api_key": API_KEY})
        self.data = json.loads(response.text)

    def get_total_cases(self):
        data = self.data['total']
        for content in data:
            return content["CVCases"]

    def get_total_deaths(self):
        data = self.data['total']
        for content in data:
            return content["Deaths"]

    def get_country_info(self, country, info):
        data = self.data['countries']
        for content in data:
            if content["name"].lower() == country.lower():
                return content[info]

            else:
                return "N/A"

    def get_total_recoveries(self):
        data = self.data['total']
        for content in data:
            return content["Recovered"]


data = Data(API_KEY, PROJECT_TOKEN)
print(data.get_total_cases())
print(data.get_country_info("USA", "recoveries"))
import requests

from basic_class import BasicClass

LINK = 'https://api.hh.ru/vacancies'

class HH_API(BasicClass):

    def get_request(self, keyword: str, count: int):
        pages = int(count/1)
        params = {
            'text': keyword,
            'page': 0,
            'per_page': 1
        }
        data = []
        for page in range(pages):
            params.update({'page': page})
            response = requests.get(LINK, params=params)
            data += response.json()['items']

        return data



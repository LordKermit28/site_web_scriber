import os
import requests
from basic_class import BasicClass

LINK = "https://api.superjob.ru/2.0/vacancies"

class SuperJobAPI(BasicClass):
    """Класс для скрайбинга сайта SJ
    возвращает список вакансий
    вакансия в json формате"""

    def get_request(self, keyword: str, count: int):
        pages = int(count / 1)
        api_key = os.getenv('X_Api_App_Id')  # Получаем значение переменной окружения
        headers = {'X-Api-App-Id': api_key}
        params = {
            'keyword': keyword,
            'page': 0,
            'count': 1
        }
        data = []
        for page in range(pages):
            params.update({'page': page})
            response = requests.get(LINK, params=params, headers=headers)
            data += response.json().get('objects', [])

        return data


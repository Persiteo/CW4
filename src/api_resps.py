from abc import ABC, abstractmethod
import requests
import os


class API(ABC):
    """
    Абстрактный базовый класс для работы с API.
    """
    @abstractmethod
    def get_response(self):
        pass


class HeadHunter(API):
    """Формирование запроса/получение ответа от """
    def __init__(self, keyword: str):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.params = {'text': keyword, 'per_page': 100}

    def get_response(self):
        response = requests.get('https://api.hh.ru/vacancies', headers=self.header, params=self.params)
        return response.json()['items']


class SuperJob(API):
    """Формирование запроса/получение ответа от SuperJob"""
    def __init__(self, keyword: str):
        self.header = {'X-Api-App-Id': os.getenv('SJ_API_KEY')}
        self.params = {'keyword': keyword, 'per0_page': 100}

    def get_response(self):
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=self.header, params=self.params)
        if response.status_code == 200:
            return response.json()['objects']
        else:
            print(response.status_code)

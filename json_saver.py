import json
import os


class JsonSaver:
    """Класс для работы с файлами
    сохраняет, выводит и удаляет вакансии"""
    def __init__(self, filename):
        self.__filename = filename

    @property
    def file(self):
        return self.__filename

    @file.setter
    def file(self, name):
        self.__filename = name

    def __str__(self):
        with open(self.__filename, 'r', encoding='utf-8') as f:
            data = f.readlines()
            objects = [json.loads(obj) for obj in data]
            return str(objects)

    def writer_data(self, data): #сохраняет вакансию
        with open(self.__filename, 'a', encoding='utf-8') as f:
            json.dump(data.to_dict(), f, ensure_ascii=False)
            f.write('\n')#разделяет сохраннёные вакансии пустой строкой


    def get_vacancies(self, keyword): #выводит вакансии, если пустая строка, то выведет все, если есть ключевое слово, то выведет по нему
        vacancies = []
        with open( self.__filename, 'r', encoding='utf-8') as f:

            for item in f:
                vacancy = json.loads(item)
                if keyword is None or keyword in vacancy.get('job_name', ''):
                    vacancies.append(vacancy)
        return vacancies

    def delete_vacancy(self, keyword):# удаляет вакансии по ключевому слову, или удаляют все при введении пустой строки

        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = [json.loads(line) for line in file if line.strip()]


        if keyword == '':
            updated_data = []
        else:
            updated_data = [item for item in data if keyword not in item['job_name']]


        with open(self.__filename, 'w', encoding='utf-8') as file:
            for item in updated_data:
                json.dump(item, file, ensure_ascii=False)
                file.write('\n')

















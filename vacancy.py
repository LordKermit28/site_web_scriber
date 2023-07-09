from urllib.parse import quote

class Vacancy:
    def __init__(self, job_name: str, salary: int, description: int, link: str, salary_currency: str):
        self.job_name = job_name
        self.salary = salary
        self.salary_currency = salary_currency
        self.description = description
        self.link = link

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary

    def __str__(self):
        return f'Вакансия: {self.job_name}\n'\
               f'Описание вакансии: {self.description}\n'\
               f'Заработная плата: {self.salary} {self.salary_currency}\n'\
               f'Ссылка на вакансию: {self.link}\n'

    def to_dict(self):
        return {
            'job_name': self.job_name,
            'salary': self.salary,
            'salary_currency': self.salary_currency,
            'description': self.description,
            'link': quote(self.link)}



from hh import HH_API
from vacancy import Vacancy
from superjobapi import SuperJobAPI
from utils import sort_vacancies
from json_saver import JsonSaver

# создает экземпляры класса Vacancy вакансий полученных с сайта hh
def hh_vacancy():
    hh = HH_API()
    hh_vacancies = hh.get_request(keyword, count)

    vacancies = [Vacancy(
        job_name=item['name'],
        salary=item['salary']['from'] if item['salary'] else 0,
        salary_currency=item['salary']['currency'] if item['salary']else None,
        description=item['snippet']['responsibility'],
        link=item['alternate_url']
    )
        for item in hh_vacancies
    ]

    sorted_vacancies = sort_vacancies(vacancies)
    return sorted_vacancies


# создает экземпляры класса Vacancy вакансий полученных с сайта superjob
def sj_vacancy():

    sj = SuperJobAPI()
    sj_vacancies = sj.get_request(keyword, count)
    vacancies = [Vacancy(
        job_name=item['profession'],
        salary=item['payment_from'] if item['payment_from'] else 0,
        salary_currency= item['currency'],
        description=item['candidat'],
        link=item['link']
    )
    for item in sj_vacancies
    ]
    sorted_vacancies = sort_vacancies(vacancies)
    return sorted_vacancies


if __name__ == '__main__':
    print('Добрый день, для остановки приложения введите: "стоп", Если вы хотите продолжить работу приложение, то нажмите "Enter"')

    while True:
        print("Выберите сайт для поиска вакансий:\nВведите 1 если хотите искать вакансии на сайте HH.ru\nВведите 2 если хотите искать вакансии на сайте SuperJob.ru\nВведите 3 если хотите посмотреть сохранённые вакансии\nВведите 4 если хотите удалить запись")
        user_input = input("Выберите вариант: ")

        if user_input == '1':
            keyword = input('Введите ключевые слова: ')
            count = int(input('Введите количество вакансий: '))
            vacancies = hh_vacancy()
            for item in vacancies:
                print(item)

                print('Желаете ли вы сохранить вакансии?')
                user_save_input = input('Д - сохранить, Н - не сохранять: ')

                if user_save_input.lower() == 'д':
                    saver = JsonSaver('file.txt')
                    saver.writer_data(item)
                    print('Сохранено')

        elif user_input =='2':
            keyword = input('Введите ключевые слова: ')
            count = int(input('Введите количество вакансий: '))
            vacancies = sj_vacancy()
            for item in vacancies:
                print(item)

                print('Желаете ли вы сохранить вакансии?')
                user_save_input = input('Д - сохранить, Н - не сохранять: ')

                if user_save_input.lower() == 'д':
                    saver = JsonSaver('file.txt')
                    saver.writer_data(item)
                    print('Сохранено')

        elif user_input == '3':
            print('Введите название профессии для поиска или оставте пустую строчку:\n, если нет, то введите Н')
            user_check_vacancies = input("Введите ключевое слово: ")

            if user_check_vacancies.lower() != 'н':
                json_saver = JsonSaver('file.txt')
                vacancies = json_saver.get_vacancies(keyword=user_check_vacancies.lower())

                for item in vacancies:
                    print(item)

        elif user_input == '4':
            record = int(input('Введите номер записи: '))
            json_saver = JsonSaver('file.txt')
            json_saver.delete_vacancy(record)
            print('Запись удалена')

        stop_app = input('Введите "стоп" чтобы остановить приложение: ')
        if stop_app.lower() == 'стоп':
            break



























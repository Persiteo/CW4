from src.api_resps import HeadHunter, SuperJob
from src.vacancy import VacancyFile


def main():
    """Функция для взаимодействия с пользователем"""
    while True:
        keyword = input('Введите ключевое слово для поиска вакансии:\n')

        hh = HeadHunter(keyword).get_response()
        sj = SuperJob(keyword).get_response()
        if not hh and not sj:
            print('К сожалению, таких вакансий не обнаружено')
            exit()

        vf = VacancyFile()

        vf.add_to_file(hh, sj)

        currency = ''
        while currency == '':
            currency_input = int(input('Выберите желаемую валюту:\n'
                                       '1 - RUB\n'
                                       '2 - USD\n'))
            if currency_input == 1:
                currency = 'rub'
            elif currency_input == 2:
                currency = 'usd'
            else:
                print('Нет такой валюты\n')
                continue

        salary = int(input('Введите размер желаемой зарплаты\n'))

        vf.get_from_file(currency, salary)
        vac_lst = vf.vacancies
        if not vac_lst:
            print('Нет вакансий, соответствующих вашему запросу')
            exit()

        choice = int(input('1 - Показать вакансии\n'
                           '2 - Выбрать уровень занятости\n'))
        if choice == 1:
            None
        elif choice == 2:
            occupation = input('Какую занятость вы хотите иметь\n\n'
                               'Полная занятость\n'
                               'Частичная занятость\n'
                               'Стажировка\n'
                               'Проектная работа\n'
                               'Удаленная работа\n'
                               'Без разницы\n')

            if occupation == 'Без разницы':
                None
            else:
                vf.delete_from_file(occupation)

        sort = int(input('Отсортировать список вакансий?\n'
                         '1 - Вывести по умолчанию\n'
                         '2 - Отсортировать по зарплате (от большего к меньшему)\n'
                         '3 - Отсортировать по дате публикации (от нового к старому)\n'))

        if sort == 1:
            fin_vac_lst = vf.structure_data()

        elif sort == 2:
            vf.sort_by_salary()
            fin_vac_lst = vf.structure_data()

        elif sort == 3:
            vf.sort_by_date()
            fin_vac_lst = vf.structure_data()

        if vac_lst:
            print(f'По вашему запросу найдено {len(fin_vac_lst)} вакансий')
        else:
            print('Нет вакансий, соответствующих вашим желаниям')

        number = 0
        for i in fin_vac_lst:
            number += 1
            print(f'№ {number}\n{i}')

        user = int(input('Желаете начать заново?\n'
                         '1 - Да\n'
                         '0 - Нет\n'))
        if user == 1:
            continue
        else:
            print('Всего хорошего!')
            exit()


if __name__ == '__main__':
    main()

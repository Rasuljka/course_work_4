from get_api_data import GetApiDataSuperJob, GetApiDataHeadHunter
from json_data import JsonData


def user_function():

    while True:
        user_input = input("Какой сайт для поиска работы Вас интересует? 1. HeadHunter, 2. Superjob, 0 - выход: ")
        if user_input == "1":
            hh = GetApiDataHeadHunter
            vac_list = hh.get_api_data()
            json_data = JsonData()
            json_data.add(vac_list)
            second_user_input = input("Хотите вывести результаты в консоль? 1 - да, 2 - нет, 0 - выход: ")
            while True:
                if second_user_input == "1":
                    json_data.read()
                    list_vacancies = json_data.read()
                    for vacancy in sorted(list_vacancies):
                        print(vacancy)
                        print("-" * 50)
                    break
                elif second_user_input == "2":
                    break
                elif second_user_input == "0":
                    print("Приходите еще!")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
            third_user_input = input("Хотите удалить результаты поиска? 1 - да, 2 - нет, 0 - выход: ")
            while True:
                if third_user_input == "1":
                    json_data.delete()
                    break
                elif third_user_input == "2":
                    break
                elif third_user_input == "0":
                    print("Приходите еще!")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
            fourth_user_input = input("Хотите посмотреть еще вакансии? 1 - да, 2 - нет: ")
            while True:
                if fourth_user_input == "1":
                    break
                elif fourth_user_input == "2":
                    print("Приходите еще!")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
        elif user_input == "2":
            sj = GetApiDataSuperJob()
            vac_list = sj.get_api_data()
            json_data = JsonData()
            json_data.add(vac_list)
            second_user_input = input("Хотите вывести данные о вакансиях в консоль? 1 - да, 2 - нет, 0 - выход: ")
            while True:
                if second_user_input == "1":
                    json_data.read()
                    list_vacancies = json_data.read()
                    for vacancy in sorted(list_vacancies):
                        print(vacancy)
                        print("-" * 50)

                    break
                elif second_user_input == "2":
                    break
                elif second_user_input == "0":
                    print("Приходите еще!")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
            third_user_input = input("Хотите удалить список вакансий? 1 - да, 2 - нет, 0 - выход: ")
            while True:
                if third_user_input == "1":
                    json_data.delete()
                    break
                elif third_user_input == "2":
                    break
                elif third_user_input == "0":
                    print("Приходите еще!")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
            fourth_user_input = input("Хотите посмотреть еще вакансии? 1 - да, 2 - нет: ")
            while True:
                if fourth_user_input == "1":
                    break
                elif fourth_user_input == "2":
                    print("Приходите еще!")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
        elif user_input == "0":
            print("Приходите еще!")
            quit()
        else:
            print("Введите 1, 2 или 0!")
            continue

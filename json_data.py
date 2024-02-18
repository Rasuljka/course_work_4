from abc import ABC, abstractmethod
import json
import os
from vacancies import Vacancies


class AppData(ABC):
    """Абстрактный класс на добавление данных"""

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def add(self, *args):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class JsonData(AppData):
    """Класс на обработку json-файлов из requests"""

    def __init__(self):
        self.vacancies_save = 'vacancies.json'

    def __repr__(self):
        return f"Файл {self.vacancies_save}"

    def add(self, vac_data):
        with open(self.vacancies_save, 'w', encoding='utf-8') as json_file:
            json.dump(vac_data, json_file, ensure_ascii=False, indent=4)
        print(f"Результат успешно сохранен в {self.vacancies_save}")

    def read(self):
        with open(self.vacancies_save, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            list_vacancies = []
            for vacancy in data:
                list_vacancies.append(Vacancies(vacancy["id_vac"],
                                                vacancy["name"],
                                                vacancy["salary_from"],
                                                vacancy["salary_to"],
                                                vacancy["currency"],
                                                vacancy["city"],
                                                vacancy["hirer"],
                                                vacancy["url"]))
        return list_vacancies

    def delete(self):
        os.remove(os.path.join(self.vacancies_save))
        print(f"Файл {self.vacancies_save} успешно удален.")


# jd = JsonData()
# vac = jd.read()
# print(vac)
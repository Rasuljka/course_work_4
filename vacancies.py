class Vacancies:
    """Класс обработки вакансий"""
    def __init__(self, id_vac, name, salary_from, salary_to, currency, city, hirer, url):
        self.id_vac = id_vac
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.city = city
        self.hirer = hirer
        self.url = url

    def __str__(self):
        return f""""ID вакансии: {self.id_vac}
Название вакансии: {self.name}
Зарплата от: {self.salary_from}
Зарплата до: {self.salary_to}
Валюта: {self.currency}
Город: {self.city}
Компания: {self.hirer}
Ссылка: {self.url}"""

    def __lt__(self, other):
        return self.salary_from < other.salary_from

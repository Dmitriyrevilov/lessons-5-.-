import file_operations

from faker import Faker

import random

from random import choice


VERSION = "1.0"

def read_file(filename):
    with open(filename, encoding='utf8') as file_:
        return file_.read()

def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf8') as file_:
        return file_.write(content)


def render_template(template_path, output_path, context):
    content = read_file(template_path)

    for key, value in context.items():
        content = content.replace('{%s}' % key, str(value))

    write_to_file(output_path, content)



fake = Faker("ru_RU")


skill = ["Стремительный прыжок",    # список навыков skill
         "Электрический выстрел",
         "Ледяной удар",
         "Стремительный удар",
         "Кислотный взгляд",
         "Тайный побег",
         "Ледяной выстрел",
         "Огненный заряд"]

sampled_skills = random.sample(skill,3)  # 3 рандомных(0.1.2,чтобы они не повторялись) навыка из skill записали в переменную sampled skills


# skill_1 = sampled_skills[0].replace ("е" , "е͠'")

letters = {                               #рунический алфавит (словарь) letters
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}



skill_1 = sampled_skills[0] # записали первый навык в skill_1 
for letter in skill_1:    # для строки в skill_1   цикл по списку
    skill_1 =  skill_1.replace(letter,letters.get(letter)) #применили метод replace 





context = {
  "first_name": fake.first_name_male(), "last_name": fake.last_name_male(), # словарь context, + заменили имя и фамилию с помощью fake
  "job": fake.job() ,                          # замена профессии
  "town": fake.city(),                         # родной город
  "strength":      random.randint(3, 18),      # сила случ. числа от 3 до 18
  "agility":       random.randint(3, 18),      # ловкость   случ. числа от 3 до 18
  "endurance":     random.randint(3,18),       # выносливость случ. числа от 3 до 18
  "intelligence":  random.randint(3, 18),      # интеллект  случ. числа от 3 до 18
  "luck":          random.randint(3, 18),      # удача
  "skill_1":       skill_1,                    # навык 1 взяли из списка skill
  "skill_2":       sampled_skills[1],          # навык 2 взяли из списка skill
  "skill_3":       sampled_skills[2]           # навык 3 взяли из списка skill
}

file_operations.render_template("charsheet.svg", "result.svg", context)

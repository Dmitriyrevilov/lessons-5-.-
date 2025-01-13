from faker import Faker

import random

from random import choice


fake = Faker("ru_RU")


skills = ["Стремительный прыжок",    # список навыков skill
         "Электрический выстрел",
         "Ледяной удар",
         "Стремительный удар",
         "Кислотный взгляд",
         "Тайный побег",
         "Ледяной выстрел",
         "Огненный заряд"]


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


# sampled_skills = random.sample(skills,3)  # 3 рандомных(0.1.2,чтобы они не повторялись) навыка из skill записали в переменную sampled skills

# runic_skills = []

for i in range(10):
    sampled_skills = random.sample(skills,3)  # 3 рандомных(0.1.2,чтобы они не повторялись) навыка из skill записали в переменную sampled skills
    runic_skills = []
    my_text = "context" # запишится только строка
    with open("charsheet_{}.svg".format(i), "w") as i:
     context = {
  "first_name": fake.first_name_male(), "last_name": fake.last_name_male(), # словарь context, + заменили имя и фамилию с помощью fake
  "job": fake.job() ,                          # замена профессии
  "town": fake.city(),                         # родной город
  "strength":      random.randint(3, 18),      # сила случ. числа от 3 до 18
  "agility":       random.randint(3, 18),      # ловкость   случ. числа от 3 до 18
  "endurance":     random.randint(3,18),       # выносливость случ. числа от 3 до 18
  "intelligence":  random.randint(3, 18),      # интеллект  случ. числа от 3 до 18
  "luck":          random.randint(3, 18),      # удача
  "skill_1":       runic_skills[0],                    # навык 1 взяли из списка skill
  "skill_2":       runic_skills[1],          # навык 2 взяли из списка skill
  "skill_3":       runic_skills[2]           # навык 3 взяли из списка skill
    } 
    i.write(my_text)
    for skill in sampled_skills: # создаем цикл for, который перебирает все элементы(навыки) перебирает по очереди все навыки(sampled skills) и сохраняет их в skill, skill это строка, в каждый момент времени навыки (ss) сохраняются в skill по очереди
         for letter in skill:       # внутр цикл, говорим что новую букву мы получаем по ключу словаря letters и заменяем эту букву на новую 
             skill = skill.replace(letter, letters[letter])   # и сохраняем её в skill
         runic_skills.append(skill) # с помощью метода append(skill) , добавляем  


render_template("charsheet.svg", "result.svg", context)


# во внешнем цикле мы перебираем способности, все элементы (навыки) и сохраняем их поочередно в skill .цикл по списку
# во внутреннем цикле, цикл по строке(letter- буква)

















# for context in range(10):
#     for skill in sampled_skills: # создаем цикл for, который перебирает все элементы(навыки) перебирает по очереди все навыки(sampled skills) и сохраняет их в skill, skill это строка, в каждый момент времени навыки (ss) сохраняются в skill по очереди
#          for letter in skill:       # внутр цикл, говорим что новую букву мы получаем по ключу словаря letters и заменяем эту букву на новую 
#               skill = skill.replace(letter, letters[letter])   # и сохраняем её в skill

#          runic_skills.append(skill) # с помощью метода append(skill) , добавляем 




# context = {
#   "first_name": fake.first_name_male(), "last_name": fake.last_name_male(), # словарь context, + заменили имя и фамилию с помощью fake
#   "job": fake.job() ,                          # замена профессии
#   "town": fake.city(),                         # родной город
#   "strength":      random.randint(3, 18),      # сила случ. числа от 3 до 18
#   "agility":       random.randint(3, 18),      # ловкость   случ. числа от 3 до 18
#   "endurance":     random.randint(3,18),       # выносливость случ. числа от 3 до 18
#   "intelligence":  random.randint(3, 18),      # интеллект  случ. числа от 3 до 18
#   "luck":          random.randint(3, 18),      # удача
#   "skill_1":       runic_skills[0],                    # навык 1 взяли из списка skill
#   "skill_2":       runic_skills[1],          # навык 2 взяли из списка skill
#   "skill_3":       runic_skills[2]           # навык 3 взяли из списка skill
# }

# ПЕРЕДАЧА ИЗМЕНЯЕМЫХ ОБЪЕКТОВ В ФУНКЦИЮ

def increase_person_age(person):
    person['age'] +=1
    return person # мы возвращаем словарь, person это словарь. После return функция перекращает свою работу!
person_one = {
    'name': 'Bob', 
    'age': 21
}
increase_person_age(person_one)
print(person_one['age']) # 22 В этом примере внутри функции мы изменили внешную переменную person_one. 
# ДЕЛАТЬ ЭТО КАК ПРАВИЛО НЕ РЕКОМЕНДУЕТСЯ!!! При этом это может происхоит даже не явно для нас, 
# потому что если передаем в функцию изменяемый объект, то внутри функции работаем с параметрами функции
# мы не меняем внешнее переменные по именам этих внешных переменных, мы меняем параметры функции,
# но при этом если мы работаем с изменяемые объектами то внешнее переменные также измениться, важно понимать это!!!
# Иногда бывает ситуации когда внутри функции мы хотим изменить внешнее объект.



# КАК ИЗБЕЖАТЬ ИЗМЕНЕНИЯ ВНЕШНЫХ ОБЪЕКТОВ В ФУНКЦИИ?
# Это можно сделать с помощи создание копии объекта и копие можно создавать как внутри функции и до вызова функции 
# 
def increase_person_age(person):
    person_copy = person.copy() # <<<
    person['age'] +=1
    return person
person_one = {
    'name': 'Bob', 
    'age': 21
}
increase_person_age(person_one)
print(person_one['age'])

# ИЛИ

def increase_person_age(person):
    person['age'] +=1
    return person
person_one = {
    'name': 'Bob', 
    'age': 21
}
increase_person_age(person_one.copy()) # <<<
print(person_one['age'])
# Если в словарей есть вложенные словарей либо списки, либо другие изменяемые объекты, то рекомендуется 
# использовать deepcopy
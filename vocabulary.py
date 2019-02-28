#Создайте словарь:
#{"city": "Москва", "temperature": "20"}
#Выведите на экран значение ключа city
#Уменьшите значение "temperature" на 5
#Выведите на экран весь словарь

cities = {"city": "Москва", "temperature": "20"}
print(cities["city"])

cities["temperature"] -= 5

print(cities)


#Проверьте, есть ли в словаре ключ country
#Выведите значение по-умолчанию "Россия" для ключа country
#Добавьте в словарь элемент date со значением '27.05.2019'
#Выведите на экран длину словаря

print(cities.get('country', 'Россия'))

cities['date'] = '27.05.2019'

print(len(cities))

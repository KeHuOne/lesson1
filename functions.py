#Задание 1
#Создайте функцию get_summ(one, two, delimiter='&') которая принимает два парамтера, вприводит их к строке и отдает объединеными 
# через разделитель delimteter
#Вызовите функцию, пердав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
#Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return (one + delimiter + two)

result = get_summ("Learn", "Python")
print(result.upper())

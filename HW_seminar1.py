# Задание 1. Написать функцию на Python, которой
# передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда
# успешно выполнена и текст найден в ее выводе
# и False в противном случае. Передаваться
# должна только одна строка, разбиение вывода
# использовать не нужно.
# Задание 2. (повышенной сложности). Доработать
# функцию из предыдущего задания таким образом,
# чтобы у нее появился дополнительный режим
# работы, в котором вывод разбивается на слова
# с удалением всех знаков пунктуации (их можно взять
# из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие
# слова в выводе.
import subprocess
import string

command = "cat /home/zm/file"

result = subprocess.run(command, shell=True, encoding="utf-8", stdout=subprocess.PIPE)
result_out = result.stdout
print(result_out)  # expecto. patronus.!!! Harry?
result_of_words = result_out.translate((str.maketrans("", "", string.punctuation)))
print(result_of_words) # expecto patronus Harry
if __name__ == '__main__':
    if "Harry" in result_of_words and result.returncode == 0:
        print("True")
    else:
        print("False")
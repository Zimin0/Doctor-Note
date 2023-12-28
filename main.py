import pytest

def func(strings:list):
    """
    Находит каждую вторую строку в массиве, 
    среди них находит с четной длиной и удаляет второй символ
    """
    result = []
    ind = 0
    while True:
        if ind == len(strings):
            break
        if ind % 2 == 1:
            if len(strings[ind]) % 2 == 0:
                result.append(strings[ind][:0] + strings[ind][1:])
        ind += 1

    return result

print(func(['helloo', 'world11!', 'ggllss', '1234']))

def test_valid():
    assert func(['helloo', 'world11!', 'ggllss', '1234']) == ['orld11!', '234']

def test_zero_elements():
    assert func([]) == [], "Пустой массив!"



# Фикстуры - функция, которая настраивает окружение для теста - 
# - например - подключение к базе данных + позволяет передавать повторяющиеся наборы входных данных разным тестам 

# def test
    



# UNITTEST PYTHON 
    
import unittest

class MyTest(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(5*12, 60)

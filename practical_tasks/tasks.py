from collections import namedtuple, Counter, OrderedDict
from typing import List, Set


def get_digits(number: int) -> List[int]:
    """1. Разбить число на цифры, не используя строки"""
    digit_list_reversed = []
    while number != 0:
        remain = int(number % 10)
        digit_list_reversed.append(remain)
        number = (number - remain) / 10
    digit_list = digit_list_reversed[::-1]
    return digit_list


def count_odd_even(number: int) -> namedtuple:
    """2. Посчитать кол-во четных и нечетных цифр в числе"""
    even_odd_counter = namedtuple("Even_odd_counter", ["even", "odd"])
    digits_list = get_digits(number)
    evens_counter = 0
    for digit in digits_list:
        if digit % 2 == 0:
            evens_counter += 1
    result = even_odd_counter(even=evens_counter, odd=len(digits_list) - evens_counter)
    return result


def reverse_list(original_list: List) -> List:
    """3. Переворачиваем список"""
    reversed_list = original_list[::-1]
    return reversed_list


def get_set_difference(first_set: Set, second_set: Set) -> Set:
    """4. Даны 2 множества. Нужно вывести элементы первого, которые отсутсутствуют во втором
    (LEFT JOIN WHERE b.key IS NULL двух списков)
    """
    return first_set - second_set


def remove_duplicates(original_list: List) -> List:
    """5. Убрать дубликаты в списке"""
    return List[OrderedDict.fromkeys(original_list)]


def get_num_of_nonuniques(original_list: List) -> int:
    """6. Подсчитать кол-во неуникальных элементов в списке/кортеже"""
    return len([elem for elem in original_list if original_list.count(elem) > 1])


def count_words(original_string: str) -> Counter:
    """8. Разбить строку на слова и подсчитать, сколько раз каждое слово встречается в тексте"""
    words_list = original_string.split()
    return Counter(words_list)


def normalize_whitespaces(original_string: str) -> str:
    """9. Заменить несколько идущих пробельных символов в строке на один пробел"""
    return ' '.join(original_string.split())


def get_strs_containing_substr(str_list: List[str], substr: str) -> List[str]:
    """10. Дан список строк. Нужно оставить только те, в которых строки содержат заданную подстроку"""
    return [item for item in str_list if substr in item]


if __name__ == '__main__':

    # 1.Разбить число на цифры, не используя строки
    input_value = int(input())
    print(get_digits(input_value))

    #  2. Посчитать кол-во четных и нечетных цифр в числе
    input_value = int(input())
    print(count_odd_even(input_value))

    #  3. Переворачиваем список
    input_string = input("Enter elements separated by space: ")
    user_list = input_string.split()
    print(reverse_list(user_list))

    # 4. Даны 2 множества. Нужно вывести элементы первого, которые отсутсутствуют во втором
    first_string = input("Enter first set elements separated by space: ")
    second_string = input("Enter second set elements separated by space: ")
    fist_set = Set[first_string.split()]
    second_set = Set[second_string.split()]
    print(get_set_difference(fist_set, second_set))

    # 5. Убрать дубликаты в списке
    input_string = input("Enter elements separated by space: ")
    user_list = input_string.split()
    print(remove_duplicates(user_list))

    # 6. Подсчитать кол-во неуникальных элементов в списке/кортеже
    input_string = input("Enter elements separated by space: ")
    user_list = input_string.split()
    print(get_num_of_nonuniques(user_list))

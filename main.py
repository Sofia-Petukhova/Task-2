import sys
from collections import Counter


def safe_input(prompt: str) -> str:
    """Безопасный ввод массива целых чисел с возможностью выхода из программы."""
    raw = input(prompt).strip()
    if raw.lower() == "exit":
        print("Выход из программы...")
        sys.exit()
    return raw


def input_array(name: str) -> list[int]:
    """Безопасный ввод массива целых чисел."""
    while True:
        raw = safe_input(f"Введите элементы массива {name} через пробел: ")
        try:
            return list(map(int, raw.split()))
        except ValueError:
            print("Ошибка: массив должен состоять только из целых чисел. "
                  "Попробуйте снова или введите 'exit' для выхода.")
            

def task_1_7(arr_a: list[int], arr_b: list[int]) -> list[int]:
    """Повторяющиеся элементы массива A, которые есть в массиве B."""
    counter_a = Counter(arr_a)
    set_b = set(arr_b)
    return sorted(x for x, cnt in counter_a.items() if cnt > 1 and x in set_b)            


def task_2_7(arr_a: list[int], arr_b: list[int]) -> list[int]:
    """Элементы, присутствующие в обоих массивах A и B."""
    return sorted(set(arr_a) & set(arr_b))
    

def main() -> None:
    print("Программа по вариантам 1.7, 2.7, 3.7\n")
    while True:
        choice = input("Выберите пункт меню: ")
        if choice == "0":
            break


if __name__ == "__main__":
    main()
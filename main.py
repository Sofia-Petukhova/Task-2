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


def task_3_7(arr_a: list[int], arr_b: list[int]) -> list[int]:
    """Элементы, которые присутствуют в нескольких экземплярах в A или B."""
    ca = Counter(arr_a)
    cb = Counter(arr_b)
    return sorted({x for x, c in ca.items() if c > 1} |
                  {x for x, c in cb.items() if c > 1})
    

def print_menu() -> None:
    print("\n=== МЕНЮ ===")
    print("1 — повторяющиеся элементы массива А, которые есть в массиве В (Задача 1.7)")
    print("2 — элементы, присутствующие в обоих массивах А и В (Задача 2.7)")
    print("3 — элементы, которые присутствуют в нескольких экземплярах либо в массиве А, либо в массиве В (либо в обоих массивах) (Задача 3.7)")
    print("0 — Выход")
    print("============")


def main() -> None:
    print("Для выхода в любой момент можно ввести слово 'exit'.")

    while True:
        print_menu()
        choice = safe_input("Выберите пункт меню: ")

        if choice == "0":
            print("Завершение программы...")
            break

        if choice not in {"1", "2", "3"}:
            print("Ошибка: выберите одну из опций меню.")
            continue

        arr_a = input_array("A")
        arr_b = input_array("B")

        if choice == "1":
            result = task_1_7(arr_a, arr_b)
            print("Результат (повторяющиеся элементы A, которые есть в B):", result)
        elif choice == "2":
            result = task_2_7(arr_a, arr_b)
            print("Элементы, присутствующие в обоих массивах:", result)
        elif choice == "3":
            result = task_3_7(arr_a, arr_b)
            print("Элементы, встречающиеся несколько раз в A или B:", result)

if __name__ == "__main__":
    main()
import sys

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

def main() -> None:
    print("Программа по вариантам 1.7, 2.7, 3.7\n")
    while True:
        choice = input("Выберите пункт меню: ")
        if choice == "0":
            break

if __name__ == "__main__":
    main()
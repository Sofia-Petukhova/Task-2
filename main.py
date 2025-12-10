import sys

def main() -> None:
    print("Программа по вариантам 1.7, 2.7, 3.7\n")
    while True:
        choice = input("Выберите пункт меню: ")
        if choice == "0":
            break

if __name__ == "__main__":
    main()
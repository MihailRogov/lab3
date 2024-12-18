import re

# Регулярное выражение для формата UTC
utc_pattern = r'\b(\d{4})-(\d{2})-(\d{2})T([01]?\d|2[0-3]):([0-5]\d):([0-5]\d)(Z|[+-][01]\d:[0-5]\d)?\b'
def is_valid_utc_time(time_str):
    return bool(re.match(utc_pattern, time_str))

def find_utc_times(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if is_valid_utc_time(line):  # Проверка на корректность формата UTC
                    print(line)  # Выводим корректные строки
                else:
                    print(f"Время не соответствует формату UTC: {line}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
def check_times_from_input():
    print("Введите строки времени в формате UTC. Введите 'exit' для завершения.")
    while True:
        user_input = input("Введите время в формате UTC: ").strip()

        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break
        
        if is_valid_utc_time(user_input):
            print(f"Время '{user_input}' является корректным в формате UTC.")
        else:
            print(f"Время '{user_input}' не соответствует формату UTC.")
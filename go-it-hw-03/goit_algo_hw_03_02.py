# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

# Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

# Вимоги до завдання:
# Параметри функції:
# min - мінімальне можливе число у наборі (не менше 1).
# max - максимальне можливе число у наборі (не більше 1000).
# quantity - кількість чисел, які потрібно вибрати (значення між min і max).
# Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
# Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

# Рекомендації для виконання:

# Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
# Використовуйте модуль random для генерації випадкових чисел.
# Використовуйте множину або інший механізм для забезпечення унікальності чисел.
# Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.

import random

def lottery_program(min_number = None, max_number = None, quantity_of_numbers = None) -> str:
    """
    Generates a sorted list of unique random numbers within a given range, ensuring user input is valid.
    """
    try:
        min_number = int(input("Please enter first number of range: "))
        max_number = int(input("Please enter last number of range: "))
        quantity_of_numbers = int(input("Please enter amount of returned numbers: "))
        
        # Validate input range
        if not (1 <= min_number <= 1000 and 1 <= max_number <= 1000 and 1 <= quantity_of_numbers < 1000):
            raise ValueError("Numbers must be in range from 1 to 1000")
        
        # Ensure valid range
        if min_number > max_number:
            raise ValueError("First number must be smaller than last number.")
        
        if quantity_of_numbers > (max_number - min_number + 1):
            raise ValueError("Amount of returned numbers is greater than the range.")
        
        # Generate unique random numbers
        chosen_numbers = set()
        while len(chosen_numbers) < quantity_of_numbers:
            chosen_numbers.add(random.randint(min_number, max_number))
        
        lottery_numbers = sorted(chosen_numbers)
        print(f"Your lottery numbers: {lottery_numbers}")
        
    except ValueError as e:
        lottery_numbers = []
        print(f"Your lottery numbers: {lottery_numbers}")
        print(f"Error: {e}. Please enter valid numbers.")

# Run the function
lottery_program()

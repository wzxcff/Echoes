from django.test import TestCase

# Create your tests here.

# Задача 1. Створити множину, що містить цілі числа 2, -5, 1, 4, -8. Знайти найбільший і найменший елементи множини.
set_1 = {2, -5, 1, 4, -8}
print(f"Max (max function): {max(set_1)}\nMin (min function): {min(set_1)}")
max_el = None
min_el = None
tuple = tuple()
for el in set_1:
    if el < 0:
        if max_el is None or el > max_el:
            max_el = el
        if min_el is None or el < min_el:
            min_el = el
print(f"Max (for): {max_el}\nMin (for): {min_el}")
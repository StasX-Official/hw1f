result = []

def divider(a, b):
    if a < b:
        raise ValueError("Значення 'a' менше, ніж 'b'.")
    if b > 100:
        raise IndexError("Значення 'b' більше 100.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])
        result.append(res)
    except ZeroDivisionError:
        print(f"Ділення на нуль для ключа {key}.")
    except TypeError:
        print(f"Неправильний тип даних для ключа {key}.")
    except ValueError as ve:
        print(f"ValueError: {ve} для ключа {key}.")
    except IndexError as ie:
        print(f"IndexError: {ie} для ключа {key}.")

print("Результат:", result)

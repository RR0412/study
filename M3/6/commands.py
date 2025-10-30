# def multiply(a, b):
#     result = a * b
#     print(f'Result is {result}')
#
# print('Multiplying strings')
# multiply('1','2')
# print('Done')
#
# e = TypeError("Error happened. Fix it, please.")
# print(e.args)
#
# raise e
#


class MySimpleException(Exception):
    pass

# raise MySimpleException({'expected': 'value', 'got': 'another_value'})



class MyInformativeException(MySimpleException):
    def __init__(self, message, *args):
        self.message = message
        super().__init__(*args)

e = MyInformativeException('This one has a message in it')
print(e.message)
# raise e

def read_numbers(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            value = int(line)
            numbers.append(value)
    return numbers

numbers = read_numbers('numbers.txt')
print(f'{numbers}')

try:
    numbers = read_numbers('letters.txt')
    print(f'Считано : {numbers}')
except:
    print('Файл не найден')

try:
    numbers = read_numbers('numbers.txt')
    print(f'Считано : {numbers}')
except FileNotFoundError:
    print('Файл не найден')
except ValueError:
    print('Файл содержит не целые числа')
except Exception:
    print('Неизвестная ошибка')

try:
    numbers = read_numbers('strings.txt')
    print(f'Считано : {numbers}')
except FileNotFoundError:
    print('Файл не найден')
except ValueError:
    print('Файл содержит не целые числа')

try:
    numbers = read_numbers('file.txt')
    print(f'Считано : {numbers}')
except FileNotFoundError:
    print('Файл не найден')
except ValueError:
    print('Файл содержит не целые числа')

try:
    numbers = read_numbers('strings.txt')
    print(f'Считано : {numbers}')
except Exception as e:
    error_type = type(e).__name__
    print(f'Неожиданная ошибка типа {error_type}')
    print(e)

try:
    numbers = read_numbers('file.txt')
    print(f'Считано : {numbers}')
except Exception as e:
    error_type = type(e).__name__
    print(f'Неожиданная ошибка типа {error_type}')
    print(e)


# ===================================================================

def get_numbers():
    try:
        numbers = read_numbers('files.txt')
    except Exception as e:
        print(f'Ошибка : {e}')
    else:
        print(f'Считано: {numbers}')
    finally:
        print('Выход')

get_numbers()

def get_numbers():
    try:
        numbers = read_numbers('strings.txt')
    except Exception as e:
        print(f'Ошибка : {e}')
    else:
        print(f'Считано: {numbers}')
    finally:
        print('Выход')


def get_numbers():
    try:
        numbers = read_numbers('files.txt')
    except Exception as e:
        print(f'Ошибка : {e}')
    else:
        print(f'Считано: {numbers}')
    finally:
        print('Выход')

def multiply(a, b):
    try:
        return a * b
    except Exception as e:
        print(e)
        return None
    finally:
        print(f'Попытка умножить {a} на {b}')
multiply(3,4)
multiply('3','4')


# ===================================================================
def move_mouse(x, y):
    raise Exception('Мышь была передвинута. Перезагрузите компьютер, что бы изменения вступили в силу!')

def click(x, y):
    try:
        move_mouse(x, y)
        print('Click!')
    except Exception as e:
        print('Не удалось кликнуть!')
        raise

def main():
    try:
        click(100, 100)
    except Exception as e:
        print(e)

main()






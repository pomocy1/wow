# calc.py

import sys

def calculate(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        print("Niepoprawna operacja. Dopuszczalne operacje to '+' i '-'.")
        return None
    return result

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Użycie: calc.py <liczba_1> <operacja +-> <liczba_2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        operator = sys.argv[2]
        num2 = float(sys.argv[3])
    except ValueError:
        print("Podano niepoprawne argumenty. Wszystkie argumenty powinny być liczbami.")
        sys.exit(1)

    result = calculate(num1, operator, num2)

    if result is not None:
        with open('/tmp/wynik.txt', 'w') as f:
            f.write(str(result))
        print("Wynik został zapisany do pliku /tmp/wynik.txt.")

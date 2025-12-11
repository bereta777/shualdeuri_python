
class BaseCalculator:   # მშობელი კლასი
    def calculate(self, a, b):
        return "Base class cannot calculate"

class Calculator(BaseCalculator):  # შვილი კლასი
    def calculate(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return "Error: division by zero"
            return a / b
        else:
            return "Invalid operation"

def run_calculator():  # მართავს კალკულატორს
    calc = Calculator()

    print("მარტივი კალკულატორი")

    while True:
        a = int(input("შეიყვანეთ პირველი რიცხვი: "))
        b = int(input("შეიყვანეთ მეორე რიცხვი: "))
        op = input("აირჩიეთ ოპერაცია (+, -, *, /): ")

        result = calc.calculate(a, b, op)
        print("Result:", result)

        again = input("გსურთ გააგრძელოთ? (კი/არა): ")
        if again.lower() != "კი":
            break

def main_menu():
    while True:
        print("\n= MENU =")
        print("1. კალკულატორის დაწყება")
        print("2. გასვლა")

        choice = input("აირჩიე: ")

        if choice == "1":
            run_calculator()
        elif choice == "2":
            print("ნახვამდის!")
            break
        else:
            print("ხელახლა სცადეთ")
main_menu()


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("\n   What calculation would you like to do? \n")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (x)")
    print("4. Divide (/)\n")
    print("")
    
    while True:
        choice = input("Enter choice: ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
                
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
                
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
                
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
                    
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes' or next_calculation.lower() != 'y':
                print("Closing application...")
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()

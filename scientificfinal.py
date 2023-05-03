import math
import statistics
choice=0
while choice !=15:
    print("\nScientific Calculator\n")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Power")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10.Tangent")
    print("11.Mean")
    print("12.Median")
    print("13.Mode")
    print("14.Standard Deviation")
    print("15.EXIT")
    
    choice = input("Enter choice (1-15): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", num1 + num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1 * num2)

        elif choice == '4':
            print(num1, "/", num2, "=", num1 / num2)
    
    elif choice == '5':
        num = float(input("Enter a number: "))
        print("Square root of", num, "is", math.sqrt(num))

    elif choice == '6':
        num1 = float(input("Enter base: "))
        num2 = float(input("Enter exponent: "))
        print(num1, "^", num2, "=", math.pow(num1, num2))

    elif choice == '7':
        num = float(input("Enter a number: "))
        print("Logarithm of", num, "is", math.log10(num))
        
    elif choice == '8':
        angle = float(input("Enter angle in degrees: "))
        print("Sine of", angle, "is", math.sin(math.radians(angle)))
        
    elif choice == '9':
        angle = float(input("Enter angle in degrees: "))
        print("Cosine of", angle, "is", math.cos(math.radians(angle)))
        
    elif choice == '10':
        angle = float(input("Enter angle in degrees: "))
        print("Tangent of", angle, "is", math.tan(math.radians(angle)))
    
    elif choice == '11':
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]
        print("Mean of", numbers, "is", statistics.mean(numbers))
    
    elif choice == '12':
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]
        print("Median of", numbers, "is", statistics.median(numbers))
    
    elif choice == '13':
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]
        print("Mode of", numbers, "is", statistics.mode(numbers))
    
    elif choice == '14':
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]
        print("Standard deviation of", numbers, "is", statistics.stdev(numbers))
    
    elif choice =='15':
        print("Thanks for using my scientific calculator!!!");
        break
    else:
        print("Invalid input")



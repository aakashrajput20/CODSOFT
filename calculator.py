print("=" * 40)
print("      SIMPLE CALCULATOR")
print("=" * 40)

while True:
    try:
        num1 = float(input("\nEnter First Number: "))
        num2 = float(input("Enter Second Number: "))

        print("\nChoose Operation")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"\nResult = {num1 + num2}")

        elif choice == "2":
            print(f"\nResult = {num1 - num2}")

        elif choice == "3":
            print(f"\nResult = {num1 * num2}")

        elif choice == "4":
            if num2 == 0:
                print("\nError! Division by zero is not allowed.")
            else:
                print(f"\nResult = {num1 / num2}")

        else:
            print("\nInvalid Choice!")

    except ValueError:
        print("\nPlease enter valid numbers!")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again != "yes":
        print("\nThank You for using Calculator!")
        break
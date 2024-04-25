from combine_factors import find_gcf


while True: 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    gcf = find_gcf(num1, num2)
    print(f"The Greatest Common Factor of {num1} and {num2} is: {gcf}")

    answer = input("Would you like to continue calculating? (Y/N)? ")
    if answer.strip().lower() not in ['y', 'yes', 'ye']:
        break 
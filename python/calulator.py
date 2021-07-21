#A simple calulator

try:
    number = int(input('Enter first number: '));
    number2 = int(input('Enter second number: '));


    operator = input("Enter a operator: ");

    if(operator == "+"):
        print("Your answer: ", number + number2);
    elif(operator == "-"):
        print("Your answer: ", number - number2);
    elif(operator == "/"):
        print("Your answer: ", number / number2);
    elif(operator == '*'):
        print("Your answer:", number * number2);
    else:
        print("Not a Valid Operator!")
except:
    print('This is not a Valid Number!')

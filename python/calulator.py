#A simple calulator
#try catch will catch an error if number or number2 is not a number
try:
    number = int(input('Enter first number: '));
    number2 = int(input('Enter second number: '));

    operator = input("Enter a operator: ");

#checks if the users added a valid operator.
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

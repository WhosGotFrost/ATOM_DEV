import random

numbers = '123456789';
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

passLength = input('Password Length: ');
passLength = int(passLength);

password = ''

for c in range(passLength):
    password += random.choice(numbers + chars);
print(password);

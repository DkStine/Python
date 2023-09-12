# print("Hello World!")

passwd = input('Enter the password: ')
passwd_length = 0
digit = False

for i in passwd:
    passwd_length = passwd_length + 1
    if i.isdigit():
        digit = True
    else:
        digit = False

if (passwd_length >= 8) and (digit == True):
    print("Valid!")
else:
    print("Invalid")
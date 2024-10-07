first = int(input('Введите число из трех цифр:'))
second = int(input('Введите число из трех цифр еще раз:'))
third = int(input('Введите число из трех цифр еще раз (это последний раз):'))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
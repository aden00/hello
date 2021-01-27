try:
    for i in [1,2,w]:
            print(i**2)
except:
        print('you should enter a integer!!!')

try:
    x = 0
    y = 0

    z = x / y
    print(z)
except ZeroDivisionError:
    print('you cannot divide zero')

def ask():
    while True:
        try:
            result=int(input('enter an integer: '))
            result2=result**2
        except:
            print('An error occurred! Please try again!')
        else:
            print(f'Thank you, your number squared is:  {result2}')
            break
ask()

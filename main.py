import string
print('='*50)
print('PASSWORD STRENGTH \033[1;92mCHECKER\033[m'.center(60))
print('-'*50)

#----CLOSE THE PROGRAM----
def leave():
    print('\033[1;90m-\033[m'*50)
    print('\033[1;91mCLOSING PROGRAM...\033[m'.center(60))
#----GRADE SYSTEMS----
def passLen(pasw):
    if len(pasw)<6 and len(pasw)>10:
        print('COMPRIMENTO INVÁLIDO')
        return False
    return True
def passUpper(pasw):
    for letter in pasw:
        if letter.isupper():
            return True
        else:
            return False
def passNumber(pasw):
    for number in pasw:
        if number.isdigit():
            return True
    return False
def passSymbol(pasw):
    for letter in pasw:
        if letter in string.punctuation:
            return True
    return False
#----MAIN FUNCTION----
def ver(pasw):
    grade=0

    if passLen(pasw)==True:
        grade+=1
    if passUpper(pasw)==True:
        grade+=1
    if passNumber(pasw)==True:
        grade+=1
    if passSymbol(pasw)==True:
        grade+=1
    if grade <=2:
        return 'WEAK'
    elif grade <=4:
        return 'GOOD! But could be better...'
    else:
        return 'STRONG!! CONGRATS!'
#----MENU----
def menu():
    print('\033[1;90m=\033[m'*50)
    print("\033[1;92m[1]\033[m Check password")
    print("\033[1;94m[2]\033[m Evaluation criteria")
    print("\033[1;91m[3]\033[m Leave")
    print('\033[1;90m=\033[m'*50)
#----MENU CODE----
def main():
    while True:
        menu()
        op=int(input('CHOOSE YOUR OPTION: '))

        if op==1:
            print('\033[1;90m=\033[m'*50)
            pasw=input('PASSWORD>> ')
            result=ver(pasw)
            print(f'Your password´s grade is: {result}')

        elif op==2:
            print('\033[1;90m-\033[m'*50)

        elif op==3:
            print('\033[1;90m*\033[m')
            leave()
            break

        else:
            print('\033[1;91mINVALID OPTION.\033[m\nTRY AGAN...')

main()

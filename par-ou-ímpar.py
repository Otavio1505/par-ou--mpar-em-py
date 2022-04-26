import random
import colorama
from colorama import Fore
from colorama import Style
ran = 0
pi = 0
user = 0
val = 0
contador = 0
while True:
    ran = random.randint(1, 10)
    pi = input('Par ou ímpar?[P/I] ').upper()
    if pi not in 'PI':
        while pi not in 'pPiI':
            pi = input('Par ou ímpar?[P/I] ').upper()
    user = int(input('Escolha um número: '))
    val = ran + user
    if user > 10 or user < 0:
        while user > 10 or user < 0:
            print(f'Digite um número entre 0 a 10.')
            user = int(input('Escolha um número: '))
    val = ran + user        
    if pi == 'P':
        print(f'Você escolheu: {user}')
        print(f'O computador escolheu: {ran}'+ Style.RESET_ALL)
        print(Fore.YELLOW + f'Resultado: {val}' + Style.RESET_ALL)
        if val%2 == 0:
            print(Fore.GREEN + Style.BRIGHT + 'Deu par,', end=' ')
            print(Fore.GREEN + Style.BRIGHT + 'Você ganhou.' + Style.RESET_ALL)
            print('=' * 20)
            print(Fore.BLUE + Style.BRIGHT +'Vamos jogar novamente.')
            contador +=1
            print(Fore.BLUE + Style.BRIGHT + f'Vitórias consecutivas: {contador}'+ Style.RESET_ALL)
            print('=' * 20)
        else:
            print(Fore.RED + Style.BRIGHT + 'Deu ímpar,', end=' ')
            print(Fore.RED + Style.BRIGHT + 'Você perdeu.' + Style.RESET_ALL)
            print('=' * 20)
            print('Programa encerrado.')
            break
    if pi == 'I':
        print(f'Você escolheu: {user}')
        print(f'O computador escolheu: {ran}')
        print(Fore.YELLOW + f'Resultado: {val}' + Style.RESET_ALL)
        if val%2 == 0:
            print(Fore.RED + Style.BRIGHT + 'Deu par,', end=' ')
            print(Fore.RED + Style.BRIGHT + 'Você perdeu.' + Style.RESET_ALL)
            print('='*20)
            print('Programa encerrado.')
            break
        else:
            print(Fore.GREEN + Style.BRIGHT +'Deu ímpar,', end=' ')
            print(Fore.GREEN + Style.BRIGHT + 'Você ganhou.' + Style.RESET_ALL)
            print('=' * 20)
            print(Fore.BLUE + Style.BRIGHT +'Vamos jogar novamente.')
            contador+=1
            print(Fore.BLUE + Style.BRIGHT + f'Vitórias consecutivas: {contador}'+ Style.RESET_ALL)
            print('=' * 20)

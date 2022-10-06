import random
def sluchaynoye_chislo():
    a = random.randint(1,101)
    start = input('Игра угадай число. Напишите "Start" чтобы начать: ')
    total = 1
    while start=='Start':
        print('Напишите любое число от 1 до 100 чтобы угадать число. ')
        guess = int(input('Напишите любое число: '))
        if guess>a:
            print('Cлишком много,попробуйте еще раз.')
            total+=1
        if guess<a:
            print('Слишком мало,попробуйте ещё раз.')
            total+=1
        if guess == a:
            print('Поздравляем вы угадали!')
            print(f'Вы потытались {total} раз!')
            print('Чтобы продолжить напишите Start\nЧтобы закончить напишите End.')
            start = input('Введите: ')
            a= random.randint(1,101)
sluchaynoye_chislo()
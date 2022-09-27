import random
def eratosthenes(number):
    sieve=list(range(2,number+1)) # последовательность начиная с 2 до number включительно
    for i in sieve: # берем один элемент из последовательности
        for j in sieve: # берём второй элемент из последовательности
            if i != j and j % i == 0: # в случае если взят не один и тот же элемент и элементы оказывается делятся: 
                sieve.remove(j) # удаляем этот элемент
    return sieve    

def generate_random_number(length_number): # принимаем на вход длину которую должны срандомить 
    number = '1'  # первый символ должен быть 1 по условию
    for i in range( 1, length_number-1): # начиная с второго символа и до предпоследнего рандомим
        number += str(random.randint(0,1))
    number += '1'  # последний символ должен быть 1 по условию
    return int(number,base=2) #вернем интовое значение преобразуя из двоичного кода


def check_div_on_prime(number):  # проверяем число на делимость на простые числа
    # для тестирования понадобятся все простые числа до 2000
    for prime_number in eratosthenes(2000): # для каждого простого числа из листа:
        if number!=prime_number  and number % prime_number ==0: # если остаток от деления на простое число не0, значит число составное, нам не подходит
            return False # число не простое
    return True # если прошли и не нашли делителя числа - число простое

def wilson(number):  # тест вильсона
    if check_div_on_prime(number): # первое условие вильсона чтобы число было простым,
        factorial=1  # тут будем хранить факториал
        for i in range(1,number):  # перемножаем не доходя до самого числа, то есть (n-1)!
            factorial*=i

        if factorial % number==number-1: # 2ое условие вильсона чтобы остаток от факториала числа меньше заданного на единицу при делении на само число был на 1 меньше самого числа
            print( "Для "+str(number)+" критерий вильсона выполняется")
            return 0 # для выхода из функции
    
    print( "Для "+str(number)+" критерий вильсона  не выполняется")

def main():
    for i in range(5):
        length_number=int(input("\n\nВведите длину, последовательность которой вы хотите сгенерировать: "))
        number=generate_random_number(length_number) # создаем последовательность и получаем ее в десятичной единице счисления
        if check_div_on_prime(number): # проверка на простые числа, если последовательность только из простых,то будет true
            wilson(number)
        else:
            print('Сгенерированный '+str(number)+' не прошел проверку на простые числа :( ')    

if __name__=='__main__':
    main()
def pertence_a_fibonacci(n):

    if n < 0:
        return False

    a, b = 0, 1

    if n == a or n == b:
        return True

    while b < n:
        a, b = b, a + b
        if b == n:
            return True

        return False


    try:
        numero = int(input('digite um número para verificar se pertence a sequência de Fibinacci:'))

        if pertence_a_fibonacci(numero):
            print(f'O número {numero} pertence a sequência de Fibonacci.')
        else:
            print(f'O número {numero} não pertence a sequência de Fibonacci.')
    except ValueError:
        print('Por favor,digite um número inteiro válido')

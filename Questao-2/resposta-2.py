def fibonacci_sequence(n):
    sequence = [0,1]
    if n < 0:
        return "O número escolhido é menor do que zero!"
    else:
        while sequence[-1] < n:
            sequence.append(sequence[-1] + sequence[-2])
        if n in sequence:
            return print("O número informado pertence a sequência de Fibonacci!")
        else:
            return print("O número informado não pertence a sequência de Fibonacci!")


number = int(input("Escolha um numero para verificar: "))
fibonacci_sequence(number)
def square_and_filter(start, end):
    squares = []
    even_squares = []
    odd_squares = []

    for number in range(start, end + 1):
        square = number ** 2
        squares.append(square)

        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("Square values:", squares)
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)


square_and_filter(1, 10)

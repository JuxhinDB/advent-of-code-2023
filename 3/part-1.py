import sys

with open(sys.argv[1]) as input_:
    lines = input_.readlines()

    length = len(lines)
    width = len(lines[0])

    # Scan for numbers in line
    numbers = []
    grid = [[col for col in row if col != '\n'] for row in lines]

    number_region = False
    for row_idx, line in enumerate(lines):
        buffer = ''

        for col_idx, c in enumerate(line):
            if c.isdigit():
                number_region = True
                buffer += c
            elif number_region: # We are now exiting the number region
                number_region = False

                # Append the coordinates to the first digit of the found number
                numbers.append((row_idx, col_idx - len(buffer), int(buffer)))
                buffer = ''  # Reset the buffer
            else:
                continue  # We are in an uninteresting region

    print(f'Numbers: {numbers}')

    # Points to fetch:
    #  x - 1, y
    #  x - 1, y - 1
    #  x - 1, y + 1
    #  x + 1, y
    #  x + 1, y - 1
    #  x + 1, y + 1
    #  y - 1, x
    #  y + 1, x
    total = 0
    for number in numbers:
        symbols = []
        for x_coord in range(number[1], number[1] + len(str(number[2]))):
            for y in range(-1, 2):
                    y = number[0] + y
                    for x in range(-1, 2):
                        x = x_coord + x
                        try:
                            symbols.append(grid[y][x])
                        except IndexError:
                            # We're lazy, don't bother calculating bounds,
                            # just proceed to next iteration
                            pass
        if any([not x.isalnum() for x in set(symbols) - {'.'}]):
            print(f'Symbols for number {number} is {set(symbols)}')
            total += number[2]

    print(f'Result: {total}')


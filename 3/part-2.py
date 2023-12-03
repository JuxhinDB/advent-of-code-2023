import sys
import itertools

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

    total = 0
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if grid[row_idx][col_idx] == '*':
                # Look for adjacent numbers to see if we have any gears
                result = []
                for (x, y) in itertools.product(
                        range(row_idx - 1, row_idx + 2), 
                        range(col_idx - 1, col_idx + 2)):
                    try:
                        if grid[x][y].isdigit():
                            for n in numbers:
                                if n[0] == x and any([col == y for col in range(n[1], n[1] + len(str(n[2])))]):
                                    result.append(n)
                    except IndexError:
                        pass

                result = list(set(result))
                if len(result) == 2:
                    total += result[0][2] * result[1][2]

    print(f'Result: {total}')


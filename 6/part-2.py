import sys

with open(sys.argv[1]) as input_:
    lines = [x.replace('\n', '') for x in input_.readlines()]
    time = int(''.join(lines[0].split(':')[1].split(None)))
    distance = int(''.join(lines[1].split(':')[1].split(None)))
    
    counter = 0
    for pressed in range(0, time):
        if pressed * (time - pressed) > distance:
            counter += 1

    print(f'Result: {counter}')


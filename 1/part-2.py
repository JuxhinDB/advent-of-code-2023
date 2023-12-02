import sys

map_ = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

with open(sys.argv[1]) as input_:
    outer = 0

    for line in input_.readlines():
        line = line.replace('\n', '')
        inner = ''

        offset = 0
        while offset < len(line):
            buf = ''
            slice = line[offset:]

            if slice[0].isdigit():
                inner += slice[0]
                buf = ''
            else:
                for c in slice:
                    buf += c
                    if num := map_.get(buf):
                        inner += num 
                        offset += len(buf) - 2

            offset += 1

        increment = int(inner[0] + inner[-1])
        outer += increment 
        print(f'Line: {line}, Inner: {inner}, increment: {increment}, Outer: {outer}')

    print(f'Result part 2: {outer}')



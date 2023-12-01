import sys

file_path = sys.argv[1]

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

with open(file_path) as input_:
    parts = [
      (lambda x: int(x[0] + x[-1]))
      ([char for char in line if char.isdigit()]) 
      for line in input_.readlines()
    ]
    print(f'Result part 1: {sum(parts)}')

    outer = 0

    for line in input_.readlines():
        line = line.replace('\n', '')
        inner = ''

        offset = 0
        while offset < len(line):
            buf = ''
            slice = line[offset:]
            #print(f'slice: {slice}')

            if slice[0].isdigit():
                inner += slice[0]
                buf = ''
            else:
                for c in slice:
                    buf += c
                    if num := map_.get(buf):
                        #print(f'found: {num}')
                        inner += num 
                        offset += len(buf) - 2

            offset += 1

        print(f'Inner: {inner} for Line: {line}')

        outer += int(inner[0] + inner[-1]) if len(inner) > 1 else int(inner[0])

    print(f'Result part 2: {outer}')


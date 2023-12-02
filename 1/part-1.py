import sys

with open(sys.argv[1]) as input_:
    parts = [
      (lambda x: int(x[0] + x[-1]))
      ([char for char in line if char.isdigit()]) 
      for line in input_.readlines()
    ]
    print(f'Result part 1: {sum(parts)}')

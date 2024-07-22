print("\nNormal Pyramid")
for i in range(1, 6):
    x = '*' * (2*i - 1)
    print(f'{x:^10}')

print("\nInverted Pyramid")
for i in range(5, 0, -1):
    x = '*' * (2*i - 1)
    print(f'{x:^10}')

print("\nLeft sided Pyramid")
for i in range(1, 6):
    x = '*' * i
    print(f'{x:<10}')

print("\nRight sided Pyramid")
for i in range(1, 6):
    x = '*' * i
    print(f'{x:>10}')

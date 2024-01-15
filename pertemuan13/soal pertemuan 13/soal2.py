def f(x):
    return x*x + 5*x - 6

# Program Utama
print('----------------------------')
print('   x     |    f(x)   ')
print('----------------------------')

x = 8
while x <= 13:
    print(f'   {x}     |    {f(x)}   ')
    x = x + 1

print('----------------------------')

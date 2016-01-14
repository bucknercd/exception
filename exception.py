import sys

def fact(n):
    if n < 0:
        raise ArithmeticError('a negative factorial has no value')
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

quit = ['q','Q','quit','exit']
while True:
    num = raw_input('Enter an integer to calculate the factorial value or q to quit\n').strip()
    if num in quit:
        sys.exit()
    try:
        num = int(num)
    except ValueError as e:
        print 'cannot parse {0} to an int!'.format(num)
	print e
    try:
        ans = fact(num)
        print 'Answer: {0}'.format(ans)
    except ArithmeticError as e:
        print e
	continue
    except TypeError as e:
        print e


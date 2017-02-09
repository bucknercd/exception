
from Errors import OperatorException
import sys

def binmath(b1,op,b2):
	valid_len1 = len(b1)
	valid_len2 = len(b2)
	count1 = 0
	count2 = 0
	valid = '01'
	valid_ops = ['+','-','*','^']
	for i in b1:
		if i in valid:
			count1+=1
	for i in b2:
		if i in valid:
			count2+=1
	if valid_len1 != count1 or valid_len2 != count2:
		raise ArithmeticError('this is not valid binary')
	elif op not in valid_ops:
		raise OperatorException('this is not a valid operator')
	else:
		d1 = int(b1,2)
		d2 =  int(b2,2)
		if op == '+':
			ans = d1 + d2
		elif op == '-':
			ans = d1 - d2
		elif op == '*':
			ans = d1 * d2
		elif op == '^':
		    ans = d1 ** d2
	ans = bin(ans)
	if ans.startswith('-'):
		ans = ans[0:1] + ans[3:]
	else:
		ans = ans[2:]
	return ans


while True:
    try:
        line  = raw_input('Enter a binary operation or q to exit.\n>').strip()
    except EOFError as e:
        sys.exit()
    try:
        option = line[0]
        if line == 'q' or line == 'Q' or line == 'quit'or line == 'exit':
	    sys.exit()
    except IndexError as e:
	print e
	print 'You must enter something.'
	continue
    try:
        var1, operation, var2 = line.split(' ')
    except ValueError as e:
        print e
	continue
    try:
        ans = binmath(var1, operation, var2)
    except ArithmeticError as e:
        print e
	continue
    except OperatorException as e:
        print e
	continue
    print '{0} {1} {2} = {3}\n'.format(var1, operation, var2, ans)
    

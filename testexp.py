expression_num = '22/7'
num, den = expression_num.split( '/' )
print(num, ' and ', den)
answer_number = str(round((float(num)/float(den)), 2))
print('Answer is', answer_number)
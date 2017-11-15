while True:
	try:
		first_number = input('\nfirst number??:')
	
		if first_number == 'q':
				break
		second_number = input('\nsecond number??:')
		if second_number == 'q':
				break
		operator = input("\noperator type by ' ' ")
		answer = int(first_number) + int(second_number)
	except ValueError:
		MSG='SORYAN YOU CALCULATE NOT CALCULABLE'
		print(MSG)
		if operator == '/':
			answer= int(first_number) / int(second_number)
		if operator == '+':
			answer=int(first_number) + int(second_number)
		elif operator == '-':
			operator =int(first_number) - int(second_number)
		elif operator == '*':
			answer= int(first_number) * int(second_number)
print('answer '+answer)
def is_dig(n):
	try:
		float(n)
		return 'Yes'
	except ValueError:
		return 'No'
print(is_dig(input()))

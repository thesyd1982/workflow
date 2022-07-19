def momoize(func):
	memoized = {}

	def inner(number):
		if number not in memoized:
			memoized[number] = func(number)
		return memoized[number]

	return inner

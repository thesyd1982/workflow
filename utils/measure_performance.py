from functools import wraps
from time import time
from datetime import timedelta


def measure(func):
	@wraps(func)
	def _time_it(*args, **kwargs):
		start = int(round(time() * 1000))
		try:
			return func(*args, **kwargs)
		finally:
			end_ = int(round(time() * 1000)) - start

			print(f"Total execution time of {func.__name__ }: {str(timedelta(seconds=end_//1000))}")
			print(f"Total execution time of {func.__name__}: {end_ if end_ > 0 else 0} ms")

	return _time_it


if __name__ == '__main__':
	@measure
	def hello():
		for i in range(200):
			print('hello world')


	hello()

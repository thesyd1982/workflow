from utils.pandas_extension import flatten_dict
import pandas as pd
import os
from abc import ABC, abstractmethod


class WritingStrategy(ABC):
	@abstractmethod
	def write(self, filename, obj):
		pass


class CSVWritingStrategy(WritingStrategy):

	def __init__(self, sep=','):
		self.sep = sep

	def write(self, filename, obj):
		obj = flatten_dict(obj, sep='_')
		df_ = pd.DataFrame([obj])

		if os.path.exists(filename):
			df_.to_csv(filename, mode='a', sep=self.sep, index=False, header=False, encoding='utf8')
		else:
			df_.to_csv(filename, sep=self.sep, index=False, encoding='utf8')


pass


class XLSXWritingStrategy(WritingStrategy):

	def __init__(self, sep=','):
		self.sep = sep

	def write(self, filename, obj):
		obj = flatten_dict(obj, sep='_')
		df_ = pd.DataFrame([obj])

		if os.path.exists(filename):
			df_.to_excel(filename, mode='a', index=False, header=False, encoding='utf8')
		else:
			df_.to_excel(filename, index=False, encoding='utf8')


pass

class FileWriter(ABC):
	def __init__(self, filename, obj):
		self.filename = filename
		self.obj = obj

	# self.writingStrategy = CSVWritingStrategy()
	def set_writing_strategy(self, strategy):
		self.writingStrategy = strategy

	def write(self):
		self.writingStrategy.write(self.filename, self.obj)


class CSVWriter(FileWriter):
	def __init__(self, filename, obj):
		super().__init__(filename, obj)
		self.writingStrategy = CSVWritingStrategy(sep=',')


pass


class XLSXWriter(FileWriter):
	def __init__(self, filename, obj):
		super().__init__(filename, obj)
		self.writingStrategy = XLSXWritingStrategy()


pass


class JsonWriter(FileWriter):
	def __init__(self, filename, obj):
		super().__init__(filename, obj)
		self.writingStrategy = JSONWritingStrategy()


class JSONWritingStrategy(WritingStrategy):

	def write(self, filename, obj):
		df_ = pd.DataFrame([obj])
		if os.path.exists(filename):
			df_.to_json(filename, orient='records')
		else:
			df_.to_json(filename, orient='records')


pass

# def append_object_to_csv(obj_, csvfilename, sep=',', header=False):
# 	obj = flatten_dict(obj_, '_')
# 	df_ = pd.DataFrame([obj])
# 	df_.to_csv(csvfilename, mode='a', index=False, header=header, sep=sep, encoding='utf8')
#
#
# def write_object_to_csv(csv_filename_, obj_):
# 	if not os.path.exists(csv_filename_):
# 		df_ = pd.DataFrame([flatten_dict(obj_, sep='_')])
# 		df_.to_csv(csv_filename_, index=False)
# 	append_object_to_csv(obj_, csvfilename=csv_filename_)


if __name__ == '__main__':
	fw = FileWriter("../output/test.json", {"nom": "Douakha", "prenom": "salah"})
	XLSXWriter("../output/test.xlsx", {"nom": "Douakha", "prenom": "salah"}).write()
	strategy = JSONWritingStrategy()
	fw.set_writing_strategy(strategy)
	fw.write()

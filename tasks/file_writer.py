from utils.write_oject_list_on_csv_file import write_object_list_on_csvfile


def write_data(self):
	print(f'Running : {self.name}')
	with open(self.data_output, mode='a', encoding='utf-8') as f:
		try:
			self.data_input = self.get_last_workflow_result()
			f.write(str(self.data_input) + '\n')
			return self.data_output
		except Exception as ex:
			print(str(ex))
			pass
	pass


def write_list_to_csv(self):
	print(f'Running : {self.name}')
	try:
		self.data_input = self.get_last_workflow_result()
		write_object_list_on_csvfile(self.data_input, self.data_output)
		return self.data_output
	except Exception as ex:
		print(str(ex))
		pass






from csv import reader


def read_data(self):
	print(f'Running : {self.name}')
	with open(self.data_input, mode='r', encoding='utf-8') as f:
		self.data_output = f.read()
	pass
	return self.data_output


def read_csv_last_workflow_result(self):
	print(f'Running : {self.name}')
	self.data_output = []
	if self.data_input == '':
		self.data_input = self.get_last_workflow_result()

	with open(self.data_input, 'r') as read_obj:
		csv_reader = reader(read_obj)
		for row in csv_reader:
			self.data_output += row
	print(self.data_output)





	return self.data_output

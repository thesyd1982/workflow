from utils.email_validator import validate_emails


def check_emails(self):
	print(f'Running : {self.name}')
	if self.data_input == '':
		self.data_input = self.get_last_workflow_result()
	self.data_output = validate_emails(self.data_input)
	return self.data_output


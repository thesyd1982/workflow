from core.Task import Task
from core.workflow import Workflow
from tasks.file_writer import write_data, write_list_to_csv
from tasks.file_reader import read_data, read_csv_last_workflow_result
from tasks.get_emails import get_emails, check_url
from tasks.get_linkedin_links import links_from_sales_list
from tasks.validate_emails import check_emails
import json


def load_config(filename):
	workflows_ = []
	with open(filename, encoding='utf-8') as f:
		data = json.load(f)
		for wf_ in data:
			workflow_name = wf_['workflow']['name']
			workflow_tasks = wf_['workflow']['tasks']
			workflow_ = Workflow(workflow_name)
			for tsk_ in workflow_tasks:
				task_name = tsk_['task']['name']
				task_input = tsk_['task']['data_input']
				task_output = tsk_['task']['data_output']
				module = __import__(tsk_['task']['module'])
				func = getattr(module, tsk_['task']['function'])

				check_ready = tsk_['task']['check_ready']
				if check_ready:
					check_ready = getattr(module, check_ready)

				task_ = Task(
					name=task_name,
					function=func,
					check_ready=check_ready,
					data_input=task_input,
					data_output=task_output
				)

				workflow_.append_child(task_)
			workflows_.append(workflow_)
	return workflows_


if __name__ == '__main__':

	workflows = load_config('config/cvfile_from_validation_list_of_emails.json')
	for wf in workflows:
		wf.execute()
		print(wf.results)



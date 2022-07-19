from utils.file_writer import CSVWriter

def write_object_list_on_csvfile(objects, filename):
	[CSVWriter(filename=filename, obj=obj).write() for obj in objects]
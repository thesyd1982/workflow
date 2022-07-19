from dotenv import load_dotenv, find_dotenv
from bots.Bot_chrome import Bot


def check_url(self):
	if not self.data_input['url']:
		print('url manquante')
		return False
	return True


def get_emails(self):
	print(f'Task : {self.name}')
	self.launch()
	load_dotenv(find_dotenv())
	bot = Bot(mobile=False)
	bot.go_to_url(self.data_input['url'])
	self.data_output = bot.get_emails()
	self.pause()
	self.resume()
	self.finish()

	return self.data_output

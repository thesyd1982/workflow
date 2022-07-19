from bots.Bot_chrome import Bot
from bots.linkedin_sales_list import extract_linkedin_links_from_sales
from utils.measure_performance import measure
import os
from dotenv import load_dotenv, find_dotenv


def links_from_sales_list(self):
	print(f'Task : {self.name}')
	sales_list_start_page = self.data_input

	load_dotenv(find_dotenv())
	cookie = {
		'name': os.getenv('LI_AT_NAME'),
		'value': os.getenv('LI_AT_GILLES'),
		'path': '/',
		'domain': '.www.linkedin.com'
	}

	bot = Bot(mobile=False)
	bot.connect_with_cookie(cookie)

	button_css_selector = 'button[aria-label="Suivant"]'

	urls = extract_linkedin_links_from_sales(
		bot_=bot,
		sales_list_start_page_=sales_list_start_page,
		stop_selector_=button_css_selector
	)
	bot.quit()
	profiles = [{'LINKEDIN': url} for url in urls]

	self.data_output = profiles
	return self.data_output


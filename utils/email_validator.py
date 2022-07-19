from time import time

from validate_email import validate_email

def is_valid_email(email):
	result = validate_email(email, True, True, debug=True, smtp_timeout=1)
	if result:
		return {'email': email, "validity": "Valid", "success": True}
	elif result is None:
		return {'email': email, "validity": "Risky", "success": True}
	else:
		return {'email': email, "validity": "Invalid", "success": False}
	time.sleep(1)


def validate_emails(emails):
	return [is_valid_email(email) for email in emails]


if __name__ == '__main__':
	print(validate_emails(['salah.yacine.douakha@gmail.com', 'salah.douakha@permisdebouger.com']))

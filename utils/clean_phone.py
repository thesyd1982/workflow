def clean_phone(phone_raw):
	if type(phone_raw) == float:
		phone_raw = int(phone_raw)
	phone_raw = str(phone_raw)
	if not phone_raw:
		return {'success': False, 'phone': ''}
	final = ""
	result = phone_raw.strip()
	result = ''.join([x for x in result if x.isdigit()]).strip()
	if result[:2] == '33' and len(result) > 9:
		result = result[2:]
	if result[:4] == '0033':
		result = result[4:]
	if len(result) == 9:
		result = '0' + result
	if len(result) == 10 and result[0] == '0':
		for o, y in enumerate(result):
			if o % 2 == 0:
				final += y

			else:
				final += y + ' '
		if final[-1] == ' ':
			final = final[:-1]
		return {'success': True, 'phone': final}
	else:
		return {'success': False, 'phone': phone_raw}

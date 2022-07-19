def empty_if_none(s):
	return '' if not s else s


def replace_sep(s, sep=',', char='.'):
	return s.replace(sep, char)

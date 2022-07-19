
import re

def phone_pattern():
	"""
			\+\d{2}[-.\s]?(?:\(0\)|0)*?[-.\s]?          # Dialing code +CC00(0) or +CC00 or +CC00 0
			00[-.\s]?\d{2}[-.\s]?(?:\(0\)|0)*?[-.\s]?   # Dialing code 0033 \(0)|0
			(?:\(0\)|0|)\d?[-.\s]?                      # First number (from 1 to 9) preceeded by a non mandatory 0 or (0)
			(?:\d{2}[-.\s]?){3,4})                      # End of the phone number (3 or 4 times 2 following digits separated or not by .- )
			(?:$|\D)                                    # Anything but a number or the end of string
	:return:
	"""
	# To be improved to make the 0 mandatory when +33 or 00 is missing. Ex it will match 234558899
	return re.compile('(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})')
	# This version should tka)
	#return re.compile(
	#	'((?:\+\d{2}[-.\s]?(?:\(0\)|0)*?[-.\s]?|00[-.\s]?\d{2}[-.\s]?(?:\(0\)|0)*?[-.\s]?|0)\d?[-.\s]?(?:\d{2}[-.\s]?){3,4})(?:$|\D)')
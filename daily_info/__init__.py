#!/usr/bin/env python3

def main_run(date_of_birth:str) -> int:
	""" Main `daily_info` run """
	from . import gui_window
	from . import numerology
	from . import horoscope

	try:
		# Initialize objects & create the text from their data.
		dh, dn = horoscope.DailyHoroscope(date_of_birth), numerology.DailyNumber(date_of_birth)
		text = '\n'.join(f'\n ~ {o!r} ~\n\n{o!s}' for o in (dh, dn)) + '\n'

		# Create the GUI with text.
		gui = gui_window.Gui('Horoscope & Numerology', text)
		gui.button_click()
		gui.run()
	except:
		from traceback import format_exc
		print(format_exc())
		return 1
	return 0

def main() -> int:
	from gui_window import Gui
	from numerology import DailyNumber
	from horoscope import DailyHoroscope

	try:
		date_input: str = str(input('Enter your date of birth (YYYY-MM-DD): '))
		default_date: str = '1991-01-31'
		date = date_input if len(date_input) > 0 else default_date

		txt: str = '\n'
		txt = txt.join(f'{txt} ~ {repr(i)} ~{txt}{txt}{i}' for i in (DailyHoroscope(date), DailyNumber(date))) + txt

		gui: Gui = Gui('Horoscope & Numerology', txt)
		gui.button_click()
		gui.run()

	except:
		from traceback import format_exc
		print(format_exc())
		return 1

	return 0

if __name__ == '__main__':
	from sys import exit
	code:int = main()
	exit(code)

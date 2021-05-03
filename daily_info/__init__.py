def main_run(argv:list[str]) -> int:
	try:
		if __name__ == '__main__':
			from gui_window import Gui
			from numerology import DailyNumber
			from horoscope  import DailyHoroscope
		else:
			from .gui_window import Gui
			from .numerology import DailyNumber
			from .horoscope  import DailyHoroscope

		date: str
		txt: str
		gui: Gui

		if len(argv) > 1 and len(argv[1]) > 0:
			date = argv[1]
		else:
			input_date: str = str(input('Please enter your date of birth (YYYY-MM-DD): '))
			date = input_date if len(input_date) > 0 else '1991-01-31'

		txt = '\n'.join(f'\n ~ {repr(i)} ~\n\n{i}' for i in (DailyHoroscope(date), DailyNumber(date))) + '\n'

		gui = Gui('Horoscope & Numerology', txt)
		gui.button_click()
		gui.run()

	except:
		from traceback import format_exc

		print(format_exc())
		return 1

	return 0


if __name__ == '__main__':
	from sys import exit, argv

	code: int = main_run(argv)
	exit(code)

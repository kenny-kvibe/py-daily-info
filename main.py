def main(argv:list[str]) -> int:
	try:
		from gui_window import Gui
		from numerology import DailyNumber
		from horoscope import DailyHoroscope

		def get_input_date() -> str:
			input_date: str = str(input('Please enter your date of birth (YYYY-MM-DD): '))
			return '1991-01-31' if len(input_date) == 0 else input_date

		date: str = get_input_date() if len(argv) <= 1 else str(argv[1])

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
	from sys import exit, argv
	code: int = main(argv)
	exit(code)

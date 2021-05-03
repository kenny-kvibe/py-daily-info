def main() -> int:
	from gui_window import Gui
	from numerology import DailyNumber
	from horoscope import DailyHoroscope
	try:
		d: str = '1990-01-31'
		t: str = '\n'
		t = t.join(f'{t} ~ {repr(i)} ~{t+t}{i}' for i in (DailyHoroscope(d), DailyNumber(d)))+t
		gui: Gui = Gui('Horoscope & Numerology', t)
		gui.button_click()
		gui.run()
	except:
		from traceback import print_exc
		print_exc()
		return 1
	return 0

if __name__ == '__main__':
	from sys import exit
	code:int = main()
	exit(code)

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

		default_date: str = '1991-01-31'
		env_date: str
		date_len: int = 10
		date: str
		text: str
		gui: Gui

		try:
			# Load the `.env` file variables.
			from os import getenv, environ
			from dotenv import find_dotenv, load_dotenv

			env_var: str = 'DATE_OF_BIRTH'
			env_path: str = str(find_dotenv(filename='.env'))
			env_loaded: bool = load_dotenv(dotenv_path=env_path)

			env_date = environ[env_var] if (env_loaded and env_var in environ.keys()) else str()
		except KeyError:
			env_date = str()

		# Check user input (from `.env`, `argv[]` or `input()`) & set the date from it.
		if len(env_date) >= date_len:
			date = env_date.strip()
		elif len(argv) >= 2 and len(argv[1]) >= date_len:
			date = argv[1].strip()
		else:
			input_date: str = input('Please enter your date of birth (YYYY-MM-DD): ').strip()
			date = input_date if len(input_date) >= date_len else default_date

		# Initialize objects & create the text from their data.
		text = '\n'.join(f'\n ~ {repr(i)} ~\n\n{i}' for i in (DailyHoroscope(date), DailyNumber(date))) + '\n'

		# Create the GUI with text.
		gui = Gui('Horoscope & Numerology', text)
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

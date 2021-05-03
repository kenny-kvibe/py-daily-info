from datetime import datetime
from json import loads as json_loads
from dataclasses import dataclass, field, InitVar

@dataclass(repr=False)
class DailyHoroscope:
	"""\n# Get your Daily Horoscope of today.\n"""

	_birth_date: InitVar[str] = field()
	_new_date:   InitVar[str] = field(default=str())
	_file_name:  InitVar[str] = field(default=str())

	_run:   InitVar[bool] = field(default=True)
	_print: InitVar[bool] = field(default=False)


	def __post_init__(self, _birth_date:str, _new_date:str, _file_name:str, _run:bool, _print:bool) -> None:
		"""\n\n#### Daily Horoscope\n
		Fetch your Daily Horoscope from an URL for today based on provided `_birth_date` argument.\n
		(Today's date is used if the `_new_date` argument is an empty string.)\n
		Example Usage:\n
		```py
		birth: str = '1990-12-31'
		dh = DailyHoroscope(birth)
		dh.print()
		```\n
		"""
		self.log: list[str] = list()

		self.description: str = ''
		self.sun_sign: str
		self.url: str

		self.new_date: datetime
		self.birth_date: datetime
		self.set_dates(_birth_date, _new_date)

		self.json_path: str
		self.json_data: list[dict[str, str]]
		self.json_name: str = 'horoscope-dates.json'
		self.load_json(_file_name)

		if _run == True:
			self.run()
		else:
			self.update_info()
			self.log.append('Info - Dates are saved but no description was fetched.')

		if _print == True:
			self.print()
			if len(self.log) > 0:
				self.print_logs()


	@property
	def dates(self) -> str:
		return f'{self.birth_date:%d.%b.%Y}, {self.new_date:%d.%b.%Y}'


	def set_dates(self, birth_date:str='', new_date:str='') -> None:
		"""\nUpdates the date with the provided argument while checking if it's in the ISO format '`YYYY-MM-DD`'.\n"""
		_now: datetime = datetime.now()
		self.new_date = _now

		if new_date != '':
			try:
				self.new_date = datetime.fromisoformat(new_date)
			except:
				self.new_date = _now
				self.log.append('Error - Argument \'new_date\' is not in ISO format (YYYY-MM-DD), using today\'s date.')

		if birth_date != '':
			try:
				self.birth_date = datetime.fromisoformat(birth_date)
			except:
				self.birth_date = self.new_date
				self.log.append('Error - Argument \'birth_date\' is not in ISO format (YYYY-MM-DD), using the \'new_date\' date.')
		else:
			self.birth_date = self.new_date


	def load_json(self, json_name:str) -> None:
		"""\nLoads horoscope dates from JSON file.\n"""
		from os.path import (join as join_path, dirname)

		_json_name: str = join_path('data', self.json_name)
		if len(json_name) > 0:
			_json_name = json_name
		self.json_path = join_path(dirname(__file__), _json_name)
		self.json_data = []

		try:
			_str: str
			with open(self.json_path, 'r') as _file:
				_str = _file.read()

			if len(_str) <= 2:
				raise Exception

			self.json_data = json_loads(_str)
		except:
			self.log.append(f'Error - JSON File \'{self.json_path}\' wasn\'t used.')


	def request_info(self) -> None:
		"""\nFetches the horoscope description from an URL and saves it as `dict`.\n"""
		from requests import (post as post_req, models as reqmodels)

		self.description = ''
		self.update_info()

		try:
			_response: reqmodels.Response = post_req(self.url)

			if _response.status_code == 200:
				from bs4 import BeautifulSoup

				_bs_string: str = BeautifulSoup(_response.text, features="lxml").find('script', { 'type': 'application/ld+json' }).string
				_bs_json: dict[str, str] = json_loads(_bs_string)

				self.description = _bs_json['articleBody'].encode('utf-8').replace(b'\xe2\x80\x99', b'\'').decode('utf-8')
		except:
			self.log.append(f'Error - Website \'{self.url} is Unreachable.')


	def update_info(self) -> None:
		"""\nUpdates the description and the sun sign`*` based on the birth date.\n(`*` => if the json file was loaded)\n"""
		self.sun_sign = self.json_data[0]['name']

		_data: tuple[list[str], list[str]]
		_in_range: object = lambda _, _begin, _end: _ >= _begin and _ <= _end

		for i in range(len(self.json_data)):
			_data = (self.json_data[i]['begin'].split('-'), self.json_data[i]['end'].split('-'))

			if _in_range(self.birth_date.month, int(_data[0][0]), int(_data[1][0])):
				if _in_range(self.birth_date.day, int(_data[0][1]), int(_data[1][1])):
					self.sun_sign = self.json_data[i]['name']
				else:
					self.sun_sign = self.json_data[int(i + 1 if i < len(self.json_data) else 0)]['name']
				break

		_params: str = f'{self.sun_sign.lower()}/{self.new_date:%Y-%m-%d}'
		self.url = f'https://www.tarot.com/daily-horoscope/{_params}'


	def print_logs(self) -> None:
		"""\nPrints each log in [] brackets on its line.\n"""
		if len(self.log) > 0:
			for log in self.log:
				print(f'[{log}]')


	def print(self, show_source:bool=False):
		"""\nPrints '`self`' as string, with optional url-source.\n"""
		_string: str = str(self)
		if show_source == True:
			_string += f'\n# Source: {self.url}'
		print(_string)


	def __repr__(self) -> str:
		"""\nReturns dates arguments of the Class as a string.\n"""
		return f'DailyHoroscope({self.dates}, {self.sun_sign.capitalize()})'


	def __str__(self):
		"""\nReturns the fetched Horoscope info`*` with dates or just the dates.\n(`*` => if the data was fetched)\n"""
		if self.description != '':
			return f'Your Daily Horoscope, {self.sun_sign.capitalize()}.\n{self.description}'
		return f'Daily Horoscope [{self.dates}]'


	def run(self):
		"""\nUpdates the info, fetches the horoscope description and returns self.\n"""
		self.request_info()
		return self



# =======================================================================================================================

if __name__ == '__main__':
	from sys import exit
	from traceback import format_exc

	def test() -> None:
		dh: DailyHoroscope
		dh = DailyHoroscope('1991-12-31')
		dh.print()
		dh.print_logs()

	try: test()
	except: print(format_exc())
	finally: exit(0)

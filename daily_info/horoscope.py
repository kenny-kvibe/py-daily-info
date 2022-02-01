#!/usr/bin/env python3
import bs4
import datetime as dt
import dataclasses as d
import json
import os.path
import requests


@d.dataclass(repr=False)
class DailyHoroscope:
	"""
# Get your Daily Horoscope of today.
Fetch your Daily Horoscope from an URL for today based on provided `_birth_date` argument.
(Today's date is used if the `_target_date` argument is an empty string.)
Example Usage:
```py
birth: str = '1990-12-31'
dh = DailyHoroscope(birth)
dh.print()
```
	"""

	_birth_date:  d.InitVar[str] = d.field()
	_target_date: d.InitVar[str] = d.field(default=str())
	_file_name:   d.InitVar[str] = d.field(default=str())

	_run:   d.InitVar[bool] = d.field(default=True)
	_print: d.InitVar[bool] = d.field(default=False)

	def __post_init__(self, _birth_date:str, _target_date:str, _file_name:str, _run:bool, _print:bool) -> None:
		""" Daily Horoscope """
		self.log: list[str] = list()

		self.description: str = ''
		self.sun_sign: str
		self.url: str

		self.target_date: dt.datetime
		self.birth_date: dt.datetime
		self.set_dates(_birth_date, _target_date)

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
		""" `dates` property (birth_date, target_date) """
		return f'{self.birth_date:%d.%b.%Y}, {self.target_date:%d.%b.%Y}'

	def set_dates(self, birth_date:str='', target_date:str='') -> None:
		"""
		Updates the date with the provided argument while
		checking if it's in the ISO format '`YYYY-MM-DD`'.
		"""

		_now: dt.datetime = dt.datetime.now()
		self.target_date = _now

		if target_date != '':
			try:
				self.target_date = dt.datetime.fromisoformat(target_date)
			except:
				self.target_date = _now
				self.log.append('Error - Argument \'target_date\' is not in ISO format (YYYY-MM-DD), using today\'s date.')

		if birth_date != '':
			try:
				self.birth_date = dt.datetime.fromisoformat(birth_date)
			except:
				self.birth_date = self.target_date
				self.log.append('Error - Argument \'birth_date\' is not in ISO format (YYYY-MM-DD), using the \'target_date\' date.')
		else:
			self.birth_date = self.target_date

	def load_json(self, json_name:str) -> None:
		""" Loads horoscope dates from JSON file. """

		_json_name: str = os.path.join('data', self.json_name)
		if len(json_name) > 0:
			_json_name = json_name
		self.json_path = os.path.join(os.path.dirname(__file__), _json_name)
		self.json_data = []

		try:
			_str: str
			with open(self.json_path, 'r') as _file:
				_str = _file.read()

			if len(_str) <= 2:
				raise Exception

			self.json_data = json.loads(_str)
		except:
			self.log.append(f'Error - JSON File \'{self.json_path}\' wasn\'t used.')

	def request_info(self) -> None:
		""" Fetches the horoscope description from an URL and saves it as `dict`. """

		self.description = ''
		self.update_info()

		try:
			_response: requests.models.Response = requests.post(self.url)

			if _response.status_code == 200:

				_bs_string: str = str(bs4.BeautifulSoup(_response.text, features="lxml").find('script', { 'type': 'application/ld+json' }).string)
				_bs_json: dict[str, str] = json.loads(_bs_string)

				self.description = _bs_json['articleBody'].encode('utf-8').replace(b'\xe2\x80\x99', b'\'').decode('utf-8')
		except Exception as e:
			print(e)
			self.log.append(f'Error - Website \'{self.url} is Unreachable.')

	def update_info(self) -> None:
		"""
		Updates the description and the sun sign`*` based on the birth date.
		(`*` if the json file was loaded)
		"""
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

		_params: str = f'{self.sun_sign.lower()}/{self.target_date:%Y-%m-%d}'
		self.url = f'https://www.tarot.com/daily-horoscope/{_params}'

	def print_logs(self) -> None:
		""" Prints each log in [] brackets on its line. """
		if len(self.log) > 0:
			for log in self.log:
				print(f'[{log}]')

	def print(self, show_source:bool=False) -> None:
		""" Prints '`self`' as string, with optional url-source. """
		_string: str = str(self)
		if show_source == True:
			_string += f'\n# Source: {self.url}'
		print(_string)

	def __repr__(self) -> str:
		""" Returns dates arguments of the Class as a string. """
		return f'DailyHoroscope({self.dates}, {self.sun_sign.capitalize()})'

	def __str__(self) -> str:
		"""
		Returns the fetched Horoscope info`*` with dates or just the dates.
		(`*` if the data was fetched)
		"""
		if self.description != '':
			return f'Your Daily Horoscope, {self.sun_sign.capitalize()}.\n{self.description}'
		return f'Daily Horoscope [{self.dates}]'

	def run(self) -> ...:
		""" Updates the info, fetches the horoscope description and returns self. """
		self.request_info()
		return self


# =======================================================================================================================

if __name__ == '__main__':
	from traceback import format_exc

	def test() -> None:
		dh: DailyHoroscope
		dh = DailyHoroscope('1999-01-31')
		dh.print()
		dh.print_logs()

	try: test()
	except: print(format_exc())
	finally: raise SystemExit(0)

#!/usr/bin/env python3
import datetime as dt
import dataclasses as d
import json
import os.path


@d.dataclass(repr=False)
class DailyNumber:
	"""
# Get your Daily Number of a day.
Calculate your Daily Number by adding your birth's day & month to another date's day, month & year.
(Today's date is used if the `_target_date` argument is an empty string.)
Example Usage:
```py
birth_date: str = '1990-12-31'
today_date: str = '2022-01-01'
dn = DailyNumber(birth_date, today_date)
dn.print()
```
	"""

	_birth_date:  d.InitVar[str] = d.field()
	_target_date: d.InitVar[str] = d.field(default=str())
	_file_name:   d.InitVar[str] = d.field(default=str())

	_run:   d.InitVar[bool] = d.field(default=True)
	_print: d.InitVar[bool] = d.field(default=False)


	def __post_init__(self, _birth_date:str, _target_date:str, _file_name:str, _run:bool, _print:bool) -> None:
		""" Daily Number """
		self.log: list[str] = list()

		self.number: int = 0
		self.numbers: tuple
		self.description: str
		self.information: str

		self.target_date: dt.datetime
		self.birth_date: dt.datetime
		self.set_dates(_birth_date, _target_date)

		self.json_path: str
		self.json_data: dict[str, str]
		self.json_name: str = 'number-descriptions.json'
		self.load_json(_file_name)

		if _run == True:
			self.run()
		else:
			self.update_info()
			self.log.append('Info - Dates are saved but no numbers were calculated.')

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
		Updates the dates with the provided arguments while
		checking if they're in the ISO format '`YYYY-MM-DD`'.
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
		"""
		Loads numbers descriptions from JSON file
		containing '`number`' & '`description`' key-value pairs.
		"""

		_json_name: str = os.path.join('data', self.json_name)
		if len(json_name) > 0:
			_json_name = json_name
		self.json_path = os.path.join(os.path.dirname(__file__), _json_name)
		self.json_data = {}

		try:
			_str: str
			with open(self.json_path, 'r') as _file:
				_str = _file.read()

			if len(_str) <= 2:
				raise Exception

			self.json_data = json.loads(_str)
		except:
			self.log.append(f'Error - JSON File \'{self.json_path}\' wasn\'t used, no description will be added.')

	def update_info(self) -> None:
		"""
		Updates the description & information with if-any json-loaded
		description & calculated numbers with dates.
		"""

		_all_nums: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33}
		self.description = ''

		if self.number in _all_nums:
			if len(self.json_data) > 0:
				self.description = self.json_data[f'{self.number}']

			_equation: str = "+".join(str(num) for num in self.numbers)
			self.information = f'Your Daily Number is {self.number}. [{_equation}]'
		else:
			self.information = f'Daily Number [{self.dates}]'

	def calc_numbers(self) -> None:
		"""
		Calculates and the numbers digits of both dates and
		the daily number with the sum of digits of both dates.
		"""
		self.numbers = (
			self.add_digits(self.birth_date.day),
			self.add_digits(self.birth_date.month),
			self.add_digits(self.target_date.day),
			self.add_digits(self.target_date.month),
			self.add_digits(self.target_date.year)
		)
		self.number = self.add_digits(sum(self.numbers))
		self.update_info()

	def add_digits(self, num:int, check:bool=True) -> int:
		"""
		Adds all digits together with filtered master
		numbers and returns the resulted sum.
		"""

		_numbers: tuple[int, ...] = tuple(int(i) for i in str(num))

		if len(_numbers) > 1:
			_num: int = sum(_numbers)
			_mn: set[int] = {11, 22, 33}

			if _num >= 10 and not (_num in _mn and check):
				return sum(int(i) for i in str(_num))

			return _num
		return num

	def print(self) -> None:
		""" Prints '`self`' as string. """
		print(self)

	def print_logs(self) -> None:
		""" Prints each log in [] brackets on its line. """
		if len(self.log) > 0:
			for log in self.log:
				print(f'[{log}]')

	def __repr__(self) -> str:
		""" Returns dates arguments of the Class as a string. """
		return f'DailyNumber({self.dates}, {self.number})'

	def __str__(self) -> str:
		"""
		Returns information and description`*` as a string.
		(`*` if the json file was loaded)
		"""
		return self.information + (f'\n{self.description}' if len(self.description) > 0 else '')

	def __int__(self) -> int:
		""" Returns calculated number, or calculates and returns it. """
		if self.number == 0:
			self.calc_numbers()
		return self.number

	def run(self) -> ...:
		""" Calculates the numbers and returns self. """
		self.calc_numbers()
		return self


# ===========================================================================================================

if __name__ == '__main__':
	from traceback import format_exc

	def test() -> None:
		dn: DailyNumber
		dn = DailyNumber('1999-01-31')
		dn.print()
		dn.print_logs()

	try: test()
	except: print(format_exc())
	finally: raise SystemExit(0)

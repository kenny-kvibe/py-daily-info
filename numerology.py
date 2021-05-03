from datetime import datetime
from json import loads as json_loads
from dataclasses import dataclass, field, InitVar

@dataclass(repr=False)
class DailyNumber:
	"""\n# Get your Daily Number of a day.\n"""

	_birth_date: InitVar[str] = field()
	_new_date:   InitVar[str] = field(default=str())
	_file_name:  InitVar[str] = field(default=str())

	_run:   InitVar[bool] = field(default=True)
	_print: InitVar[bool] = field(default=False)


	def __post_init__(self, _birth_date:str, _new_date:str, _file_name:str, _run:bool, _print:bool) -> None:
		"""\n\n#### Daily Number\n
		Calculate your Daily Number by adding your birth's day & month to another date's day, month & year.\n
		(Today's date is used if the `_new_date` argument is an empty string.)\n
		Example Usage:\n
		```py
		birth: str = '1990-12-31'
		_date: str = '2022-01-01'
		dn = DailyNumber(birth, _date)
		dn.print()
		```\n
		"""
		self.log: list[str] = list()

		self.number: int = 0
		self.numbers: tuple
		self.description: str
		self.information: str

		self.new_date: datetime
		self.birth_date: datetime
		self.set_dates(_birth_date, _new_date)

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
		return f'{self.birth_date:%d.%b.%Y}, {self.new_date:%d.%b.%Y}'


	def set_dates(self, birth_date:str='', new_date:str='') -> None:
		"""\nUpdates the dates with the provided arguments while checking if they're in the ISO format '`YYYY-MM-DD`'.\n"""
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
		"""\nLoads numbers descriptions from JSON file containing '`number`' & '`description`' key-value pairs.\n"""
		from os.path import (join as join_path, dirname)

		_json_name: str = join_path('data', self.json_name)
		if len(json_name) > 0:
			_json_name = json_name
		self.json_path = join_path(dirname(__file__), _json_name)
		self.json_data = {}

		try:
			_str: str
			with open(self.json_path, 'r') as _file:
				_str = _file.read()

			if len(_str) <= 2:
				raise Exception

			self.json_data = json_loads(_str)
		except:
			self.log.append(f'Error - JSON File \'{self.json_path}\' wasn\'t used, no description will be added.')


	def update_info(self) -> None:
		"""\nUpdates the description & information with if-any json-loaded description & calculated numbers with dates.\n"""
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
		"""\nCalculates and the numbers digits of both dates and\nthe daily number with the sum of digits of both dates.\n"""
		self.numbers = (
			self.add_digits(self.birth_date.day),
			self.add_digits(self.birth_date.month),
			self.add_digits(self.new_date.day),
			self.add_digits(self.new_date.month),
			self.add_digits(self.new_date.year)
		)
		self.number = self.add_digits(sum(self.numbers))
		self.update_info()


	def add_digits(self, num:int, check:bool=True) -> int:
		"""\nAdds all digits together with filtered master numbers and returns the resulted sum.\n"""
		_numbers: tuple[int, ...] = tuple(int(i) for i in str(num))

		if len(_numbers) > 1:
			_num: int = sum(_numbers)
			_mn: set[int] = {11, 22, 33}

			if _num >= 10 and not (_num in _mn and check):
				return sum(int(i) for i in str(_num))

			return _num
		return num


	def print(self) -> None:
		"""\nPrints '`self`' as string.\n"""
		print(self)


	def print_logs(self) -> None:
		"""\nPrints each log in [] brackets on its line.\n"""
		if len(self.log) > 0:
			for log in self.log:
				print(f'[{log}]')


	def __repr__(self) -> str:
		"""\nReturns dates arguments of the Class as a string.\n"""
		return f'DailyNumber({self.dates}, {self.number})'


	def __str__(self) -> str:
		"""\nReturns information and description`*` as a string.\n(`*` => if the json file was loaded)\n"""
		return self.information + (f'\n{self.description}' if len(self.description) > 0 else '')


	def __int__(self) -> int:
		"""\nReturns calculated number, or calculates and returns it.\n"""
		if self.number == 0:
			self.calc_numbers()
		return self.number


	def run(self):
		"""\nCalculates the numbers and returns self.\n"""
		self.calc_numbers()
		return self



# ===========================================================================================================

if __name__ == '__main__':
	from sys import exit
	from traceback import format_exc

	def test() -> None:
		dn: DailyNumber
		dn = DailyNumber('1991-12-31')
		dn.print()
		dn.print_logs()

	try: test()
	except: print(format_exc())
	finally: exit(0)

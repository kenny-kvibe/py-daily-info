#!/usr/bin/env python3
import daily_info
import json


def main() -> int:
	with open('DATA.json', 'r') as file:
		date = json.loads(file.read())['DATE_OF_BIRTH']
	return daily_info.main_run(date)


if __name__ == '__main__':
	raise SystemExit(main())

# Repository: [py-daily-info](https://github.com/kenny-kvibe/py-daily-info/)
Python - Script that shows Daily Information

# Contents:
- DailyNumber
- DailyHoroscope
- Tkinter Gui

# Usage:

```sh
git clone https://github.com/kenny-kvibe/py-daily-info DailyInfo
cd DailyInfo
python ./main.py
```

# Example Usage of Modules:

### DailyNumber

```py
from numerology import DailyNumber as DN

birth: str = '1990-12-31'
dn: DN = DN(birth)
dn.print()
```

### DailyHoroscope

```py
from horoscope import DailyHoroscope as DH

birth: str = '1990-12-31'
dh: DH = DH(birth)
dh.print()
```

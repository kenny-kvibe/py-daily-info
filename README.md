# Repository: [py-daily-info](https://github.com/kenny-kvibe/py-daily-info/)
Python - Script that shows Daily Information

# Contents:
- DailyNumber
- DailyHoroscope
- Tkinter Gui

# Example Main Usage:

```sh
git clone https://github.com/kenny-kvibe/py-daily-info DailyInfo
cd DailyInfo
python ./main.py "1991-12-31"
```

# Example Modules Usage:

### DailyNumber

```py
from numerology import DailyNumber as DN
dn: DN = DN('1991-12-31')
dn.print()
```

### DailyHoroscope

```py
from horoscope import DailyHoroscope as DH
dh: DH = DH('1991-12-31')
dh.print()
```

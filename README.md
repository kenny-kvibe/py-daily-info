# Repository: [py-daily-info](https://github.com/kenny-kvibe/py-daily-info/)
Python - Script that shows Daily Information of **Horoscope** & **Numerology**

## Classes:
- DailyNumber: `daily_info.horoscope.DailyNumber()`
- DailyHoroscope: `daily_info.horoscope.DailyHoroscope()`
- Gui: `daily_info.gui_window.Gui()` (*dep: Tkinter*)

# Example Main Usage:
```bash
git clone https://github.com/kenny-kvibe/py-daily-info
python ./py-daily-info/main.py 1991-12-31
```

# Example Modules Usage (*in python*):

### DailyNumber
```py
from daily_info.numerology import DailyNumber
dn = DailyNumber('1991-12-31')
dn.print()
```

### DailyHoroscope
```py
from daily_info.horoscope import DailyHoroscope
dh = DailyHoroscope('1991-12-31')
dh.print()
```

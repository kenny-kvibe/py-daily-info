# Repository: [py-daily-info](https://github.com/kenny-kvibe/py-daily-info/)
Python - Script that shows Daily Information of **Horoscope** & **Numerology**

# Contents

#### Packages:
- `daily_info`

#### Modules:
- `daily_info.numerology`
- `daily_info.horoscope`
- `daily_info.gui_window`

#### Classes:
- `daily_info.numerology.DailyNumber()`
- `daily_info.horoscope.DailyHoroscope()`
- `daily_info.gui_window.Gui()`

# Example Main Usage
```sh
git clone https://github.com/kenny-kvibe/py-daily-info
python ./py-daily-info/main.py 1991-12-31
```

# Example Modules Usage (*in python*)

#### DailyNumber():
```py
from daily_info.numerology import DailyNumber
dn = DailyNumber('1991-12-31')
dn.print()
```

#### DailyHoroscope():
```py
from daily_info.horoscope import DailyHoroscope
dh = DailyHoroscope('1991-12-31')
dh.print()
```

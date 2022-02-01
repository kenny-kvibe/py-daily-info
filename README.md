# Daily Information of Horoscope & Numerology

> Python 3 script

> Repository: [py-daily-info](https://github.com/kenny-kvibe/py-daily-info/)

-------------------------------------------------------------------------------

## Installation

1.) Install `Python>=3.9` & `Git>=2.0`

2.) Create a new folder and Open a Command Prompt in it

3.) Clone the repository & Change Directory into it:

> `git clone https://github.com/kenny-kvibe/py-daily-info && cd py-daily-info/`

4.) Change the **`DATE_OF_BIRTH`** value inside `./DATA.json` file!

5.) Create a Python Virtual Environment & activate it:
 
> `python -m venv ./venv && venv/Scripts/activate`

6.) Install the requirements inside that Virtual Environment:
 
> `pip install -r ./requirements.txt; pip cache purge`

7.) Run the code:

> `python ./main.py`

8.) Deactivate the Virtual Environment (also optionally delete the `./venv` folder):

> `deactivate`


## Contents

#### Module:

- `daily_info`

#### Classes:

- `daily_info.numerology.DailyNumber()`
- `daily_info.horoscope.DailyHoroscope()`
- `daily_info.gui_window.Gui()`


## Example Usage (*in python*)

#### DailyNumber:

```py
import daily_info.numerology as n
dn = n.DailyNumber('1991-12-31')
dn.print()
```

#### DailyHoroscope:

```py
import daily_info.horoscope as h
dh = h.DailyHoroscope('1991-12-31')
dh.print()
```

#### Gui:

```py
import daily_info.gui_window as g
gui = g.Gui('Title')
gui.set_text('Text')
gui.run()
```

-------------------------------------------------------------------------------

<sub><u>UPDATED</u>: 01.Feb.2022</sub>

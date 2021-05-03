import tkinter as tk
from dataclasses import dataclass, field, InitVar

@dataclass
class Gui:
	"""\nGraphical User Interface with `Tkinter`.\n
	Displays text in a GUI window.\n
	Example Usage:\n
	```py
	gui: Gui = Gui('Gui Title', 'Test Text', height=90)
	gui.set_text('New Text')
	gui.button_click()
	gui.run()
	```\n
	"""

	title:  str = field(default='Gui')
	text:   str = field(default='')
	width:  InitVar[int] = field(default=0)
	height: InitVar[int] = field(default=0)

	def __post_init__(self, width:int, height:int) -> None:
		"""\nGraphical User Interface\n"""
		self.root: tk.Tk = tk.Tk()
		self.root.title(self.title)
		self.loop: bool = True

		init_w: int = width  if width  > 0 and width  <= self.root.winfo_screenwidth()  else 320
		init_h: int = height if height > 0 and height <= self.root.winfo_screenheight() else 160
		init_x: int = self.root.winfo_screenwidth()//2  - init_w//2
		init_y: int = self.root.winfo_screenheight()//2 - init_h//2
		self.root.geometry(f'{init_w}x{init_h}+{init_x}+{init_y}')

		self.root.attributes('-topmost', True)
		self.root.resizable(True, True)
		self.root.bind("<Configure>", self.move_resize_window)
		self.root.protocol("WM_DELETE_WINDOW", self.exit_window)

		self.frame: tk.Frame = tk.Frame(self.root, width=init_w, height=init_h, border=0)
		self.frame.grid()

		self.set_text(self.text)

		self.text_label: tk.Label
		self.button: tk.Button
		self.init_widgets()


	@property
	def w(self) -> int:
		"""\n`w` property (window width)\n"""
		return self.root.winfo_width()


	@property
	def h(self) -> int:
		"""\n`h` property (window height)\n"""
		return self.root.winfo_height()


	@property
	def x(self) -> int:
		"""\n`x` property (window position x)\n"""
		return self.root.winfo_x()


	@property
	def y(self) -> int:
		"""\n`y` property (window position y)\n"""
		return self.root.winfo_y()


	@property
	def color(self) -> dict[str, str]:
		"""\n`color` property (window colors), keys → `'fg'`, `'bg'`\n"""
		return {'fg': '#dedede', 'bg': '#151515'}


	@property
	def font(self) -> str:
		"""\n`font` property (window font)\n"""
		return 'Arial 11'


	def set_text(self, text:str) -> ...:
		"""\nSets the text if it's provided, returns self.\n"""
		self.text = 'No Text.' if len(text) == 0 else text
		return self


	def init_widgets(self) -> None:
		"""\nCreates tkinter widgets, calls `colorize()` and adds them to the grid.\n"""
		self.frame.config(padx=self.w//5, pady=self.h//5)
		self.text_label = tk.Label(self.frame, font=self.font, anchor=tk.CENTER, text='', relief=tk.FLAT, justify='left')
		self.button = tk.Button(self.frame, font=self.font, anchor=tk.CENTER, text='Load', command=lambda:self.button_click(), padx=10)
		self.button_textr = tk.Label(self.frame, font=self.font, anchor=tk.CENTER, text='← press to Start', justify='left', padx=10)
		self.colorize()
		self.text_label.grid(row=0, column=0)
		self.button.grid(row=0, column=0)
		self.button_textr.grid(row=0, column=1)


	def button_click(self) -> ...:
		"""\nDisplays the text and destroys the button, returns self.\n"""
		self.text_label.config(text=self.text, relief=tk.RAISED, padx=10, wraplength=self.w-24)

		size: int = 512
		pos: tuple[int, int] = (self.root.winfo_screenwidth()//2 - size//2, self.root.winfo_screenheight()//2 - size//2)
		self.root.geometry(f'{size}x{size}+{pos[0]}+{pos[1]}')

		self.button.destroy()
		self.button_textr.destroy()

		self.root.update()
		return self


	def colorize(self) -> None:
		"""\nSets the widgets colors.\n"""
		self.set_color(self.root, False)
		self.set_color(self.frame, False)
		self.set_color(self.text_label)
		self.set_color(self.button)
		self.set_color(self.button_textr)


	def set_color(self, widget, with_fg:bool=True) -> ...:
		"""\nSets window's widget theme colors, returns self.\n"""
		widget.configure(bg=self.color['bg'])
		if with_fg == True:
			widget.configure(fg=self.color['fg'])
		return self


	def move_resize_window(self, event) -> None:
		"""\nUpdates the `text_label` text-wrap on window resize/move.\n"""
		if event.x == self.x and event.y == self.y:
			self.frame.config(padx=20, pady=20)
			self.text_label.config(wraplength=self.w-50)
			self.root.update()


	def exit_window(self) -> None:
		"""\nDestroys the `root` window.\n"""
		self.root.destroy()


	def run(self, ms:float=0.01) -> None:
		"""\nStarts the `root` window's main loop.\n"""
		self.root.mainloop()


if __name__ == '__main__':
	from sys import exit
	from traceback import format_exc
	try:
		gui: Gui = Gui('Gui Test', 'Test...', height=90)
		gui.set_text('New Text')
		gui.button_click()
		gui.run()
	except: print(format_exc())
	finally: exit(0)

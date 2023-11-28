import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing

URL = "https://api.edenai.run/v2/audio/text_to_speech"

pdf = filedialog.askopenfile(mode='r', title='Select PDF File', initialdir='./', filetypes=[('PDF Files', '*.pdf')])

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Print Preview")
#root.geometry("700x500")

frmMain = tk.Frame(root)
frmMain.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

frmLeft = tk.Frame(frmMain) 
frmLeft.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

frmRight = tk.Frame(frmMain)
frmRight.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.NO, ipadx=5)

psLabel = tk.Frame(frmLeft) 
psLabel.pack(side=tk.TOP, fill=tk.NONE, expand=tk.NO, padx=5, pady=5)

psLabelFrame = tk.LabelFrame(psLabel, text="Printer Settings:")
psLabelFrame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.NO, ipady=3)

printerLabel = tk.Label(psLabelFrame, text="Printer:", padx=5)
printerLabel.grid(row=0, column=0, sticky=tk.W)
chb1 = tk.Checkbutton(psLabelFrame, text="Always use system default printer at dialog start")
chb1.grid(row=0, column=2, sticky=tk.W, columnspan=2)

cmb1 = ttk.Combobox(psLabelFrame, values=["Microsoft Print To PDF"], width=76)
cmb1['state'] = 'readonly'
cmb1.grid(row=1, column=0, columnspan=4, padx=5, sticky=tk.W)
cmb1.current(0)

var = tk.IntVar()
rb1 = tk.Radiobutton(psLabelFrame, text="Portrait", variable=var, value=1, command=tk.SEL)
rb1.select()
rb1.grid(row=2, column=0, sticky=tk.W)

paperLabel = tk.Label(psLabelFrame, text="Paper:")
paperLabel.grid(row=2, column=1, sticky=tk.W)
chb2 = tk.Checkbutton(psLabelFrame, text="Auto-rotate")
chb2.grid(row=2, column=2, sticky=tk.W)

rb2 = tk.Radiobutton(psLabelFrame, text="Landscape      ", variable=var, value=2, command=tk.SEL)
rb2.grid(row=3, column=0, sticky=tk.W)

a4Label = tk.Label(psLabelFrame, text="A4.           600 DPI", padx=5, relief=tk.SUNKEN, width=35)
a4Label.grid(row=3, column=1, columnspan=2, sticky=tk.W)
psButton = tk.Button(psLabelFrame, text="Printer Setup", width=15, relief=tk.GROOVE)
psButton.grid(row=3, column=3, sticky=tk.E, padx=5)

#SECOND SECTION START
secondSection = tk.Frame(frmLeft)
secondSection.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, ipady=2)

ssLeftFrame = tk.Frame(secondSection)
ssLeftFrame.grid(row=0, column=0, padx=4)

ssRightFrame = tk.Frame(secondSection)
ssRightFrame.grid(row=0, column=1, sticky=tk.NE)

#PRINT SIZE
printSizeFrame = tk.Frame(ssLeftFrame)
printSizeFrame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.NO)

printSizeLabelFrame = tk.LabelFrame(printSizeFrame, text="Print size:")
printSizeLabelFrame.pack(side=tk.TOP, ipady=7)

var2 = tk.IntVar()
rb3 = tk.Radiobutton(printSizeLabelFrame, text="Original Size (from image DPI)", variable=var2, value=1, command=tk.SEL)
rb3.select()
rb3.grid(row=0, column=0, sticky=tk.W, columnspan=4)

rb4 = tk.Radiobutton(printSizeLabelFrame, text="Best fit to page (aspect ratio)", variable=var2, value=2, command=tk.SEL)
rb4.grid(row=1, column=0, sticky=tk.W, columnspan=4)

rb5 = tk.Radiobutton(printSizeLabelFrame, text="Stretch to page (no aspect ratio)", variable=var2, value=3, command=tk.SEL)
rb5.grid(row=2, column=0, sticky=tk.W, columnspan=4)

rb6 = tk.Radiobutton(printSizeLabelFrame, text="Custom:", variable=var2, value=4, command=tk.SEL)
rb6.grid(row=3, column=0, sticky=tk.NW)

wl1 = tk.Label(printSizeLabelFrame, text="Width: ")
wl1.grid(row=3, column=1, sticky=tk.W)

wvar1 = tk.StringVar(root, "5.00")
we1 = tk.Entry(printSizeLabelFrame, state=tk.DISABLED, textvariable=wvar1, width=7)
we1.grid(row=3, column=2, sticky=tk.W, pady=3)

hl1 = tk.Label(printSizeLabelFrame, text="Height: ")
hl1.grid(row=4, column=1, sticky=tk.W)

hvar1 = tk.StringVar(root, "5.00")
he1 = tk.Entry(printSizeLabelFrame, state=tk.DISABLED, textvariable=hvar1, width=7)
he1.grid(row=4, column=2, sticky=tk.W)

chb3 = tk.Checkbutton(printSizeLabelFrame, text="Aspect ratio", state=tk.DISABLED)
chb3.select()
chb3.grid(row=3, column=3, rowspan=2, sticky=tk.W)

rb7 = tk.Radiobutton(printSizeLabelFrame, text="Scale:", variable=var2, value=5, command=tk.SEL)
rb7.grid(row=6, column=0, sticky=tk.NW)

wl2 = tk.Label(printSizeLabelFrame, text="Width: ")
wl2.grid(row=6, column=1, sticky=tk.W)

wvar2 = tk.StringVar(root, "1.00")
we2 = tk.Entry(printSizeLabelFrame, state=tk.DISABLED, textvariable=wvar2, width=7)
we2.grid(row=6, column=2, sticky=tk.W, pady=3)

hl2 = tk.Label(printSizeLabelFrame, text="Height: ")
hl2.grid(row=7, column=1, sticky=tk.W)

hvar2 = tk.StringVar(root, "1.00")
he2 = tk.Entry(printSizeLabelFrame, state=tk.DISABLED, textvariable=hvar2, width=7)
he2.grid(row=7, column=2, sticky=tk.W)

psl1 = tk.Label(printSizeLabelFrame, text="(of original size)")
psl1.grid(row=6, column=3, sticky=tk.W, rowspan=2)

#HEADNOTE
headnoteFrame = tk.Frame(ssRightFrame)
headnoteFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

headnoteLabelFrame = tk.LabelFrame(headnoteFrame, text="Headnote/Footend text:")
headnoteLabelFrame.pack(side=tk.TOP)

chb4 = tk.Checkbutton(headnoteLabelFrame, text="Headnote:")
chb4.grid(row=0, column=0, sticky=tk.W)

headentry = tk.Entry(headnoteLabelFrame, state=tk.DISABLED, width=34)
headentry.grid(row=1, column=0, sticky=tk.W, padx=5, columnspan=2)

chb5 = tk.Checkbutton(headnoteLabelFrame, text="Footnote:")
chb5.grid(row=2, column=0, sticky=tk.W)

foodentry = tk.Entry(headnoteLabelFrame, state=tk.DISABLED, width=34)
foodentry.grid(row=3, column=0, sticky=tk.W, padx=5, columnspan=2)

helpLabel = tk.Label(headnoteLabelFrame, text="Hint:$D = file folder,\n$F = file name ...", justify=tk.LEFT)
helpLabel.grid(row=4, column=0, sticky=tk.W)

helpButton = tk.Button(headnoteLabelFrame, text="Help", width=7, relief=tk.GROOVE)
helpButton.grid(row=4, column=1, sticky=tk.NE, padx=5, pady=5)

fontLabel = tk.Label(headnoteLabelFrame, text="Font:")
fontLabel.grid(row=5, column=0, sticky=tk.SW)

fontButton = tk.Button(headnoteLabelFrame, text="Choose", width=12, relief=tk.GROOVE)
fontButton.grid(row=5, column=1, sticky=tk.E, padx=5, pady=3)

fontDisLabel = tk.Label(headnoteLabelFrame, text="Courier New, Size: 10", padx=5, relief=tk.SUNKEN, width=28, anchor=tk.W)
fontDisLabel.grid(row=6, column=0, columnspan=2, padx=4, pady=2)

#POSITION
positionFrame = tk.Frame(ssLeftFrame)
positionFrame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.NO)

positionLabelFrame = tk.LabelFrame(positionFrame, text="Position on paper:")
positionLabelFrame.pack(side=tk.TOP)

lmLabel = tk.Label(positionLabelFrame, text="Left Margin:")
lmLabel.grid(row=0, column=0, sticky=tk.W)

lmvar = tk.StringVar(root, "0.00")
lmEntry = tk.Entry(positionLabelFrame, textvariable=lmvar, width=6)
lmEntry.grid(row=0, column=1, sticky=tk.W)

horCheck = tk.Checkbutton(positionLabelFrame, text="Center horz.")
horCheck.grid(row=0, column=2, sticky=tk.W)

tmLabel = tk.Label(positionLabelFrame, text="Top Margin:")
tmLabel.grid(row=1, column=0, sticky=tk.W)

tmvar = tk.StringVar(root, "0.00")
tmEntry = tk.Entry(positionLabelFrame, textvariable=tmvar, width=6)
tmEntry.grid(row=1, column=1, sticky=tk.W, pady=2)

verCheck = tk.Checkbutton(positionLabelFrame, text="Center vert.")
verCheck.grid(row=1, column=2, sticky=tk.W)

verCheck = tk.Checkbutton(positionLabelFrame, text="Borderless printing")
verCheck.grid(row=2, column=0, sticky=tk.W)

#UNITS
unitFrame = tk.Frame(ssLeftFrame)
unitFrame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.NO)

unitLabelFrame = tk.LabelFrame(unitFrame, text="Units for 'custom' and 'position':")
unitLabelFrame.pack(side=tk.TOP, ipady=4)

var3 = tk.IntVar()
rb8 = tk.Radiobutton(unitLabelFrame, text="cm", variable=var3, value=1, command=tk.SEL)
rb8.select()
rb8.grid(row=0, column=0, sticky=tk.W)

rb9 = tk.Radiobutton(unitLabelFrame, text="inches", variable=var3, value=2, command=tk.SEL)
rb9.grid(row=1, column=0, sticky=tk.W)

emptyLabel = tk.Label(unitLabelFrame, text="", width=8)
emptyLabel.grid(row=0, column=1)

overCheck = tk.Checkbutton(unitLabelFrame, text="No overflow on page")
overCheck.grid(row=0, column=2, sticky=tk.E)

#PROFILES
proFrame = tk.Frame(ssLeftFrame)
proFrame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.NO)

proLabelFrame = tk.LabelFrame(proFrame, text="Profiles:")
proLabelFrame.pack(side=tk.TOP, ipady=2)

cmb2 = ttk.Combobox(proLabelFrame, values=[""], width=38)
cmb2['state'] = 'readonly'
cmb2.grid(row=0, column=0, columnspan=3, padx=6, pady=5)
cmb2.current(0)

loadButton = tk.Button(proLabelFrame, text="Load", width=9, relief=tk.GROOVE)
loadButton.grid(row=1, column=0, padx=5)

deleteButton = tk.Button(proLabelFrame, text="Delete", width=9, relief=tk.GROOVE)
deleteButton.grid(row=1, column=1, padx=5)

saveButton = tk.Button(proLabelFrame, text="Save", width=9, relief=tk.GROOVE)
saveButton.grid(row=1, column=2, padx=5)

#MULTIPAGE
mulFrame = tk.Frame(ssRightFrame)
mulFrame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.NO)

mulLabelFrame = tk.LabelFrame(mulFrame, text="Multipage images:")
mulLabelFrame.pack(side=tk.TOP)

var4 = tk.IntVar()
rb10 = tk.Radiobutton(mulLabelFrame, text="Print current page", variable=var4, value=1, command=tk.SEL, state=tk.DISABLED)
rb10.grid(row=0, column=0, sticky=tk.W, columnspan=4)

rb11 = tk.Radiobutton(mulLabelFrame, text="Print all pages", variable=var4, value=2, command=tk.SEL, state=tk.DISABLED)
rb11.grid(row=1, column=0, sticky=tk.W, columnspan=4)

rb12 = tk.Radiobutton(mulLabelFrame, text="Print from:    ", variable=var4, value=3, command=tk.SEL, state=tk.DISABLED)
rb12.grid(row=2, column=0, sticky=tk.W)

fromentry = tk.Entry(mulLabelFrame, state=tk.DISABLED, width=6)
fromentry.grid(row=2, column=1, sticky=tk.W)

toLabel = tk.Label(mulLabelFrame, text="to")
toLabel.grid(row=2, column=2, padx=5)

toentry = tk.Entry(mulLabelFrame, state=tk.DISABLED, width=6)
toentry.grid(row=2, column=3, sticky=tk.W, padx=5)

rb13 = tk.Radiobutton(mulLabelFrame, text="Pages", variable=var4, value=4, command=tk.SEL, state=tk.DISABLED)
rb13.grid(row=3, column=0, sticky=tk.W)

pageentry = tk.Entry(mulLabelFrame, state=tk.DISABLED, width=18)
pageentry.grid(row=3, column=1, sticky=tk.W, columnspan=3)

printLabel = tk.Label(mulLabelFrame, text="Print:")
printLabel.grid(row=4, column=0, sticky=tk.W)

cmb3 = ttk.Combobox(mulLabelFrame, values=[""], width=30, state=tk.DISABLED)
cmb3.grid(row=5, column=0, columnspan=4, pady=5)
cmb3.current(0)

#COPIES
copFrame = tk.Frame(ssRightFrame)
copFrame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.NO)

copLabelFrame = tk.LabelFrame(mulFrame, text="Copies:")
copLabelFrame.pack(side=tk.TOP, ipady=2, ipadx=6)

copLabel = tk.Label(copLabelFrame, text="Number of copies:     ")
copLabel.grid(row=0, column=0, sticky=tk.W, padx=3, pady=3)

noSpin = tk.Spinbox(copLabelFrame, from_=1, to=2, width=3)
noSpin.grid(row=0, column=1, sticky=tk.W, padx=5)

chb10 = tk.Checkbutton(copLabelFrame, text="Collate (multiple images)", state=tk.DISABLED)
chb10.select()
chb10.grid(row=1, column=0, rowspan=2, sticky=tk.W, pady=2)

#RIGHT FRAME
preLabel = tk.Label(frmRight, text="Preview:")
preLabel.grid(row=0, column=0, sticky=tk.W, pady=8)

puppy_image = tk.PhotoImage(file='pup.gif')
puppy_label = tk.Label(frmRight, image=puppy_image, relief=tk.SUNKEN)
puppy_label.grid(row=1, column=0, sticky=tk.W)

hintLabel = tk.Label(frmRight, text="Hint: you can print several (smaller)\ncopies of same image if you first use\nthe menu: \"Image->Create Tiled\nimage\"", justify=tk.LEFT)
hintLabel.grid(row=2, column=0, pady=40)

curButton = tk.Button(frmRight, text="Save current dialog settings", relief=tk.GROOVE, width=26)
curButton.grid(row=3, column=0)

finalFrame = tk.Frame(frmRight)
finalFrame.grid(row=4, column=0, pady=40, sticky=tk.W)

finalLabel = tk.Label(finalFrame, text="Resulting image size on paper:")
finalLabel.grid(row=0, column=0, sticky=tk.W)

finalDisLabel = tk.Label(finalFrame, text="20.3 x 14.4 cm; 8.01 x 5.67 inches", relief=tk.SUNKEN, width=26)
finalDisLabel.grid(row=1, column=0)

prFrame = tk.Frame(frmRight)
prFrame.grid(row=5, column=0, pady=20)

prbtn = tk.Button(prFrame, text="Print", relief=tk.GROOVE, width=11)
prbtn.focus()
prbtn.grid(row=0, column=0, padx=7)

canbtn = tk.Button(prFrame, text="Cancel", relief=tk.GROOVE, width=11)
canbtn.grid(row=0, column=1)

root.mainloop()
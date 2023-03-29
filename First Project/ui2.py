import tkinter as tk
import tkinter.font as tkf

white="#ffffff"
gray="#636363"
lightGray="#C1C1C1"
bgcolor="#E4E4E4"

root = tk.Tk()
root.title("Menu")

icons = tkf.Font(family='Segoe MDL2 Assets', size=13, weight='normal')
fontNormal = tkf.Font(family='Segoe UI', size=11, weight='normal', )
fontNormalbig = tkf.Font(family='Segoe UI', size=20, weight='normal', )
fontNormalbig2 = tkf.Font(family='Segoe UI', size=16, weight='normal', )
fontSemibold = tkf.Font(family='Segoe UI Semibold', size=11, weight='normal', )


class MenuButton(tk.Frame):
  def __init__(self, frame, icon, text, variable, value, size=12):
    tk.Frame.__init__(self, frame, bg=bgcolor)

    self.variable = variable
    self.variable.trace_add("write", self._notify)
    self.value = value
     
    self.mark = tk.Label(self, font=icons, bg=gray if self.is_active() else bgcolor)
    self.mark.pack(side=tk.LEFT, anchor=tk.W)

    self.icon = tk.Label(self, text=icon, font=icons, bg=bgcolor, fg="black")
    self.icon.pack(side=tk.LEFT, anchor=tk.W, ipadx=size, ipady=size)
    
    self.text = tk.Label(self, text=text, font=fontNormal, bg=bgcolor, fg="black")
    self.text.pack(side=tk.LEFT, anchor=tk.W, ipadx=0, ipady=size)

    self.bind("<Enter>", self._enter)
    self.bind("<Leave>", self._leave)
    self.bind("<Button-1>", self._select)
    self.mark.bind("<Button-1>", self._select)
    self.icon.bind("<Button-1>", self._select)
    self.text.bind("<Button-1>", self._select)
  
  
  def is_active(self):
    return self.variable.get() == self.value
    
  def _enter(self, event, color=lightGray):        
    self.configure(bg=color)
    self.mark.configure(bg=gray if self.is_active() else color)
    self.icon.configure(bg=color)
    self.text.configure(bg=color)
    
  def _leave(self, event, color=bgcolor):        
    self.configure(bg=color)    
    self.mark.configure(bg=gray if self.is_active() else color)
    self.icon.configure(bg=color)
    self.text.configure(bg=color)
    
  def _select(self, event, color=bgcolor):
    self.variable.set(self.value)
    self._enter(event)
    
  def _notify(self, name, msg, mode):
    self._leave(None) 

class MenuLabel(tk.Frame):
  def __init__(self, frame, text, size=12):
    tk.Frame.__init__(self, frame, bg=bgcolor)

    self.text = tk.Label(self, text=text, font=fontSemibold, bg=bgcolor, fg="black")
    self.text.pack(side=tk.LEFT, anchor=tk.W, ipadx=15, ipady=size)

class MenuLabel2(tk.Frame):
  def __init__(self, frame, text, size=10):
    tk.Frame.__init__(self, frame, bg="white")

    self.text = tk.Label(self, text=text, font=fontNormalbig, bg="white", fg="black")
    self.text.pack(side=tk.LEFT, anchor=tk.W, ipadx=15, ipady=size)

class MenuLabel3(tk.Frame):
  def __init__(self, frame, text, size=10):
    tk.Frame.__init__(self, frame, bg="white")

    self.text = tk.Label(self, text=text, font=fontNormalbig2, bg="white", fg="black")
    self.text.pack(side=tk.LEFT, anchor=tk.W, ipadx=15, ipady=size)

class MenuLabel4(tk.Frame):
  def __init__(self, frame, text, size=0):
    tk.Frame.__init__(self, frame, bg="white")

    self.text = tk.Label(self, text=text, font=fontNormal, bg="white", fg="black", justify=tk.LEFT)
    self.text.pack(side=tk.LEFT, anchor=tk.W, ipadx=15, ipady=size)

class MenuLabel5(tk.Frame):
  def __init__(self, frame, text, size=0):
    tk.Frame.__init__(self, frame, bg="white")

    self.text = tk.Label(self, text=text, font=fontNormal, bg="white", fg=gray, justify=tk.LEFT)
    self.text.pack(side=tk.LEFT, anchor=tk.W, ipadx=15, ipady=size)

def focusInSearchHint(event):
  if event.widget.get() == "Search":
     event.widget.delete(0, 'end')

def focusOutSearchHint(event):
  if event.widget.get() == "":
     event.widget.insert(0, "Search")

frmLeft = tk.Frame(root, bg=bgcolor)
frmLeft.pack(side=tk.LEFT, fill=tk.Y, expand=tk.NO)
frmRight = tk.Frame(root, bg="white")
frmRight.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES, ipady=10)

m = tk.IntVar()
m.set(3)

btnHome = MenuButton(frmLeft, icon="\ue80f", text="Home", variable=m, value=1);
btnHome.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

frmTopLeft = tk.Frame(frmLeft, bg="white", highlightbackground="#636363", highlightcolor="#636363", highlightthickness=2)
frmTopLeft.pack(side=tk.TOP, padx=20, pady=5)

entSearch2 = tk.Entry(frmTopLeft, width=40, bg="white", fg="#888888", relief=tk.FLAT, font=fontNormal)
entSearch2.bind("<FocusIn>", focusInSearchHint)  
entSearch2.bind("<FocusOut>", focusOutSearchHint)
entSearch2.insert(0, "Find a Setting")
entSearch2.pack(side=tk.LEFT, padx=8)
lblSearch2 = tk.Label(frmTopLeft, text="\ue721", font=icons, bg="white", fg="#888888")
lblSearch2.pack(side=tk.LEFT, padx=8, pady=8)

lbl1 = MenuLabel(frmLeft, text="Time & Language")
lbl1.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

btnDate = MenuButton(frmLeft, icon="\uec92", text="Date & Time", variable=m, value=2);
btnDate.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

btnRegion = MenuButton(frmLeft, icon="\uf2b7", text="Region & Language", variable=m, value=3);
btnRegion.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

btnSpeech = MenuButton(frmLeft, icon="\ue720", text="Speech", variable=m, value=4);
btnSpeech.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

lbl2 = MenuLabel2(frmRight, text="Region & Language")
lbl2.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

lbl3 = MenuLabel3(frmRight, text="Country or Region")
lbl3.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

lbl4 = MenuLabel4(frmRight, text="Windows and apps might use your country or region to give you\nlocal content")
lbl4.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

frm2 = tk.Frame(frmRight, bg="white", highlightbackground="#636363", highlightcolor="#636363", highlightthickness=2)
frm2.pack(side=tk.TOP, anchor=tk.W, fill=tk.NONE, padx=20, pady=10)

entSearch = tk.Entry(frm2, width=48, bg="white", fg="black", relief=tk.FLAT, font=fontNormal)
entSearch.bind("<FocusIn>", focusInSearchHint)  
entSearch.bind("<FocusOut>", focusOutSearchHint)
entSearch.insert(0, "United States")
entSearch.pack(side=tk.LEFT, padx=8)
lblSearch = tk.Label(frm2, text="\ue70d", font=icons, bg="white", fg="#888888")
lblSearch.pack(side=tk.RIGHT, padx=8, pady=8)

lbl5 = MenuLabel4(frmRight, text="")
lbl5.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

lbl6 = MenuLabel3(frmRight, text="Languages")
lbl6.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

lbl7 = MenuLabel4(frmRight, text="Windows display Language")
lbl7.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

lbl8 = MenuLabel5(frmRight, text="Windows features like Settings and File Explorer will appear in this\nlanguage")
lbl8.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

frm3 = tk.Frame(frmRight, bg="white", highlightbackground="#636363", highlightcolor="#636363", highlightthickness=2)
frm3.pack(side=tk.TOP, anchor=tk.W, fill=tk.NONE, padx=20, pady=10)

entSearch3 = tk.Entry(frm3, width=48, bg="white", fg="black", relief=tk.FLAT, font=fontNormal)
entSearch3.bind("<FocusIn>", focusInSearchHint)  
entSearch3.bind("<FocusOut>", focusOutSearchHint)
entSearch3.insert(0, "English (United States)")
entSearch3.pack(side=tk.LEFT, padx=8)
lblSearch3 = tk.Label(frm3, text="\ue70d", font=icons, bg="white", fg="#888888")
lblSearch3.pack(side=tk.RIGHT, padx=8, pady=8)

lbl5 = MenuLabel5(frmRight, text="")
lbl5.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

lbl9 = MenuLabel4(frmRight, text="Preferred languages")
lbl9.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

lbl10 = MenuLabel5(frmRight, text="Apps and websites will apear in the first language in the list that\nthey support")
lbl10.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

root.mainloop()

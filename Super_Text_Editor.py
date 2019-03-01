from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkfontchooser import askfont

class main:
    global newicon,openicon,saveicon,copynewicon,cuticon,pasteicon,redoicon,undoicon
    def __init__(self,master):
        self.master = master
        self.filename = 'Untitled'
        self.updateTitle()
        self.widgets()
        self.menubar()
    def updateTitle(self):
        print(self.filename)
        self.master.title(self.filename+": "+'DouchePad')

    def menubar(self):
        
        
        self.menu = Menu(self.master,bg='#6459c3',fg='#2ef03e')
        self.master.config(menu=self.menu)
        filemenu = Menu(self.menu,bg='#6459c3',fg='#2ef03e')
        self.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label='New',command=self.NewFile,accelerator='Ctrl+N',compound=LEFT,image=newicon,underline=0)
        filemenu.add_command(label="Open", command=self.opn,compound=LEFT,image=openicon,underline=0,accelerator='Ctrl+O')
        filemenu.add_command(label="Save", command=self.save,compound=LEFT,image=saveicon,underline=0,accelerator='Ctrl+S')
        filemenu.add_command(label="Save As..", command=self.saveas,underline=0,accelerator='Ctrl+Shift+S',image=saveicon,compound=LEFT)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit,underline=0,accelerator='Ctrl+F4',compound=LEFT)
        Config = Menu(self.menu,bg='#6459c3',fg='#2ef03e')
        self.menu.add_cascade(label="Config", menu=Config)
        Config.add_command(label="Font",command=self.chfont)
        Config.add_command(label="Text Color",command=self.txtcolor)
        bt = Menu(Config,bg='#6459c3',fg='#2ef03e')
        bt.add_command(label="Black Theme",command=self.black)
        bt.add_command(label="White Theme",command=self.default)
        bt.add_command(label="Amazing Theme",command=self.amazing)
        Config.add_cascade(label="Background Theme",menu=bt)
        editmenu=Menu(self.menu,bg='#6459c3',fg='#2ef03e')
        
        editmenu.add_command(label='Undo',command=self.undo,compound=LEFT,image=undoicon,accelerator='Ctrl+Z')
        editmenu.add_command(label='Redo',command=self.redo,compound=LEFT,image=redoicon,accelerator='Ctrl+Y')
        editmenu.add_command(label='Paste',command=self.paste,compound=LEFT,image=pasteicon,accelerator='Ctrl+V')
        editmenu.add_command(label='Cut',command=self.cut,compound=LEFT,image=cuticon,accelerator='Ctrl+X')
        editmenu.add_command(label='Copy',command=self.copy,compound=LEFT,image=copyicon,accelerator='Ctrl+C')
        self.menu.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(self.menu,bg='#6459c3',fg='#2ef03e')
        self.menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...",command=self.about)
    def black(self):
        self.ta['insertbackground'] = 'white'
        self.ta['bg'] = 'black'
        self.ta['fg'] = '#00de00'
        self.ta.config(font=('Dancing Script','11','bold','italic'))
    def amazing(self):        
        self.ta['insertbackground'] = 'white'
        self.ta['bg'] = '#7c18b8'
        self.ta['fg'] = '#00de00'        
        self.ta.config(font=('Dancing Script','15','bold','italic'))
        self.ta['height'] =7 
        self.ta['width'] =28
    def default(self):
        self.ta['insertbackground'] = 'black'
        self.ta['bg'] = 'white'
        self.ta['fg'] = 'black'
        self.ta.config(font=('SECBengali UI','11','bold','italic'))

    def quit(self):
        if messagebox.askyesno("Save","Do you want to save the file before closing."):
            self.save()
        quit()

    def about(self):
        messagebox.showinfo('About','This super funny TextEditor is developed by Razz Sawhoney...\nFor more info please do contact us:rajsahani1819@gmail.com')

    def txtcolor(self):
        color = colorchooser.askcolor(self.ta['fg'])
        if color:
            self.ta['fg'] = color[1]

    def chfont(self):
        font = askfont(self.master,self.ta['font'])
        if font:
            font['family'] = font['family'].replace(' ', '\ ')
            font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
            if font['underline']:
                font_str += ' underline'
            if font['overstrike']:
                font_str += ' overstrike'
            self.ta['font'] = font_str
			
			#self.ta['height'] = self.ta['height']-font['size']
			#self.ta['width'] =  self.ta['width']-font['size']

	
    def widgets(self):        
        self.master.protocol("WM_DELETE_WINDOW",self.quit)
        scrollbar=Scrollbar(self.master)
        self.ta = Text(self.master,height=10,width=38,yscrollcommand=scrollbar.set,wrap='word',font=('Dancing Script','11','bold','italic'),padx=10,pady=10)
        scrollbar.config(bg='#ac78ce',command=self.ta.yview)
        scrollbar.pack(side='right',fill='y')
        self.ta.pack(expand=True,fill=BOTH)
        
        #ShortCuts
        
        self.ta.bind('<Control-o>',self.opn)
        self.ta.bind('<Control-n>',self.NewFile)
        self.ta.bind('<Control-s>',self.save)
        self.ta.bind('<Control-a>',self.select_all)
        self.ta.bind('<Control-z>',self.undo)
        self.ta.bind('<Control-y>',self.redo)
        self.ta.bind('<Control_R>',lambda e:self.new_line('\n'))
		
	

    def new_line(self,event):        
        self.ta.insert('insert',event)
    def NewFile(self,event=None):
        if messagebox.askyesno("New","Do you want to save the file..."):
            self.save()

        self.ta.delete(0.0, END)
        self.filename = "Untitled"
        self.updateTitle()

    def select_all(self,event=None):
        self.ta.tag_add('sel', 1.0, 'end')
        self.ta.focus_set()

    def paste(self,event=None):
        self.ta.event_generate('<<Paste>>')
        
    def cut(self,event=None):
        self.ta.event_generate('<<Cut>>')
        
    def copy(self,event=None):
        self.ta.event_generate('<<Copy>>')
        
    def undo(self,event=None):
        self.ta.event_generate('<<Undo>>')
        
    def redo(self,event=None):
        self.ta.event_generate('<<Redo>>')
                                        
    def opn(self,event=None):
        File = str(filedialog.askopenfilename(title="Open File",filetypes=[("all files","*.*"),
			('CSS','.css'),('HTML','.html'),('PYTHON','.py'),('DOCUMENT','.docx')],initialdir='/storage/emulated/0/Documents/My_text_editor'))
        if len(File) > 0:
            self.ta.delete("1.0",END)
            try:
                f = open(File)
                for line in f:
                    self.ta.insert(END,line)
                f.close()
                self.filename = str(File)
                self.updateTitle()
            except IOError:
                messagebox.showwarning("Open file","Cannot open this file...") 

    def save(self,event=None):
        if self.filename == 'Untitled':
            self.saveas()
        else:
            f = open(self.filename,"w")
            text = self.ta.get("1.0",END)
            f.write(text)
            f.close()
            self.updateTitle()

    def saveas(self,event=None):
        file=str(filedialog.asksaveasfilename(title="Save as File",defaultextension=".txt",filetypes=[("all files","*.*"),('CSS','.css'),('TEXT','.txt'),('HTML','.html'),('PYTHON','.py'),('DOCUMENT','.docx')],initialdir='/storage/emulated/0/Documents/My_text_editor'))
        if len(file)>0:
            f = open(file,'w')
            text = self.ta.get("1.0",END)
            f.write(text)
            f.close()
            self.filename = file 
            self.updateTitle()

root = Tk()
newicon = PhotoImage(file='new_file.gif',width=24,height=24)
openicon = PhotoImage(file='open_file.gif')   
saveicon = PhotoImage(file='save.gif')
cuticon = PhotoImage(file='cut.gif')
copyicon = PhotoImage(file='copy.gif')
pasteicon = PhotoImage(file='paste.gif')
undoicon = PhotoImage(file='undo.gif')
redoicon = PhotoImage(file='redo.gif')   
main(root)
root.mainloop()
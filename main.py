import tkinter
import os
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    _root = Tk()
    # default window width and height
    _thisWidth = 300
    _thisHeight = 300
    _thisTextArea = Text(_root)
    _thisMenuBar = Menu(_root)
    _thisFileMenu = Menu(_thisMenuBar,tearoff=0)
    _thisEditMenu = Menu(_thisMenuBar,tearoff=0)
    _thisHelpMenu = Menu(_thisMenuBar,tearoff=0)

    # To add scrollbar
    _thisScrollBar = Scrollbar(_thisTextArea)
    _file = None

    def __init__(self,**kwargs):
        # Set icon
        try:
            self._root.wm_iconbitmap('Notepad.ico')
        except:
            pass

        # Set Window size (the default is 300x300)
        try:
            self._thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self._thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set window text
        self._root.title("Untitled-Notepad")

        # Center the window
        screenWidth = self._root.winfo_screenwidth()
        screenHeight = self._root.winfo_screenheight()

        # For left-allign
        left = (screenWidth/2)-(self._thisWidth/2)

        # For right allign
        top = (screenHeight/2)-(self._thisHeight/2)

        # For topo and botton
        self._root.geometry('%dx%d+%d+%d'%(self._thisWidth,self._thisHeight,left,top))

        # To make the text area auto resizeable
        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0,weight=1)

        # Add controls(widget)
        self._thisTextArea.grid(sticky=N+E+S+W)

        # To open new file
        self._thisFileMenu.add_command(label='New',command=self._newFile)

        # To open a already existing file
        self._thisFileMenu.add_command(label='Open',command=self._openFile)

        # To save a current file
        self._thisFileMenu.add_command(label='Save',command=self._saveFile)

        # To create a line in the dialog
        self._thisFileMenu.add_separator()  # add separation between commands
        self._thisFileMenu.add_command(label='Exit',command=self._quitApplication)
        self._thisMenuBar.add_cascade(label="File",menu=self._thisFileMenu)
        # add_cascade creates a hierarchical menu to the parent menu
        # To give a feature of cut
        self._thisEditMenu.add_command(label='Cut',command=self._cut)

        # To give a feature of copy
        self._thisEditMenu.add_command(label='Copy',command=self._copy)

        # To give a feature of paste
        self._thisEditMenu.add_command(label='Paste',command=self._paste)

        # To give a feature of editing
        self._thisMenuBar.add_cascade(label='Edit',menu=self._thisEditMenu)

        # To create a feature of description of the notepad
        self._thisHelpMenu.add_command(label='About Notepad',command=self._showAbout)
        self._thisMenuBar.add_cascade(label='Help',menu=self._thisHelpMenu)

        self._root.config(menu=self._thisMenuBar)
        self._thisScrollBar.pack(side=RIGHT,fill=Y)

        # Scrollbar will adjust automatically according to the content
        self._thisScrollBar.config(command=self._thisTextArea.yview)
        self._thisTextArea.config(yscrollcommand=self._thisScrollBar.set)

    def _quitApplication(self):
        self._root.destroy()
        # exit()

    def _showAbout(self):
        showinfo('Notepad',"Sarvesh Kumar")

    def _openFile(self):
        self._file=askopenfilename(defaultextension='.txt',filetypes=[('All Files:','*.*'),('Text Documents','*.txt')])

        if self._file == '':
            # no file to open
            self._file=None
        else:
            # Try to open the file
            # set the window title
            self._root.title(os.path.basename(self._file)+ "- Notepad")
            self._thisTextArea.delete(1.0,END)
            file = open(self._file,'r')
            self._thisTextArea.insert(1.0,file.read())
            file.close()

    def _newFile(self):
        self._root.title('Untitled - Notepad')
        self._file = None
        self._thisTextArea.delete(1.0,END)

    def _saveFile(self):
        if self._file == None:
            # Save as new file
            self._file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*,*'),("Text Documents",'*.txt')])

            if self._file == '':
                self._file=None
            else:
                # Try to save the file
                file = open(self._file,'w')
                file.write(self._thisTextArea.get(1.0,END))
                file.close()

                # Change the window title
                self._root.title(os.path.basename(self._file)+ "- Notepad")
        else:
            file = open(self._file,'w')
            file.write(self._thisTextArea.get(1.0,END))
            file.close()

    def _cut(self):
        self._thisTextArea.event_generate('<<Cut>>')

    def _copy(self):
        self._thisTextArea.event_generate("<<Copy>>")

    def _paste(self):
        self._thisTextArea.event_generate('<<Paste>>')

    def run(self):
        # Run main application
        self._root.mainloop()

# Run main application
notepad = Notepad(width=600,height=400)
notepad.run()




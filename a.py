from tkinter import *



class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("TCPDUMP Creator")
        #self.centerWindow()
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)
        self.columnconfigure(2, weight=5)

        lf = LabelFrame(parent, text="Filter Data")
        lf.pack(fill="both", expand="yes")
        f = LabelFrame(lf, width=600, height=300)
        frame1 = LabelFrame(lf, text="Interface")


        frame1.pack(side="top", fill="both")
        #frame1.place(relx=0.10, rely=0.125, anchor=NW)
        int_lbl = Label(frame1, text="Int.")
        int_lbl.pack(side="left", fill=X)
        self.int_entry = Entry(frame1, width=15)
        self.int_entry.pack(side="left")

        frame2 = Label(lf, text="")
        frame2.pack(side='top', fill=X)

        self.anyInt = BooleanVar()
        Checkbutton(frame1, text="Any", variable = self.anyInt).pack(side="left")

        frame2=LabelFrame(lf, text="IP Options")
        frame2.pack(side="top", fill="both")
        self.notSrc = BooleanVar()
        Checkbutton(frame2, text = "Not--", variable = self.notSrc).pack(side="left")
        self.srcIP = BooleanVar()
        Checkbutton(frame2, text="Src", variable = self.srcIP).pack(side="left")
        self.src_entry = Entry(frame2, width=15)
        self.src_entry.pack(side="left")

        self.AndOr = StringVar()
        self.AndOr.set(None)

        andbtn = Radiobutton(frame2, text = "And", variable = self.AndOr, value = "And").pack(side="left", padx=25)
        orbtn = Radiobutton(frame2, text = "Or", variable = self.AndOr, value = "Or").pack(side="left", padx=15)

        self.notDst = BooleanVar()
        Checkbutton(frame2, text = "Not--", variable = self.notDst).pack(side="left", padx=20)

        self.dstIP = BooleanVar()
        Checkbutton(frame2, text="Dst", variable = self.dstIP).pack(side="left")

        self.dst_entry = Entry(frame2, width=15)
        self.dst_entry.pack(side="left")

        frame3 = Label(lf, text="")
        frame3.pack(side='top', fill=X)

        frame3 = LabelFrame(lf, text="")
        frame3.pack(side="top", fill="both")

        self.AndOrport = StringVar()
        self.AndOrport.set(None)

        srcAnd=Radiobutton(frame3, text = "And", variable = self.AndOrport, value = "And").pack(side='left')
        self.srcOr=Radiobutton(frame3, text = "Or", variable = self.AndOrport, value = "Or").pack(side='left')

        frame4 = Label(lf, text="")
        frame4.pack(side='top', fill=X)

        frame4 = LabelFrame(lf, text="Ports")
        frame4.pack(side="top", fill="both")

        self.notSrcPort = BooleanVar()
        Checkbutton(frame4, text = "Not--", variable = self.notSrcPort).pack(side="left")

        self.srcport_lbl = Label(frame4, text="Src Port")
        self.srcport_lbl.pack(side="left")

        self.srcport_entry = Entry(frame4, width=15)
        self.srcport_entry.pack(side="left")

        self.SrcDstport = StringVar()
        self.SrcDstport.set(None)

        Radiobutton(frame4, text = "And", variable = self.SrcDstport, value = "And").pack(side='left', padx=25)
        Radiobutton(frame4, text = "Or", variable = self.SrcDstport, value = "Or").pack(side='left', padx=15)

        self.notDstPort = BooleanVar()
        Checkbutton(frame4, text = "Not--", variable = self.notDstPort).pack(side="left")

        self.dstport_lbl = Label(frame4, text="Dst Port")
        self.dstport_lbl.pack(side="left")

        self.dstport_entry = Entry(frame4, width=15)
        self.dstport_entry.pack(side="left")

        frame5 = Label(lf, text="")
        frame5.pack(side="top", fill=X)

        frame5 = LabelFrame(lf, text="Options")
        frame5.pack(side="top", fill="both")

        self.listInterfaces = BooleanVar()
        Checkbutton(frame5, text = "List Interfaces", variable = self.listInterfaces).pack(side="left")

        cap_lbl = Label(frame5, text="# of Packets to Capture")
        cap_lbl.pack(side="left")
        self.cap_entry = Entry(frame5, width=3)
        self.cap_entry.pack(side="left")

        self.noDNS = BooleanVar()
        Checkbutton(frame5, text = "Don't Translate Hostnames & Ports", variable = self.noDNS).pack(side="left", padx=15)

        verbosity_lbl = Label(frame5, text="Verbosity:")
        verbosity_lbl.pack(side="left")

        self.verbosity = StringVar()
        self.verbosity.set(None)

        Radiobutton(frame5, text = "Low", variable = self.verbosity, value = "-v").pack(side='left')
        Radiobutton(frame5, text = "Med", variable = self.verbosity, value = "-vv").pack(side='left', padx=15)
        Radiobutton(frame5, text = "High", variable = self.verbosity, value = "-vvv").pack(side='left', padx=15)

        frame6 = LabelFrame(lf, text="")
        frame6.pack(side="top", fill="both")

        self.timeformat = StringVar()
        self.timeformat.set(None)

        Radiobutton(frame6, text="Human Readable Time Format", variable=self.timeformat, value="-tttt").pack(side="left", padx=10)
        self.write2file = StringVar()
        self.write2file.set(None)
        Radiobutton(frame6, text = "Write to File", variable = self.write2file, value="-w").pack(side='left')
        write_lbl = Label(frame6, text="Filename")
        write_lbl.pack(side="left")
        self.file_entry = Entry(frame6, width=15)
        self.file_entry.pack(side='left')

        frame7 = Label(lf, text="")
        frame7.pack(side='top', fill=X)

        frame8 = Label(lf, text="")
        frame8.pack(side="top", fill=X)

        createBttn = Button(frame8, text="Create", width=15, height=2, relief="ridge", anchor=CENTER, command=self.create)
        createBttn.pack(side="left", padx=70)

        clearBttn = Button(frame8, text="Clear", width=15, height=2, relief="ridge", anchor=CENTER, command=self.clear)
        clearBttn.pack(side="left", padx=70)

        self.exitBttn = Button(frame8, text="Exit", width=15, height=2, relief="ridge", anchor=CENTER, command=self.exit)
        self.exitBttn.pack(side="left", padx=70)

        frame9 = Label(lf, text="Filter Data")
        frame9.pack(side="top", fill=X)

        frame10 = Label(lf, text="")
        frame10.pack(side="left")

        self.filterData = Text(frame10, width=95, height=1.2)
        self.filterData.pack(side="left")


    def centerWindow(self):
        w = 600
        h = 300
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2.7
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))

    def clear(self):
        try:
            self.filterData.delete(0.0, END)    #delete from text box
            self.int_entry.delete(0, END)       #delete from entry box
            self.src_entry.delete(0, END)
            self.dst_entry.delete(0, END)
            self.srcport_entry.delete(0, END)
            self.dstport_entry.delete(0, END)
            self.file_entry.delete(0, END)
            self.cap_entry.delete(0, END)
            self.anyInt.set(0)
            self.notSrc.set(0)
            self.srcIP.set(0)
            self.noDNS.set(0)
            self.listInterfaces.set(0)
            self.notDstPort.set(0)
            self.notSrcPort.set(0)
            self.dstIP.set(0)
            self.srcAnd.deselect()
            self.srcOr.deselect()
            self.SrcDstport.deselect()
            deselect(self.timeformat)
            self.write2file.deselect()
            self.SrcDstport.deselect()


        except:
            pass
    def exit(self):
        self.quit()

    def create(self):
        if self.anyInt.get():
            self.filterData.insert(0.0, "tcpdump " + "-i " + "any")
        else:
            self.filterData.insert(0.0, "tcpdump " + "-i " + self.int_entry.get())





def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
from random import randint as ran
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
stelleInFrame=0
master=Tk()
master.geometry("1000x707+-7+0")
master.title("Fragebogengestaltung")
Label(master,text="Neuer Fragebogeneintrag:").place(x=13,y=570)
appendFrame=Frame(master,width=90,height=7)
appscr=Scrollbar(appendFrame,orient=VERTICAL)
newEntry=Text(appendFrame,width=80,height=7,yscrollcommand=appscr.set)
appscr.config(command=newEntry.yview)
dotfr=Frame(master,width=120,height=30)
dotscr=Scrollbar(dotfr,orient=VERTICAL)
dotText=Text(dotfr,width=110,height=30,yscrollcommand=dotscr.set)
dotscr.config(command=dotText.yview)
Label(master,text="° ist Enter im Programm.").place(x=300,y=5)
saveLabel=Label(master,text="nicht gespeichert")
def appendNew():
    st=newEntry.get("1.0",END)
    new_list=[]
    for int1 in st:
        new_list.append(int1)
    sk=new_list[:-1]
    sl="".join(sk)
    sp=sl.split("\n")
    sn="°".join(sp)
    new_entr=sn.split("°°")
    
    for i in new_entr:
        dotText.insert(END,"  -"+i+"\n")
    del(sl)
    del(sk)
    del(new_list)
    del(st)
    del(sn)
    del(sp)
newEntry.pack(side=RIGHT,fill=Y)
appscr.pack(side=LEFT,fill=Y)
appendFrame.place(x=170,y=565)
hinzufug=Button(master,text="Hinzufügen",command=appendNew,width=25,height=7).place(x=815,y=565)
Label(master,text="Zufallszuweisung:").place(x=14,y=588)
def zufalls_():
    k=[]
    text_=dotText.get("1.0",END)
    text=text_[0:-1]
    eint=text.split("\n")
    lenEintr=len(eint)-1
    for i in range(0,lenEintr):
        k.append(i)
    typedL=list()
    typedL.extend(eint)
    randL=[]
    k=k
    for j in range(lenEintr):
        c=ran(0,k[-1])
        m=typedL[c]
        randL.append(m)
        typedL.remove(m)
        k.remove(k[-1])
    op="\n".join(randL)
    kop_=op.split("°")
    kop="\n   ".join(kop_)
    op=kop
    del(kop)
    del(kop_)
    def save_file():
        saaa=savtext_.get("1.0",END)
        savwin.destroy()
        nonlocal op
        file_name = filedialog.askdirectory()
        tk=Tk()
        tk.geometry("291x163")
        tk.title("Dateiname")
        Label(tk,text="Dateiname:").place(x=7,y=4)
        dn_=Entry(tk,width=29)
        Label(tk,text=".txt").place(x=263,y=5)
        def save():
            nonlocal op
            file=file_name+"/"+dn_.get()+".txt"
            l=open(file,"a")
            l.write(saaa)
            l.close()
            tk.destroy()
            saveLabel.config(text="gespeichert")
        sb=Button(tk,text="Fertig",command=save,width=37,height=4).place(x=10,y=50)
        dn_.place(x=77,y=5)
        tk.mainloop()
    savwin=Tk()
    savwin.title("Speichern")
    savwin.geometry("470x320")
    texfr=Frame(savwin,width=55,height=10)
    savscr=Scrollbar(texfr,orient=VERTICAL)
    savtext_=Text(texfr,height=10,width=49,yscrollcommand=savscr.set)
    savtext_.insert(END,op)
    savscr.config(command=savtext_.yview)
    savtext_.pack(side=LEFT,fill=Y)
    savscr.pack(side=RIGHT,fill=Y)
    texfr.place(x=5,y=3)
    saveB=Button(savwin,text="Speichern",width=50,height=2,command=save_file).place(x=20,y=180)
    savwin.mainloop()
zuweisen=Button(master,text="Zuweisen",width=18,height=4,command=zufalls_).place(x=18,y=609)
dotText.pack(side=RIGHT,fill=Y)
dotscr.pack(side=LEFT,fill=Y)
dotfr.place(x=30,y=30)
saveLabel.place(x=835,y=515)
mainloop()

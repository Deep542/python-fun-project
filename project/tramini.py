from tkinter import*
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator


root=Tk()
root.title("Language Translator")
root.geometry("1000x400")
root.resizable(1,1)
root.configure(background="#AEE2FF")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

#-----------------------------------------------------------------------------------

def translate_now():
    
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate( text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text


    text2.delete(1.0,END)
    text2.insert(END,trans_text)    

#--------------------------------------------------------------------------------------
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,image_icon)

arrow_image=PhotoImage(file="arrow.png")
image_label=Label(root,image=arrow_image,width=225)
image_label.place(x=560,y=70)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Arial",state="r")
combo1.place(x=130,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="Arial 30 bold",bg="white",width=20,bd=10,relief=GROOVE)
label1.place(x=15,y=55)
#-------------------------------------------------------------------------------------------------------------
combo2=ttk.Combobox(root,values=languageV,font="Arial",state="r")
combo2.place(x=950,y=20)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font="Arial 30 bold",bg="white",width=20,bd=10,relief=GROOVE)
label2.place(x=830,y=55)

f=Frame(root,bg="Black",bd=10)
f.place(x=40,y=170,width=445,height=400)

text1=Text(f,font="Robote 25",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=425,height=380)

Scrollbar1=Scrollbar(f)
Scrollbar1.pack(side="right",fill='y')



Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)


f1=Frame(root,bg="Black",bd=10)
f1.place(x=860,y=170,width=445,height=400)


#-------------------------------------------------------------------------------------------------------

text2=Text(f1,font="Robote 25",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=425,height=380)

Scrollbar3=Scrollbar(f1)
Scrollbar3.pack(side="right",fill='y')

Scrollbar3.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar3.set)


translate=Button(root,text="Translate",font=("Robote",25),activebackground="white",cursor="hand2",bd=1,width=10,height=2,bg="black",fg="#1597BB",command=translate_now)
translate.place(x=555,y=450)


label_change()

root.mainloop()
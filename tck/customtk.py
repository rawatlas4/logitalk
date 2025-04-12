from  customtkinter import*
from PIL import Image
from socket import*#імпортуємо моудль
import threading
client = socket(AF_INET , SOCK_STREAM)
# client.connect(("6.tcp.eu.ngrok.io",17952))
client.connect(("localhost",12345))


load_image = Image.open("Imagee.png")#загрузка фото
img = CTkImage(light_image=load_image,size= (50,50))#тоже загрузка
windows = CTk()
windows.configure(fg_color="blue")
windows.title("пупсичек")
windows.geometry("390x500")
f1 = CTkFrame(windows,width=350,height=380,fg_color="black")#f = фрейм
f1.pack_propagate(False)
f2 = CTkFrame(windows,width=350,height=60)
f2.pack_propagate(False)

def recive():
    while 1:
        try:
            prinyat_sms = client.recv(1024).decode()
            gde_smotret_tekst.configure(state="normal")
            gde_smotret_tekst.insert(END,"server:" + prinyat_sms + "\n")
            gde_smotret_tekst.configure(state='disable')
        except:
            pass    
threading.Thread(target=recive).start()#поток

def click():#когда нажимаеш на кнопку чтоб переносился текст
    sms = ent.get()
    client.send(sms.encode())
    ent.delete(0,END)
    gde_smotret_tekst.configure(state="normal")
    gde_smotret_tekst.insert(END,"user1:" + sms + "\n")
    gde_smotret_tekst.configure(state='disable')
def on_enter(event):#текст только вместо кнопки ентер
    click()
ent = CTkEntry(f2,placeholder_text="ТЕКСТ ТУТ",width=230,height=40,)
ent.bind("<Return>", on_enter)

ent.pack(side='left')
b1 = CTkButton(f2,text="S E N D",image = img,compound="right",width=10, command=click)
b1.pack(side = "right")
f1.pack(pady = 20)
f2.pack(pady = 20)
gde_smotret_tekst = CTkTextbox(f1,state='disable', width=300, height=360)
gde_smotret_tekst.pack()



windows.mainloop()
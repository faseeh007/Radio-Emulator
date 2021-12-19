# Import module
from os import terminal_size
from tkinter import *
from PIL import ImageTk,Image
import requests
import time 
import datetime
import asyncio
import  tkinter.filedialog as fd
import sys
import tkinter
from playsound import playsound
import webbrowser
import winsound
import sounddevice as sd
from scipy.io.wavfile import write
import multiprocessing
import socket
import pyaudio
import wave
import time
import os


#BACKEND
p = multiprocessing.Process(target=playsound, args=("Noise.wav",))
q = multiprocessing.Process(target=playsound, args=("Starting.wav",))
r = multiprocessing.Process(target=playsound, args=("bite.wav",))

def turnon():
    playsound("VPS Emulator/Noise.wav")


def turnoff():
    #playsound("Noise.wav")
    if p.is_alive():
        p.terminate()


def turnseroff():
    global ptts
    #playsound("Noise.wav")
    if ptts.is_alive():
        ptts.terminate()
   

def turnclioff():
    global pttc
    #playsound("Noise.wav")
    if pttc.is_alive():
        pttc.terminate()


def sq():
    playsound("VPS Emulator\Starting.wav")
    

def bite():
    playsound("VPS Emulator\bite.wav")


def test():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording) 
    playsound("output.wav")
  


def pttser():
    global ptts
    if ptts.is_alive():
        ptts.join()
    else:
        ptts = multiprocessing.Process(target=server)
        ptts.start()

   
    return({"Server":"Closed"})

def pttcli():
    global pttc
    if pttc.is_alive():
        pttc.join()
    else:
        pttc = multiprocessing.Process(target=client)
        pttc.start()

    return({"Client":"Closed"})
#from beepy import beep
#from pybeep.pybeep import PyVibrate, PyBeep




frequency = 800  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

#Global Variable
    
# Create object
root = Tk()
pwd="PW****"
deg=360
deg1=360
login=0
sq=0
clickEnt=0
clickCr=0
clickInc=0
ptts=0
pttc=0
incpf=2
d1=0
d2=0
d3=0
d4=0
inco=0
#Sound Functions


def test():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording) 
    playsound("output.wav")
# Thread funcs
'''
def change_color():
    current_color = box.cget("background")
    next_color = "green" if current_color == "red" else "red"
    box.config(background=next_color)
    root.after(1000, change_color)

'''
def delay(e,cm,d=0):
    global deg,incpf,inco,d1,d2,d3,clickInc

    print("wait")
    e.delete(d,END)
    if(cm=="BITE"):
        e1.configure(bg="yellow")
    else:
        e1.configure(bg="#321f21")
    e.insert(d,cm)
    print("Done "+ str(cm))
    if (deg==180) and (clickInc==1):
        print("Done "+ str(e.get()))
        if (inco==0 and d1==0 and d2==0 and d3==0 and d4==0):
            print(incpf, " incp ",clickEnt)
            incpf=incpf+1
            
       

#getting screen width and height of display
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
#Frame
frame1 = Frame(root, height = height, width = width)
#Create Logo
root.title("Emulator")
root.iconbitmap("./Images/logo_icon.ico")


# Adjust size
#root.geometry("1400x1400")

#Header
my_head=Menu(root)
root.config(menu=my_head)


def open():
        os.startfile("Docs\BOOKLET ON EMULATOR.pdf")
def ietm_comm():
    webbrowser.open_new("http://localhost/VPS/")
def our_comm():
    pass
def chatbot_comm():
    webbrowser.open_new("http://localhost/chatbot/wp-login.php?")
#Creating a menu item
file_menu=Menu(my_head)
my_head.add_cascade(label="About",menu=file_menu)
file_menu.add_command(label="Server")
file_menu.add_command(label="Client")
file_menu.add_command(label="Help",command=our_comm)
file_menu.add_command(label="Contact",command=open)
file_menu.add_command(label="IETM",command=ietm_comm)
file_menu.add_command(label="Chatbot",command=chatbot_comm)
file_menu.add_command(label="Specifications",command=our_comm)

root.configure(bg="white")
'''
#Coordinates
def doSome(event):
    print("MOUSE CORDINATES " +str( event.x)+","+str( event.y)+" ")
root.bind("<Any-Button>",doSome)
'''


# Create a photoimage object of the side view image in the path

image2 = Image.open("Images\side_view.png")
side_view = ImageTk.PhotoImage(image2)

label2 = Label(image=side_view,borderwidth=0)
label2.image = side_view

# Position image
label2.place(x=50, y=10)


#Sq
def onSq(): 
    print("Hello SQ")
    global sq
    #if (deg==288):
    print(e.get())
    c=e.get()
    e1.configure(background="red")
    #e1.insert(0,".")
    if (e.get()=="BAT ***") or (e.get()=="C SQL OFF"):
        root.after(5,e1.configure(bg="red"))
        print(e1.get())
        sq=1
        print(sq)
        root.after(2000,delay,e,"C SQL ON")
        root.after(3000,playsound,"VPS Emulator/Noise.wav")
    elif e.get()=="C SQL ON":
        root.after(1000,e1.configure(bg="#321f21"))
        sq=0        
        root.after(10,delay,e,"C SQL OFF")
        print(sq)

# Create a photoimage object of the sq image in the path
image2_1 = (Image.open("Images/sq.png"))
image2_11=image2_1.resize((35,46), Image.ANTIALIAS)
sq = ImageTk.PhotoImage(image2_11)

label2_1 = Label(image=sq)
label2_1.image = sq
button_sq=Button(root,image=label2_1.image,command=onSq,bg="#241e1e",borderwidth=0)
# Position image
button_sq.place(x=205, y=335)

#Ptt
def onPtt(event):
    global ptts
    global pttc
    e.delete(0,END)
    e.insert(0,"M*403000")
    if(event.num==1):
        #In Server Apllication
        if(ptts==0) and (pttc!=1):
            requests.get('http://localhost:5000//pttserver')
            #pttser()
            print("Waiting to connect to client")
            ptts=1
        elif ptts==1 and (pttc!=1) :
            requests.get('http://localhost:5000//pttseroff')
            #turnseroff()
            print("Disconnected from client")
            ptts=0

    if(event.num==3):
        #IN client applicatioon
        if(pttc==0) and(ptts!=1):
            requests.get('http://localhost:5000//pttclient')
            #pttcli()
            print("Waiting to connect to server")
            pttc=1
        elif pttc==1 and (ptts!=1):
            requests.get('http://localhost:5000//pttclioff')
            #turnclioff()
            print("Disconnected from server")
            pttc=0
    
    
# Create a photoimage object of the ppt image in the path
image2_2 = (Image.open("Images/ptt.png"))
image2_22=image2_2.resize((35,75), Image.ANTIALIAS)
ppt = ImageTk.PhotoImage(image2_22)

label2_2 = Label(image=ppt)
label2_2.image = ppt
button_ppt=Button(root,image=label2_2.image,bg="#222020",borderwidth=0)
button_ppt.bind("<Any-Button>",onPtt)

# Position image
button_ppt.place(x=198, y=395)
#'''
# Create a photoimage object of the front view image in the path
image3 = Image.open("Images/front_view.png")
front_view = ImageTk.PhotoImage(image3)

label3 = Label(image=front_view,borderwidth=0)
label3.image = front_view

# Position image
label3.place(x=550, y=10)

#Blink
e1=Entry(root,bg="#321f21",fg="white",borderwidth=0)
e1.grid(row=650,column=20)
e1.place(x=670,y=469,width=10,height=10)
'''
my_canvas = tkinter.Canvas(root, width=20, height=20)  # Create 200x200 Canvas widget
my_canvas.pack()

my_oval = my_canvas.create_oval(50, 50, 100, 100)  # Create a circle on the Canvas

'''
#Entry 
e=Entry(root,bg="black",fg="black",borderwidth=3,insertontime=1,justify="center",font="Helvetica 15 bold")
e.grid(row=650,column=20,padx=100,pady=380)
e.place(x=635,y=494,width=198,height=35)
e.insert(1,"")



#MDV
def onmdv():
    global  pwd
    global deg,deg1,d1,d2,d3,d4
    global login
    #pwd.length
    
  
   
   # print(e.get())
    
    if e.get()==pwd and deg==324:
        login=1
        #root.after(1000)
        root.after(3000,delay,e,'PW OK')
        root.after(4000,delay,e,"BITE")        
        # requests.get("http://localhost:5000/sq")
        root.after(5000,delay,e,'*PASS*')
        winsound.Beep(440, 500)
         #print('\a')
         #PyBeep().beep()
         #root.after(1000)
         #delay(e,"ID 28361")
        root.after(6000,delay,e,'ID 28361') 
        root.after(7000,delay,e,"CLR INL")
        root.after(8000,delay,e, "M*403000")
    
    elif deg==324:
        e.insert(2,"*")
    
    elif(deg==180):
        '''
        if incpf==5:
             t=e.get()
             t=int(t[3:])+10000
             print(t,incpf)
             d1=1
             d2,d3=0,0
             d4=0
             if(t<80000):
                root.after(10,delay,e,t,3)
        '''
        if incpf==4:
             #print(t1)
             d2=1
             d1,d3=0,0
             d4=0
             t1=e.get()
             t1=int(t1[4:])+1000
             print(t1,incpf)
             if(t1<9999):
                root.after(10,delay,e,t1,4)
                print(e.get())
        elif incpf==5:
             #print(t1)
             d3=1
             d1,d2,d4=0,0,0
             t2=e.get()
             t2=int(t2[5:])+100
             print(t2,incpf)
             if(t2<1000):
                print(t2,incpf)
                root.after(10,delay,e,t2,5)
                print(e.get())
        elif incpf==6:
             #print(t1)
             d4=1
             d1,d2=0,0
             d3=0
             t3=e.get()
             t3=int(t3[6:])+25
             
             if(t3<100):
                print(t3,incpf)
                root.after(10,delay,e,t3,6)
                print(e.get())


        # print(login)
    ##  print("hello")
       
   

# Create a photoimage object of the mdv image in the path
image3_1 = (Image.open("Images/mdv.png"))
image3_11=image3_1.resize((35,35), Image.ANTIALIAS)
mdv = ImageTk.PhotoImage(image3_11)
label3_1 = Label(image=mdv)
label3_1.image = mdv
button_mdv=Button(root,image=label3_1.image,command=onmdv,bg="#321f21",borderwidth=0)

# Position image
button_mdv.place(x=811, y=303) 
#button_mdv.pack(ipadx= 5, ipady=5, padx= 20)

#CRV
def oncrv():    
    #e.delete(0,END)
    print("CRV")
    global clickCr,d1,d2,d3,d4
    clickCr=1
    if(deg==180): 
        if (e.get()=="M*403025") or (e.get()=="HIGH POW"):
            root.after(10,delay,e,"LOW POW")
        elif(e.get()=="LOW POW"):
           root.after(10,delay,e,"HIGH POW")
        else:
            '''
            if incpf==4:
                t=e.get()
                t=int(t[3:])-10000
                print(t,incpf)
                d1=1
                d2,d3=0,0
                d4=0
                if(t>9999):
                    root.after(10,delay,e,t,3)
            el'''
            if incpf==4:
                #print(t1)
                d2=1
                d1,d3=0,0
                d4=0
                t1=e.get()
                t11=int(t1[4:])-1000
                print(t11,incpf)
                if(t11>999):
                    root.after(10,delay,e,t11,4)
                    print(e.get())
                else:
                    t12="0"+str(t1[5:])
                    print(t12,incpf)
                    root.after(10,delay,e,t12,4)
                    print(e.get())
            

            elif incpf==5:
                #print(t1)
                d3=1
                d1,d2,d4=0,0,0
                t2=e.get()
                t21=int(t2[5:])-100
                if(t21>99):                    
                    print(t21,incpf)
                    root.after(10,delay,e,t21,5)
                    print(e.get())
                else:
                    t22="0"+str(t2[6:])
                    print(t22,incpf)
                    root.after(10,delay,e,t22,5)
                    print(e.get())
            
                    
            elif incpf==6:
                #print(t1)
                d4=1
                d1,d2=0,0
                d3=0
                t3=e.get()
                t31=int(t3[6:])-25
                print(t31,incpf)
                if(t31>0):
                    root.after(10,delay,e,t31,6)
                    print(e.get())
                else:
                    t22="00"
                    print(t22,incpf)
                    root.after(10,delay,e,t22,6)
                    print(e.get())

    elif(deg==108):
        print("Hello 108 from crv")
        if e.get()=="CLONE" or e.get()=="CLN FRQ?":
            root.after(10,delay,e,"CLN KEY?")
        elif e.get()=="CLN KEY?":
            root.after(10,delay,e,"CLN FRQ?")
    elif(deg1==360):
        e.delete(0,END)
        e.insert(0,"M* 403000")
# Create a photoimage object of the crv image in the path
image3_2 = (Image.open("Images/crv1.png"))
image3_22=image3_2.resize((35,35), Image.ANTIALIAS)
crv = ImageTk.PhotoImage(image3_22)

label3_2 = Label(image=crv)
button_mdv=Button(root,image=crv,command=oncrv)
label3_2.image = crv
button_crv=Button(root,image=label3_2.image,command=oncrv,bg="#321f21",borderwidth=0)

# Position image
button_crv.place(x=811,y=347) 

#Inc
def onInc(): 
    global incpf,deg,d1,d2,d3,inco,d4,clickInc
    print("INC",deg,incpf)
    inco=1
    
    if deg==180:
        clickInc=1
        if(incpf==2):
            inco=0
            root.after(1000,delay,e,e.get())
            print(incpf)
            d1,d2,d3,d4=0,0,0,0
        elif (incpf==3):
            inco=0
            root.after(1000,delay,e,e.get())
            print(incpf)
            d1,d2,d3,d4=0,0,0,0
        elif (incpf==4):
            inco=0
            root.after(1000,delay,e,e.get())
            print(incpf)
            d1,d2,d3,d4=0,0,0,0
        elif (incpf==5):
            inco=0
            root.after(1000,delay,e,e.get())
            print(incpf)
           
            d1,d2,d3,d4=0,0,0,0
        elif (incpf==6):
            inco=0
            root.after(1000,delay,e,e.get())
            print(incpf)
            d1,d2,d3,d4=0,0,0,0
        elif(incpf>=7):
            while(incpf!=3):
                incpf-=1
    elif(deg==108):
        if (e.get()=="CLN FRQ?") or (e.get()=="CLN KEY?") or (e.get()=="SLAVE"):
           print("Hello 108 from MASTER")
           root.after(10,delay,e,"MASTER")
        elif (e.get()=="MASTER"):
            print("Hello 108 from SLAVE")
            root.after(10,delay,e,"SLAVE")
    elif(deg1==360):
         e.delete(0,END)
         e.insert(0,"MASTER")
         #time.sleep(1)
         e.delete(0,END)
         e.insert(0,"SLAVE")

# Create a photoimage object of the inc image in the path
image3_3 = (Image.open("Images/inc1.png"))
image3_33=image3_3.resize((35,35), Image.ANTIALIAS)
inc = ImageTk.PhotoImage(image3_33)

label3_3 = Label(image=inc)
label3_3.image = inc
button_inc=Button(root,image=label3_3.image,command=onInc,bg="#321f21",borderwidth=0)


# Position image
button_inc.place(x=811, y=385) 

#Ent
def onEnt():    
    #e.delete(0,END)
    #e.insert(0,"Start")
    global deg
    global login
    global clickEnt
    print(e.get())
    if (deg==252):
        root.after(3000,delay,e,"SEC  L")
        root.after(4000,delay,e,"M*403000")
        root.after(5000,delay,e,"ID 28369")
        root.after(6000,delay,e,"ID 28361")
        root.after(7000,delay,e,"CoM 30E4")
        root.after(8000,delay,e,"DAM 3Fg2")
        root.after(9000,delay,e,"AKY D50E")
        root.after(10000,delay,e,"BAT  ***")
    if (deg==216):
        root.after(2000,delay,e,"SEC LCL")
        root.after(3000,delay,e,"L2 C2")
        root.after(4000,delay,e,"M*403000")
    if (deg==180):
        
        if(e.get()=="PROGRM"):
            root.after(1000,delay,e,"PW")
        elif(e.get()=="PW****"):
            clickEnt=1
            print("Hello P and Ent")
            root.after(2000,delay,e,"PRESET")
            root.after(3000,delay,e,"M*407000")
            root.after(4000,delay,e,"M*40325")
        elif (e.get!="PW****"):
            e.insert(2,"*")
            print(e.get())
       
    if(deg==144):
        root.after(1,delay, playsound,"VPS Emulator\bite.wav")
        root.after(2000,delay,e,"A1")
        root.after(3000,delay,e,"* PASS *")
        root.after(4000,delay,e,"A2")
        
        root.after(5000,delay,e,"* PASS *")
        root.after(6000,delay,e,"A3")
        root.after(7000,delay,e,"* PASS *")
        root.after(8000,delay,e,"BATRY OK ")
        root.after(9000,delay,e,"* TALK *")
        root.after(10000,test)
        root.after(11000,delay,e,"BITE")
         
    #degfunc(deg)
# Create a photoimage object of the ent image in the path
image3_4 = (Image.open("Images/ent1.png"))
image3_44=image3_4.resize((35,35), Image.ANTIALIAS)
ent = ImageTk.PhotoImage(image3_44)

label3_4 = Label(image=ent)
label3_4.image = ent
button_ent=Button(root,image=label3_4.image,command=onEnt,bg="#321f21",borderwidth=0)


# Position image
button_ent.place(x=811, y=423) 


# Create a photoimage object of the up view image in the path
image4 = Image.open("Images/up_view.png")
up_view = ImageTk.PhotoImage(image4)

label4 = Label(image=up_view,borderwidth=0)
label4.image = up_view

# Position image
label4.place(x=950, y=250)

#rsn
def sn(key=2000,i=1):
    print("Hello sn")
    global deg1
    snmod=["S CHN 1A","S CHN 2A","S CHN 3A","S CHN 4A","S CHN 5A","S CHN 6A","S CHN 7A","S CHN 8A"]
    for value  in snmod:
        key+=1000
        root.after(key,delay,e,value)
        if(i==3) and( key==29000):
            break
    sn(key=10000,i=2)
    sn(key=19000,i=3)
    #     i+=1
    #elif(i==1):
    #    for key, value in snmod.items():
    #        root.after(key,delay,e,value)
  

#DEG FUNC
def degfunc(deg,login):
    if(deg==360):
       # e.delete(0,END)
        #e.insert(0,"OFF")
        e.configure(bg="black")
    if(deg==324) :
        root.after(1000,delay,e,"RETR MOD")
        root.after(2000,delay,e,"PW")
        e.configure(bg="green")
       # e.delete(0,END)
       # e.insert(0,"PW")
        #oot.after(5,e.insert(0,"PW"))
    if (deg==288)and (login==1):
        print("Hello C")
        root.after(2000,delay,e,"CLR CR L")
        root.after(3000,delay,e,"M*403000")
        root.after(4000,delay,e,"ID 28369")
        root.after(5000,delay,e,"DAM 3F 31")
        root.after(6000,delay,e,"AKY D50E")
        root.after(7000,delay,e,"BAT ***")
        root.after(8000,playsound,"VPS Emulator/Noise.wav")
    
    if (deg==252) and (login==1):
        print("Hello S")
        root.after(100,delay,e,"SEC L")
        
    if (deg==216) and (login==1):
        print("Hello L")
        root.after(100,delay,e,"SEC LCL")

        
    if (deg==180) and (login==1):
        print("Hello P")
        root.after(100,delay,e,"PROGRM")
    if (deg==108) and (login==1):
        print("Hello N")
        root.after(100,delay,e,"CLONE")
    
    if (deg==144) and (login==1):
        print("Hello b")
        root.after(100,delay,e,"BITE")
    if (deg==72) and (login==1):
        print("Hello F")
        root.after(100,delay,e,"FIL/TRAN")
    if (deg==36) and (login==1):
            print("Hello E")
            root.after(100,delay,e,"ERAS/REM")

#DEG FUNC
def degfunc1(deg1,login):
    if(deg1==360):
            root.after(10,delay,e,"M* 403000")
    if(deg1==324):
            root.after(10,delay,e,"1A*40900")
    if (deg1==288):
         root.after(10,delay,e,"2A415025")
    if (deg1==252):
        root.after(10,delay,e,"3A425025")
    if (deg1==216):
      root.after(10,delay,e,"4A436025")    
    if (deg1==180):
        root.after(10,delay,e,"5A447025")
    if (deg1==144):
       root.after(10,delay,e,"6A458025")
    if (deg1==108):
       root.after(10,delay,e,"7A 468 025")
    if (deg1==72):
      root.after(10,delay,e,"8A470025")
    if (deg1==36):
       root.after(10,delay,e,"SN mod")
       sn()
#Knobs

def onKnob1(event):
    global deg 
    global login
    if(event.num==1):
        deg-=36
        if deg>=0:
            print(deg)
            image4_1 = (Image.open("Images/knob1.png"))
            image4_1=image4_1.resize((35,35), Image.ANTIALIAS).rotate(deg)
            knob = ImageTk.PhotoImage(image4_1)
            label4_1 = Label(image=knob)
            label4_1.image=knob
            button_knob1=Button(root,image=label4_1.image,bg="#321f21",borderwidth=0)
            button_knob1.bind("<Any-Button>",onKnob1)
            #  Position image
            button_knob1.place(x=1085, y=422)
            degfunc(deg,login)
        
        #print("Left")

    if (event.num==3): 
        deg+=36
        if deg<=360:
            print(deg)
            image4_1 = (Image.open("Images/knob1.png"))
            image4_1=image4_1.resize((35,35), Image.ANTIALIAS).rotate(deg)
            knob = ImageTk.PhotoImage(image4_1)
            label4_1 = Label(image=knob)
            label4_1.image=knob
            button_knob1=Button(root,image=label4_1.image,bg="#321f21",borderwidth=0)
            button_knob1.bind("<Any-Button>",onKnob1)
            degfunc(deg,login)
            #if(deg==72):
             #   e.delete(0,END)
              #  e.insert(0,"CN FG/PC ")

        # Position image
        button_knob1.place(x=1085, y=422)
       #print("right")
# Create a photoimage object of the knob image in the path
image4_1 = (Image.open("Images/knob1.png"))
image4_1=image4_1.resize((35,35), Image.ANTIALIAS)
knob = ImageTk.PhotoImage(image4_1)

label4_1 = Label(image=knob)
label4_1.image = knob
button_knob1=Button(root,image=label4_1.image,bg="#321f21",borderwidth=0)
# Position image
button_knob1.place(x=1085, y=422)

button_knob1.bind("<Any-Button>",onKnob1)



def onKnob(event):
    global deg1
    global login
    if(event.num==1):
        deg1-=36
        if deg1>=0:
            print(deg1)
            image4_2 = (Image.open("Images/knob1.png"))
            image4_2=image4_2.resize((35,35), Image.ANTIALIAS).rotate(deg1)
            knob1 = ImageTk.PhotoImage(image4_2)   
            label4_2 = Label(image=knob1)
            label4_2.image=knob1

            button_knob=Button(root,image=label4_2.image,bg="#321f21",borderwidth=0)
            button_knob.bind("<Any-Button>",onKnob)
            # Position image
            button_knob.place(x=1155, y=422)
            degfunc1(deg1,login)
    
     

    elif (event.num==3):
        deg1+=36
        if deg1<=360:
            print(deg1)
            image4_2 = (Image.open("Images/knob1.png"))
            image4_2=image4_2.resize((35,35), Image.ANTIALIAS).rotate(deg1)
            knob1 = ImageTk.PhotoImage(image4_2)   
            label4_2 = Label(image=knob1)
            label4_2.image=knob1
            button_knob=Button(root,image=label4_2.image,bg="#321f21",borderwidth=0)
            # Position image
            button_knob.place(x=1155, y=422)
            button_knob.bind("<Any-Button>",onKnob)
            degfunc1(deg1,login)
        print("right")
# Create a photoimage object of the knob image in the path

image4_2 = (Image.open("Images/knob1.png"))
image4_2=image4_2.resize((35,35))
knob1 = ImageTk.PhotoImage(image4_2)
label4_2 = Label(image=knob1)
label4_2.image = knob1
button_knob=Button(root,image=label4_2.image,repeatinterval=True,bg="#321f21",borderwidth=0)
# Position image
button_knob.place(x=1155, y=422)
button_knob.bind("<Any-Button>",onKnob)


#'''

# Execute tkinter
root.mainloop()
  

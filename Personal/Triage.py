from tkinter import *
import math
from tkinter.ttk import *
from tkinter import ttk
import os


class Triage(Frame):
    
   
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Triage")
        self.grid()
        self.master.geometry("600x300")

        #labels- first
        self.firstnameLabel = Label(self, text = "First")
        self.firstnameLabel.grid(row = 0, column =0 )
        self.firstnameVar = StringVar()
        self.firstnameEntry = Entry(self,textvariable = self.firstnameVar)
        self.firstnameEntry.grid(row = 2 , column = 0 )
        # second
        self.lastnameLabel = Label (self, text = "Last")
        self.lastnameLabel.grid(row=0, column = 1)
        self.lastnameVar = StringVar()
        self.lastnameEntry = Entry(self, textvariable = self.lastnameVar)
        self.lastnameEntry.grid(row =2, column =1)
        # middle combobox

        self.middlenameLabel= Label(self,text= "Middle")
        self.middlenameLabel.grid(row =0, column =2)
        self.combo()
        # Dob labels and boxes
        self.dobLabel = Label(self,text = "DOB")
        self.dobLabel.grid(row = 5, column = 3)
        self.monthLabel= Label(self,text = "Month")
        self.monthLabel.grid(row = 7 ,column =3)
        self.monthVar = StringVar()
        self.monthEntry = Entry(self,width =7, textvariable = self.monthVar)
        self.monthEntry.grid(row =8 , column =3)
        self.dayLabel= Label(self,text = "Day")
        self.dayLabel.grid(row = 7 ,column =4)
        self.dayVar = StringVar()
        self.dayEntry = Entry(self, width =7 , textvariable = self.dayVar)
        self.dayEntry.grid(row =8 , column =4)
        self.yearLabel= Label(self,text = "Year")
        self.yearLabel.grid(row = 7 ,column =5, sticky = W)
        self.yearVar = StringVar()
        self.yearEntry = Entry(self, width =7 , textvariable = self.yearVar)
        self.yearEntry.grid(row =8 , column =5, sticky =W)
        #Gender
        self.genderLabel = Label(self,text= "Gender")
        self.genderLabel.grid( row =5, column = 0)
        self.mybutton = IntVar()

        self.mbutton = Radiobutton(self,text= "Male",variable = self.mybutton, value =1)
        self.fbutton= Radiobutton(self,text= "Female",variable= self.mybutton, value =2)
        

        self.mbutton.grid(row = 7, column=0)
        self.fbutton.grid(row= 7 , column = 1)

        #rating
        self.ratingLabel = Label(self, text = "Rating")
        self.ratingLabel.grid( row = 9 , column = 0 )
        self.combo2()
        self.rating2Label = Label(self , text = " 1 -Worst / 9 -Best")
        self.rating2Label.grid( row = 10 , column =1)

        #injury

        self.injuryLabel = Label (self, text = "Decription of Injury")
        self.injuryLabel.grid(row = 12, column = 2)
        self.injuryVar = StringVar()
        #self.injuryEntry = Entry(self, width = 18, textvariable = self.injuryVar)
        self.injuryEntry = Text(self, width = 18, height = 4)
        self.injuryEntry.grid(row = 13, column = 2 )


        #nested button
        self.buttonPane = Frame(self)
        self.buttonPane.grid(row =20, column = 3)
        
        #submit button
        self.submitButton = Button(self.buttonPane, text = "Submit", command=self.onButton)
        self.submitButton.grid(row = 20, column = 3)

        #done button
        self.buttonPane2 = Frame(self)
        self.buttonPane2.grid(row = 20, column =1)
        self.doneButton = Button(self.buttonPane2 , text = "Done", command= self.clearButton)
        self.doneButton.grid(row = 20 ,column = 3)
        

    def combo(self):
        self.boxValue = StringVar()
        self.box = ttk.box = ttk.Combobox(self,width =7, textvariable = self.boxValue)
        self.box[ 'values'] = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z')
        self.box.current(0)
        self.box.grid(row = 2, column = 2)

    def combo2(self):
        self.box1Value = StringVar()
        self.box1 = ttk.box1 = ttk.Combobox(self, width = 7 , textvariable = self.box1Value)
        self.box1['values'] = ('1','2','3','4','5','6','7','8','9')
        self.box1.current(0)
        self.box1.grid(row = 11, column = 0 )

    
    
    
    def onButton(self):

        if self.mybutton.get() == 2:
            temp ="Female"
        elif self.mybutton.get() ==1:
            temp = "Male"
        else:
            temp = "Unknown"

        
        
        #print( self.lastnameEntry.get(),".", self.firstnameEntry.get(),".",self.box.get(),"\n",
        #"--------------------","\n","Gender: ",temp ,"\n","--------------------", "\n",
               #self.monthEntry.get()," / ",self.dayEntry.get(), " / ", self.yearEntry.get(),"\n","--------------------\n"
               #,"Rating: ",self.box1.get(), "\n","--------------------\n","Description of injury: \n",self.injuryEntry.get('0.0',END),"\n",
               #"--------------------")
         

       # want = self.lastnameEntry.get(),".", self.firstnameEntry.get(),"."+self.box.get(),"\n",
       # "--------------------"+"\n","Gender: ",temp ,"\n","--------------------", "\n"
        #self.monthEntry.get()," / ", self.dayEntry.get(), " / ", self.yearEntry.get(),"\n","--------------------\n",
        #"Rating: ", self.box1.get(), "\n"+"--------------------\n"+"Description of injury: {0} \n",self.injuryEntry.get('0.0',END),"\n",
        #"--------------------"


        need = self.lastnameEntry.get(), self.firstnameEntry.get(),self.box.get(),temp 
        #self.monthEntry.get(), self.dayEntry.get(),  self.yearEntry.get(),
        #self.box1.get(), self.injuryEntry.get('0.0',END)

        want2 = self.monthEntry.get(), self.dayEntry.get(),  self.yearEntry.get()

        want3 = self.box1.get()
        want4 = self.injuryEntry.get('0.0',END)
        
        #global var
        
        var.append(want)
        var2.append(need)
        var3.append(want2)
        var4.append(want3)
        var5.append(want4)
        
        #clear after submit
        self.lastnameEntry.delete(0,END)
        self.firstnameEntry.delete(0,END)
        self.monthEntry.delete(0,END)
        self.dayEntry.delete(0,END)
        self.yearEntry.delete(0,END)
        self.injuryEntry.delete('0.0',END)
        self.box1.current(0)
        self.box.current(0)


        #bug cannont deselect radiobuttons


    
    
    def clearButton(self):

        #print(var4)
        def swap(lyst, i , j):

            temp = lyst[i]
            lyst[i] = lyst[j]
            lyst[j] = temp 


        n = len(var4)
        while n > 1:
            i =1
            while i <n:
                if var4[i] < var4[i-1]:
                    swap(var4 , i , i-1)
                    swap(var3, i, i-1)
                    swap(var2,i, i-1)
                    swap(var5,i,i-1)
                i+=1
            n -= 1
        #print(var4)
        #print(var2)
        
        #print(var)
        print("##############################")
        for x in range(len(var2)):
            #index = var2[x
            print("------------------------------")
            print(var2[x][0]," . ",var2[x][1]," . ",var2[x][2] ,"\n","Gender: ",var2[x][3])
            print("------------------------------")
            print(var3[x][0]," / ", var3[x][1], " / ",var3[x][2])
            print("------------------------------")
            print("Rating: " , var4[x])
            print("------------------------------")
            print("Description: ",var5[x])
            print("##############################")
        #print(var2)
        #print("-------------")
        #print(var3)
        #print("------------")
        #print(var4)
        #print(var5)
        os._exit(1)


def main():
    
       


    
    Triage().mainloop()
count = 0
global var
global want
global need
global var2
global want2
global want3
global want4
want3 = ""
want4= ""
want2 =""
need = ""
want = ""
var = []
var2 =[]
var3 =[]
var4 = []
var5 = []
count +1
#var.append(want)
#print(var)
    
    
main()
     
    

#import tkinter and timeit library
from tkinter import *
import random
from tkinter import messagebox
from timeit import default_timer as timer 


window = Tk()#creating  first window 

#intialising needed variables 
count = 0
score = 0
miss = 0
l= []
l1 =[]
count = 0
correct_count =0
timeleft = 60
sliderWords = ''

#creating label for the title in first window
lbl = Label(window,text = 'TYPING SPEED TEST',font=('arial',25,'italic bold'),bg = 'black',fg='white')
lbl.place(x=200,y=10)
        
#creating beginner function
def beginner():
    root = Tk() #creating second window for beginner level 
    t0 = timer() #timer will be started 
    root.geometry('800x600+400+100')#setting the geometry of the window(height=800,width=600,X-axis=400,Y-axis=100)
    root.configure(bg = 'black')# configuring backgroud color of window 
    
    root.title('Typing Speed Test Game')#giving the title 

    root.iconbitmap("image.ico")#changing the icon
 

    #creating the function sliding the title
    def labelSlider():
        global count,sliderWords
        text = 'Welcome To Typing Speed Game ' #initiasing the text variable with  project name
        if(count>=len(text)): #checking condition
            
            count = 0
            sliderWords = ''
        sliderWords += text[count] #if the condition is false then add text[count] in sliderwords
        count += 1 #incrementing count
        fontLabel.configure(text = sliderWords) #configuring fontLabel with sliderWords
        fontLabel.after(100,labelSlider) #after every 100 milliseconds it will call the labelSlider()


   
         #creating function to get words using file hadling
    def get_sentence():
        f = open("beginner.txt","r")
        lines = f.read().split("\n") #contains word in list wherever  find next line 
        line = random.choice(lines) #randomly picking word from list
        return line
    

   
    
    def startGame(event): #creating function using event handling
        global score,miss,timeleft,l,count
        if (timeleft==60):
             time()   #when time left is 60 it will call the time function
        gamePlayDetailLabel.configure(text = '') #once the game has started the hint{enter and hit} will vanish
        if (wordEntry.get()==wordLabel['text']): #condition to check wheather user has given the correct input
            
            score += 1 #incrementing score 
            l.append(wordEntry.get()) #append the input in list l
            l1.append(wordEntry.get()) #append the input in list l1
            scoreLabelCount.configure(text = score) #configuring  the label with score
           

        else:       #when condition  is False
            
            
            miss += 1 #incrementing the variable miss
            l.append(wordEntry.get())  #appending the input in list l
        wordLabel.configure(text=get_sentence()) #configuring  the wordLabel with funcion get_sentence()
        wordEntry.delete(0,END)  #it will clear the entry box after hiting enter
          
        #creating time function        
    def time(): 
         
         
         global timeleft,score,miss,count,correct_count
         if timeleft>=11: 
             
             pass
         else:
             
             timeLabelCount.configure(fg = 'red') #when time left is less then 11 fg of timeLabelcout change to red
         if(timeleft>0):
             
             timeleft -= 1  #decrementing time
             timeLabelCount.configure(text = timeleft)   # to configure the count with left time
             timeLabelCount.after(1000,time)    # after every 1000 milli sec..it will call time
         else:
             t1 = timer() #timer will be stopped when timeleft becomes zero
             for i in l:   #traversing in the list
                 count += len(i) #adding the length of each in list
             print(l)  #list l contains all input 
             print(count)
             print(l1)  #list l1 contains only correct input
             for i in l1:  #traversing the list l1
                 correct_count += len(i) 
             print(correct_count)   #printing the total length of correct input by user    
             t = str(round(t1-t0))  #total time taken by user
               
             #configuring  label with total Score,WPM,Accurancy
             gamePlayDetailLabel.configure(text = 'Total Score = {} | WPM={} | Accuracy={}'.format(score-miss,int((count*60)/int(5*(t1-t0))),int((correct_count*100)/count)))
             rr = messagebox.askretrycancel('Notification','Hit Retry to Play Again')  #asking for retry or cancle 
             if rr == True: #if user has selected retry then set all variable as earlier 
                 
                 score = 0
                 timeleft = 60
                 miss = 0
                 timeLabelCount.configure(text = timeleft)
                 wordLabel.configure(text = get_sentence())
                 scoreLabelCount.configure(text = score)

  
     #creating different labels 
         
    fontLabel = Label(root,text = 'Welcome to Typing Speed Game in ',font=('arial',25,'italic bold'),bg ='black',fg = 'red',width = 40)
    fontLabel.place(x = 10,y = 10)
    labelSlider()   #calling labelSlider function
    

    
    wordLabel = Label(root, text = get_sentence(),font=('arial',20,'italic bold'),bg = 'black',width =50,fg='dark green')
    wordLabel.place(x = 10,y = 250)

    scoreLabel = Label(root,text = 'Your Score : ',font=('arial',25,'italic bold'),bg = 'black',fg='blue')
    scoreLabel.place(x =10,y = 100)

    scoreLabelCount = Label(root,text = score,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    scoreLabelCount.place(x = 80,y =180)

    timerLabel = Label(root,text = 'Time Left :',font=('arial',25,'italic bold'),bg ='black',fg ='blue')
    timerLabel.place(x = 600, y = 100)

    timeLabelCount = Label(root,text = timeleft,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    timeLabelCount.place(x = 680,y= 180)

    gamePlayDetailLabel = Label(root, text = 'Type Word and Hit Enter',font = ('arial',20,'italic'),bg = 'black', fg = 'dark grey')
    gamePlayDetailLabel.place(x = 220,y = 400)
     
    #creating Entry box    
    wordEntry = Entry(root,font=('arial',20,'italic bold'),bd = 10,width = 15,justify='center') # justify enable the text to be input in center
    wordEntry.place(x = 300,y = 300)
    wordEntry.focus_set()  # by this no need to enter into the entry box and then write...enable the input wothout clicking into the entry box


    root.bind('<Return>',startGame) # binding enter with the function  startGame() .. we will be able to get the words typed after hitting enter.part of event handling
    root.mainloop()

######### FOR INTERMEDIATE LEVEL ###########

def intermediate():
    root = Tk()
    t0 = timer()
    root.geometry('800x600+400+100')
    root.configure(bg = 'black')
    
    root.title('Typing Speed Test Game')

    root.iconbitmap("image.ico")
 

    
    def labelSlider():
        global count,sliderWords
        text = 'Welcome To Typing Speed Game '
        if(count>=len(text)):
            
            count = 0
            sliderWords = ''
        sliderWords += text[count]
        count += 1
        fontLabel.configure(text = sliderWords)
        fontLabel.after(100,labelSlider)


   
   
    def get_sentence():
        f = open("intermediate.txt","r")
        lines = f.read().split("\n")
        line = random.choice(lines)
        return line
    

   
    
    def startGame(event):
        global score,miss,timeleft,l,count
        if (timeleft==60):
             time()
        gamePlayDetailLabel.configure(text = '')
        if (wordEntry.get()==wordLabel['text']):
            
            score += 1
            l.append(wordEntry.get())
            l1.append(wordEntry.get())
            scoreLabelCount.configure(text = score)
           

        else:
            
            
            miss += 1
            l.append(wordEntry.get())
        wordLabel.configure(text=get_sentence())
        wordEntry.delete(0,END)

    def time():
         
         
         global timeleft,score,miss,count,correct_count
         if timeleft>=11:
             
             pass
         else:
             
             timeLabelCount.configure(fg = 'red')
         if(timeleft>0):
             
             timeleft -= 1
             timeLabelCount.configure(text = timeleft)   # to configure the count woth left time
             timeLabelCount.after(1000,time)    # after every 1000 micro sec..it will call time
         else:
             t1 = timer()
             for i in l:
                 count += len(i)
             print(l)
             print(count)
             print(l1)
             for i in l1:
                 correct_count += len(i)
             print(correct_count)    
             t = str(round(t1-t0))   
             gamePlayDetailLabel.configure(text = 'Total Score = {} | WPM={} | Accuracy={}'.format(score-miss,int((count*60)/int(5*(t1-t0))),int((correct_count*100)/count)))
             rr = messagebox.askretrycancel('Notification','Hit Retry to Play Again')
             if rr == True:
                 
                 score = 0
                 timeleft = 60
                 miss = 0
                 timeLabelCount.configure(text = timeleft)
                 wordLabel.configure(text = get_sentence())
                 scoreLabelCount.configure(text = score)

  

         
    fontLabel = Label(root,text = 'Welcome to Typing Speed Game',font=('arial',25,'italic bold'),bg ='black',fg = 'red',width = 40)
    fontLabel.place(x = 10,y = 10)
    labelSlider()
    

    
    wordLabel = Label(root, text = get_sentence(),font=('arial',20,'italic bold'),bg = 'black',width =50,fg='dark green')
    wordLabel.place(x = 10,y = 250)

    scoreLabel = Label(root,text = 'Your Score : ',font=('arial',25,'italic bold'),bg = 'black',fg='blue')
    scoreLabel.place(x =10,y = 100)

    scoreLabelCount = Label(root,text = score,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    scoreLabelCount.place(x = 80,y =180)

    timerLabel = Label(root,text = 'Time Left :',font=('arial',25,'italic bold'),bg ='black',fg ='blue')
    timerLabel.place(x = 600, y = 100)

    timeLabelCount = Label(root,text = timeleft,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    timeLabelCount.place(x = 680,y= 180)

    gamePlayDetailLabel = Label(root, text = 'Type Word and Hit Enter',font = ('arial',20,'italic'),bg = 'black', fg = 'dark grey')
    gamePlayDetailLabel.place(x = 220,y = 400)

    wordEntry = Entry(root,font=('arial',20,'italic bold'),bd = 10,width = 15,justify='center') # justify enable the text to be input in center
    wordEntry.place(x = 300,y = 300)
    wordEntry.focus_set()  # by this no need to enter into the entry box and then write...enable the input wothout clicking


    root.bind('<Return>',startGame) # binding enter with the function call .. we will be able to get the words typed after hitting enter.part of event handling
    root.mainloop() 


################# FOR ADVANCED LEVEL###########


def advanced():
    root = Tk()
    t0 = timer()
    root.geometry('800x600+400+100')
    root.configure(bg = 'black')
    
    root.title('Typing Speed Test Game')

    root.iconbitmap("image.ico")
 

    
    def labelSlider():
        global count,sliderWords
        text = 'Welcome To Typing Speed Game '
        if(count>=len(text)):
            
            count = 0
            sliderWords = ''
        sliderWords += text[count]
        count += 1
        fontLabel.configure(text = sliderWords)
        fontLabel.after(100,labelSlider)


   
   
    def get_sentence():
        f = open("advanced.txt","r")
        lines = f.read().split("\n")
        line = random.choice(lines)
        return line
    

   
    
    def startGame(event):
        global score,miss,timeleft,l,count
        if (timeleft==60):
             time()
        gamePlayDetailLabel.configure(text = '')
        if (wordEntry.get()==wordLabel['text']):
            
            score += 1
            l.append(wordEntry.get())
            l1.append(wordEntry.get())
            scoreLabelCount.configure(text = score)
           

        else:
            
            
            miss += 1
            l.append(wordEntry.get())
        wordLabel.configure(text=get_sentence())
        wordEntry.delete(0,END)

    def time():
         
         
         global timeleft,score,miss,count,correct_count
         if timeleft>=11:
             
             pass
         else:
             
             timeLabelCount.configure(fg = 'red')
         if(timeleft>0):
             
             timeleft -= 1
             timeLabelCount.configure(text = timeleft)   # to configure the count woth left time
             timeLabelCount.after(1000,time)    # after every 1000 micro sec..it will call time
         else:
             t1 = timer()
             for i in l:
                 count += len(i)
             print(l)
             print(count)
             print(l1)
             for i in l1:
                 correct_count += len(i)
             print(correct_count)    
             t = str(round(t1-t0))   
             gamePlayDetailLabel.configure(text = 'Total Score = {} | WPM={} | Accuracy={}'.format(score-miss,int((count*60)/int(5*(t1-t0))),int((correct_count*100)/count)))
             rr = messagebox.askretrycancel('Notification','Hit Retry to Play Again')
             if rr == True:
                 
                 score = 0
                 timeleft = 60
                 miss = 0
                 timeLabelCount.configure(text = timeleft)
                 wordLabel.configure(text = get_sentence())
                 scoreLabelCount.configure(text = score)

  

         
    fontLabel = Label(root,text = 'Welcome to Typing Speed Game',font=('arial',25,'italic bold'),bg ='black',fg = 'red',width = 40)
    fontLabel.place(x = 10,y = 10)
    labelSlider()
    

    
    wordLabel = Label(root, text = get_sentence(),font=('arial',20,'italic bold'),bg = 'black',width =50,fg='dark green')
    wordLabel.place(x = 10,y = 250)

    scoreLabel = Label(root,text = 'Your Score : ',font=('arial',25,'italic bold'),bg = 'black',fg='blue')
    scoreLabel.place(x =10,y = 100)

    scoreLabelCount = Label(root,text = score,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    scoreLabelCount.place(x = 80,y =180)

    timerLabel = Label(root,text = 'Time Left :',font=('arial',25,'italic bold'),bg ='black',fg ='blue')
    timerLabel.place(x = 600, y = 100)

    timeLabelCount = Label(root,text = timeleft,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    timeLabelCount.place(x = 680,y= 180)

    gamePlayDetailLabel = Label(root, text = 'Type Word and Hit Enter',font = ('arial',20,'italic'),bg = 'black', fg = 'dark grey')
    gamePlayDetailLabel.place(x = 220,y = 400)

    wordEntry = Entry(root,font=('arial',20,'italic bold'),bd = 10,width = 15,justify='center') # justify enable the text to be input in center
    wordEntry.place(x = 300,y = 300)
    wordEntry.focus_set()  # by this no need to enter into the entry box and then write...enable the input wothout clicking


    root.bind('<Return>',startGame) # binding enter with the function call .. we will be able to get the words typed after hitting enter.part of event handling
    root.mainloop() 
                 
    

#creating label     
             
lbl=Label(window,text="Select Your Level",font=('arial',25,'italic bold'),bg ='black',fg = 'brown')
lbl.place(x=250,y=100)

#creating three different buttons for three levels

btn=Button(window,text="Beginner",command=beginner,bg='orange red',width=10,height=2,font=('arial',10,'italic bold'))
btn.place(x=350,y=150)
btn=Button(window,text="Intermediate",command = intermediate, bg='orange red',width=10,height=2,font=('arial',10,'italic bold'))
btn.place(x=350,y=200)
btn=Button(window,text="Advanced",bg='orange red',command = advanced,width=10,height=2,font=('arial',10,'italic bold'))
btn.place(x=350,y=250)

filename = PhotoImage(file = "image2.png") #setting image into lebel for first window 
imglabel = Label(window,image=filename,width=770)
imglabel.place(x=10,y= 300)



window.geometry('800x600+400+100') #setting geometry
window.configure(bg ='black')   #setting background
window.title('Typing Speed Test Game') #setting title
window.iconbitmap('image.ico')   #changing icon

window.mainloop()

        

     
        
        
    
        



    
    

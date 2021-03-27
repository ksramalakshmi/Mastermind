from tkinter import *
from tkinter import messagebox
from Backend_module import *
from PIL import ImageTk, Image

def game():
    root = Tk()
    root.geometry("1000x1000")
    root.title("Mastermind")
    root.config(bg='black')

    i=0
    n=0

    def click_button():
        mastermind_button.destroy()

        root.config(bg='gray30')
        global text1
        text1 = Label(root, text="Welcome to Mastermind Game!", width = 50, height = 10, bg= 'gray40')

        global play_button
        play_button = Button(root, text = 'Click to play!', command=play, bg='gray45')

        global instruction_button
        instruction_button = Button(root, text="Instructions", width = 15, command=instruction, bg='gray45')

        f = open("instruction.txt")
        rdlines = f.readlines()

        global inst
        inst = " ".join(rdlines)

        play_button.place(x=450, y=160)
        text1.place(x=290, y=50)
        instruction_button.place(x=420, y=250)
        return

    def instruction():
        global text3
        text3 = Label(root, text=inst)
        text3.place(x=30,y=290)
        
    def play():
        try:
            text3.destroy()
            instruction_button.destroy()
            text1.destroy()
            play_button.destroy()
        except:
            instruction_button.destroy()
            text1.destroy()
            play_button.destroy()
        boxes(i)
        return

    def boxes(i):
        global c1_var,c2_var, c3_var, c4_var
        c1_var = StringVar()
        c2_var = StringVar()
        c3_var = StringVar()
        c4_var = StringVar()
    
        global e1
        e1_options = ['Select Colour','RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE'] 
        e1 = OptionMenu(root, c1_var, *e1_options)
        e1.config(width=15)
        e1.grid(row=0, column=0)
        c1_var.set(e1_options[0])
    
       
        global e2
        e2_options = ['Select Colour','RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE']
        e2 = OptionMenu(root, c2_var, *e2_options)
        e2.config(width=15)
        e2.grid(row=0, column=1)
        c2_var.set(e2_options[0])
        
        global e3
        e3_options = ['Select Colour','RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE']
        e3 = OptionMenu(root, c3_var, *e3_options)
        e3.grid(row=0, column=2)
        e3.config(width=15)
        c3_var.set(e3_options[0])

        
        global e4
        e4_options = ['Select Colour','RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE']
        e4 = OptionMenu(root, c4_var, *e4_options)
        e4.config(width=15)
        e4.grid(row=0, column=3)
        c4_var.set(e4_options[0])

        check_button = Button(root, text = ' Check! ', width = 5, command = check_click)
        check_button.grid(row = 0, column = 4)
        return
    
    def check_click():
        c1 = c1_var.get()
        c2 = c2_var.get()
        c3 = c3_var.get()
        c4 = c4_var.get()

        if c1.upper() == 'RED':     
            red_peg = Image.open("red_peg.png")
            resized_red_peg = red_peg.resize((30,30), Image.ANTIALIAS)
            red_peg = ImageTk.PhotoImage(resized_red_peg)
            red_button = Button(image = red_peg)
            red_button.image = red_peg   
            red_button.grid(row = i+1, column = 0)

        elif c1.upper() == 'BLUE':
            blue_peg = Image.open("blue_peg.png")
            resized_blue_peg = blue_peg.resize((30,30), Image.ANTIALIAS)
            blue_peg = ImageTk.PhotoImage(resized_blue_peg)
            blue_button = Label(root, image = blue_peg)
            blue_button.image = blue_peg
            blue_button.grid(row = i+1, column = 0)
        elif c1.upper() == 'GREEN':
            green_peg = Image.open("green_peg.png")
            resized_green_peg = green_peg.resize((30,30), Image.ANTIALIAS)
            green_peg = ImageTk.PhotoImage(resized_green_peg)
            green_button = Label(root, image = green_peg)
            green_button.image = green_peg
            green_button.grid(row = i+1, column = 0)
        elif c1.upper() == 'YELLOW':
            yellow_peg = Image.open("yellow_peg.png")
            resized_yellow_peg = yellow_peg.resize((30,30), Image.ANTIALIAS)
            yellow_peg = ImageTk.PhotoImage(resized_yellow_peg)
            yellow_button = Label(root, image = yellow_peg)
            yellow_button.image = yellow_peg
            yellow_button.grid(row = i+1, column = 0)
        elif c1.upper() == 'PURPLE':
            purple_peg = Image.open("purple_peg.png")
            resized_purple_peg = purple_peg.resize((30,30), Image.ANTIALIAS)
            purple_peg = ImageTk.PhotoImage(resized_purple_peg)
            purple_button = Label(root, image = purple_peg)
            purple_button.image = purple_peg
            purple_button.grid(row = i+1, column = 0)
        elif c1.upper() == 'ORANGE':
            orange_peg = Image.open("orange_peg.png")
            resized_orange_peg = orange_peg.resize((30,30), Image.ANTIALIAS)
            orange_peg = ImageTk.PhotoImage(resized_orange_peg)
            orange_button = Label(root, image = orange_peg)
            orange_button.image = orange_peg
            orange_button.grid(row = i+1, column = 0)
        
        if c2.upper() == 'RED': 
            red_peg = Image.open("red_peg.png")
            resized_red_peg = red_peg.resize((30,30), Image.ANTIALIAS)
            red_peg = ImageTk.PhotoImage(resized_red_peg)
            red_button = Button(image = red_peg)
            red_button.image = red_peg
            red_button.grid(row = i+1, column = 1)
        elif c2.upper() == 'BLUE':
            blue_peg = Image.open("blue_peg.png")
            resized_blue_peg = blue_peg.resize((30,30), Image.ANTIALIAS)
            blue_peg = ImageTk.PhotoImage(resized_blue_peg)
            blue_button = Label(root, image = blue_peg)
            blue_button.image = blue_peg
            blue_button.grid(row = i+1, column = 1)
        elif c2.upper() == 'GREEN':
            green_peg = Image.open("green_peg.png")
            resized_green_peg = green_peg.resize((30,30), Image.ANTIALIAS)
            green_peg = ImageTk.PhotoImage(resized_green_peg)
            green_button = Label(root, image = green_peg)
            green_button.image = green_peg
            green_button.grid(row = i+1, column = 1)
        elif c2.upper() == 'YELLOW':
            yellow_peg = Image.open("yellow_peg.png")
            resized_yellow_peg = yellow_peg.resize((30,30), Image.ANTIALIAS)
            yellow_peg = ImageTk.PhotoImage(resized_yellow_peg)
            yellow_button = Label(root, image = yellow_peg)
            yellow_button.image = yellow_peg
            yellow_button.grid(row = i+1, column = 1)
        elif c2.upper() == 'PURPLE':
            purple_peg = Image.open("purple_peg.png")
            resized_purple_peg = purple_peg.resize((30,30), Image.ANTIALIAS)
            purple_peg = ImageTk.PhotoImage(resized_purple_peg)
            purple_button = Label(root, image = purple_peg)
            purple_button.image = purple_peg
            purple_button.grid(row = i+1, column = 1)
        elif c2.upper() == 'ORANGE':
            orange_peg = Image.open("orange_peg.png")
            resized_orange_peg = orange_peg.resize((30,30), Image.ANTIALIAS)
            orange_peg = ImageTk.PhotoImage(resized_orange_peg)
            orange_button = Label(root, image = orange_peg)
            orange_button.image = orange_peg
            orange_button.grid(row = i+1, column = 1)
            

        if c3.upper() == 'RED':
            red_peg = Image.open("red_peg.png")
            resized_red_peg = red_peg.resize((30,30), Image.ANTIALIAS)
            red_peg = ImageTk.PhotoImage(resized_red_peg)
            red_button = Button(image = red_peg)
            red_button.image = red_peg
            red_button.grid(row = i+1, column = 2)
        elif c3.upper() == 'BLUE':
            blue_peg = Image.open("blue_peg.png")
            resized_blue_peg = blue_peg.resize((30,30), Image.ANTIALIAS)
            blue_peg = ImageTk.PhotoImage(resized_blue_peg)
            blue_button = Label(root, image = blue_peg)
            blue_button.image = blue_peg
            blue_button.grid(row = i+1, column = 2)
        elif c3.upper() == 'GREEN':
            green_peg = Image.open("green_peg.png")
            resized_green_peg = green_peg.resize((30,30), Image.ANTIALIAS)
            green_peg = ImageTk.PhotoImage(resized_green_peg)
            green_button = Label(root, image = green_peg)
            green_button.image = green_peg
            green_button.grid(row = i+1, column = 2)
        elif c3.upper() == 'YELLOW':
            yellow_peg = Image.open("yellow_peg.png")
            resized_yellow_peg = yellow_peg.resize((30,30), Image.ANTIALIAS)
            yellow_peg = ImageTk.PhotoImage(resized_yellow_peg)
            yellow_button = Label(root, image = yellow_peg)
            yellow_button.image = yellow_peg
            yellow_button.grid(row = i+1, column = 2)
        elif c3.upper() == 'PURPLE':
            purple_peg = Image.open("purple_peg.png")
            resized_purple_peg = purple_peg.resize((30,30), Image.ANTIALIAS)
            purple_peg = ImageTk.PhotoImage(resized_purple_peg)
            purple_button = Label(root, image = purple_peg)
            purple_button.image = purple_peg
            purple_button.grid(row = i+1, column = 2)
        elif c3.upper() == 'ORANGE':
            orange_peg = Image.open("orange_peg.png")
            resized_orange_peg = orange_peg.resize((30,30), Image.ANTIALIAS)
            orange_peg = ImageTk.PhotoImage(resized_orange_peg)
            orange_button = Label(root, image = orange_peg)
            orange_button.image = orange_peg
            orange_button.grid(row = i+1, column = 2)


        if c4.upper() == 'RED':
            red_peg = Image.open("red_peg.png")
            resized_red_peg = red_peg.resize((30,30), Image.ANTIALIAS)
            red_peg = ImageTk.PhotoImage(resized_red_peg)
            red_button = Button(image = red_peg)
            red_button.image = red_peg
            red_button.grid(row = i+1, column = 3)

        elif c4.upper() == 'BLUE':
            blue_peg = Image.open("blue_peg.png")
            resized_blue_peg = blue_peg.resize((30,30), Image.ANTIALIAS)
            blue_peg = ImageTk.PhotoImage(resized_blue_peg)
            blue_button = Label(root, image = blue_peg)
            blue_button.image = blue_peg
            blue_button.grid(row = i+1, column = 3)
        elif c4.upper() == 'GREEN':
            green_peg = Image.open("green_peg.png")
            resized_green_peg = green_peg.resize((30,30), Image.ANTIALIAS)
            green_peg = ImageTk.PhotoImage(resized_green_peg)
            green_button = Label(root, image = green_peg)
            green_button.image = green_peg
            green_button.grid(row = i+1, column = 3)
        elif c4.upper() == 'YELLOW':
            yellow_peg = Image.open("yellow_peg.png")
            resized_yellow_peg = yellow_peg.resize((30,30), Image.ANTIALIAS)
            yellow_peg = ImageTk.PhotoImage(resized_yellow_peg)
            yellow_button = Label(root, image = yellow_peg)
            yellow_button.image = yellow_peg
            yellow_button.grid(row = i+1, column = 3)
        elif c4.upper() == 'PURPLE':
            purple_peg = Image.open("purple_peg.png")
            resized_purple_peg = purple_peg.resize((30,30), Image.ANTIALIAS)
            purple_peg = ImageTk.PhotoImage(resized_purple_peg)
            purple_button = Label(root, image = purple_peg)
            purple_button.image = purple_peg
            purple_button.grid(row = i+1, column = 3)
        elif c4.upper() == 'ORANGE':
            orange_peg = Image.open("orange_peg.png")
            resized_orange_peg = orange_peg.resize((30,30), Image.ANTIALIAS)
            orange_peg = ImageTk.PhotoImage(resized_orange_peg)
            orange_button = Label(root, image = orange_peg)
            orange_button.image = orange_peg
            orange_button.grid(row = i+1, column = 3)
        
        global input_code
        temp_i = i
        input_code = [c1.upper(), c2.upper(), c3.upper(), c4.upper()]
        check(input_code, temp_i)
        return

    def check(input_code, temp_i):

        return_value = code_compution(input_code)
        copy_return_value = [x for x in return_value]
        text2 = Label( root, text = return_value)
        nonlocal i
        
        

        for j in return_value:
            if j == 'black':
                black_peg = Image.open("black_peg.png")
                resized_black_peg = black_peg.resize((30,30), Image.ANTIALIAS)
                black_peg = ImageTk.PhotoImage(resized_black_peg)
                black_button = Button(root, image = black_peg)
                black_button.image = black_peg
                black_button.grid(row = (temp_i+1), column = (copy_return_value.index(j) + 4))
                copy_return_value[return_value.index(j)] = -1
            elif j == 'white':
                white_peg = Image.open("white_peg.png")
                resized_white_peg = white_peg.resize((30,30), Image.ANTIALIAS)
                white_peg = ImageTk.PhotoImage(resized_white_peg)
                white_button = Button(image = white_peg)
                white_button.image = white_peg
                white_button.grid(row = (temp_i+1), column = (copy_return_value.index(j) + 4))
                copy_return_value[return_value.index(j)] = -1

        #text2.grid(row= i+2)

        if return_value == ['black', 'black', 'black', 'black']:
            msg = messagebox.askokcancel('Mastermind','Congratulations! You have cracked the code!\n Do you want to play again?')
            if msg == True:
                i=0
                root.destroy()
                game()
            else:
                quit()
        else :
            nonlocal n
            if n <= 8:
                n += 1 
                i += 3
                boxes(i)
        
            elif n==9:
                m = "Oh no! You lost the game!\n"+'Correct Combination is:\n'+ " ".join(set_code)+'\nDo you want to try again?'
                msg = messagebox.askokcancel('Mastermind',m)
                if msg == True:
                    i=0
                    root.destroy()
                    game()
                else:
                    quit()

        return   
    mastermind_image = PhotoImage(file='mastermind.png')
    mastermind_button = Button(root, image = mastermind_image, bg='green', command = click_button, width=1000, height=1000)
    mastermind_button.pack()
    root.mainloop()
    return
game()

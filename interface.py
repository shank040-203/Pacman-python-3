from tkinter import *
import tkinter.font as tkfont
from importlib import reload
import sys
import mysql.connector as sqLtor

# Import the pacman game
from Pacman import game

interface = Tk()
interface.title('Arcade Games')
interface.state('zoomed')
interface.resizable(width = False, height = False)

interface.grid_columnconfigure(0, weight = 1)
interface.grid_rowconfigure(0, weight = 1)

def done():
    interface.destroy()

def begin(easy):
    modules = list(sys.modules.keys())
    for mod in modules:
        if mod.startswith('Battleship.'):
            del(sys.modules[mod])
    import Battleship.shared
    Battleship.shared.easy = easy
    import Battleship.Attacking
    try:
        batship()
    except:
        pass
    
def print_Rules():
    pass

def print_Rules_pacman():
    pass
    
def add_To_Database(score, username, game):
    global cursor, mycon
    cursor.execute('INSERT INTO allscores VALUES("{0}", {1}, "{2}")'.format(username, score, game))
    mycon.commit()

def show_Scores():
    pass

def show_Scores_pacman():
    cursor.execute('SELECT * FROM allscores WHERE Game = "Pacman"')
    print(cursor.fetchall())

def batship():
    global check,initial,frame2
    try:
        frame2.destroy()
    except:
        pass
    initial = name.get()
    if initial.strip() == '':
        check = 0
        frame1.destroy()
        normal()
    elif len(initial) > 40:
        check = 1
        frame1.destroy()
        normal()
    else:
        check = 2
        frame1.destroy()
        frame2 = Frame(interface)
        frame2.grid(row=0,column=0)

        heading = Label(frame2,text = 'Battleship', fg = 'red')
        heading['font'] = tkfont.Font(family = 'Jokerman', size=80, weight = 'bold')
        heading.grid(row = 0,column = 0, columnspan = 2)

        Label(frame2).grid(row=1,column = 0)

        play1 = Button(frame2,text = 'Play\n(Easy)', command = lambda: begin(True), fg = 'blue', padx = 20)
        play1['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        play1.grid(row = 2, column = 0, padx = 100)

        play2 = Button(frame2,text = 'Play\n(Hard)', command = lambda: begin(False), fg = 'blue', padx = 20)
        play2['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        play2.grid(row = 2, column = 1, padx = 100)

        Label(frame2).grid(row=3,column = 0)

        rules = Button(frame2,text = 'Rules', command = print_Rules, fg = 'Green')
        rules['font'] = tkfont.Font(family = 'Verdana', size=35, weight = 'bold')
        rules.grid(row = 4, column = 0, columnspan = 2)

        Label(frame2).grid(row=5,column = 0)

        high = Button(frame2,text = 'High Scores', command = show_Scores, fg = 'Yellow')
        high['font'] = tkfont.Font(family = 'Verdana', size=35, weight = 'bold')
        high.grid(row = 6, column = 0, columnspan = 2)

        Label(frame2).grid(row=7,column = 0,pady = 15)
        
        back = Button(frame2,text = 'Main Menu', command = normal)
        back['font'] = tkfont.Font(family = 'Arial', size=20)
        back.grid(row=8,column=0,columnspan = 2)

def play_pacman(name):  # LOOK OVER HERE! HERE! HEY! ****-----****----****-----*****----*****
    player_score = game.game()
    # Add the player score and the player name to the database
    add_To_Database(player_score, name, 'Pacman')

def pacman_game(condition):
    global check, initial, frame2
    try:
        frame2.destroy()
    except:
        pass
    if condition:
        initial = name.get()
    if initial.strip() == '' and condition:
        check = 0
        frame1.destroy()
        normal()
    elif len(initial) > 40 and condition:
        check = 1
        frame1.destroy()
        normal()
    else:
        check = 2
        frame1.destroy()
        frame2 = Frame(interface)
        frame2.grid(row=0, column=0)

        heading = Label(frame2, text='Pacman', fg='red')
        heading['font'] = tkfont.Font(family='Jokerman', size=80, weight='bold')
        heading.pack()

        Label(frame2).pack()

        play1 = Button(frame2, text='Play game', command=lambda:play_pacman(initial), fg='blue', padx=20)
        play1['font'] = tkfont.Font(family='Verdana', size=45, weight='bold')
        play1.pack()

        Label(frame2).pack()

        rules = Button(frame2, text='Rules', command=print_Rules_pacman, fg='Green')
        rules['font'] = tkfont.Font(family='Verdana', size=35, weight='bold')
        rules.pack()

        Label(frame2).pack()

        high = Button(frame2, text='High Scores', command=show_Scores_pacman, fg='Yellow')  # There's a yellow here
        high['font'] = tkfont.Font(family='Verdana', size=35, weight='bold')
        high.pack()

        Label(frame2).pack()

        back = Button(frame2, text='Main Menu', command=normal)
        back['font'] = tkfont.Font(family='Arial', size=20)
        back.pack()

def normal():
    global frame1, name, initial, check
    
    try:
        frame2.destroy()
    except:
        initial = ''
    
    frame1 = Frame(interface)
    frame1.grid(row=0,column=0)

    heading = Label(frame1,text = 'ARCADE GAMES 1.0', fg = 'red')
    heading['font'] = tkfont.Font(family = 'Jokerman', size=70, weight = 'bold')
    heading.grid(row = 0,column = 0, columnspan = 3)

    Label(frame1).grid(row=1,column = 0)

    lb1 = Label(frame1, text = 'Enter your name:', fg = 'green')
    lb1['font'] = tkfont.Font(family = 'Arial', size=30)
    lb1.grid(row = 2,column = 1)
    
    name = Entry(frame1,width = 40, justify = 'center')
    name['font'] = tkfont.Font(family = 'Arial', size=25)
    name.insert(0,initial)
    name.grid(row = 3,column = 1)

    if check == 0:
        error = Label(frame1, text = '*Please enter your name first*', fg = 'red')
        error['font'] = tkfont.Font(size = 15)
        error.grid(row = 4, column = 1)
    elif check == 1:
        error = Label(frame1, text = '*Entered name is too long, please enter a shorter name*', fg = 'red')
        error['font'] = tkfont.Font(size = 15)
        error.grid(row = 4, column = 1)

    Label(frame1).grid(row=4,column = 0)
    Label(frame1).grid(row=5,column = 0)

    lb2 = Label(frame1, text = 'Choose a Game', fg = 'blue')
    lb2['font'] = tkfont.Font(family = 'Arial', size=55, weight = 'bold')
    lb2.grid(row = 6,column = 1)

    Label(frame1).grid(row=7,column = 0)

    game1 = Button(frame1, text = 'Battleship', fg = '#FF7000', command = batship)
    game1['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
    game1.grid(row = 8, column = 0)
    game2 = Button(frame1, text = 'Pac-Man', fg = '#FF7000', command = lambda:pacman_game(True))
    game2['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
    game2.grid(row = 8, column = 2)

    Label(frame1).grid(row=9,column = 0)
    Label(frame1).grid(row=10,column = 0)

    Exit = Button(frame1, text = 'Exit', command = done)
    Exit['font'] = tkfont.Font(family = 'Arial', size=20)
    Exit.grid(row = 11, column = 1)
    interface.mainloop()

# DATABASE CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
mycon = sqLtor.connect(host='localhost', user='root', passwd='srivya74')
cursor = mycon.cursor()

try:
    # See if database exists
    cursor.execute('USE scores')
except sqLtor.errors.ProgrammingError:
    # Database doesn't exist
    cursor.execute('CREATE DATABASE scores')
    cursor.execute('USE scores')
    cursor.execute('CREATE TABLE allscores(username varchar(40), score int, game varchar(12))')
# END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
check = 2
normal()

mycon.close()
import os
import time
from typing import Any

#This just some examples and basic functions as I constantly
#forget how to use ansi escape codes
#in python the control code is \033[

#bunch of string variables
esc = "\033["

black = f"{esc}30m"
red = f"{esc}31m"
green = f"{esc}32m"
yellow = f"{esc}33m"
blue = f"{esc}34m"
magenta = f"{esc}35m"
cyan = f"{esc}36m"
white = f"{esc}37m"
gray = f"{esc}90m"
bright_red = f"{esc}91m"
bright_green = f"{esc}92m"
bright_yellow = f"{esc}93m"
bright_blue = f"{esc}94m"
bright_magenta = f"{esc}95m"
bright_cyan = f"{esc}96m"
bright_white = f"{esc}97m"
rst = f"{esc}0m"

def scroll_up(lines):
    print(f"\033[{lines}S")

def scroll_down(lines):
    print(f"\033[{lines}T")

def goto(row, col):
    print(f"\033[{row};{col}H")

def clr():
    print("\033[2J")

def get_size():
    cols, rows = os.get_terminal_size(0)
    return (rows, cols)


#class with memory for animation
class Spinner:
    def __init__(self, col=1, row_shift=0, in_list=[]):
        if len(in_list) == 0:
            #this is the moon animation just as something as default
            self.l = ["\U0001F311", "\U0001F312", "\U0001F313", "\U0001F314", "\U0001F315", "\U0001F316", "\U0001F317", "\U0001F318"]
        else:
            self.l = in_list
        self.idx = 0
        self.col = col
        self.rs = row_shift

    def __call__(self):
        (rows, cols) = get_size()
        row = rows - self.rs
        s = f"\033[{row};{self.col}H"
        s += self.l[self.idx]
        #this sends the cursor 2 spaces beyond the bottom left
        #so the animation can serve as a prompt
        s += f"\033[{rows};{3}H\033[0m"
        print(s, end='', flush=True)
        
        #setup the next emoji to print
        self.idx += 1
        if self.idx == len(self.l):
            self.idx = 0

def spinner_example(rounds=50, sleep=0.25, in_list = []):
    #initilaze the object
    if len(in_list) != 0: 
        moon = Spinner(in_list = in_list)
    else:
        moon = Spinner()
    for i in range(rounds):
        #call the object, which executes __call__ and prints an update
        moon()
        time.sleep(sleep)

spl0 = []
spl0.append(blue+'/')
spl0.append(cyan+ '-')
spl0.append(blue+ '\\')
spl0.append(cyan+ '|')
spl0.append(blue+ '/')
spl0.append(cyan+ '-')
spl0.append(blue+ '\\')
spl0.append(cyan+ '|')

class Progress_Bar():
    def __init__(self):
        pass

    def __call__(self, percent):
        (yo, xo) = get_size()

        s = f"\033[{y};{x}HO\033[{yo};1H"
        
        #move cursor up a line 
        s = f"\033[{y};{x}HO\033[{yo};1H"
        print(s, end='', flush=True)




class Circle:
    def __init__(self):
        self.l =  [[0,6],[3,5],[4,4],[5,3],[6,0]]
        self.l += [[5,-3],[4,-4],[3,-5],[0,-6]]
        self.l += [[-3,-5],[-4,-4],[-5,-3],[-6,0]]
        self.l += [[-5,3],[-4,4],[-3,5]]

        self.l =  [[0,6],[2,6],[6,5],[8,4],[10,3],[11,2], [12,1], [12,0]]
        self.l += [[12,-1],[11,-2],[10,-3],[8,-4],[6,-5],[2,-6],[0,-6]]
        self.l += [[-2, -6], [-6,-5],[-8,-4],[-10,-3],[-11,-2],[-12,-1],[-12,0]]
        self.l += [[-12,1],[-11,2],[-10,3],[-8,4],[-6,5],[-2,6]]
        self.idx = 0 


    def __call__(self):
        clr()
        (yo, xo) = get_size()
        yc = int(yo/2)
        xc = int(xo/2)
        pt = self.l[self.idx]
        x = xc + pt[0]
        y = yc + pt[1]
        s = f"\033[{y};{x}HO\033[{yo};1H"
        print(s, end='', flush=True)

        self.idx += 1
        if self.idx == len(self.l):
            self.idx = 0 
        
class Circle_Color(Circle):
    def __call__(self):
        clr()
        pt = self.l[self.idx]
        self.guts_of_call(pt, f"{bright_cyan}O")

        pt = self.l[self.get_idx(-1)]
        self.guts_of_call(pt, f"{cyan}o")

        pt = self.l[self.get_idx(-2)]
        self.guts_of_call(pt, f"{cyan}.")


        self.idx = self.get_idx()

    def get_idx(self, incr=1):
        r = incr + self.idx
        if r >= len(self.l):
            r -= len(self.l)
        elif r < 0: 
            r += len(self.l)
        return r

    def guts_of_call(self, pt, s):
        (yo, xo) = get_size()
        yc = int(yo/2)
        xc = int(xo/2)
        
        x = xc + pt[0]
        y = yc + pt[1]
        s = f"\033[{y};{x}H{s}\033[{yo};1H\033[0m"
        print(s, end='', flush=True)





def circle_example(rounds=50, sleep=0.25):
    #initilaze the object
    circle = Circle()
    for i in range(rounds):
        #call the object, which executes __call__ and prints an update
        circle()
        time.sleep(sleep)

def color_circle_example(rounds=50, sleep=0.25):
    #initilaze the object
    circle = Circle_Color()
    for i in range(rounds):
        #call the object, which executes __call__ and prints an update
        circle()
        time.sleep(sleep)


def get_next(last, ordered_list):
    if last == "":
        return ordered_list[0]
    i = ordered_list.index(last)
    i += 1
    if i == len(ordered_list):
        i = 0 
    return ordered_list[i]

def animation_triangle(rounds=50, sleep=0.5):
    i = 0 
    loop = True
    toggle = True
    (rows, cols) = get_size()
    locations0 = [[2,5], [4,2], [4,8]]
    locations1 = [[5,5], [3,2], [3,8]]
    while(loop):
        clr()
        s = ""

        if toggle:
            for (row, col) in locations0:
                s += f"\033[{row};{col}HO"
            for (row, col) in locations1:
                s += f"\033[{row};{col}Ho"
            toggle = False
        else:
            for (row, col) in locations0:
                s += f"\033[{row};{col}Ho"
            for (row, col) in locations1:
                s += f"\033[{row};{col}HO"
            toggle = True
        s += f"\033[{rows};1H"
        print(s)
        i += 1
        if (rounds != 0 and i >= rounds):
            loop = False
        time.sleep(sleep)

#  *
#*   *
#*   *
#  *

if __name__ == "__main__":
    pass


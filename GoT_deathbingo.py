# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:13:29 2019

@author: nbartlett
"""
from collections import Counter #delete this?
import numpy as np

np.random.seed(1)

names = ["Jon Snow",
         "Arya",
         "Sansa",
         "Bran",
         "Daenerys",
         "Tyrion",
         "Jaime",
         "Sandor",
         "Brienne",
         "Theon",
         "Jorah",
         "Dondarrion",
         "Varys",
         "Samwell",
         "Drogon",
         "Rheagal",
         "Bronn",
         "Tormund",
         "Davos",
         "Faceless Man",
         "Missandei",
         "Podrick",
#         "Catelyn",
         "Daario",
         "Grey Worm",
         "Gendry",
         "Robert Arryn",
         "Meera",
         "Ed Tollett",
         "Yara",
         "Cersei",
         "Gregor",
         "Night King",
         "Euron",
         "Qyburn",
         "Melisandre",
         "Viserion",
         "Lyanna M",
#         "Hodor",
#         "Wun Wun",
         "Ghost",
         "Nymeria"
         ]

deaths = ["Gendry",
         "Robert Arryn",
         "Meera",
         "Ed Tollett",
         "Yara",
         "Cersei",
         "Gregor",
         "Night King",
         "Euron",
         "Qyburn",
         "Melisandre",
         "Bronn",
         "Tormund",
         "Davos",
         "Faceless Man",
         "Missandei",
         "Podrick"
          ]

players = ["nobody00",
           "nobody01",
           "Nick",
           "nobody03",
           "Kevin",
           "Jayden",
           "Shaney",
           "Blake",
           "Lauren",
           "Dean",
           "Arthur",
           "Eugene",
           "Penny",
           "Don",
           "nobody14",
           "nobody15",
           "Ben Cooper",
           "nobody17",
           "Chris P",
           "Dan J"
           ]


choice1  = np.random.choice(names, 25, replace =False)


def choose_25_names(names):
    choices = np.random.choice(names, 25, replace =False)
    return list(choices)

width = 6+5*14

m = 12 #max name length
k = m+2
top_line = "+"+"-"*k+"+"+"-"*k+"+"+"-"*k+"+"+"-"*k+"+"+"-"*k+"+"
blank_line = "|"+" "*k+"|"+" "*k+"|"+" "*k+"|"+" "*k+"|"+" "*k+"|"

def content_line(five_names):
    line = "|"
    for name in five_names:
        n = len(name)
        n_spaces = k - n
        if n_spaces % 2 == 1:
            padding1 = int((k - n - 1)/2)
            padding2 = padding1 + 1 
        else:
            padding1 = int((k - n)/2)
            padding2 = padding1
        line = line+" "*padding1+name+" "*padding2+"|"
    return line

#print("\n", top_line,"\n", blank_line,"\n",  content_line(names[0:5]))

def print_block(choice):
    block = ""
    for i in range(5):
        start = 5*i
        stop  = 5*(i+1)
        names = choice[start:stop]
        lines = [top_line, 
                 blank_line,
                 blank_line,
                 content_line(names),
                 blank_line,
                 blank_line]
        for line in lines:
            block = block + "\n" + line
    block = block +"\n" + top_line
    return block
    
def write_bingo_card(text_for_file):
    with open(r"Deathbingo{}.txt".format(i),"w") as f:
        f.write(text_for_file)    
    return None

def my_reshape(choice):
    return [choice[5*i:5*(i+1)] for i in range(5)]

def check_deaths(name_grid, death_register):
    '''takes a name grid and returns a death index grid filled with 0's and 1's,
    along with the row, column and diagonal sums of the grid'''
    num_grid = [[],[],[],[],[]]
    for i in range(5):
        for j in range(5):
            if name_grid[i][j] in death_register:
                num_grid[i].append(1)
            else:
                num_grid[i].append(0)
    rowsums = [sum(i) for i in num_grid]
    colsums = [sum([num_grid[i][j] for i in range(5)]) for j in range(5)]
    diag_ltr = [sum([num_grid[i][i] for i in range(5)])]
    diag_rtl = [sum([num_grid[4-i][i] for i in range(5)])]
    return num_grid, rowsums, colsums, diag_ltr, diag_rtl
   
def check_for_winner(name_grid, death_register):
    """takes a bingo card and list of dead characters and returns the total number
    of dead characters on the card, the highest linesum and whether the card has 
    won
    """
    num_grid, rowsums, colsums, diag_ltr, diag_rtl = check_deaths(name_grid, death_register)
    score = sum(rowsums)
    max_score = max(rowsums + colsums + diag_ltr + diag_rtl)
    is_winner = 1 if max_score == 5 else 0
    return score, max_score, is_winner

def check_for_all_winners(name_grids, death_register, players):
    winners = []
    for i, name_grid in enumerate(name_grids):
        score, max_score, is_winner  = check_for_winner(name_grid, death_register)
        if is_winner:
            winners.append([players[i], score, max_score, is_winner])
    if len(winners) == 0:
        print("There's no winners yet!")
    else:
        print("Winners!")
    return winners
    
def resolve_deaths(partial_death_register):
    """transforms a partial list of the death register containing names and lists
    of names into just a big list of names"""
    old_list = partial_death_register
    new_list = []
    for i in partial_death_register:
        if isinstance(i, list):
            new_list = new_list + i
        else:
            new_list.append(i)
    return new_list            


#  begin script  

all_names = []
all_choices = []

for i in range(20):
    choices = choose_25_names(names)
    all_choices.append(choices)
    all_names = all_names + list(choices)
    text_for_file = print_block(choices)
#   print(i)
#   print(text_for_file)
#   write_bingo_card(text_for_file)
    
#print(all_names)        
#print(Counter(all_names))

#create 5x5 name grids
all_grids = [my_reshape(choice) for choice in all_choices]


#testing
print(deaths)
print(print_block(all_choices[19]))

print(check_for_winner(all_grids[19],deaths))

print(check_deaths(all_grids[19],deaths))

print(check_for_all_winners(all_grids, deaths, players))
#G, rs,cs, dl, dr = check_deaths(all_grids[0], ["Bronn","Jon Snow"])

#print(all_grids[0])
#print(G)
#print(rs)
#print(cs)
#print(dl)
#print(dr)
#              
#print(rs + cs + dl + dr)  
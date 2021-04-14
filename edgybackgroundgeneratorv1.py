#generates an edgy backstory for your D&D or other fantasy TTRPG character
#based off the Random Edgelord Backstory Table by Dungeon Masterminds, whoever they may be

#In order for weights to work, each dictionary entry must have the backstory components it
#holds as keys, and the probability of getting a given entry as part of your backstory
#as a value.

#At some point in future, rewrite code so that probabilites are stored in a separate list,
#and can be edited there

#tossed ideas for the generate and delete button's names include "Give me an OC" and "Not Anime Enough"

import random
import tkinter as tk
import mouse

#villain dictionary
villaindict = dict([
    ("An evil wizard ", 0.3),
    ("A dragon ", 0.3),
    ("The drow ", 0.3),
    ("Goblins ", 0.3),
    ("Kobolds ", 0.3),
    ("A mind flayer ", 0.3),
    ("Evil cultists ", 0.3),
    ("Orcs ", 0.3),
    ("Trolls ", 0.3),
    ("A banshee ", 0.3),
    ("A demon lord ", 0.3),
    ("An archdevil ", 0.3),
    ("Giants ", 0.3),
    ("Vampires ", 0.3),
    ("A wereworlf ", 0.3),
    ("A djinni ", 0.3),
    ("A mimic ", 0.3),
    ("A tarrasque ", 0.3),
    ("A beholder ", 0.3),
    ("A hag coven ", 0.3),
    ("A lich ", 0.3),
    ("Barbarians ", 0.3),
    ("An aboleth ", 0.3),
    ("A succubus ", 0.3),
    ("A criminal organization ", 0.3),
    ("Gnolls ", 0.3),
    ("A necromancer ", 0.3),
    ("Corrupt nobles ", 0.3),
    ("A death knight ", 0.3),
    ("The BBEG ", 0.3),
    ("The bard ", 0.3),
    ("Natural Selection ", 0.3),
    ("A gelatinous cube ", 0.3),
    ("The DM ", 0.1),
    ])

#action dictionary
actiondict  = dict([
    ("killed ", 0.09),
    ("murdered ", 0.1),
    ("slaughtered ", 0.1),
    ("massacred ", 0.1),
    ("assassinated ", 0.1),
    ("brainwashed ", 0.03),
    ("captured ", 0.03),
    ("banished ", 0.03),
    ("enslaved ", 0.03),
    ("betrayed ", 0.03),
    ("sacrificed ", 0.03),
    ("mauled ", 0.03),
    ("stole ", 0.03),
    ("blackmailed ", 0.03),
    ("conned ", 0.03),
    ("framed ", 0.03),
    ("humiliated ", 0.03),
    ("pillaged ", 0.03),
    ("ruined ", 0.03),
    ("ate ", 0.03),
    ("cursed ", 0.03),
    ("befriended ", 0.02),
    ("seduced ", 0.01),
    ])

#victim dictionary
victimdict  = dict([
    ("my family ", 0.04),
    ("my hometown ", 0.04),
    ("my parents ", 0.04),
    ("my clan ", 0.04),
    ("my sibling ", 0.04),
    ("my mentors ", 0.04),
    ("my significant other ", 0.04),
    ("my master ", 0.04),
    ("my side squeeze ", 0.04),
    ("my apprentice ", 0.04),
    ("my previous adventuring party ", 0.04),
    ("everyone I knew ", 0.04),
    ("my crew of sailors ", 0.04),
    ("my crew of pirates ", 0.04),
    ("my crew of noble outlaws ", 0.04),
    ("my crew of thieves ", 0.04),
    ("the tavern I basically lived in ", 0.04),
    ("my start-up business ", 0.04),
    ("my military unit ", 0.04),
    ("my social status ", 0.04),
    ("my treasure ", 0.04),
    ("my aspirations ", 0.04),
    ("my confidence ", 0.04),
    ("my hounour ", 0.03),
    ("my imaginary friends ", 0.01),
    ])

#outcome dictionary
outcomedict = dict([
    ("and it will have no effect on how I roleplay my character.", 0.29),
    ("and now I'm a murder hobo.", 0.1),
    ("and now I'm a lawful good stick in the mud.", 0.1),
    ("and now I seek vengeance.", 0.04),
    ("and now I trust no one.", 0.04),
    ("and now I have a bleak outlook on the world.", 0.04),
    ("and now I strive to live by their ideals.", 0.04),
    ("and now I must become stronger.", 0.04),
    ("and now I seek to bring back what I have lost.", 0.05),
    ("and now I vow to prevent that from happening to anyone else.", 0.04),
    ("and now I am haunted by their memory.", 0.04),
    ("and now I seek to unvocer the truth about what happened.", 0.04),
    ("and now I fear it will happen again.", 0.04),
    ("and now I am stronger because of it.", 0.03),
    ("and now I'm an alcoholic.", 0.03),
    ("and now I have multiclassed into warlock.", 0.03),
    ("and now I'm Batman.", 0.01),
    ])


#initialize gui code
root = tk.Tk()

gui = tk.Canvas(root, width = 300, height = 300)
gui.pack

#erase the backstory to create new one - in place to avoid cluttering gui
def backstoryeraser():
    backstory.destroy()
    generator['state'] = tk.NORMAL
    eraser['state'] = tk.DISABLED

#backstory generation
def backstorygenerator():

    global backstory
    
    #functions to choose dictionary entries
    
    villain = random.choices(list(villaindict.keys()), weights=villaindict.values(), k=1)
    action  = random.choices(list(actiondict.keys()), weights=actiondict.values(), k=1)
    victim  = random.choices(list(victimdict.keys()), weights=victimdict.values(), k=1)
    outcome = random.choices(list(outcomedict.keys()), weights=outcomedict.values(), k=1)

    #function to convert lists to strings
    def listToString(s): 
        
        # initialize an empty string
        str1 = "" 
        
        # traverse in the string  
        for ele in s: 
            str1 += ele  
        
        # return string  
        return str1 
            
    #convert lists to strings        
    villainstr = listToString(villain)
    actionstr  = listToString(action)
    victimstr  = listToString(victim)
    outcomestr = listToString(outcome)

    combined = villainstr + actionstr + victimstr + outcomestr

    #display the backstory in the gui
    backstory = tk.Label(root, text=combined, font=('helvetica', 12, 'bold'))
    gui.create_window(150, 150, window=backstory)

    backstory.pack()
    generator['state'] = tk.DISABLED
    eraser['state'] = tk.NORMAL

    
#create the generator GUI

generator = tk.Button(root, text = "Generate", command = backstorygenerator)
eraser = tk.Button(root,text = "Delete", command=backstoryeraser)
eraser['state'] = tk.DISABLED
gui.create_window(150, 200, window=generator)

generator.pack()
eraser.pack()

root.mainloop()

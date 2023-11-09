from generaldb import *
from musicdb import *
import os
def takeinput(time_picker,reps,sound,change,ohour,ominute,otype):
    init()
    active=True
    if(change==0):
        add(time_picker,reps,sound,active)
    else:
        alter(time_picker,reps,sound,ohour,ominute,otype)
def read_input():
    init()
    records=show()
    return records

def Delete(hour,minute,type):
    dele(hour,minute,type)

def takefilepath(path):
    name=os.path.basename(path) 
    m_init()
    m_add(path,name)
def readfile():
    m_init()
    soundtracks=m_show()
    print(soundtracks)
    return soundtracks
def delefile(path):
    m_dele(path)
def switch(state,curhour,curmin,type):
    turn(state,curhour,curmin,type)
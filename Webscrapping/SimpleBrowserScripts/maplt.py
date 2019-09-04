import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #Get address from the command line, [1:] will chop the program name from the sys.argv
    address = ' '.join(sys.argv[1:])
else:
    #Get the adddress from clipboard by using pyperclip
    address = pyperclip.paste()    

webbrowser.open('https://www.google.com/maps/place/' + address)


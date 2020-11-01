

import keyboard
import webbrowser


def openGithub():
    webbrowser.open_new_tab('https://github.com')

def openStackoverflow():
    webbrowser.open_new_tab('https://stackoverflow.com')

def openYoutube():
    webbrowser.open_new_tab('https://youtube.com')



keyboard.add_hotkey('shift + g', openGithub)
keyboard.add_hotkey('shift + s', openStackoverflow)
keyboard.add_hotkey('shift + y', openYoutube)




# Blocks until you press esc.
keyboard.wait('esc')








if __name__ == '__main__':
    pass





import keyboard
import webbrowser
import os

def newPythonProject():
    # desktop path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # move intp the desktop
    os.chdir(desktop)

    # Ask for a project name
    projectName = input("Project Name: ")

    # create a folder for the project
    folder = os.path.join(projectName)
    os.makedirs(folder)

    # go into the created folder
    os.chdir(folder)

    # create a .gitignore file
    with open('README.md', 'w') as fileObject:
        fileObject.write("# {}".format(projectName))

    # create a reademe file
    with open('.gitignore', 'w') as fileObject:
        fileObject.write("venv")

    # initialize git in the folder
    os.system("git init")

    # add the two current files
    os.system("git  add .")

    # create a virtual environment
    os.system("virtualenv venv")

    # open VS code
    os.system("code .")  # open the folder in the


def openGithub():
    webbrowser.open_new_tab('https://github.com')

def openStackoverflow():
    webbrowser.open_new_tab('https://stackoverflow.com')

def openYoutube():
    webbrowser.open_new_tab('https://youtube.com')



keyboard.add_hotkey('shift + g', openGithub)
keyboard.add_hotkey('shift + s', openStackoverflow)
keyboard.add_hotkey('shift + y', openYoutube)
keyboard.add_hotkey('shift + h', newPythonProject)



# Blocks until you press esc.
keyboard.wait('esc')








if __name__ == '__main__':
    pass



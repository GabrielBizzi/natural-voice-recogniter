import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'code': "C:\\Users\\Gabriel\\AppData\\Local\\Programs\\Microsoft VS Code Insiders\\bin\\code-insiders.exe",
    'discord': "C:\\Users\\Gabriel\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'shell': "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])

def open_shell():
    sp.Popen(paths['shell'])
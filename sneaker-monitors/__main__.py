from pyfiglet import  figlet_format
import six
import os
import threading
import signal
import ctypes
#import cursor
try:
    from termcolor import colored
except ImportError:
    colored = None
import time

from db import create_config_db, get_config, update_config, get_all_config, columns

from __init__ import __version__, __author__, __monitors__


def clear():
    if os.name in ("nt", "dos"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"SNEAKER MONITORS [v{__version__}] - Created by {__author__}")
        #cursor.hide()
        os.system("cls")
    elif os.name in ("linux", "osx", "posix"): os.system("clear")
    else: print("\n") * 100


def log(text, colour, font='slant', figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(text, colour))
        else:
            six.print_(colored(figlet_format(
                text, font=font), colour))
    else:
        six.print_(text)


def run(path):
    pass


def configure(monitor):
    clear()
    log(F' ***** CONFIGURE {monitor.upper()} *****', colour='green')
    items = get_config(monitor)
    log(f'Type in the value you want for... ', colour='blue')
    log('If you want to keep the current value, just hit ENTER', colour='blue')
    inputs = []
    for index, column in enumerate(columns):
        log(f' CURRENT VALUE OF {column.upper()} = {items[index+1]}', colour='blue')
        value = input('NEW VALUE: ')
        if value == "":
            inputs.append(None)
        else:
            inputs.append(str(value))
    log('* UPDATING... *', colour='blue')
    update_config(monitor, inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], inputs[7], inputs[8])
    log('* UPDATED *', colour='blue') 
    log('Going back...', colour='blue')
    time.sleep(1)
    configure_screen()


def get_monitor(index):
    return __monitors__[int(index)].lower()


def get_monitor_path(index):
    '''
    params:
     - index (str): Index of monitor 

    return:
     - path of monitor.py file 
    '''
    return os.path.realpath(get_monitor(index)+'/monitor.py')


def monitor_command(command):
    os.system(command)


def run_screen():
    clear()
    log('Select the monitor(s) you want to run. To run multiple, list them with spaces (Example: 1 5 6 7), but note the risks related to running multiple monitors here: ', colour='green')
    for i, m in enumerate(__monitors__):
        log(f'    [{i}] {m}', colour='blue')
    log(f'    [{i+1}] Back', colour='blue')
    log('Type the option(s) here: ', colour='green')
    monitor_options = input().split(' ')

    # Go back
    if str(int(i)+1) in monitor_options:
        main()

    commands = ''
    start = 0
    for m in monitor_options:
        if start == 0:
            commands+=f'python {os.path.abspath(f"sneaker-monitors/monitors/{get_monitor(m)}/monitor.py")}'
            start = 1
        else:
            commands+=f' && python {os.path.abspath(f"sneaker-monitors/monitors/{get_monitor(m)}/monitor.py")}'

    print(commands)


def configure_screen():
    clear()
    log('Select the monitor you want to configure.', colour='green')
    for i, m in enumerate(__monitors__):
        log(f'    [{i}] {m}', colour='blue')
    log(f'    [{i+1}] View all configurations', colour='blue')
    log(f'    [{i+2}] Back', colour='blue')
    log('Type the option here: ', colour='green')
    monitor_option = input()

    if str(int(i)+1) in monitor_option:
        clear()
        log(' ** ALL CONFIGURATIONS **', colour='green')
        items = get_all_config()
        print('MONITOR NAME | WEBHOOK | USERNAME | AVATAR URL | COLOUR | DELAY | KEYWORDS | PROXIES | FREE PROXIES | DETAILS')
        for i in items:
            print(i)

        if type(input()) == type(""):
            configure_screen()

    # Go back
    if str(int(i)+2) in monitor_option:
        main()

    try:
        monitor = get_monitor(monitor_option)
        configure(monitor)

    except:
        pass


def main():
    create_config_db()
    clear()
    log('Sneaker Monitors', colour='red', figlet=True)
    log('Created by GitHub:yasserqureshi1   Discord:TheBrownPanther2#8491', colour='yellow')
    log('Choose option: ', colour='green')
    log('    [1] Run Monitors', colour='blue')
    log('    [2] Configure Monitors', colour='blue')
    log('    [3] Help', colour='blue')
    log('    [4] Exit', colour='blue')
    print('')
    log('Type option value here: ', colour='green')

    option = input()
    if option == '1':
        # Run Monitors
        run_screen()

    elif option == '2':
        configure_screen()

    elif option == '3':
        clear()
        log(' ***** HELP *****\n', colour='green')
        log('You can find documentation at the following link:', colour='blue')
        log('', colour='blue')  # Link to documentation
        log('You can join the Discord server for more help here:', colour='blue')
        log('', colour='blue')  # Link to discord server
        log('', colour='blue')
        if type(input()) == type(""):
            main()

    elif option == '4':
        os.kill(os.getppid(), signal.SIGHUP)
    
    else:
        log('Invalid option. Please try again in...', colour='red')
        time.sleep(1)
        log('3', colour='red')
        time.sleep(1)
        log('2', colour='red')
        time.sleep(1)
        log('1', colour='red')
        main()

main()



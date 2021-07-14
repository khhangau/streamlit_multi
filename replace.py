import subprocess, time

while(True):
    with open('wbnm.py') as f:
        s = f.read()

    with open('wbnm.py') as f:
        if 'satellite' not in s:
            s = f.read().replace('light', 'satellite')
        else:
            s = f.read().replace('satellite', 'light')

    with open('wbnm.py', 'w') as f:
        f.write(s)

    subprocess.call(['push.bat'])
    time.sleep(30)

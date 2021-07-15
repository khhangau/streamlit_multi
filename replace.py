import subprocess, time

while(True):
    with open('BCC_Meta.out') as f:
        s = f.read()

    with open('BCC_Meta.out') as f:
        if 'satellite' not in s:
            s = f.read().replace('258.587', '358.587')
        else:
            s = f.read().replace('358.587', '258.587')

    with open('BCC_Meta.out', 'w') as f:
        f.write(s)

    subprocess.call(['push.bat'])
    time.sleep(30)

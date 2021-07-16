import subprocess, time

while(True):
    # toggle BCC_Meta.out
    with open('BCC_Meta.out') as f:
        s = f.read()

    with open('BCC_Meta.out') as f:
        if '358.587' not in s:
            s = f.read().replace('258.587', '358.587')
        else:
            s = f.read().replace('358.587', '258.587')

    with open('BCC_Meta.out', 'w') as f:
        f.write(s)

    # toggle wbnm.py
    with open('wbnm.py') as f:
        s = f.read()

    with open('wbnm.py') as f:
        if '# Ren' not in s:
            s = f.read().replace('# Render', '# Ren')
        else:
            s = f.read().replace('# Ren', '# Render')

    with open('wbnm.py', 'w') as f:
        f.write(s)

    subprocess.call(['push.bat'])
    time.sleep(30)

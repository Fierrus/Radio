import subprocess
commands = ['set comport com14 9600 8n1']
#command = "achno 35 setup :-60951889 get2 chno"
#commands.append(command)


for command in commands:
    output = subprocess.check_output(['C:/11/nncltool/nncltool.exe', f'{command}'])
    output = str(output)
    print(output)
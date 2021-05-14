import time
import subprocess
import LoadMAC

comport = 7
channel = 10
cur_sec = time.localtime()
cur_time = time.strftime("%H-%M-%S", cur_sec)


mac_state = {}
def exchange():
    macs = LoadMAC.read_mac()
    for mac in macs:
        command = f"""--com={comport},9600 --plc --intro2 --ch={channel} --t=5000 --mac={mac} --noraw -i 5"""
        output = subprocess.check_output(['C:/SMPConsole/SMPConsole.exe', f'{command}'])
        output = str(output)
        print(output)
        check_output(output, mac)


def check_output(output, mac):
    if output[12:15] == "5=e":
        state = 'not OK'
        line = f'{mac} is {state}'
        LoadMAC.write_down(cur_time, line)
        print(line)
        mac_state.update(mac=state)
        return
    elif output[12:14] == "5=":
        state = 'OK'
        line = f'{mac} is {state}'
        LoadMAC.write_down(cur_time, line)
        print(line)
        mac_state.update(mac=state)
        return
    else:
        state = 'Error'
        line = f'{state}'
        LoadMAC.write_down(cur_time, line)
        print('Error')
        mac_state.update(mac=state)
        return

if __name__ == '__main__':
    exchange()
    print (mac_state)
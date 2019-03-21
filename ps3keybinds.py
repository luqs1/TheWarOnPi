import evdev
from Classes.Movement import *
m = Movement()
speed = int(input('Speed: ')) % 101
deadzone = 10

buttonMap = {'312':[m.forward,(speed,0,1)],'310':[m.turn,('l',0,speed)],'311':[m.turn,('r',0,speed)],'316':[exit,()]}

for i in buttonMap.values():
    i.append(False)

def buttonPressed(button):
    a = buttonMap[button]
    print(a)
    a[2] = not a[2]
    if a[2]:
        a[0](*a[1])
    elif not a[2]:
        m.stop()

def deadZones(conInput):
    a = conInput - 127
    if abs(a) < deadzone: return 0
    else: return a

def scale(coord,scaler):
    dirl,dirr=0,0
    l,r=127,127
    if coord>0:
        dirr=1
        l=abs(coord)
        r=125-l
    elif coord<0:
        dirl=1
        r=abs(coord)
        l=125-r
    l *= scaler/127
    r *= scaler/127
    return (l,r,dirl,dirr)  
x = 0
R2 = 0

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)
number = input('Event No: ')
device = evdev.InputDevice('/dev/input/event'+number)
print(device)
pressed = False
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
        button = str(evdev.categorize(event)).split()[4]
        buttonPressed(button)
"""
    elif event.type == evdev.ecodes.EV_ABS:
        if event.code == evdev.ecodes.ABS_X:
            x = deadZones(event.value)
        if event.code == 5:
            R2 = event.value
        m.set(*scale(x,R2))
"""

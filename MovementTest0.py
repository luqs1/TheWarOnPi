from Classes.Movement import *
m = Movement()
print(m.outpins)
m.forward(100,1)
m.turn('l',1)
m.turn('r',1)
m.forward(100,1,1)
print('Done')
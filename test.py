from Classes.Movement import *
m = Movement()
print(m.outpins)
m.forward(50,1)
m.turn('l',1)
m.turn('r',1)
print('Done')
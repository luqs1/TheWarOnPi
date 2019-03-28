import pixy
from ctypes import *
from pixy import *

# Pixy2 Python SWIG get blocks example #

print ("Pixy2 Python SWIG Example -- Get Blocks")

pixy.init ()
pixy.change_prog ("color_connected_components");

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

number = 2
class Vision():
    def __init__(self):
        self.blocks = BlockArray(number)
        self.frame = 0
    def get_block(self):
        blocks = self.blocks
        count = ccc_get_blocks(number, self.blocks)
        if count > 0:
            self.frame += 1
            return [blocks[index] for index in range(0,count)]
        else:
            return None
    def get_colour(self,signature):
        read = self.get_block()
        result = []
        for line in read:
            if line.m_signature == signature:
                result.append(line)
        return result
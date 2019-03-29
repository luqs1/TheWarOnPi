import pixy
from ctypes import *
from pixy import *

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

class Vector (Structure):
  _fields_ = [
    ("m_x0", c_uint),
    ("m_y0", c_uint),
    ("m_x1", c_uint),
    ("m_y1", c_uint),
    ("m_index", c_uint),
    ("m_flags", c_uint) ]

class IntersectionLine (Structure):
  _fields_ = [
    ("m_index", c_uint),
    ("m_reserved", c_uint),
    ("m_angle", c_uint) ]

class Vision():
    def __init__(self):
        pixy.init()
        self.frame = 0
    def setmode(self,mode):
        if mode == 1:
            pixy.change_prog("color_connected_components")
            self.blocks = BlockArray(number)
        else:
            pixy.change_prog("line")
            self.vectors = VectorArray(100)
            self.intersections = IntersectionLineArray(100)
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
        if read == None:
            return None
        result = []
        for line in read:
            if line.m_signature == signature:
                result.append(line)
        return result
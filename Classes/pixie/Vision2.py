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
        elif mode == 2:
            pixy.change_prog("line")
            self.vectors = VectorArray(100)
            self.intersections = IntersectionLineArray(100)
        else:
            print('Invalid Mode')
    def lamp(self,a,b):
        set_lamp(a,b)
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
        if len(result) == 0: return None
        return result
    def get_lines(self):
        print(1)
        read = line_get_all_features()
        count = line_get_vectors(number,self.vectors)
        if count > 0:
            print(2)
            return [self.vectors,count]
        else:
            return None
    def get_lowest_line(self):
        print(3)
        arr = self.get_lines()
        if arr == None:
            return None
        lines = arr[0]
        count = arr[1]
        if lines == None:
            return None
        lline = lines[0]
        lines = [lines[i] for i in range(count)]
        for a in lines:
            if lline.m_y0 > a.m_y0:
                lline = a
        print(4)
        return lline
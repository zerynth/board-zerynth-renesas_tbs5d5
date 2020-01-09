from base import *
from devices import *

class Renesas_TBS5D5ser(Board):
    @staticmethod
    def match(dev):
        return dev["vid"] =="0403" and dev["pid"]=="6001"

    def reset(self):
        pass

    def burn(self,bin,outfn=None):
        pass
    
    def __init__(self,info={},dev={}):
        super().__init__(info,dev)
        self._info["name"] = "Renesas TB-S5D5 Serial"

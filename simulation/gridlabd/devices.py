"""Devices
"""

import uuid
import datetime as dt
import random

gridlabd = None
DATABASE = None

device_list = {}

def init(**kwargs):
    for key,value in kwargs.items():
        if key in ["gridlabd","DATABASE"]:
            globals()[key] = value

def find(name):
    return device_list[name]

def create(obj,t0):
    data = gridlabd.get_object(obj)
    device = globals()[data["type"]](data,t0)
    device_list[obj] = device
    return device

def update(t):
    return min([d.update(t) for d in device_list.values()])

def guid():
    return uuid.uuid4().hex[2:]

class Device:

    def __init__(self,data,t0):
        for key,value in data.items():
            setattr(self,key,value)
        self.t0 = t0
        DATABASE.insert_devices(data['name'],data['agent'],data['type'])

    def sync_data(self,names=[],read=True):
        for name in names:
            if read:
                gridlabd.set_value(self['name'],name,getattr(self,name))
            else:
                setattr(self,name,gridlabd.get_value(self['name'],name))

    def update_settings(self,names):
        for name in names:
            DATABASE.insert_settings(guid(),self.name,name,getattr(self,name))

    def update(self,t1):
        return gridlabd.NEVER

class CD(Device):

    pass

class SD(Device):

    pass

class HC(Device):
    
    def __init__(self,data,t0):
        super().__init__(data,t0)
        self.Tmin = round(random.uniform(68,72),1);
        self.Tmax = round(random.uniform(74,78),1);
        self.Tdesired = round(random.uniform(self.Tmin,self.Tmax),1);
        self.Tnow = round(random.uniform(self.Tmin,self.Tmax),1);
        self.Tlast = round(random.uniform(self.Tnow-1,self.Tnow+1),1)
        self.Khvac = round(random.uniform(0.0,1.0),1);
        self.update_settings(["Tmin","Tmax","Tdesired","Khvac"])

class HW(Device):
    
    def __init__(self,data,t0):
        super().__init__(data,t0)
        self.Tset = round(random.uniform(68,72),1);
        self.Tdb = round(random.uniform(8,14),1);
        self.Tnow = round(random.uniform(self.Tset-self.Tdb/2,self.Tset+self.Tdb/2),1);
        self.Khw = round(random.uniform(0.0,1.0),1);
        self.update_settings(["Khw"])

class PV(Device):
    
    def __init__(self,data,t0):
        super().__init__(data,t0)

class EV(Device):
    
    def __init__(self,data,t0):
        super().__init__(data,t0)
        self.Qdesired = round(random.uniform(10,40),1)
        self.tdone = round(t0 + random.uniform(1,8)*3600,1)
        self.Kev = round(random.uniform(0.0,1.0),1);
        self.update_settings(["Qdesired","tdone","Kev"])

class ES(Device):
    
    def __init__(self,data,t0):
        super().__init__(data,t0)
        self.Qdesired = round(random.uniform(10,40),1)
        self.Kes = round(random.uniform(0.0,1.0),1);
        self.update_settings(["Qdesired","Kes"])

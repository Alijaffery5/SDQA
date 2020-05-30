import os
import sys
import glob
from app import getFile, Metrics_defined

class DesignSmells():

    def detect_LM(self, file):
        
        counter = 0
        smells = {}
        for func, val in  Metrics_defined.get_NOML(self,file).items():
            x = len(val)
            if x <= 10:
                continue
            elif 10 < x <= 30:
                continue
            elif x > 30:
                counter += 1
                smells[func] = x
                continue
        return smells

    def detect_LBCL(self):
        counter = 0
        for i in getFile.get_full_classname(self):
            x = len(Metrics_defined.dit_list(self,i))
            if x <= 2:
                continue
            elif 2 < x <= 4:
                continue
            elif x > 4:
                counter += 1
                continue
        return counter

    def detect_LPL(self):

        dict = Metrics_defined.Number_of_parameters(self,"phones.py")
        counter = 0
        new_dict = {}
        for x,y in dict.items():
            if y <= 2:
                continue
            elif 2 < y <= 4:
                continue
            elif y > 4:
                new_dict[x] = y
                counter += 1
                continue
        return  new_dict

    def data_class(self):
        dict = Metrics_defined().Number_of_accessors("phones.py")
        smell_dict = {}
        for class_name,val in dict.items():
            if val >= 4:
                smell_dict[class_name] = val
                continue

        return smell_dict

    def LTCL(self):
            
        counter = 0
        dict = {}
        loc = Metrics_defined().get_LOC_class("phones.py")
        for x,y in loc.items():
            if y > 50:
                dict[x] = y

        return dict



    def swiss_army_knife(self):
        counter = 0
        for i in getFile.get_full_classname(self):
            x = len(Metrics_defined.dit_list(self,i))
            if x <= 2:
                continue
            elif 2 < x <= 4:
                continue
            elif x >= 4:
                counter += 1
                continue
        return counter

    def large_class(self):  ## LOC < 300
        
        counter = 0
        dict = {}
        loc = Metrics_defined().get_LOC_class("phones.py")
        for x,y in loc.items():
            if y > 50:
                dict[x] = y

        return dict


    def feature_envy(self):
        var = 2
        def inner_method(self):

            dict = {}


        
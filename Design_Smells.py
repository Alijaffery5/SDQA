import os
import sys
import glob
from app import getFile, Metrics_defined

class DesignSmells():

    def detect_LM(self):
        
        smells = {}
        
        for file in getFile.get_fileName(self):
            
            for func , details in  Metrics_defined.get_NOML(self,file).items():
                
                value = len(details['body'])
                
                if value <= 10:
                    continue
                elif 10 < value <= 30:
                    continue
                elif value > 30:
                    
                    smells [file] = {
                    'line_number' : details['line'],
                    'class_name' : details['class_'],
                    'function_' : func,
                    'value' : value,
                    'normal' : "1-30"
                    }
                    continue

        return smells

    def detect_LBCL(self):

        smells = {}
        for file in getFile.get_fileName(self):
            for class_ in getFile.get_full_classname(self,file):
                dit = Metrics_defined.dit_list(self, class_ , file)
                x = len(dit)
                if x <= 2:
                    continue
                elif 2 < x <= 4:
                    continue
                elif x > 4:
                    smells [file] = {
                    'DIT List' : dit,
                    'value' : x,
                    'normal' : "1-4"
                    }
                    continue
        return smells

    def detect_LPL(self):

        smells = {}

        for file in getFile.get_fileName(self):
            for func , details in  Metrics_defined.Number_of_parameters(self,file).items():

                value = details['parameters']
                if value <= 2:
                    continue
                elif 2 < value <= 4:
                    continue
                elif value > 4:

                    smells [file] = {
                    'line_number' : details['line'],
                    'class_name' : details['class_'],
                    'function_' : func,
                    'value' : value,
                    'normal' : "1-4"
                    }
                    
                    continue
        return  smells

    def data_class(self):
        
        for i in getFile.get_fileName(self):
            dict = Metrics_defined().Number_of_accessors(i)
            smell_dict = {}
            for class_name,val in dict.items():
                if val >= 4:
                    smell_dict[class_name] = val
                    continue

        return smell_dict

    def LTCL(self):
            
        dict = {}
        for i in getFile.get_fileName(self):
            loc = Metrics_defined().get_LOC_class(i)
            for x,y in loc.items():
                if y > 50:
                    dict[x] = y

        return dict

    def swiss_army_knife(self):
        counter = 0
        for i in getFile.get_fileName(self):
            for class_ in getFile.get_full_classname(self,i):
                x = len(Metrics_defined.dit_list(self, class_ , i))
                if x <= 2:
                    continue
                elif 2 < x <= 4:
                    continue
                elif x >= 4:
                    counter += 1
                    continue
        return counter

    def large_class(self):  ## LOC < 300
        
        smells = {}
        for file in getFile.get_fileName(self):
            loc = Metrics_defined().get_LOC_class(file)
            for class_ , details in loc.items():
                if details['value'] > 50:
                    smells [file] = {
                    'line_number' : details['line_number'],
                    'class_name' : class_,
                    'loc' : details['value'],
                    'normal' : "1-300"
                    }

        return smells


    def feature_envy(self):
        var = 2
        def inner_method(self):

            dict = {}


        
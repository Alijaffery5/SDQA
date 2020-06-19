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
                dit_str = ''
                value = len(dit)
                if value <= 2:
                    continue
                elif 2 < value <= 4:
                    continue
                elif value > 4:
                    for x in dit:
                        dit_str += x + ',  '
                    smells [file] = {
                    'DIT List' : dit_str,
                    'value' : value,
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
        
        smell_dict = {}

        for file in getFile.get_fileName(self):
            dict = Metrics_defined().Number_of_accessors(file)
            for class_name,value in dict.items():
                if value >= 4:
                    smell_dict [file] = {
                    'class_name' : class_name,
                    'value' : value,
                    'normal' : "1-4"
                    }
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

        smell_dict = {}
        for file in getFile.get_fileName(self):
            sup = Metrics_defined.Number_of_SUP(self, file)
            for class_name, details in sup.items():
                if details['SUP'] <= 2:
                    continue
                elif 2 < details['SUP'] < 4:
                    continue
                elif details['SUP'] >= 4:
                    smell_dict [file] = {
                    'class_name' : class_name,
                    'line_number' : details['line_number'],
                    'value' : details['SUP'],
                    'normal' : "1-4"
                    }
                    continue
                
        return smell_dict

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


        
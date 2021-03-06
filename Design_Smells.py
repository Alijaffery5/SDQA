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

    def large_class(self):  ## LOC < 200
        
        smells = {}
        for file in getFile.get_fileName(self):
            loc = Metrics_defined().get_LOC_class(file)
            for class_ , details in loc.items():
                if details['value'] > 200:
                    smells [file] = {
                    'line_number' : details['line_number'],
                    'class_name' : class_,
                    'loc' : details['value'],
                    'normal' : "1-200"
                    }

        return smells


    def feature_envy(self):
        smells = {}
        for file in getFile.get_fileName(self):
            AID = Metrics_defined().get_aid(file)
            for class_ , details in AID.items():
                if details['AID'] > 4:
                    smells [file] = {
                    'class_name' : class_,
                    'AID' : details['AID'],
                    'normal' : "1-4"
                    }

        return smells


    def God_Class(self):

        smells = {}
        y = 0
        
        for file in getFile.get_fileName(self):
            loc = Metrics_defined().get_LOC_class(file)
            
            NOM = Metrics_defined().Number_of_methods(file)
            NOF = Metrics_defined().Number_of_fields(file)
            NOA = Metrics_defined().Number_of_accessors(file)
            LCOM = Metrics_defined().get_lcom4(file)
            
                    
            
            for class_ , value in NOM.items():
                for class_ , value_3 in NOF.items():
                    for class_ , value_4 in NOA.items():
                        
                        for lcom in LCOM:
                            for class_ , details2 in loc.items():
                                for x,y in details2.items():
                                    
                                    if int(y) > 50 and value_4 > 2 and float(lcom) >= 2:
                                        
                                        smells [file] = {
                                        'class_name' : class_,
                                        # 'value' : counter,
                                        'violations' : 'loc, LCOM, NOA'
                                        }

                return smells

    def ltce(self):
        smells = {}
        for file in getFile.get_fileName(self):
            NOL = Metrics_defined().get_LOC_class(file)
            with open("data/"+file, "r") as file:
                for line in file:
                    word = line.split()
                    if word == 'if' and word == 'else':
                            print(word)
                    # for x in word:
                    #     if x == 'if' and x == 'else':
                    #         print(x)
                    
                    # if 'if' and 'else' or 'lambda' in word:
                    #     print('ternary')
                    for class_ , details in NOL.items():
                        if details['value'] > 50:
                            smells [file] = {
                            'class_name' : class_,
                            'LOC' : details['value'],
                            'normal' : "1-4"
                            }

        return smells



    def test(self):

        def hh(self):
            pass
    
        DesignSmells().ltce()
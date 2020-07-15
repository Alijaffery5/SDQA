import os
from radon.visitors import ComplexityVisitor
from radon.complexity import cc_rank, cc_visit

class Metrics_defined:

    def lcom4(self, file):
        cmd = os.popen("lcom data/"+file).read().split('\n')
        return cmd

    def cyclomatic_complexity(self, file):
        cmd = os.popen("radon cc data/"+file + " -s").read().split('\n')
        return cmd

    def LOC_metrics(self, file):
        cmd = os.popen("radon raw data/"+file).read().split('\n')
        cmd.pop(0)
        cmd.pop()
        return cmd

    def Number_of_methods(self, file):
        counter = 0
        with open("data/"+file, "r") as file:
            for line in file:
                for word in line.split():
                    if word == "def" or word == "def __":
                        counter += 1

        return counter


    def Number_of_parameters_(self, file):
        counter = 0
        dic = {}
        with open("data/"+file, "r") as file:

            for line in file:
                arr = line.split()
                if len(arr) < 2:
                    continue
                if arr[0] == 'def':

                    args = ""
                    flag = False
                    for char in line:
                        if char == ')':
                            flag = False
                        if char == '(':
                            flag = True
                        if flag:
                            args += char

                    args_arr = args.split(',')
                    counter = len(args_arr)
                    dic[line] = counter

        return dic

    def Number_of_public_methods(self, file):
        counter = 0
        with open("data/"+file, "r") as file:

            for line in file:
                arr = line.split()
                if len(arr) < 2:
                    continue
                if arr[0] == 'def':
                    if arr[1][:2] != '__':
                        counter += 1

        return counter

    def Number_of_fields(self, file):
        counter = 0
        with open("data/"+file, "r") as file:

            flag = False

            for line in file:
                arr = line.split()
                if len(arr) < 2:
                    continue

                if arr[1].find('__init__') != -1:
                    flag = True
                    continue

                if flag:
                    if line.find("self.") != -1:
                        counter += 1

                    else:
                        flag = False

        return counter

    def get_WMC(self, file):
        dict = {"Phone": 5, "Mobile Phone": 8, "Iphone": 3, "Ïphone6": 2,
                "Iphone7": 2, "Samsung": 3, "SamsungGalaxyS8": 2}
        return dict


    def get_LOC(self, file):
        method = Metrics_defined().LOC_metrics(file)
        LOC = method[1].split(":")
        return int(LOC[1])


    def get_SLOC(self, file):
        method = Metrics_defined().LOC_metrics(file)
        SLOC = method[2].split(":")
        return int(SLOC[1])

    def get_NOML(self, file):
        with open("data/"+file, "r") as file:
            def space_ccount(line): return len(line)-len(line.lstrip(' '))
            methods = {}
            class_ = ''
            line_num = 0
            list = []
            def_start = False

            for line in file:
                line_num += 1

                #get current class
                if 'class ' in line:
                    class_ = line.split('class')[1][1:-2].strip()

                # get method bodies
                tab = 0
                if 'def' in line:
                    new_line = line_num
                    tab = space_ccount(line)
                    def_start = True
                    method_name = line.split('(')[0].split('def')[1][1:]
                    list = []
        
                elif def_start and space_ccount(line) >= tab+4:
                    
                    list.append(line.strip(' '))

                    methods[method_name] = {
                    'body': list,
                    'line': str(new_line),
                    'class_':  class_
                    }

                else:
                    def_start = False
        return methods

    def find_parent(self, c, file):
        
        cleanpath = os.path.abspath("data/"+file)
        datafile = open(cleanpath, 'r')

        imports = []
        classes = []

        for line in datafile:
            if 'import' in line:
                for x in line.split('import')[1].split(','):
                    imports.append(x.strip())

            if 'class ' in line:
                classes.append(line.split('class')[1][1:-2].strip())
        if '(' not in c:
            return ''

        s = c[c.find("(")+1:c.find(")")].split(',')
        s = s[0]
        parent = ''
        flag = True
        for x in imports:
            if s == x:
                parent = x
                flag = False
                break
        if flag:
            for x in classes:
                if s in x:
                    parent = x
                    break
        return s + ' ' + Metrics_defined().find_parent(parent, file)


    def get_aid(self, file):
        with open("data/"+file, "r") as file:
            class_ = ''
            imports = []
            dict = {}
            flag = False
            counter = 0

            for line in file:

                if 'import' in line:
                    for x in line.split('import')[1].split(','):
                        imports.append(x.strip())

                if 'class ' in line:
                    class_ = line.split('class')[1][1:-2].strip()


                if line.find('__init__') != -1:
                    flag = True
                    continue

                if flag:
                    if line.find("self.") != -1:
                        word = line.split()
                        for x in imports:
                            for y in word:
                                if y.find(x) != -1:
                                    counter += 1
                                    dict[class_] = {
                                    'AID': counter
                                    }

                else:
                    flag = False                

        return dict

    def get_ald(self, file):
        with open("data/"+file, "r") as file:
            class_ = ''
            imports = []
            dict = {}
            flag = False
            counter = 0

            for line in file:

                if 'import' in line:
                    for x in line.split('import')[1].split(','):
                        imports.append(x.strip())

                if 'class ' in line:
                    class_ = line.split('class')[1][1:-2].strip()


                if line.find('__init__') != -1:
                    flag = True
                    continue

                elif flag:
                    if line.find("self.") != -1:
                        word = line.split()
                        # for x in word:
                            # print(x)
                        
                        for y in word:
                            for x in imports:
                                print(y)
                                if y != x:
                                    counter += 1
                                    dict[class_] = {
                                    'AID': counter
                                    }
                            else:
                                counter = 0
                    else:
                        flag = False

        return dict


    def dit_list(self, c, file):
        array = []
        whole_array = Metrics_defined().find_parent(c, file)
        for i in whole_array.split(' '):
            array.append(i)
        return ' '.join(array).split()


    def Number_of_parameters(self, file):
        counter = 0
        line_num = 0
        main_dict = {}
        class_ = ''
        with open("data/"+file, "r") as file:

            for line in file:
                
                line_num += 1
                if 'class ' in line:
                    class_ = line.split('class')[1][1:-2].strip()
                arr = line.split()
                if len(arr) < 2:
                    continue
                if arr[0] == 'def':
                    
                    new_line = line_num
                    method_name = line.split('(')[0].split('def')[1][1:]
                    args = ""
                    flag = False
                    for char in line:
                        if char == ')':
                            flag = False
                        if char == '(':
                            flag = True
                        if flag:
                            args += char
                        else:
                            args_arr = args.split(',')
                            counter = len(args_arr)
                            main_dict[method_name] = {
                            'parameters': counter,
                            'line': str(new_line),
                            'class_':  class_
                            }

        return main_dict

    def Number_of_SUP (self, file):
        counter = 0
        line_num = 0
        main_dict = {}
        class_ = ''
        with open("data/"+file, "r") as file:

            for line in file:
                
                line_num += 1
                if 'class ' in line:
                    new_line = line_num
                    class_ = line.split('class')[1][1:-2].strip()
                    args = ""
                    flag = False
                    for char in line:
                        if char == ')':
                            flag = False
                        if char == '(':
                            flag = True
                        if flag:
                            args += char
                        else:
                            args_arr = args.split(',')
                            counter = len(args_arr)
                            main_dict[class_] = {
                            'SUP': counter,
                            'line_number': str(new_line),
                            }

        return main_dict


    def Number_of_accessors(self,file):
        counter = 0
        dic = {}
        with open("data/"+file, "r") as file:
            
            class_name = ''
            previous_name = ''
            for line in file:
                if 'class ' in line:
                    previous_name = class_name
                    dic[previous_name] = counter
                    class_name = line.split('class')[1][1:-2].strip()
                    counter = 0
                if 'def ' in line:
                    method_name = line.split('def')[1][1:-2].strip()
                    if method_name[0:4] == 'get_':
                        counter += 1

        if '' in dic:
            del dic['']

        return dic

    def get_LOC_class(self,file):

        counter = 0
        main_dic = {}
        class_ = ''
        line_num = 0
        new_line = ''
        
        with open("data/"+file, "r") as file:
            
            for line in file:
                line_num += 1
                if 'class ' in line:
                    new_line = line_num
                    class_ = line.split('class')[1][1:-2].strip()
                    counter = 0

                elif not line.strip():
                    continue
                else:
                    counter += 1
                    main_dic[class_] = {
                        'line_number': str(new_line),
                        'value':  counter
                    }

        if '' in main_dic:
            del main_dic['']

        return main_dic


    def get_AID(self,file):
        counter = 0
        dic = {}
        with open("data/"+file, "r") as file:
            
            class_name = ''
            previous_name = ''
            for line in file:
                if 'class ' in line:
                    previous_name = class_name
                    dic[previous_name] = counter
                    class_name = line.split('class')[1][1:-2].strip()
                    counter = 0
                for word in line.split():
                    if isinstance(word, type(class_name)):
                        counter += 1

        if '' in dic:
            del dic['']

        return dic
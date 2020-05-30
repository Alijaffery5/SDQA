import sys

from astroid import Attribute
from astroid import ClassDef
from astroid import FunctionDef
from astroid import Name
from astroid import parse
from itertools import permutations

class parseCode:
  
    def is_method(self,element):
        """
        Determines whether a given element is a method. Excludes __init__ and any
        @property methods.
        :param astroid.node_classes.Attribute element: the element to check
        :return: True if the element is a method and interesting; False otherwise
        :rtype : bool
        """
        return (
                isinstance(element, FunctionDef)
                and element.name != '__init__'
                
                and '__builtin__.property' not in element.decoratornames()
        )


    def is_variable_reference(self,element):
        """
        Checks if the element is a reference to an instance variable.
        :param astroid.node_classes.Attribute element: the element to check
        :return: True if the element is a reference to an instance variable, False
        otherwise
        :rtype : bool
        """
        return isinstance(element.expr, Name) and element.expr.name == 'self'


    def find_attributes(self,element):
        """
        Recursively traverse the AST, finding all references to instance variables.
        :param astroid.node_classes.NodeNG element: a root node to start at
        :return: the set of instance variables
        :rtype : set[str]
        """
        if isinstance(element, Attribute) and self.is_variable_reference(element):
            return {element.attrname}

        return {
            element for child in element.get_children()
            for element in self.find_attributes(child)
        }


    def analyze(self,definition):
        """
        Given a class definition, calculate the LCOM value for the class.
        :param astroid.scoped_nodes.ClassDef definition: the class definition
        :return: the LCOM value of the class. Higher is worse.
        """
        methods = [
            child for child in definition.get_children()
            if self.is_method(child)
        ]
        method_references = [self.find_attributes(method) for method in methods]

        return max(
            0,
            sum(
                -1 if left.intersection(right) else 1
                for left, right in permutations(method_references, r=2)
            )
        )


    def find_classes(self,ast):
        """
        Given a module syntax tree, find all of the class definition nodes.
        :param astroid.nodes.Module ast: the module source tree to examine
        :return: a dictionary of class names to the definition nodes
        :rtype : dict[str, astroid.scoped_nodes.ClassDef]
        """
        return {
            class_name: definitions[0]
            for class_name, definitions in ast.globals.items()
            if any(isinstance(definition, ClassDef) for definition in definitions)
        }

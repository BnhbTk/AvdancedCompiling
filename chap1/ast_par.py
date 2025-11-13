# This import allows to use the special class ABC (intended as a base class
# for all abstract classes)
from abc import ABC

# This import is used to declare the type of the arguments of the constructor
# of PR
from typing import Tuple



# The base class
class Node(ABC):
    pass

    def __str__(self)->str:
        return ""


class Symbol(Node):
    """This class represents a simple symbol in the AST
    """
    
    def __init__(self,c:str):
        """This constructor builds a symbol node. It takes the symbol as an argument

        Args:
            c (str): the symbol to be stored in the node
        """
        self.c:str=c
    
    def __str__(self)->str:
        """This methods returns a string representation of the node (in this case,
        it is just the symbol itself)

        Returns:
            str: the string description of the object
        """
        return self.c
    


class PR(Node):
    """This class represent a pair of parentheses and the content inside. The content
    is stored as children of this node
    """
    def __init__(self,*nodes:Tuple[Node]):
        """This constructor builds the PR node. It takes its children (as varargs) as argument (notice
        the use of Tuple in type hints)
        Args:
            *nodes (Tuple[Node]): a varargs argument representing the children of this node
        """
        self.children=nodes
    
    def __str__(self)->str:
        """This methods returns a string representation of this node. It consist of "("
        followed by the string representations of its children (separated by commas) and a final ")". In fact,
        this function is recursive

        Returns:
            str: The string representation of this node
        """
        return f'PR({",".join([str(ch) for ch in self.children])})'



if __name__=="__main__":
    node:Node=PR(Symbol("a"),PR(Symbol("b"),Symbol("c"))) # This represents the word (a(bc))
    print(node)

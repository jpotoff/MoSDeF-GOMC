__author__ = 'sallai'

from copy import copy, deepcopy
from warnings import warn

class Bond(object):
    __slots__ = ['atom1','atom2']

    def __init__(self, atom1, atom2):
        assert(not atom1 == atom2)
        self.atom1 = atom1
        self.atom2 = atom2

    def __hash__(self):
        return id(self.atom1) ^ id(self.atom2) 

    def __eq__(self, bond):
        return isinstance(bond, Bond) and (self.atom1 == bond.atom1 and self.atom2 == bond.atom2
             or self.atom2 == bond.atom1 and self.atom1 == bond.atom1)

    def __repr__(self):
        return "Bond{0}({1}, {2})".format(id(self), self.atom1, self.atom2)

    def __deepcopy__(self, memo):
        cls = self.__class__
        newone = cls.__new__(cls)
        memo[id(self)] = newone

        newone.atom1 = deepcopy(self.atom1, memo)
        newone.atom2 = deepcopy(self.atom2, memo)
        return newone


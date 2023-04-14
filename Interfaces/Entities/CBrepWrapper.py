# Author : Michael Brunner
# Date : 2023-04-14
# Description : Wrapper for the CBrep class

from typing import List
import geometry_controller as gc
from CFacetWrapper import CFacetWrapper
from Interfaces import IFacetWrapper
from Interfaces.IBrepWrapper import IBrepWrapper


class CBrepWrapper(IBrepWrapper):
    def __init__(self, element_id: int):
        if len(str(abs(element_id))) < 6:
            raise ValueError("Element ID must be positive")
        self.element_id = element_id
        self.facets: List[IFacetWrapper] = list()

        self.__set_facets()

    # public methods
    def get_brep_faces(self):
        return gc.get_element_facets(self.element_id)

    def get_brep_edges(self):
        pass

    def get_brep_vertices(self):
        return gc.get_element_vertices(self.element_id)

    # def get_brep_shells(self):
    #     return self.brep.shells

    # private methods
    def __set_facets(self):
        l_facets = gc.get_element_facets(self.element_id)
        for il in range(0, len(l_facets)):
            self.facets.append(CFacetWrapper(il, l_facets[il]))

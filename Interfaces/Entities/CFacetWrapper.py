# Author : Michael Brunner
# Date : 2023-04-14
# Description : Wrapper for the CBrep class
from typing import List

import cadwork

from Interfaces.IFacetWrapper import IFacetWrapper


class CFacetWrapper(IFacetWrapper):
    def __init__(self, facet_number: int, facet: List[cadwork.point_3d]):
        if facet_number < 0:
            raise ValueError("Facet number must be positive")
        self.facet_nr = facet_number
        self.facet = facet

    # public methods
    def get_facet_edges(self):
        pass

    def get_facet_vertices(self):
        pass

    def get_facet_normal(self):
        pass

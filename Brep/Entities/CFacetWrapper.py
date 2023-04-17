# Author : Michael Brunner
# Date : 2023-04-14
# Description : Wrapper for the CBrep class

from Brep.Interfaces.IFacet import IFacet


class CFacetWrapper(IFacet):
    def __init__(self, facet_number: int, facet):  # : List[cadwork.point_3d]
        if facet_number < 0:
            raise ValueError("Facet number must be positive")
        self.facet_nr = facet_number
        self.facet = facet

    # public methods
    def get_facet_vertices(self):
        pass

    def get_facet_normal(self):
        pass

    def get_external_polygon(self):
        pass

    def get_internal_polygon(self):
        pass

    def get_distance_to_origin(self):
        pass

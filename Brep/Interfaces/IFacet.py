# Author : Michael Brunner
# Date : 2023-04-14
# Description : Wrapper for the IBrep class

from abc import ABC, abstractmethod


class IFacet(ABC):

    @abstractmethod
    def get_external_polygon(self):
        pass

    @abstractmethod
    def get_internal_polygon(self):
        pass

    @abstractmethod
    def get_facet_vertices(self):
        pass

    @abstractmethod
    def get_facet_normal(self):
        pass

    @abstractmethod
    def get_distance_to_origin(self):
        pass

# Author : Michael Brunner
# Date : 2023-04-14
# Description : Wrapper for the IBrep class

from abc import ABC, abstractmethod


class IFacetWrapper(ABC):

    @abstractmethod
    def get_facet_edges(self):
        pass

    @abstractmethod
    def get_facet_vertices(self):
        pass

    @abstractmethod
    def get_facet_normal(self):
        pass

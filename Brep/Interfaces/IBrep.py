# Author : Michael Brunner
# Date : 2023-04-14
# Description : Wrapper for the IBrep class

from abc import ABC, abstractmethod


class IBrep(ABC):

    @abstractmethod
    def get_brep_faces(self):
        pass

    @abstractmethod
    def get_brep_edges(self):
        pass

    @abstractmethod
    def get_brep_vertices(self):
        pass

    # @abstractmethod
    # def get_brep_shells(self):
    #     pass

import unittest
from typing import List

from Interfaces.IBrepWrapper import IBrepWrapper
from Interfaces.IFacetWrapper import IFacetWrapper


class Cpoint3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class CFacetTestWrapper(IFacetWrapper):
    def __init__(self, facet_number: int, facet: List[Cpoint3d]):
        self.facet_nr = facet_number
        self.facet = facet

    def get_facet_edges(self):
        pass

    def get_facet_vertices(self):
        pass

    def get_facet_normal(self):
        pass


class CBrepTestWrapper(IBrepWrapper):
    def __init__(self, element_id: int):
        if len(str(abs(element_id))) < 6:
            raise ValueError("Element ID must be positive")
        self.element_id = element_id
        self.facets: List[IFacetWrapper] = list()

        self.__set_facets()

    def get_brep_faces(self) -> List[IFacetWrapper]:
        return self.facets

    def get_brep_edges(self):
        pass

    def get_brep_vertices(self):
        pass

    def __set_facets(self):
        l_facets = [[Cpoint3d(0, 0, 0), Cpoint3d(1, 0, 0), Cpoint3d(0, 1, 0), Cpoint3d(0, 1, 0)],
                    [Cpoint3d(0, 0, 0), Cpoint3d(0, 1, 0), Cpoint3d(0, 0, 1)]]
        for il in range(0, len(l_facets)):
            self.facets.append(CFacetTestWrapper(il, l_facets[il]))
            print(f"facet {il} has {len(l_facets[il])} vertices")


class MyTestCase(unittest.TestCase):
    def test_faces_count(self):
        element_id = 123456
        brep = CBrepTestWrapper(element_id)

        self.assertEqual(len(brep.get_brep_faces()), 2)  # add assertion here

    def test_exception(self):
        element_id = 12345
        with self.assertRaises(ValueError):
            brep = CBrepTestWrapper(element_id)


if __name__ == '__main__':
    unittest.main()

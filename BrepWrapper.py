# Author : Michael Brunner
# Date : 2023-04-14
# Description : Wrapper for the CBrep class

import sys

import element_controller as ec
import utility_controller as uc

print(sys.version_info)
print(sys.executable)
for p in sys.path:
    print(p)

plugin_path = uc.get_plugin_path()
print(plugin_path)

cwps = [
    plugin_path + '\\Brep',
    plugin_path + '\\Test',
]
[(sys.path.append(cwp), print(f"appending to path: {cwp}")) for cwp in cwps if cwp]

from Brep.Entities.CBrepWrapper import CBrepWrapper
from Brep.Interfaces.IBrep import IBrep
import Test

if __name__ == '__main__':
    print(IBrep.__dict__)
    print(Test.add_one(5))

    element_ids = ec.get_active_identifiable_element_ids()
    print(f"element_ids: {element_ids}")
    for element_id in element_ids:
        print(f"element_id: {element_id}")
        brep: IBrep = CBrepWrapper(element_id)
        print(brep.get_brep_vertices())

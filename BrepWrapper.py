# Author : Michael Brunner
# Date : 2023-04-14
# Description : Wrapper for the CBrep class

import sys
import element_controller as ec
import utility_controller as uc

plugin_path = uc.get_plugin_path()
sys.path.append(plugin_path)
sys.path.append(plugin_path + r'/Interfaces/')
sys.path.append(plugin_path + r'/Interfaces/Entities/')

print(sys.version_info)
print(sys.executable)
for p in sys.path:
    print(p)

cwps = [
    plugin_path + r'/Interfaces/',
    plugin_path + r'/Interfaces/Entities/',
]
[(sys.path.append(cwp), print(f"appending to path: {cwp}")) for cwp in cwps if cwp]

from Interfaces.Entities.CBrepWrapper import CBrepWrapper
from Interfaces.IBrepWrapper import IBrepWrapper

if __name__ == '__main__':
    element_ids = ec.get_active_identifiable_element_ids()
    print(f"element_ids: {element_ids}")
    for element_id in element_ids:
        print(f"element_id: {element_id}")
        brep: IBrepWrapper = CBrepWrapper(element_id)
        print(brep.get_brep_vertices())

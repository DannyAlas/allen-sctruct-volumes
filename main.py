from allensdk.core.reference_space_cache import ReferenceSpaceCache
import sys

sys.tracebacklimit=0
# set up the cache and resolution
reference_space_key = 'annotation/ccf_2017'
resolution = 100
rspc = ReferenceSpaceCache(resolution, reference_space_key, manifest='manifest.json')
# set up the reference space
tree = rspc.get_structure_tree(structure_graph_id=1) 
rsp = rspc.get_reference_space()

def get_struct(val):
    """Get structure ID from name, acronym, or ID"""
    try:
        struct_id = rsp.structure_tree.get_structures_by_name([val])[0]['id']
    except:
        try:
            struct_id = rsp.structure_tree.get_structures_by_acronym([val])[0]['id']
        except:
            try:
                struct_id = rsp.structure_tree.get_structures_by_id([val])[0]['id']
            except:
                pass
    return struct_id

def struct_vol(struct_id):
    """Get the volume of a structure from its ID"""
    return rsp.total_voxel_map[struct_id] / 1000

def struct_name(struct_id):
    """Get the name of a structure from its ID"""
    return rsp.structure_tree.get_structures_by_id([struct_id])[0]['name']

def main():
    while True:
        struct = input("Enter structure by Name, Acronym, or ID: ")
        try:
            volume = struct_vol(get_struct(struct))
            name = struct_name(get_struct(struct))
            print(f"The volume of {name} is {volume}mm\u00b3")
        except:
            print('Try another Name, Acronym, or ID')

if __name__ == '__main__':
    main()

import bpy
import json
import os

def find_auto_spline_object():
    print("Searching for object with custom property 'auto_spline' set to 't'...")
    for obj in bpy.context.scene.objects:
        if 'auto_spline' in obj:
            print(f"Object '{obj.name}' has custom property 'auto_spline' with value: {obj['auto_spline']}")
        if obj.get('auto_spline', "") == "t":
            print(f"Found object: {obj.name}")
            return obj
    print("No object with custom property 'auto_spline' set to 't' found.")
    return None

def export_vertex_group_data(obj):
    print(f"Exporting vertex group data for object: {obj.name}")

    # Ensure we're in object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Get the evaluated mesh with all modifiers applied
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval = obj.evaluated_get(depsgraph)
    mesh_eval = bpy.data.meshes.new_from_object(obj_eval)

    # Extract vertex groups
    vertex_groups = {vg.index: vg.name for vg in obj.vertex_groups}
    print(f"Vertex groups found: {list(vertex_groups.values())}")

    # Initialize data structure
    vertex_data = {group_name: [] for group_name in vertex_groups.values()}

    # Get the transformation matrix to convert local to global coordinates
    matrix_world = obj.matrix_world

    # Iterate through all vertices
    for vertex in mesh_eval.vertices:
        global_vertex = matrix_world @ vertex.co  # Convert to global coordinates
        for group in vertex.groups:
            group_name = vertex_groups[group.group]
            position = {"x": global_vertex.x, "y": global_vertex.y, "z": global_vertex.z}
            if group_name in vertex_data:
                vertex_data[group_name].append(position)

    # Define output directory
    output_dir = bpy.path.abspath("//gen/auto_spline/")
    os.makedirs(output_dir, exist_ok=True)

    # Write each vertex group to a separate JSON file
    for group_name, points in vertex_data.items():
        json_data = json.dumps(points, indent=4)
        output_file = os.path.join(output_dir, f"{group_name}_vertex_data.json")
        with open(output_file, 'w') as f:
            f.write(json_data)
        print(f"Vertex data for group '{group_name}' exported to {output_file}")

# Main execution
print("Starting script...")
auto_spline_obj = find_auto_spline_object()
if auto_spline_obj and auto_spline_obj.type == 'MESH':
    export_vertex_group_data(auto_spline_obj)
else:
    print("No suitable object found or the object is not a mesh.")
print("Script finished.")

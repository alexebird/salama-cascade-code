import bpy
import json

# Function to check if the curve has the custom property
def has_export_property(obj):
    return obj.get('export_curve', False)

# List to store the exported curves data
exported_curves = []

# Iterate through all objects in the scene
for obj in bpy.context.scene.objects:
    if obj.type == 'CURVE' and has_export_property(obj):
        curve_data = obj.data

        # Extract points from the Bezier curve
        points = []
        for spline in curve_data.splines:
            if spline.type == 'BEZIER':
                for point in spline.bezier_points:
                    # Extract control point coordinates
                    coord = {
                        # "handle_left": list(point.handle_left),
                        "pos": {"x": point.co.x, "y": point.co.y, "z": point.co.z},
                        #"handle_right": list(point.handle_right)
                    }
                    points.append(coord)

        # Store the curve data with object name
        curve_info = {
            "name": obj.name,
            "points": points
        }
        exported_curves.append(curve_info)

# Convert the curves data to JSON
json_data = json.dumps(exported_curves, indent=4)

# Define the output file path
output_file = bpy.path.abspath("//bezier_curves.json")

# Write the JSON data to a file
with open(output_file, 'w') as f:
    f.write(json_data)

print(f"Bezier curves with custom property exported to {output_file}")

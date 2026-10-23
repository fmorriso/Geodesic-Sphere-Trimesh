import trimesh

# Create a sample 3D box programmatically (no external files needed)
box = trimesh.creation.box(extents=[2.0, 3.0, 4.0])

print("--- Trimesh Installation Test ---")
print(f"Successfully loaded Trimesh version: {trimesh.__version__}")
print(f"Is the box watertight? {box.is_watertight}")
print(f"Box volume: {box.volume:.2f}")
print(f"Number of vertices: {len(box.vertices)}")
print(f"Number of faces: {len(box.faces)}")

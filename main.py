import os
import sys

import pyautogui
import trimesh
from dotenv import load_dotenv


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def get_scale_factor() -> float:
    load_dotenv()
    scale_value = float(os.getenv("SCALE_FACTOR","50.0"))
    scale_value = max(1.0, min(100,0, scale_value))
    return scale_value

# Press the green button in the gutter to run the script.
def main(scale_value: float) -> None:
    # 2. Generate a sphere using trimesh, scaled dynamically
    base_radius = 5.0
    scaled_radius = base_radius * (scale_value / 10.0)  # adjusting radius proportionally
    sphere = trimesh.creation.icosphere(subdivision=2, radius=scaled_radius)

    # Extract geometric properties
    num_vertices = len(sphere.vertices)
    num_triangles = len(sphere.faces)
    wireframe_edges = len(sphere.edges)

    print("=== 3D Hollow Wireframe Sphere Report ===")
    print(f"Environment SCALE percentage: {scale_value}%")
    print(f"Computed Radius: {scaled_radius}")
    print(f"Number of Vertices: {num_vertices}")
    print(f"Number of Triangles (Faces): {num_triangles}")
    print(f"Number of Wireframe Edges: {wireframe_edges}")

    # 3. Dynamic Centered PyAutoGUI Screenshot
    print("\n[PyAutoGUI] Calculating centered capture region...")
    pyautogui.PAUSE = 0.5

    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()
    print(f"Detected Screen Resolution: {screen_width}x{screen_height}")

    # Determine the smallest dimension (handles portrait vs. landscape automatically)
    min_dimension = min(screen_width, screen_height)

    # Calculate region size as a percentage of the smallest dimension
    region_size = int(min_dimension * (scale_value / 100.0))

    # Calculate top-left coordinates to center the region on the screen
    left = (screen_width - region_size) // 2
    top = (screen_height - region_size) // 2

    # Define the dynamic centered region: (left, top, width, height)
    capture_region = (left, top, region_size, region_size)
    print(f"Capture Region (Left, Top, Width, Height): {capture_region}")

    # Take and save the screenshot
    screenshot = pyautogui.screenshot(region=capture_region)
    output_filename = f"sphere_scale_{int(scale_value)}pct_snapshot.png"
    screenshot.save(output_filename)
    print(f"[PyAutoGUI] Snapshot saved successfully as '{output_filename}'.")

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    scale_factor = get_scale_factor()
    print(f'Scale factor: {scale_factor:.1f}')
    main(scale_factor)

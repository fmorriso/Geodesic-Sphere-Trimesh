import os
import sys

from dotenv import load_dotenv


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def get_scale_factor() -> float:
    load_dotenv()
    scale_value = float(os.getenv("SCALE_FACTOR"))
    return scale_value

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'Scale factor: {get_scale_factor()}')

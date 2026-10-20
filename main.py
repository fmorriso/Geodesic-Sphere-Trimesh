# This is a sample Python script.
import sys


# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

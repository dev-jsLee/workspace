import os
import sys
day07 = os.path.dirname(__file__)
root_folder_path = os.path.dirname(day07)
root_folder_name = os.path.basename(root_folder_path)
print(f"root_folder_name: {root_folder_name}")
sys.path.append(root_folder_path)

from import_test import specific_var
print(specific_var)
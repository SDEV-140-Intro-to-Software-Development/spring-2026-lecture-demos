import os

path = os.path.join("C:\\", "Users", "esexton", "Destop")

print(f"split={os.path.split(path)}")
print(f"sep={os.path.sep}")
print(f"split on sep={path.split(os.path.sep)}")
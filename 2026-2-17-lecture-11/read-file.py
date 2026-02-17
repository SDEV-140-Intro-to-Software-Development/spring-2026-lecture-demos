import os
f = open(os.path.join("2026-2-17-lecture-11", "hello-world.txt"))
content = f.read()
f.close()
print(content)
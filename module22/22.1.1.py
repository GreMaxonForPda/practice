import os

folder = "access"
filename = "admins.bat"

path = os.path.join(folder, filename)
abs_path = os.path.abspath(os.path.join('..', folder, filename))

print(path)
print(abs_path)

import os

print(os.path.basename(os.getcwd()))
parent_folder = os.path.dirname(os.getcwd())
for root, dirs, files in os.walk(parent_folder):
    if not files:
        continue
    #prefix = os.path.basename(root)
    for f in files:
        print(f)
        #os.rename(os.path.join(root, f), os.path.join(root, "{}_{}".format(prefix, f)))
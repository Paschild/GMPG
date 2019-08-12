import os

os.chdir("/Users/mzichert/Documents/Institute")
for root, dirs, files in os.walk(".", topdown=True):
    for name in files:          # gibt Dateinamen aus
        if name.endswith(".xlsx"):
            print(os.path.join("/Users/mzichert/Documents/Institute"), name)
    for name in dirs:           # gibt Ordernamen aus
        #print(os.path.join(root, name))
        pass

'''for file in os.listdir("/Users/mzichert/Documents/Institute"):
    if file.endswith(".xlsx"):
        print(os.path.join("/Users/mzichert/Documents/Institute"), file)'''

import os, os.path

fileNameX = "../xData"
cutOffPoint=1524

print("=====================|start|=====================")
for root, _, files in os.walk(fileNameX):
    for f in files:
        fullpath = os.path.join(root, f)
        print('11-os.path.getsize(fullpath)==>',os.path.getsize(fullpath))
        print("12-limiterse by myself===========>",cutOffPoint)
        try:
            if os.path.getsize(fullpath) < cutOffPoint:#  Limit
                print(fullpath)
                print('21-os.path.getsize(fullpath)=====>',os.path.getsize(fullpath))
                print("22-limiterse by myself===========>",cutOffPoint)
                os.remove(fullpath)
        except WindowsError:
            print ("Error" + fullpath)

print("===================|Clearning_End|==================")
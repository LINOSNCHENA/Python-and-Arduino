import os, os.path

fileNameX = "../xData"
cutOffPoint=1524
print(os.path.getsize(fileNameX))
fileName2=(os.path.getsize(fileNameX))
cleanXOut=int(fileName2*2/100)
# cleanXOut

print("===============|start_deleting_smaller_files|=====================")

for root, _, files in os.walk(fileNameX):
    for f in files:
        fullpath = os.path.join(root, f)
        print('11-os.path.getsize(fullpath)==>',os.path.getsize(fullpath))
        print("12-limiterse by myself===========>",cutOffPoint)
        print("13-limiterse by myself===========>",fileName2)
        print("14-limiterse by Percntage========>",cleanXOut)
        try:
            if os.path.getsize(fullpath) < cleanXOut:#  Limit
                print(fullpath)
                print('21-os.path.getsize(fullpath)=====>',os.path.getsize(fullpath))
                print("22-limiterse by myself===========>",cutOffPoint)
                print("23-limiterse by myself===========>",fileName2)
                print("24-limiterse by myself===========>",cutOffPoint/fileName2)
                os.remove(fullpath)
        except WindowsError:
            print ("Error" + fullpath)

print("============================|Clearning_End|=========================")
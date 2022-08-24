import os
import os.path

fileNameX = "../xData"
print(os.path.getsize(fileNameX))
fileSizeX = (os.path.getsize(fileNameX))
fileMinX = int(fileSizeX*(3/100))

print("===============|start_deleting_smaller_files|=====================")
count = 0
for path in os.listdir(fileNameX):
    if os.path.isfile(os.path.join(fileNameX, path)):
        count += 1
print('A-File count:', count)

for root, _, files in os.walk(fileNameX):
    for f in files:
        fullpath = os.path.join(root, f)
        print('11-os.path.getsize(fullpath)==>', os.path.getsize(fullpath))
        print("12-Total-File-Size============>", fileSizeX, "KB")
        print("13-Percentage-of-total-size===>", fileMinX, "-| on 3%")
        try:
            if os.path.getsize(fullpath) < fileMinX:  # Limit
                print(fullpath)
                print('21-os.path.getsize(f)==>',os.path.getsize(fullpath))
                print("22-Total-File-Size=====>", fileSizeX, "KB")
                print("23-Percent-total-size==>", fileMinX, "-| on 3%")
                os.remove(fullpath)
        except WindowsError:
            print("Error" + fullpath)

count = 0
for path in os.listdir(fileNameX):
    # check if current path is a file
    if os.path.isfile(os.path.join(fileNameX, path)):
        count += 1
print('B-File count:', count)
print("============================|Clearning_End|=========================")

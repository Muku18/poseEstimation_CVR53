import os

folder_path = 'C:\\Users\\mukesh kumar\\Desktop\\coordinates\\Labels'

# List all the files in the folder
files = os.listdir(folder_path)

satx = []
saty = []

portx = []
porty = []

# Iterate over each file and read its contents
for filename in files:
    # Create the full file path by joining the folder path and the filename
    file_path = os.path.join(folder_path, filename)
    # Check if the file is a regular file (i.e., not a directory or other special file)
    filecount = 0
    if os.path.isfile(file_path):
        # Open the file for reading
        if filecount == 2:
            with open(file_path, 'r') as file:
            # Read all the lines in the file and print them
                count = 0
                for line in file:
                    if count == 1:
                        break
                    s = line.split(" ")
                    xofsat = float(s[1])*34.3
                    wofsat = float(s[3])*34.3
                    yofsat = float(s[2])*19.2
                    hofsat = float(s[4])*19.2
                    satx.append(xofsat)
                    saty.append(yofsat)
                    count = count + 1
print(satx)
print(saty)

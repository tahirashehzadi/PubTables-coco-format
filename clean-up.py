# written by: Matthew Howlett
# date: September 24, 2019
# python script for editing text files_in

files_in = ['check.txt']
files_out = ['check1.txt']



# clean up file format
for i in range(len(files_in)):
    with open(files_in[i], 'r') as file_in, \
         open(files_out[i], 'w') as file_out:
            data = file_in.read()
            data = data.replace("_", "")
            data = data.replace("PMC", "")
            data = data.replace(".", "")
            data = data.replace("xml", "")
            data = data.replace("val/", "")
            data = data.replace("XML", "\t")
            file_out.write(data)

# import os

# directory = 'C:/Users/Matt/OneDrive/Documents/Kettering/courses/summer-2019/ce-senior-design/creating-kitti-datasets/cocosynth-master/datasets/cards/KITTI/test/images/'

# for filename in os.listdir(directory):
#     if filename.endswith(".xml"): 
#          os.remove(directory + filename)
#     else:
#         continue

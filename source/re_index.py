import os 
import cv2 

def slicing_index(folder_path): 
    ## Adding image path & label path
    image_path = folder_path + "\images"
    label_path = os.path.join(folder_path, "labels")

    ## Check the image file's name
    for filename in os.listdir(image_path):
        if filename.endswith('.jpg'):

            ## Create label file's name 
            label = os.path.join(label_path, filename.replace('.jpg','.txt'))

            ## If label exists, read the label content 
            if os.path.exists(label):
                with open(label, 'r') as f:
                    lines = f.readlines()
                
                ## Modify the label content
                modified_lines = []
                for line in lines: 
                    values= line.strip().split()

                    if int(values[0]) > 12: 
                        values[0] = '12'
                    modified_line = ' '.join(values) + '\n'
                    modified_lines.append(modified_line)
    
    
                with open(label, 'w') as f:
                    f.writelines(modified_lines)
                
                print(f"Modified label file: {label}")
    
                        

                
folder_path = r'D:\pleizsonoob\Others\\bfmc\dataset\obdet_v25_1\\valid'

slicing_index(folder_path)


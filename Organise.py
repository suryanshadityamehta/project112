import os
import shutil


from_dir= "C:\Users\hp\Downloads\images"
to_dir="C:\Users\hp\Desktop\suryansh"


list_of_files = os.listdir(from_dir)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif','.txt', '.doc', '.docx', '.pdf']:

        path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Document_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   # Example path3 : D:/My Files/Image_Files/ImageName1.jpg
 
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)


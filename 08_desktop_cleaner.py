import os
import shutil
#https://youtu.be/4TZ1K8EHT2M

def create_subfolder_if_needed(folder_path,subfolder_name):
    #join the subfolder name with the path
    subfolder_path = os.path.join(folder_path,subfolder_name)
    #if the path does not exist, then it will create it
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path


def clean_folder(folder_path):

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path,filename)):
            #print all the files in the folder
            #print((os.path.join(folder_path,filename)))


            #get the file extension
            #normally split(), has a default that will split everything into a list
            # by using [-1], you are indicating to get the last word of the list, i.e extension
            #https://www.geeksforgeeks.org/python-string-split/
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                #create a folder for each extension
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path,subfolder_name)
                file_path = os.path.join(folder_path,filename)
                new_location = os.path.join(subfolder_path,filename)
                #Check if the file already exists in the sub folder
                if not os.path.exists(new_location):
                    shutil.move(file_path,subfolder_path)
                    print(f"Moved {filename} -> {subfolder_name}/")
                else:
                    print(f"Skipped: {filename} already exists in {subfolder_name}/")





if __name__ == '__main__':
    print('Desktop Cleaner Script')
    folder_path ='/home/edanebarton/Downloads/test/'
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print('Cleaning complete.')
    else:
        print('Invalid folder path. Please ensure the path is correct and try again.')
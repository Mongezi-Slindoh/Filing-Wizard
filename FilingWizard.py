"""
Filing Wizard
BhunganeDev
30 March 2024
"""

import os
import shutil

#------------------------------------------------------First Segment-------------------------------------------------------------------

#Decoy directories
downloads_dir = os.path.join(os.path.expanduser('~'), "Downloads")
dl_imgs_dir = os.path.join(os.path.expanduser('~'), "Downloads/Images")
dl_vids_dir = os.path.join(os.path.expanduser('~'), "Downloads/Videos")
dl_music_dir = os.path.join(os.path.expanduser('~'), 'Downloads/Music')
dl_pe_dir = os.path.join(os.path.expanduser('~'), 'Downloads/Programs')
dl_docs_dir = os.path.join(os.path.expanduser('~'), "Downloads/Documents")
dl_other_dir = os.path.join(os.path.expanduser('~'), "Downloads/Other")

#-----------------------------------------------------Second Segment-------------------------------------------------------------------

#Creating new folders if they are not there
if os.path.exists(dl_imgs_dir):                           #Check if folder for images exist. 
    pass
else:                                                       #If not, create new Images folder.
    os.mkdir(dl_imgs_dir)

if os.path.exists(dl_vids_dir):                           #Check if folder for Videos exist.
    pass
else:                                                       #If not, create new Videos folder.
    os.mkdir(dl_vids_dir)

if os.path.exists(dl_music_dir):                            #Check if folder for Music exist.
    pass
else:                                                       #If not, create new Music folder.
    os.mkdir(dl_music_dir)

if os.path.exists(dl_music_dir):                            #Check if folder for Windows PE files exist.
    pass
else:                                                       #If not, create new Windows PE files folder.
    os.mkdir(dl_music_dir)

if os.path.exists(dl_docs_dir):                             #Check if folder for Documents exist.
    pass
else:                                                       #If not, create new Documents folder.
    os.mkdir(dl_docs_dir)

if os.path.exists(dl_other_dir):                            #Check if folder for Others exist.
    pass
else:                                                       #If not, create new Others folder.
    os.mkdir(dl_other_dir)

#-------------------------------------------------------Third Segment-----------------------------------------------------------------

#Moving Files from Downloads to  Designated folders

for dir, sub_dir_list, file_list in os.walk(downloads_dir):                        #Looping through Downloads directory
    
    #Looping through files in directory
    for filename in file_list: 
        file_path = os.path.join(dir, filename)

        if ".jpg" in filename or ".png" in filename or ".jpeg" in filename:     
           if os.path.exists(os.path.join(dl_imgs_dir,filename)):                         #check if filename exists in the images destination
               pass 
           else:    
                shutil.move(file_path, dl_imgs_dir) 


        elif ".mov" in filename or ".mkv" in filename or ".mp4" in filename or ".avi" in filename:      
            if os.path.exists(os.path.join(dl_vids_dir,filename)):                        #check if filename exists in the videos destination
               pass 
            else:    
                shutil.move(file_path, dl_vids_dir) 
        
        elif ".mp3" in filename or ".wav" in filename:      
            if os.path.exists(os.path.join(dl_music_dir,filename)):                        #check if filename exists in the music destination
               pass 
            else:    
                shutil.move(file_path, dl_music_dir) 
        
        elif ".exe" in filename:      
            if os.path.exists(os.path.join(dl_music_dir,filename)):                        #check if filename exists in the music destination
               pass 
            else:    
                shutil.move(file_path, dl_music_dir) 


        elif ".pdf" in filename or ".doc" in filename or ".pptx" in filename or ".xlsx" in filename:       
            if os.path.exists(os.path.join(dl_docs_dir,filename)):                          #check if filename exists in the destination
               pass
            else:    
                shutil.move(file_path, dl_docs_dir) 


        else:
            if os.path.exists(os.path.join(dl_other_dir,filename)):                         #check if filename exists in the destination
               pass
            else:    
               shutil.move(file_path, dl_other_dir)

#------------------------------------------------------------Code End----------------------------------------------------------------

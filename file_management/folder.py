'''
    Folder management, i.e. creating/removing folders and updating reg.json,
    is performed here.
'''
import os

from flask_login import current_user


class FolderManager(object):
    '''
        Class for object management.
    '''
    base_url = "./static/servables/"
    shared_video = "./static/servables/vid/"
    shared_music = "./static/servables/music/"
    music_url = ""
    video_url = ""
    
    def __init__(self):
        self.base_url += current_user.username + "/"
        self.music_url = self.base_url + "music/"
        self.video_url = self.base_url + "video/"
        
    def __repr__(self):
        return "<Folder: {}>".format(self.base_url)
    
    def Get_urls(self):
        URLS = {
                "BASE": self.base_url,
                "SHARED MUSIC": self.shared_music,
                "SHARED VIDEO": self.shared_video
        }
        return URLS
    
    # Create
    def Create_personal_base(self):
        '''
            Creates the base personal folder for a user.
        '''
        try:
            os.makedirs(self.base_url, exist_ok=True)
            return True
        except Exception as e:
            print("Create error:",e)
        
        raise NotImplementedError
    
    def Add_personal_subfolder(self, name):
        raise NotImplementedError
    
    # Retrieve
    def Retrieve_folder_list(self):
        raise NotImplementedError
    
    # Remove
    def Remove_folder(self):
        raise NotImplementedError
from os import listdir
from os.path import isfile, join

class Helpers:
    """This class represents all helper functions that are used for backend
    """
    
    """ 
    Returns all files, excluding subdirectories, inside the specificed directory
    params:
        folder (str): folder to obtain file names from
    """
    @staticmethod
    def get_files_from_folder(folder: str):
        return [folder + f for f in listdir(folder) if isfile(join(folder,f))]

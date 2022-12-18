
import tarfile
import zipfile
import shutil

def extract_zip(path,directory):
  with zipfile.ZipFile(path) as f:
    f.extractall(directory)

def extract_targz(path,directory):
  with tarfile.open(path) as f:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(f, directory)

def extract(path,directory):

  """
    this function extract compressed folder 

    currently i implemented the gz and zip extension 

    there would be more extension when i need to .
  """
  extract_dict = {
    
    "gz" : extract_targz,

    "zip" : extract_zip
  }
  words = path.split('.')

  assert (words[-1] in extract_dict)
  extract_dict[words[-1]](path,directory)

extract('/content/yaser.zip','/content/hus')

def compress(current_path,new_path,extension):
  """
    this function is used to compress a folder on zip format .

    it takes 2 argument

    current_path : the path of the folder you want to express .

    new_path : the path of the compressed folder .

    extension : the extension of the compressed folder
  """
  shutil.make_archive(new_path,extension,current_path)



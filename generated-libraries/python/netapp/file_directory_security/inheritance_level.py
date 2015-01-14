class InheritanceLevel(basestring):
    """
    this-folder|sub-folders|files
    Possible values:
    <ul>
    <li> "this_folder"   ,
    <li> "sub_folders"   ,
    <li> "files"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "inheritance-level"
    

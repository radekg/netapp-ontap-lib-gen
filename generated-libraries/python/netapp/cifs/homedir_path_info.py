class HomedirPathInfo(basestring):
    """
    path to user home directory paths
    Unix style path to user home directories, example:
    /vol/vol1/users1
    The paths are listed in the same order that the
    filer will use to evaluate whether a user has a
    cifs home directory.
    """
    
    @staticmethod
    def get_api_name():
          return "homedir-path-info"
    

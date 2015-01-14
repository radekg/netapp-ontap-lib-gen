from netapp.netapp_object import NetAppObject

class SystemPathVersion(NetAppObject):
    """
    Image-path and image version for diagnostics and
    firmware files of the node
    """
    
    _version_info = None
    @property
    def version_info(self):
        """
        File version . Kernel and file versions
        Example: Firmware #.#.# or OS version
        """
        return self._version_info
    @version_info.setter
    def version_info(self, val):
        if val != None:
            self.validate('version_info', val)
        self._version_info = val
    
    _path_info = None
    @property
    def path_info(self):
        """
        File path  . Displays the file path in form /cfcard/x86_64/..
        """
        return self._path_info
    @path_info.setter
    def path_info(self, val):
        if val != None:
            self.validate('path_info', val)
        self._path_info = val
    
    @staticmethod
    def get_api_name():
          return "system-path-version"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'version-info',
            'path-info',
        ]
    
    def describe_properties(self):
        return {
            'version_info': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path_info': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

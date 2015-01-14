from netapp.netapp_object import NetAppObject

class CifsHomeDirectorySearchPath(NetAppObject):
    """
    This is a list of CIFS Home Directory search paths. When a CIFS
    client connects to a home directory share, these paths are
    searched in the order indicated by the 'position' field to find
    the user's home directory.
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver associated with this CIFS
        server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _position = None
    @property
    def position(self):
        """
        The position of this entry in the list of paths that will
        be searched for finding a CIFS user's home directory.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._position
    @position.setter
    def position(self, val):
        if val != None:
            self.validate('position', val)
        self._position = val
    
    _path = None
    @property
    def path(self):
        """
        The file system path that will be searched for finding a
        CIFS user's home directory.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    @staticmethod
    def get_api_name():
          return "cifs-home-directory-search-path"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'position',
            'path',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'position': { 'class': int, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

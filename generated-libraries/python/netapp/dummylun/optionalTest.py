from netapp.netapp_object import NetAppObject

class Optionaltest(NetAppObject):
    """
    Test optional output
    """
    
    _ostype = None
    @property
    def ostype(self):
        """
        OS type of the LUN
        Attributes: required-for-create, non-modifiable
        """
        return self._ostype
    @ostype.setter
    def ostype(self, val):
        if val != None:
            self.validate('ostype', val)
        self._ostype = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _size = None
    @property
    def size(self):
        """
        LUN size
        Attributes: required-for-create, modifiable
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    @staticmethod
    def get_api_name():
          return "optionalTest"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ostype',
            'vserver',
            'size',
        ]
    
    def describe_properties(self):
        return {
            'ostype': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

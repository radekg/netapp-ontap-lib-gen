from netapp.netapp_object import NetAppObject

class LunCloneListsInfo(NetAppObject):
    """
    Details of the LUN clone in the specified snapshot.
    """
    
    _path = None
    @property
    def path(self):
        """
        Path of the LUN clone.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    @staticmethod
    def get_api_name():
          return "lun-clone-lists-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'path',
        ]
    
    def describe_properties(self):
        return {
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

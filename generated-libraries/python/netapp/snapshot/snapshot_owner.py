from netapp.netapp_object import NetAppObject

class SnapshotOwner(NetAppObject):
    """
    owner of a busy snapshot
    """
    
    _owner = None
    @property
    def owner(self):
        """
        Name of the owner of a busy snapshot
        """
        return self._owner
    @owner.setter
    def owner(self, val):
        if val != None:
            self.validate('owner', val)
        self._owner = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-owner"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'owner',
        ]
    
    def describe_properties(self):
        return {
            'owner': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

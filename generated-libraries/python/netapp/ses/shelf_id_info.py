from netapp.netapp_object import NetAppObject

class ShelfIdInfo(NetAppObject):
    """
    A list of shelf-ids that can be used in other
    storage-shelf interface calls.
    """
    
    _shelf_id = None
    @property
    def shelf_id(self):
        """
        The shelf id itself.  shelf-id's are only
        unique within a particular channel.
        An example shelf-id is 1.  A channel-name
        and shelf-id pair are required to uniquely
        identify a shelf on a system.
        Range : [0..2^24-1]
        """
        return self._shelf_id
    @shelf_id.setter
    def shelf_id(self, val):
        if val != None:
            self.validate('shelf_id', val)
        self._shelf_id = val
    
    @staticmethod
    def get_api_name():
          return "shelf-id-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'shelf-id',
        ]
    
    def describe_properties(self):
        return {
            'shelf_id': { 'class': int, 'is_list': False, 'required': 'required' },
        }

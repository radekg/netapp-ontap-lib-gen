from netapp.netapp_object import NetAppObject

class ShelfEnvironChannelAddressMap(NetAppObject):
    """
    A list of all the shelf assigned addresses assigned
    on this channel.
    """
    
    _shelf_id = None
    @property
    def shelf_id(self):
        """
        Shelf number for presented address map.
        """
        return self._shelf_id
    @shelf_id.setter
    def shelf_id(self, val):
        if val != None:
            self.validate('shelf_id', val)
        self._shelf_id = val
    
    _address_map = None
    @property
    def address_map(self):
        """
        A comma separated list of addresses assigned on this channel
        by the shelf specified in shelf-no output above.
        """
        return self._address_map
    @address_map.setter
    def address_map(self, val):
        if val != None:
            self.validate('address_map', val)
        self._address_map = val
    
    @staticmethod
    def get_api_name():
          return "shelf-environ-channel-address-map"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'shelf-id',
            'address-map',
        ]
    
    def describe_properties(self):
        return {
            'shelf_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'address_map': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

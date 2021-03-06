from netapp.netapp_object import NetAppObject

class NetRoutingGroupRouteGetIterKeyTd(NetAppObject):
    """
    Key typedef for table rg_routes_view
    """
    
    _key_2 = None
    @property
    def key_2(self):
        """
        Field destination
        """
        return self._key_2
    @key_2.setter
    def key_2(self, val):
        if val != None:
            self.validate('key_2', val)
        self._key_2 = val
    
    _key_1 = None
    @property
    def key_1(self):
        """
        Field routing_group
        """
        return self._key_1
    @key_1.setter
    def key_1(self, val):
        if val != None:
            self.validate('key_1', val)
        self._key_1 = val
    
    _key_0 = None
    @property
    def key_0(self):
        """
        Field server
        """
        return self._key_0
    @key_0.setter
    def key_0(self, val):
        if val != None:
            self.validate('key_0', val)
        self._key_0 = val
    
    @staticmethod
    def get_api_name():
          return "net-routing-group-route-get-iter-key-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'key-2',
            'key-1',
            'key-0',
        ]
    
    def describe_properties(self):
        return {
            'key_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_0': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

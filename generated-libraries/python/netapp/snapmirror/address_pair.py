from netapp.netapp_object import NetAppObject

class AddressPair(NetAppObject):
    """
    Source and destination address pair.
    """
    
    _destination_addr = None
    @property
    def destination_addr(self):
        """
        Destination address in the form of filer name or
        IP address.
        """
        return self._destination_addr
    @destination_addr.setter
    def destination_addr(self, val):
        if val != None:
            self.validate('destination_addr', val)
        self._destination_addr = val
    
    _source_addr = None
    @property
    def source_addr(self):
        """
        Source address in the form of filer name or
        IP address.
        """
        return self._source_addr
    @source_addr.setter
    def source_addr(self, val):
        if val != None:
            self.validate('source_addr', val)
        self._source_addr = val
    
    @staticmethod
    def get_api_name():
          return "address-pair"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'destination-addr',
            'source-addr',
        ]
    
    def describe_properties(self):
        return {
            'destination_addr': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'source_addr': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

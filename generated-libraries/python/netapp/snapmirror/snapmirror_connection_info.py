from netapp.snapmirror.address_pair import AddressPair
from netapp.snapmirror.snapmirror_error import SnapmirrorError
from netapp.netapp_object import NetAppObject

class SnapmirrorConnectionInfo(NetAppObject):
    """
    Information about one connection.
    """
    
    _address_pair2 = None
    @property
    def address_pair2(self):
        """
        The second source and destination address pair.
        """
        return self._address_pair2
    @address_pair2.setter
    def address_pair2(self, val):
        if val != None:
            self.validate('address_pair2', val)
        self._address_pair2 = val
    
    _snapmirror_error = None
    @property
    def snapmirror_error(self):
        """
        Present if there is an error for a snapmirror
        connection.
        """
        return self._snapmirror_error
    @snapmirror_error.setter
    def snapmirror_error(self, val):
        if val != None:
            self.validate('snapmirror_error', val)
        self._snapmirror_error = val
    
    _address_pair1 = None
    @property
    def address_pair1(self):
        """
        The first source and destination address pair.
        """
        return self._address_pair1
    @address_pair1.setter
    def address_pair1(self, val):
        if val != None:
            self.validate('address_pair1', val)
        self._address_pair1 = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the connection.  The name is in ASCII
        and must begin with an alpha character.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _mode = None
    @property
    def mode(self):
        """
        Connection mode.  Possible values are:
        "multi" and "failover".
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-connection-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'address-pair2',
            'snapmirror-error',
            'address-pair1',
            'name',
            'mode',
        ]
    
    def describe_properties(self):
        return {
            'address_pair2': { 'class': AddressPair, 'is_list': False, 'required': 'optional' },
            'snapmirror_error': { 'class': SnapmirrorError, 'is_list': False, 'required': 'optional' },
            'address_pair1': { 'class': AddressPair, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

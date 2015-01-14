from netapp.netapp_object import NetAppObject

class AdapterBarInfo(NetAppObject):
    """
    display base address information
    """
    
    _bar_type = None
    @property
    def bar_type(self):
        """
        Type of base address information.
        Possible values are: "I/O", and
        "memory mapped I/O".
        """
        return self._bar_type
    @bar_type.setter
    def bar_type(self, val):
        if val != None:
            self.validate('bar_type', val)
        self._bar_type = val
    
    _bar_size = None
    @property
    def bar_size(self):
        """
        Address range occupied by the storage port adapter.
        Range : [0..2^32-1]
        """
        return self._bar_size
    @bar_size.setter
    def bar_size(self, val):
        if val != None:
            self.validate('bar_size', val)
        self._bar_size = val
    
    _bar_base = None
    @property
    def bar_base(self):
        """
        Base address occupied by the storage port adapter.
        Range : [0..2^32-1]
        """
        return self._bar_base
    @bar_base.setter
    def bar_base(self, val):
        if val != None:
            self.validate('bar_base', val)
        self._bar_base = val
    
    @staticmethod
    def get_api_name():
          return "adapter-bar-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'bar-type',
            'bar-size',
            'bar-base',
        ]
    
    def describe_properties(self):
        return {
            'bar_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'bar_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'bar_base': { 'class': int, 'is_list': False, 'required': 'required' },
        }

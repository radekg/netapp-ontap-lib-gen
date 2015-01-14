from netapp.ntdtest.dummy_vserver_2 import DummyVserver2
from netapp.netapp_object import NetAppObject

class DummyVserver1(NetAppObject):
    """
    Default Typedef 1
    """
    
    _element2 = None
    @property
    def element2(self):
        """
        Default Typdef 2
        """
        return self._element2
    @element2.setter
    def element2(self, val):
        if val != None:
            self.validate('element2', val)
        self._element2 = val
    
    _zfield2 = None
    @property
    def zfield2(self):
        """
        Generic/Dummy Field 2
        Attributes: key, required-for-create, non-modifiable
        """
        return self._zfield2
    @zfield2.setter
    def zfield2(self, val):
        if val != None:
            self.validate('zfield2', val)
        self._zfield2 = val
    
    @staticmethod
    def get_api_name():
          return "dummy-vserver-1"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'element2',
            'zfield2',
        ]
    
    def describe_properties(self):
        return {
            'element2': { 'class': DummyVserver2, 'is_list': True, 'required': 'optional' },
            'zfield2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

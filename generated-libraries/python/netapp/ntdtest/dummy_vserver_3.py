from netapp.ntdtest.dummy_vserver_4 import DummyVserver4
from netapp.netapp_object import NetAppObject

class DummyVserver3(NetAppObject):
    """
    Default Typdef 3
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        Generic/Dummy Field 1
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _element2 = None
    @property
    def element2(self):
        """
        Default Typedef 4
        """
        return self._element2
    @element2.setter
    def element2(self, val):
        if val != None:
            self.validate('element2', val)
        self._element2 = val
    
    @staticmethod
    def get_api_name():
          return "dummy-vserver-3"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'element2',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'element2': { 'class': DummyVserver4, 'is_list': True, 'required': 'optional' },
        }

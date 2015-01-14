from netapp.ntdtest.dummy_vserver_1 import DummyVserver1
from netapp.netapp_object import NetAppObject

class DummyVserver(NetAppObject):
    """
    Default Typedef
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
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
    
    _element1 = None
    @property
    def element1(self):
        """
        Default Typedef 1
        """
        return self._element1
    @element1.setter
    def element1(self, val):
        if val != None:
            self.validate('element1', val)
        self._element1 = val
    
    @staticmethod
    def get_api_name():
          return "dummy-vserver"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'element1',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'element1': { 'class': DummyVserver1, 'is_list': True, 'required': 'optional' },
        }

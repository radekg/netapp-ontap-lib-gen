from netapp.netapp_object import NetAppObject

class IscsiInterfaceAccesslistEntryInfo(NetAppObject):
    """
    Information about a single accesslist entry
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
        Vserver hosting the iSCSI LIF
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _initiator = None
    @property
    def initiator(self):
        """
        Initiator that can access the iSCSI LIFs
        Attributes: key, non-creatable, non-modifiable
        """
        return self._initiator
    @initiator.setter
    def initiator(self, val):
        if val != None:
            self.validate('initiator', val)
        self._initiator = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        iSCSI LIF Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-interface-accesslist-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'initiator',
            'interface-name',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'initiator': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

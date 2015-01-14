from netapp.netapp_object import NetAppObject

class AvEventInfo(NetAppObject):
    """
    Log Entry Written by an Antivirus Agent
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
    
    _vendor_string = None
    @property
    def vendor_string(self):
        """
        Vendor String
        Attributes: key, required-for-create, non-modifiable
        """
        return self._vendor_string
    @vendor_string.setter
    def vendor_string(self, val):
        if val != None:
            self.validate('vendor_string', val)
        self._vendor_string = val
    
    _vendor_id = None
    @property
    def vendor_id(self):
        """
        Vendor ID
        Attributes: optional-for-create, modifiable
        """
        return self._vendor_id
    @vendor_id.setter
    def vendor_id(self, val):
        if val != None:
            self.validate('vendor_id', val)
        self._vendor_id = val
    
    _datetime = None
    @property
    def datetime(self):
        """
        When the event is logged. The time value is in seconds
        since January 1, 1970.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._datetime
    @datetime.setter
    def datetime(self, val):
        if val != None:
            self.validate('datetime', val)
        self._datetime = val
    
    @staticmethod
    def get_api_name():
          return "av-event-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vendor-string',
            'vendor-id',
            'datetime',
        ]
    
    def describe_properties(self):
        return {
            'vendor_string': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vendor_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'datetime': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

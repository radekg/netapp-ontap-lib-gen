from netapp.netapp_object import NetAppObject

class LicenseV2Result(NetAppObject):
    """
    License operation result
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
    
    _entry = None
    @property
    def entry(self):
        """
        Failed license entry.
        Attributes: non-creatable, non-modifiable
        """
        return self._entry
    @entry.setter
    def entry(self, val):
        if val != None:
            self.validate('entry', val)
        self._entry = val
    
    _errcode = None
    @property
    def errcode(self):
        """
        Failure error code.
        Attributes: non-creatable, non-modifiable
        """
        return self._errcode
    @errcode.setter
    def errcode(self, val):
        if val != None:
            self.validate('errcode', val)
        self._errcode = val
    
    _description = None
    @property
    def description(self):
        """
        Additional information of the failure.
        Attributes: non-creatable, non-modifiable
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    @staticmethod
    def get_api_name():
          return "license-v2-result"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'entry',
            'errcode',
            'description',
        ]
    
    def describe_properties(self):
        return {
            'entry': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'errcode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

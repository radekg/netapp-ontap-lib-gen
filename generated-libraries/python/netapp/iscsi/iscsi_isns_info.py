from netapp.netapp_object import NetAppObject

class IscsiIsnsInfo(NetAppObject):
    """
    iSCSI iSNS Service Configuration.
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
    
    _isns_entity_id = None
    @property
    def isns_entity_id(self):
        """
        Entity id existing on the iSNS server
        Attributes: non-creatable, non-modifiable
        """
        return self._isns_entity_id
    @isns_entity_id.setter
    def isns_entity_id(self, val):
        if val != None:
            self.validate('isns_entity_id', val)
        self._isns_entity_id = val
    
    _isns_ip_addr = None
    @property
    def isns_ip_addr(self):
        """
        iSNS server IP address.
        Attributes: required-for-create, modifiable
        """
        return self._isns_ip_addr
    @isns_ip_addr.setter
    def isns_ip_addr(self, val):
        if val != None:
            self.validate('isns_ip_addr', val)
        self._isns_ip_addr = val
    
    _last_update_attempt = None
    @property
    def last_update_attempt(self):
        """
        Last iSNS update attempt time in seconds since January 1,
        1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_update_attempt
    @last_update_attempt.setter
    def last_update_attempt(self, val):
        if val != None:
            self.validate('last_update_attempt', val)
        self._last_update_attempt = val
    
    _last_successful_update = None
    @property
    def last_successful_update(self):
        """
        Last successful iSNS update time in seconds since January
        1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_successful_update
    @last_successful_update.setter
    def last_successful_update(self, val):
        if val != None:
            self.validate('last_successful_update', val)
        self._last_successful_update = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver hosting the iSNS service.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _last_update_result = None
    @property
    def last_update_result(self):
        """
        Result of the last iSNS update.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_update_result
    @last_update_result.setter
    def last_update_result(self, val):
        if val != None:
            self.validate('last_update_result', val)
        self._last_update_result = val
    
    _is_isns_enabled = None
    @property
    def is_isns_enabled(self):
        """
        true if the iSNS Service is running, false otherwise.
        Attributes: optional-for-create, non-modifiable
        """
        return self._is_isns_enabled
    @is_isns_enabled.setter
    def is_isns_enabled(self, val):
        if val != None:
            self.validate('is_isns_enabled', val)
        self._is_isns_enabled = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-isns-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'isns-entity-id',
            'isns-ip-addr',
            'last-update-attempt',
            'last-successful-update',
            'vserver',
            'last-update-result',
            'is-isns-enabled',
        ]
    
    def describe_properties(self):
        return {
            'isns_entity_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'isns_ip_addr': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_update_attempt': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_successful_update': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_update_result': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_isns_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

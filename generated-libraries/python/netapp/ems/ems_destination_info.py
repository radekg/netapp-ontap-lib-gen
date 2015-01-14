from netapp.netapp_object import NetAppObject

class EmsDestinationInfo(NetAppObject):
    """
    EMS Destination Info
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
    
    _name = None
    @property
    def name(self):
        """
        The name of the EMS destination.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _snmp = None
    @property
    def snmp(self):
        """
        The SNMP addresses to which traps are sent.
        Attributes: optional-for-create, modifiable
        """
        return self._snmp
    @snmp.setter
    def snmp(self, val):
        if val != None:
            self.validate('snmp', val)
        self._snmp = val
    
    _syslog = None
    @property
    def syslog(self):
        """
        The remote syslog servers to which messages are sent.
        Attributes: optional-for-create, modifiable
        """
        return self._syslog
    @syslog.setter
    def syslog(self, val):
        if val != None:
            self.validate('syslog', val)
        self._syslog = val
    
    _snmp_community = None
    @property
    def snmp_community(self):
        """
        The SNMP community name.
        Attributes: optional-for-create, modifiable
        """
        return self._snmp_community
    @snmp_community.setter
    def snmp_community(self, val):
        if val != None:
            self.validate('snmp_community', val)
        self._snmp_community = val
    
    _syslog_facility = None
    @property
    def syslog_facility(self):
        """
        The syslog logging facility.
        Attributes: optional-for-create, modifiable
        """
        return self._syslog_facility
    @syslog_facility.setter
    def syslog_facility(self, val):
        if val != None:
            self.validate('syslog_facility', val)
        self._syslog_facility = val
    
    _mail = None
    @property
    def mail(self):
        """
        The e-mail address to which events are sent.
        Attributes: optional-for-create, modifiable
        """
        return self._mail
    @mail.setter
    def mail(self, val):
        if val != None:
            self.validate('mail', val)
        self._mail = val
    
    _hide_parameters = None
    @property
    def hide_parameters(self):
        """
        Hide parameter values?
        Attributes: optional-for-create, modifiable
        """
        return self._hide_parameters
    @hide_parameters.setter
    def hide_parameters(self, val):
        if val != None:
            self.validate('hide_parameters', val)
        self._hide_parameters = val
    
    @staticmethod
    def get_api_name():
          return "ems-destination-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'snmp',
            'syslog',
            'snmp-community',
            'syslog-facility',
            'mail',
            'hide-parameters',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snmp': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'syslog': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'snmp_community': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'syslog_facility': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mail': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'hide_parameters': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

from netapp.netapp_object import NetAppObject

class FilterAttrsInfo(NetAppObject):
    """
    List of filters based on attributes of an
    aggregate.
    """
    
    _is_local = None
    @property
    def is_local(self):
        """
        If true, returns aggregates owned by the local
        node. It includes taken over aggregates with
        'sfo' policy. Default is false.
        """
        return self._is_local
    @is_local.setter
    def is_local(self, val):
        if val != None:
            self.validate('is_local', val)
        self._is_local = val
    
    _all = None
    @property
    def all(self):
        """
        If true, returns all aggregates owned by the
        local node and also taken over by the local
        node. Default is false.
        """
        return self._all
    @all.setter
    def all(self, val):
        if val != None:
            self.validate('all', val)
        self._all = val
    
    _is_sfo = None
    @property
    def is_sfo(self):
        """
        If true, returns aggregates with 'sfo' HA
        policy which includes local and taken over
        aggregates. Default is false.
        """
        return self._is_sfo
    @is_sfo.setter
    def is_sfo(self, val):
        if val != None:
            self.validate('is_sfo', val)
        self._is_sfo = val
    
    _is_dr_auxiliary = None
    @property
    def is_dr_auxiliary(self):
        """
        If true, returns aggregates taken over by the
        local node but owned by the partner of DR (disaster
        recovery) partner (i.e. auxiliary partner).
        Default is false.
        """
        return self._is_dr_auxiliary
    @is_dr_auxiliary.setter
    def is_dr_auxiliary(self, val):
        if val != None:
            self.validate('is_dr_auxiliary', val)
        self._is_dr_auxiliary = val
    
    _is_partner = None
    @property
    def is_partner(self):
        """
        If true, returns aggregates taken over by the
        local node but owned by the partner. Default
        is false.
        """
        return self._is_partner
    @is_partner.setter
    def is_partner(self, val):
        if val != None:
            self.validate('is_partner', val)
        self._is_partner = val
    
    _is_cfo = None
    @property
    def is_cfo(self):
        """
        If true, returns aggregates with 'cfo' HA
        policy which includes local and taken over
        aggregates. Default is false.
        """
        return self._is_cfo
    @is_cfo.setter
    def is_cfo(self, val):
        if val != None:
            self.validate('is_cfo', val)
        self._is_cfo = val
    
    _is_dr_partner = None
    @property
    def is_dr_partner(self):
        """
        If true, returns aggregates taken over by the
        local node but owned by the DR (disaster
        recovery) partner. Default is false.
        """
        return self._is_dr_partner
    @is_dr_partner.setter
    def is_dr_partner(self, val):
        if val != None:
            self.validate('is_dr_partner', val)
        self._is_dr_partner = val
    
    @staticmethod
    def get_api_name():
          return "filter-attrs-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-local',
            'all',
            'is-sfo',
            'is-dr-auxiliary',
            'is-partner',
            'is-cfo',
            'is-dr-partner',
        ]
    
    def describe_properties(self):
        return {
            'is_local': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'all': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_sfo': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_dr_auxiliary': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_partner': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_cfo': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_dr_partner': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

from netapp.netapp_object import NetAppObject

class AggrSnapmirrorAttributes(NetAppObject):
    """
    SnapMirror specific information of the aggregate
    """
    
    _ls_snapmirror_destinations = None
    @property
    def ls_snapmirror_destinations(self):
        """
        When present, this field indicates the number of
        load sharing (ls) snapmirror destination
        volumes.
        """
        return self._ls_snapmirror_destinations
    @ls_snapmirror_destinations.setter
    def ls_snapmirror_destinations(self, val):
        if val != None:
            self.validate('ls_snapmirror_destinations', val)
        self._ls_snapmirror_destinations = val
    
    _dp_snapmirror_destinations = None
    @property
    def dp_snapmirror_destinations(self):
        """
        When present, this field indicates the number of
        data protection (dp) snapmirror destination
        volumes.
        """
        return self._dp_snapmirror_destinations
    @dp_snapmirror_destinations.setter
    def dp_snapmirror_destinations(self, val):
        if val != None:
            self.validate('dp_snapmirror_destinations', val)
        self._dp_snapmirror_destinations = val
    
    _mv_snapmirror_destinations = None
    @property
    def mv_snapmirror_destinations(self):
        """
        When present, this field indicates the number of
        move snapmirror destination volumes that are
        created for volume move operations.
        """
        return self._mv_snapmirror_destinations
    @mv_snapmirror_destinations.setter
    def mv_snapmirror_destinations(self, val):
        if val != None:
            self.validate('mv_snapmirror_destinations', val)
        self._mv_snapmirror_destinations = val
    
    @staticmethod
    def get_api_name():
          return "aggr-snapmirror-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ls-snapmirror-destinations',
            'dp-snapmirror-destinations',
            'mv-snapmirror-destinations',
        ]
    
    def describe_properties(self):
        return {
            'ls_snapmirror_destinations': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dp_snapmirror_destinations': { 'class': int, 'is_list': False, 'required': 'optional' },
            'mv_snapmirror_destinations': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

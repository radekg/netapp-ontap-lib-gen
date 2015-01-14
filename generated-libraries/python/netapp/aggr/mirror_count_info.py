from netapp.netapp_object import NetAppObject

class MirrorCountInfo(NetAppObject):
    """
    Various counts information for mirror volumes in the
    aggregate. This information is returned only when the
    aggregate contains mirror volumes. Currently, Vfiler
    owned mirror destination volumes are counted only if
    those volumes are online.
    """
    
    _dp_qtree_snapmirror_destinations = None
    @property
    def dp_qtree_snapmirror_destinations(self):
        """
        When present, this field indicates the number of
        data protection (dp) qtree snapmirror
        destination volumes.
        <p>
        Range: [0..2^31-1]
        """
        return self._dp_qtree_snapmirror_destinations
    @dp_qtree_snapmirror_destinations.setter
    def dp_qtree_snapmirror_destinations(self, val):
        if val != None:
            self.validate('dp_qtree_snapmirror_destinations', val)
        self._dp_qtree_snapmirror_destinations = val
    
    _ls_snapmirror_destinations = None
    @property
    def ls_snapmirror_destinations(self):
        """
        When present, this field indicates the number of
        load sharing (ls) snapmirror destination
        volumes.
        <p>
        Range: [0..2^31-1]
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
        <p>
        Range: [0..2^31-1]
        """
        return self._dp_snapmirror_destinations
    @dp_snapmirror_destinations.setter
    def dp_snapmirror_destinations(self, val):
        if val != None:
            self.validate('dp_snapmirror_destinations', val)
        self._dp_snapmirror_destinations = val
    
    _move_snapmirror_destinations = None
    @property
    def move_snapmirror_destinations(self):
        """
        When present, this field indicates the number of
        move snapmirror destination volumes that are
        created for volume move operations.
        <p>
        Range: [0..2^31-1]
        """
        return self._move_snapmirror_destinations
    @move_snapmirror_destinations.setter
    def move_snapmirror_destinations(self, val):
        if val != None:
            self.validate('move_snapmirror_destinations', val)
        self._move_snapmirror_destinations = val
    
    @staticmethod
    def get_api_name():
          return "mirror-count-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'dp-qtree-snapmirror-destinations',
            'ls-snapmirror-destinations',
            'dp-snapmirror-destinations',
            'move-snapmirror-destinations',
        ]
    
    def describe_properties(self):
        return {
            'dp_qtree_snapmirror_destinations': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ls_snapmirror_destinations': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dp_snapmirror_destinations': { 'class': int, 'is_list': False, 'required': 'optional' },
            'move_snapmirror_destinations': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

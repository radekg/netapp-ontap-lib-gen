from netapp.netapp_object import NetAppObject

class PrevCpInofileInfo(NetAppObject):
    """
    Information about one inofile in the volume
    checking it. The default value is "false".
    <p>
    The "backup", "use-backup", and "prev-cp" elements are
    mutually exclusive.
    """
    
    _volume_name = None
    @property
    def volume_name(self):
        """
        Flexvol name with optional ordinal suffix.
        The name uniquely identifies the volume
        inside the aggregate.
        Example: v1, v2, v2(1)
        """
        return self._volume_name
    @volume_name.setter
    def volume_name(self, val):
        if val != None:
            self.validate('volume_name', val)
        self._volume_name = val
    
    _inofile_id = None
    @property
    def inofile_id(self):
        """
        Identify an inofile in the volume,
        <p>
        Possible values:
        - ID of one snapshot in the volume
        - "r" for active file system
        - "c" for previous CP
        - "#VBN" for a VVBN number
        """
        return self._inofile_id
    @inofile_id.setter
    def inofile_id(self, val):
        if val != None:
            self.validate('inofile_id', val)
        self._inofile_id = val
    
    @staticmethod
    def get_api_name():
          return "prev-cp-inofile-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume-name',
            'inofile-id',
        ]
    
    def describe_properties(self):
        return {
            'volume_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'inofile_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

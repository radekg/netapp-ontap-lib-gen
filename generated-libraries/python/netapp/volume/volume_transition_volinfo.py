from netapp.netapp_object import NetAppObject

class VolumeTransitionVolinfo(NetAppObject):
    """
    Information describing the volume and how to transition it.
    Possible values are:
    "copy_based" (default)
    "in_place"
    "untransition"
    Copy Based Transition is currently the only supported mode
    for transition; "in_place" and "untransition" should only
    be used in testing scenarios.
    This is not available for all volume configurations.  If a value
    is not specified, this field will default to true - non-disruptive
    desired.
    process.  The system will select default values as appropriate.  If not specified,
    values will not be overridden.
    """
    
    _volume_name = None
    @property
    def volume_name(self):
        """
        The name of the volume which is to be transitioned.
        """
        return self._volume_name
    @volume_name.setter
    def volume_name(self, val):
        if val != None:
            self.validate('volume_name', val)
        self._volume_name = val
    
    _junction_path = None
    @property
    def junction_path(self):
        """
        The path in the vserver into which the volume should
        be mounted.  Note that this is only valid for transitions
        from 7-mode to Cluster-mode and not untransition.
        Path should be of the format "/<pathname>".
        """
        return self._junction_path
    @junction_path.setter
    def junction_path(self, val):
        if val != None:
            self.validate('junction_path', val)
        self._junction_path = val
    
    @staticmethod
    def get_api_name():
          return "volume-transition-volinfo"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume-name',
            'junction-path',
        ]
    
    def describe_properties(self):
        return {
            'volume_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'junction_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

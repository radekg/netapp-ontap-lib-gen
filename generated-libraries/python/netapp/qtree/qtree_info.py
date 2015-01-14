from netapp.netapp_object import NetAppObject

class QtreeInfo(NetAppObject):
    """
    Information about a single qtree.
    """
    
    _status = None
    @property
    def status(self):
        """
        Status of the qtree. Possible values include:
        "snapvaulted", "snapmirrored", "normal", and "readonly".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _volume = None
    @property
    def volume(self):
        """
        Name of the volume containing the qtree
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _export_policy = None
    @property
    def export_policy(self):
        """
        Export policy of the qtree.
        """
        return self._export_policy
    @export_policy.setter
    def export_policy(self, val):
        if val != None:
            self.validate('export_policy', val)
        self._export_policy = val
    
    _qtree = None
    @property
    def qtree(self):
        """
        Name of the qtree, blank if qtree is the volume itself
        """
        return self._qtree
    @qtree.setter
    def qtree(self, val):
        if val != None:
            self.validate('qtree', val)
        self._qtree = val
    
    _is_export_policy_inherited = None
    @property
    def is_export_policy_inherited(self):
        """
        If true, this qtree inherits the export policy of the parent volume.
        """
        return self._is_export_policy_inherited
    @is_export_policy_inherited.setter
    def is_export_policy_inherited(self, val):
        if val != None:
            self.validate('is_export_policy_inherited', val)
        self._is_export_policy_inherited = val
    
    _security_style = None
    @property
    def security_style(self):
        """
        Security style of the qtree. Possible values are "unix",
        "ntfs", or "mixed".
        """
        return self._security_style
    @security_style.setter
    def security_style(self, val):
        if val != None:
            self.validate('security_style', val)
        self._security_style = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The vserver in which the volume belongs
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _oplocks = None
    @property
    def oplocks(self):
        """
        Indicates whether opportunistic locks are enabled on
        the qtree.  Possible values: "enabled", "disabled".
        """
        return self._oplocks
    @oplocks.setter
    def oplocks(self, val):
        if val != None:
            self.validate('oplocks', val)
        self._oplocks = val
    
    _owning_vfiler = None
    @property
    def owning_vfiler(self):
        """
        Name of the vfiler which owns this qtree. This value will
        be returned only if the request is coming to vfiler0 and
        MultiStore is licensed.
        """
        return self._owning_vfiler
    @owning_vfiler.setter
    def owning_vfiler(self, val):
        if val != None:
            self.validate('owning_vfiler', val)
        self._owning_vfiler = val
    
    _id = None
    @property
    def id(self):
        """
        Id of the qtree (unique within the volume),
        which is 0 if qtree is the volume itself.
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    @staticmethod
    def get_api_name():
          return "qtree-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'volume',
            'export-policy',
            'qtree',
            'is-export-policy-inherited',
            'security-style',
            'vserver',
            'oplocks',
            'owning-vfiler',
            'id',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'export_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'qtree': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_export_policy_inherited': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'security_style': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'oplocks': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'owning_vfiler': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'id': { 'class': int, 'is_list': False, 'required': 'required' },
        }

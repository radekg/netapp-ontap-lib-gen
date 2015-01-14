from netapp.netapp_object import NetAppObject

class VolumeExportAttributes(NetAppObject):
    """
    Information about export settings of the volume.
    """
    
    _policy = None
    @property
    def policy(self):
        """
        The name of the Export Policy to be used by NFS/CIFS
        protocols. The default policy name is 'default'.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._policy
    @policy.setter
    def policy(self, val):
        if val != None:
            self.validate('policy', val)
        self._policy = val
    
    @staticmethod
    def get_api_name():
          return "volume-export-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'policy',
        ]
    
    def describe_properties(self):
        return {
            'policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

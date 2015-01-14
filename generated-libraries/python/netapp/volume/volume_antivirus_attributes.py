from netapp.netapp_object import NetAppObject

class VolumeAntivirusAttributes(NetAppObject):
    """
    {Deprecated, this field does not have any effect on the
    operation of the volume.} Information about Antivirus settings
    for the volume.
    """
    
    _on_access_policy = None
    @property
    def on_access_policy(self):
        """
        {Deprecated, this field does not have any effect on the
        operation of the volume.} The name of the Antivirus
        On-Access policy. The default policy name is 'default'.
        <p>
        If not specified when creating a volume, the Antivirus
        On-Access Policy is inherited from the owning vserver.
        Currently, this policy can only be managed using the
        'antivirus' command line interfaces.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._on_access_policy
    @on_access_policy.setter
    def on_access_policy(self, val):
        if val != None:
            self.validate('on_access_policy', val)
        self._on_access_policy = val
    
    @staticmethod
    def get_api_name():
          return "volume-antivirus-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'on-access-policy',
        ]
    
    def describe_properties(self):
        return {
            'on_access_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

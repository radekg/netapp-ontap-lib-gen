from netapp.netapp_object import NetAppObject

class VolumeQosAttributes(NetAppObject):
    """
    QoS policy group attached with a volume.
    """
    
    _policy_group_name = None
    @property
    def policy_group_name(self):
        """
        The QoS policy group associated with this volume.
        <p>
        This optionally specifies which QoS policy group to apply
        to the volume. This policy group defines measurable
        service level objectives (SLOs) that apply to the storage
        objects with which the policy group is associated. If you
        do not assign a policy group to a volume, the system will
        not monitor and control the traffic to it. This parameter
        is not supported on Infinite Volumes. <p>
        Attributes: optional-for-create, modifiable
        """
        return self._policy_group_name
    @policy_group_name.setter
    def policy_group_name(self, val):
        if val != None:
            self.validate('policy_group_name', val)
        self._policy_group_name = val
    
    @staticmethod
    def get_api_name():
          return "volume-qos-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'policy-group-name',
        ]
    
    def describe_properties(self):
        return {
            'policy_group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

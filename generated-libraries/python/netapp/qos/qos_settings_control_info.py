from netapp.netapp_object import NetAppObject

class QosSettingsControlInfo(NetAppObject):
    """
    Information about QoS control settings.
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
    
    _enforcement = None
    @property
    def enforcement(self):
        """
        Cluster-wide QoS enforcement
        Attributes: non-creatable, modifiable
        """
        return self._enforcement
    @enforcement.setter
    def enforcement(self, val):
        if val != None:
            self.validate('enforcement', val)
        self._enforcement = val
    
    _ratebucket_rebalance = None
    @property
    def ratebucket_rebalance(self):
        """
        Manage QoS ratebucket budgets across the cluster
        Attributes: non-creatable, modifiable
        """
        return self._ratebucket_rebalance
    @ratebucket_rebalance.setter
    def ratebucket_rebalance(self, val):
        if val != None:
            self.validate('ratebucket_rebalance', val)
        self._ratebucket_rebalance = val
    
    @staticmethod
    def get_api_name():
          return "qos-settings-control-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'enforcement',
            'ratebucket-rebalance',
        ]
    
    def describe_properties(self):
        return {
            'enforcement': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ratebucket_rebalance': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

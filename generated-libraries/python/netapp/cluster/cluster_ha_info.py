from netapp.netapp_object import NetAppObject

class ClusterHaInfo(NetAppObject):
    """
    cluster HA configuration information
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
    
    _ha_configured = None
    @property
    def ha_configured(self):
        """
        This parameter specifies the current state of cluster HA.
        A boolean value of true means that cluster HA is enabled
        Attributes: non-creatable, modifiable
        """
        return self._ha_configured
    @ha_configured.setter
    def ha_configured(self, val):
        if val != None:
            self.validate('ha_configured', val)
        self._ha_configured = val
    
    @staticmethod
    def get_api_name():
          return "cluster-ha-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ha-configured',
        ]
    
    def describe_properties(self):
        return {
            'ha_configured': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

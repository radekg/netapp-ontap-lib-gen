from netapp.netapp_object import NetAppObject

class QosSettingsArchivedWorkloadInfo(NetAppObject):
    """
    Archival settings for QoS workload Objects.
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
    
    _max_workloads = None
    @property
    def max_workloads(self):
        """
        Maximum Number of Workloads to be Archived
        Attributes: non-creatable, modifiable
        """
        return self._max_workloads
    @max_workloads.setter
    def max_workloads(self, val):
        if val != None:
            self.validate('max_workloads', val)
        self._max_workloads = val
    
    @staticmethod
    def get_api_name():
          return "qos-settings-archived-workload-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'max-workloads',
        ]
    
    def describe_properties(self):
        return {
            'max_workloads': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

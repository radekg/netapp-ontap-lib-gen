from netapp.system.operation_info import OperationInfo
from netapp.netapp_object import NetAppObject

class CapabilityInfo(NetAppObject):
    """
    Capability information about the object and their operations.
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
    
    _operation_list = None
    @property
    def operation_list(self):
        """
        Operation details. Contains the operation name, command
        path and API name.
        """
        return self._operation_list
    @operation_list.setter
    def operation_list(self, val):
        if val != None:
            self.validate('operation_list', val)
        self._operation_list = val
    
    _object_name = None
    @property
    def object_name(self):
        """
        Object name, for e.g., 'volume', 'storage.aggregate',
        'vserver.nfs' etc..
        Attributes: key, non-creatable, non-modifiable
        """
        return self._object_name
    @object_name.setter
    def object_name(self, val):
        if val != None:
            self.validate('object_name', val)
        self._object_name = val
    
    @staticmethod
    def get_api_name():
          return "capability-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'operation-list',
            'object-name',
        ]
    
    def describe_properties(self):
        return {
            'operation_list': { 'class': OperationInfo, 'is_list': True, 'required': 'optional' },
            'object_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

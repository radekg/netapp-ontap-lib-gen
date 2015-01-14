from netapp.cf.takeover_related_info import TakeoverRelatedInfo
from netapp.cf.storage_related_info import StorageRelatedInfo
from netapp.cf.options_related_info import OptionsRelatedInfo
from netapp.cf.interconnect_related_info import InterconnectRelatedInfo
from netapp.cf.node_related_info import NodeRelatedInfo
from netapp.cf.giveback_related_info import GivebackRelatedInfo
from netapp.netapp_object import NetAppObject

class StorageFailoverInfo(NetAppObject):
    """
    Storage Failover Info
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
    
    _sfo_takeover_info = None
    @property
    def sfo_takeover_info(self):
        """
        Takeover related Info
        """
        return self._sfo_takeover_info
    @sfo_takeover_info.setter
    def sfo_takeover_info(self, val):
        if val != None:
            self.validate('sfo_takeover_info', val)
        self._sfo_takeover_info = val
    
    _sfo_storage_info = None
    @property
    def sfo_storage_info(self):
        """
        Storage Info
        """
        return self._sfo_storage_info
    @sfo_storage_info.setter
    def sfo_storage_info(self, val):
        if val != None:
            self.validate('sfo_storage_info', val)
        self._sfo_storage_info = val
    
    _sfo_options_info = None
    @property
    def sfo_options_info(self):
        """
        Options Info
        """
        return self._sfo_options_info
    @sfo_options_info.setter
    def sfo_options_info(self, val):
        if val != None:
            self.validate('sfo_options_info', val)
        self._sfo_options_info = val
    
    _sfo_interconnect_info = None
    @property
    def sfo_interconnect_info(self):
        """
        Interconnect Info
        """
        return self._sfo_interconnect_info
    @sfo_interconnect_info.setter
    def sfo_interconnect_info(self, val):
        if val != None:
            self.validate('sfo_interconnect_info', val)
        self._sfo_interconnect_info = val
    
    _sfo_node_info = None
    @property
    def sfo_node_info(self):
        """
        Node Info
        """
        return self._sfo_node_info
    @sfo_node_info.setter
    def sfo_node_info(self, val):
        if val != None:
            self.validate('sfo_node_info', val)
        self._sfo_node_info = val
    
    _sfo_giveback_info = None
    @property
    def sfo_giveback_info(self):
        """
        Giveback related Info
        """
        return self._sfo_giveback_info
    @sfo_giveback_info.setter
    def sfo_giveback_info(self, val):
        if val != None:
            self.validate('sfo_giveback_info', val)
        self._sfo_giveback_info = val
    
    @staticmethod
    def get_api_name():
          return "storage-failover-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'sfo-takeover-info',
            'sfo-storage-info',
            'sfo-options-info',
            'sfo-interconnect-info',
            'sfo-node-info',
            'sfo-giveback-info',
        ]
    
    def describe_properties(self):
        return {
            'sfo_takeover_info': { 'class': TakeoverRelatedInfo, 'is_list': False, 'required': 'optional' },
            'sfo_storage_info': { 'class': StorageRelatedInfo, 'is_list': False, 'required': 'optional' },
            'sfo_options_info': { 'class': OptionsRelatedInfo, 'is_list': False, 'required': 'optional' },
            'sfo_interconnect_info': { 'class': InterconnectRelatedInfo, 'is_list': False, 'required': 'optional' },
            'sfo_node_info': { 'class': NodeRelatedInfo, 'is_list': False, 'required': 'optional' },
            'sfo_giveback_info': { 'class': GivebackRelatedInfo, 'is_list': False, 'required': 'optional' },
        }

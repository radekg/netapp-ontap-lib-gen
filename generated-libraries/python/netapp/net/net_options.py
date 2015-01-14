from netapp.net.switchless_cluster_info import SwitchlessClusterInfo
from netapp.net.ipv6_options_info import Ipv6OptionsInfo
from netapp.netapp_object import NetAppObject

class NetOptions(NetAppObject):
    """
    Network Options Typedef
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
    
    _switchless_cluster_info = None
    @property
    def switchless_cluster_info(self):
        """
        Network options switchless-cluster
        """
        return self._switchless_cluster_info
    @switchless_cluster_info.setter
    def switchless_cluster_info(self, val):
        if val != None:
            self.validate('switchless_cluster_info', val)
        self._switchless_cluster_info = val
    
    _ipv6_options_info = None
    @property
    def ipv6_options_info(self):
        """
        Network options ipv6
        """
        return self._ipv6_options_info
    @ipv6_options_info.setter
    def ipv6_options_info(self, val):
        if val != None:
            self.validate('ipv6_options_info', val)
        self._ipv6_options_info = val
    
    @staticmethod
    def get_api_name():
          return "net-options"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'switchless-cluster-info',
            'ipv6-options-info',
        ]
    
    def describe_properties(self):
        return {
            'switchless_cluster_info': { 'class': SwitchlessClusterInfo, 'is_list': False, 'required': 'optional' },
            'ipv6_options_info': { 'class': Ipv6OptionsInfo, 'is_list': False, 'required': 'optional' },
        }

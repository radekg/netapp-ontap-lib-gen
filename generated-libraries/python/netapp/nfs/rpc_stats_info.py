from netapp.nfs.rpc_data_info import RpcDataInfo
from netapp.netapp_object import NetAppObject

class RpcStatsInfo(NetAppObject):
    """
    structure containing statistics for RPC operations
    """
    
    _tcp_info = None
    @property
    def tcp_info(self):
        """
        detailed statistics for RPC over TCP operations
        """
        return self._tcp_info
    @tcp_info.setter
    def tcp_info(self, val):
        if val != None:
            self.validate('tcp_info', val)
        self._tcp_info = val
    
    _udp_info = None
    @property
    def udp_info(self):
        """
        detailed statistics for RPC over UDP operations
        """
        return self._udp_info
    @udp_info.setter
    def udp_info(self, val):
        if val != None:
            self.validate('udp_info', val)
        self._udp_info = val
    
    @staticmethod
    def get_api_name():
          return "rpc-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'tcp-info',
            'udp-info',
        ]
    
    def describe_properties(self):
        return {
            'tcp_info': { 'class': RpcDataInfo, 'is_list': False, 'required': 'required' },
            'udp_info': { 'class': RpcDataInfo, 'is_list': False, 'required': 'required' },
        }

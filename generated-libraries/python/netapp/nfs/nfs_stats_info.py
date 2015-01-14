from netapp.nfs.nfsv4_client_stats_info import Nfsv4ClientStatsInfo
from netapp.nfs.nfsv3_client_stats_info import Nfsv3ClientStatsInfo
from netapp.nfs.nfsv2_client_stats_info import Nfsv2ClientStatsInfo
from netapp.netapp_object import NetAppObject

class NfsStatsInfo(NetAppObject):
    """
    structure containing statistics for each NFS version
    """
    
    _nfsv4_client_stats = None
    @property
    def nfsv4_client_stats(self):
        """
        detailed statistics for NFSv4 operations
        """
        return self._nfsv4_client_stats
    @nfsv4_client_stats.setter
    def nfsv4_client_stats(self, val):
        if val != None:
            self.validate('nfsv4_client_stats', val)
        self._nfsv4_client_stats = val
    
    _calls_total = None
    @property
    def calls_total(self):
        """
        total NFS calls
        Range : [0..2^64-1].
        """
        return self._calls_total
    @calls_total.setter
    def calls_total(self, val):
        if val != None:
            self.validate('calls_total', val)
        self._calls_total = val
    
    _badcalls_total = None
    @property
    def badcalls_total(self):
        """
        total bad NFS calls
        Range : [0..2^32-1].
        """
        return self._badcalls_total
    @badcalls_total.setter
    def badcalls_total(self, val):
        if val != None:
            self.validate('badcalls_total', val)
        self._badcalls_total = val
    
    _nfsv3_client_stats = None
    @property
    def nfsv3_client_stats(self):
        """
        detailed statistics for NFSv3 operations
        """
        return self._nfsv3_client_stats
    @nfsv3_client_stats.setter
    def nfsv3_client_stats(self, val):
        if val != None:
            self.validate('nfsv3_client_stats', val)
        self._nfsv3_client_stats = val
    
    _nfsv2_client_stats = None
    @property
    def nfsv2_client_stats(self):
        """
        detailed statistics for NFSv2 operations
        """
        return self._nfsv2_client_stats
    @nfsv2_client_stats.setter
    def nfsv2_client_stats(self, val):
        if val != None:
            self.validate('nfsv2_client_stats', val)
        self._nfsv2_client_stats = val
    
    @staticmethod
    def get_api_name():
          return "nfs-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'nfsv4-client-stats',
            'calls-total',
            'badcalls-total',
            'nfsv3-client-stats',
            'nfsv2-client-stats',
        ]
    
    def describe_properties(self):
        return {
            'nfsv4_client_stats': { 'class': Nfsv4ClientStatsInfo, 'is_list': False, 'required': 'required' },
            'calls_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'badcalls_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'nfsv3_client_stats': { 'class': Nfsv3ClientStatsInfo, 'is_list': False, 'required': 'required' },
            'nfsv2_client_stats': { 'class': Nfsv2ClientStatsInfo, 'is_list': False, 'required': 'required' },
        }

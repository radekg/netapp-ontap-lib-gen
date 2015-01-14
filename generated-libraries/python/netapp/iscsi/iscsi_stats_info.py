from netapp.iscsi.iscsi_cdb_stats_info import IscsiCdbStatsInfo
from netapp.iscsi.iscsi_error_stats_info import IscsiErrorStatsInfo
from netapp.iscsi.iscsi_transmitted_stats_info import IscsiTransmittedStatsInfo
from netapp.iscsi.iscsi_received_stats_info import IscsiReceivedStatsInfo
from netapp.netapp_object import NetAppObject

class IscsiStatsInfo(NetAppObject):
    """
    Statistics block
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver hosting the iSCSI service.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _iscsi_cdb_stats = None
    @property
    def iscsi_cdb_stats(self):
        """
        Statistics of Command Descriptor Blocks.
        """
        return self._iscsi_cdb_stats
    @iscsi_cdb_stats.setter
    def iscsi_cdb_stats(self, val):
        if val != None:
            self.validate('iscsi_cdb_stats', val)
        self._iscsi_cdb_stats = val
    
    _iscsi_error_stats = None
    @property
    def iscsi_error_stats(self):
        """
        Statistics of errors.
        """
        return self._iscsi_error_stats
    @iscsi_error_stats.setter
    def iscsi_error_stats(self, val):
        if val != None:
            self.validate('iscsi_error_stats', val)
        self._iscsi_error_stats = val
    
    _iscsi_transmitted_stats = None
    @property
    def iscsi_transmitted_stats(self):
        """
        Statistics of PDUs transmitted.
        """
        return self._iscsi_transmitted_stats
    @iscsi_transmitted_stats.setter
    def iscsi_transmitted_stats(self, val):
        if val != None:
            self.validate('iscsi_transmitted_stats', val)
        self._iscsi_transmitted_stats = val
    
    _iscsi_received_stats = None
    @property
    def iscsi_received_stats(self):
        """
        Statistics of PDUs received.
        """
        return self._iscsi_received_stats
    @iscsi_received_stats.setter
    def iscsi_received_stats(self, val):
        if val != None:
            self.validate('iscsi_received_stats', val)
        self._iscsi_received_stats = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'iscsi-cdb-stats',
            'iscsi-error-stats',
            'iscsi-transmitted-stats',
            'iscsi-received-stats',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'iscsi_cdb_stats': { 'class': IscsiCdbStatsInfo, 'is_list': False, 'required': 'required' },
            'iscsi_error_stats': { 'class': IscsiErrorStatsInfo, 'is_list': False, 'required': 'required' },
            'iscsi_transmitted_stats': { 'class': IscsiTransmittedStatsInfo, 'is_list': False, 'required': 'required' },
            'iscsi_received_stats': { 'class': IscsiReceivedStatsInfo, 'is_list': False, 'required': 'required' },
        }

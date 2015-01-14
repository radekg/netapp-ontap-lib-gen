from netapp.netapp_object import NetAppObject

class DongleInfo(NetAppObject):
    """
    dongle information
    """
    
    _dongle_firmware_revision = None
    @property
    def dongle_firmware_revision(self):
        """
        Dongle firmware revision.
        Will be missing if not supported or not available.
        """
        return self._dongle_firmware_revision
    @dongle_firmware_revision.setter
    def dongle_firmware_revision(self, val):
        if val != None:
            self.validate('dongle_firmware_revision', val)
        self._dongle_firmware_revision = val
    
    _disable_reason = None
    @property
    def disable_reason(self):
        """
        If phy-state is "disabled", then this will give
        explanation as to the reason.
        Possible values:
        "manual", "no_drive", "brst_los", "los", "brst_rdd",
        "rdd", "brst_idd", "idd", "brst_prp", "prp", "brst_pcd",
        "pcd", "brst_crc", "crc", "osc", "mir", "rsrv", "man_smp",
        "clk_flt", "unknown".
        """
        return self._disable_reason
    @disable_reason.setter
    def disable_reason(self, val):
        if val != None:
            self.validate('disable_reason', val)
        self._disable_reason = val
    
    _dongle_type = None
    @property
    def dongle_type(self):
        """
        Dongle type. Possible values:
        "ss1300b", "sas", "sps3g",
        Will be missing if not supported or not available.
        """
        return self._dongle_type
    @dongle_type.setter
    def dongle_type(self, val):
        if val != None:
            self.validate('dongle_type', val)
        self._dongle_type = val
    
    @staticmethod
    def get_api_name():
          return "dongle-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'dongle-firmware-revision',
            'disable-reason',
            'dongle-type',
        ]
    
    def describe_properties(self):
        return {
            'dongle_firmware_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disable_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dongle_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

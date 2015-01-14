from netapp.netapp_object import NetAppObject

class InvalidCfmodeSettingInfo(NetAppObject):
    """
    local and partner cfmode settings
    """
    
    _local_fcp_cfmode = None
    @property
    def local_fcp_cfmode(self):
        """
        cfmode setting of the local filer
        Possible values: dual_fabric, mixed, partner, standby,
        single_image
        """
        return self._local_fcp_cfmode
    @local_fcp_cfmode.setter
    def local_fcp_cfmode(self, val):
        if val != None:
            self.validate('local_fcp_cfmode', val)
        self._local_fcp_cfmode = val
    
    _partner_fcp_cfmode = None
    @property
    def partner_fcp_cfmode(self):
        """
        cfmode setting of the partner filer
        Possible values: dual_fabric, mixed, partner, standby,
        single_image
        """
        return self._partner_fcp_cfmode
    @partner_fcp_cfmode.setter
    def partner_fcp_cfmode(self, val):
        if val != None:
            self.validate('partner_fcp_cfmode', val)
        self._partner_fcp_cfmode = val
    
    @staticmethod
    def get_api_name():
          return "invalid-cfmode-setting-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'local-fcp-cfmode',
            'partner-fcp-cfmode',
        ]
    
    def describe_properties(self):
        return {
            'local_fcp_cfmode': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'partner_fcp_cfmode': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

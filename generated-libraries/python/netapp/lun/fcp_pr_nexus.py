from netapp.netapp_object import NetAppObject

class FcpPrNexus(NetAppObject):
    """
    Information about fcp nexus owning the persistent reservation
    These two componients identify the relationship between the
    FCP initiator and the target.
    """
    
    _initiator_port = None
    @property
    def initiator_port(self):
        """
        FCP initiator port part of I_T_Nexus owning the
        persistent reservation key.
        """
        return self._initiator_port
    @initiator_port.setter
    def initiator_port(self, val):
        if val != None:
            self.validate('initiator_port', val)
        self._initiator_port = val
    
    _third_party_initiator_port = None
    @property
    def third_party_initiator_port(self):
        """
        The FCP port name (WWPN) of the third-party initiator the reservation
        is being held for. For use in SCSI-2 only.
        """
        return self._third_party_initiator_port
    @third_party_initiator_port.setter
    def third_party_initiator_port(self, val):
        if val != None:
            self.validate('third_party_initiator_port', val)
        self._third_party_initiator_port = val
    
    _target_port = None
    @property
    def target_port(self):
        """
        FCP target port part of I_T_Nexus owning the
        persistent reservation key.
        """
        return self._target_port
    @target_port.setter
    def target_port(self, val):
        if val != None:
            self.validate('target_port', val)
        self._target_port = val
    
    @staticmethod
    def get_api_name():
          return "fcp-pr-nexus"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-port',
            'third-party-initiator-port',
            'target-port',
        ]
    
    def describe_properties(self):
        return {
            'initiator_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'third_party_initiator_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'target_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

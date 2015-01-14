from netapp.netapp_object import NetAppObject

class IscsiPrNexus(NetAppObject):
    """
    Information about iscsi nexus owning the persistent reservation
    These three componients identify the relationship between the
    iSCSI initiator and the target.
    """
    
    _tpgtag = None
    @property
    def tpgtag(self):
        """
        The target portal group tag of the persistent
        reservation owner. For historical reasons, the
        value is represented as a 4-byte hexadecimal
        number in little-endian byte order.
        """
        return self._tpgtag
    @tpgtag.setter
    def tpgtag(self, val):
        if val != None:
            self.validate('tpgtag', val)
        self._tpgtag = val
    
    _tpgroup_tag = None
    @property
    def tpgroup_tag(self):
        """
        The target portal group tag of the
        persistent reservation owner.
        """
        return self._tpgroup_tag
    @tpgroup_tag.setter
    def tpgroup_tag(self, val):
        if val != None:
            self.validate('tpgroup_tag', val)
        self._tpgroup_tag = val
    
    _initiator = None
    @property
    def initiator(self):
        """
        Name of initiator holding the reservation
        i.e. iqn.1987-06.com.initvendor1:appsrv.sn.2346.
        """
        return self._initiator
    @initiator.setter
    def initiator(self, val):
        if val != None:
            self.validate('initiator', val)
        self._initiator = val
    
    _isid = None
    @property
    def isid(self):
        """
        The Initiator Session ID for the persistent reservation
        owner.  The ISID is a numeric Initiator Session ID
        assigned by the initiator which acts as part of the
        initiators identity.
        """
        return self._isid
    @isid.setter
    def isid(self, val):
        if val != None:
            self.validate('isid', val)
        self._isid = val
    
    _third_party_initiator_name = None
    @property
    def third_party_initiator_name(self):
        """
        The name of the third-party initiator the reservation
        is being held for. For use in SCSI-2 only.
        i.e. iqn.1987-06.com.initvendor1:appsrv.sn.2346.
        """
        return self._third_party_initiator_name
    @third_party_initiator_name.setter
    def third_party_initiator_name(self, val):
        if val != None:
            self.validate('third_party_initiator_name', val)
        self._third_party_initiator_name = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-pr-nexus"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'tpgtag',
            'tpgroup-tag',
            'initiator',
            'isid',
            'third-party-initiator-name',
        ]
    
    def describe_properties(self):
        return {
            'tpgtag': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tpgroup_tag': { 'class': int, 'is_list': False, 'required': 'optional' },
            'initiator': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'isid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'third_party_initiator_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

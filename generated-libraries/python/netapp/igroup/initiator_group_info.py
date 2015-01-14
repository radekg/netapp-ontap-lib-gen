from netapp.igroup.initiator_info import InitiatorInfo
from netapp.netapp_object import NetAppObject

class InitiatorGroupInfo(NetAppObject):
    """
    Information about an initiator group.
    """
    
    _initiator_group_alua_enabled = None
    @property
    def initiator_group_alua_enabled(self):
        """
        Boolean value to indicate if this initiator group
        has ALUA (Asymmetric Logical Unit Access) features
        enabled for luns mapped to this initiator group.
        """
        return self._initiator_group_alua_enabled
    @initiator_group_alua_enabled.setter
    def initiator_group_alua_enabled(self, val):
        if val != None:
            self.validate('initiator_group_alua_enabled', val)
        self._initiator_group_alua_enabled = val
    
    _initiator_group_throttle_borrow = None
    @property
    def initiator_group_throttle_borrow(self):
        """
        Boolean value to indicate that the igroups throttle
        reserve may be exceeded if the igroup attempts to use
        more than it has reserved.
        """
        return self._initiator_group_throttle_borrow
    @initiator_group_throttle_borrow.setter
    def initiator_group_throttle_borrow(self, val):
        if val != None:
            self.validate('initiator_group_throttle_borrow', val)
        self._initiator_group_throttle_borrow = val
    
    _initiator_group_use_partner = None
    @property
    def initiator_group_use_partner(self):
        """
        Boolean value to indicate if this initiator group
        is configured for its luns to require the use of
        host multi-pathing software for correct high-availability
        failover operation.
        In Data ONTAP 7-Mode, this value is optional and
        is only returned for FCP initiator groups on an storage
        system in an HA pair.
        In Data ONTAP Cluster-Mode, this field will always be 'true'.
        """
        return self._initiator_group_use_partner
    @initiator_group_use_partner.setter
    def initiator_group_use_partner(self, val):
        if val != None:
            self.validate('initiator_group_use_partner', val)
        self._initiator_group_use_partner = val
    
    _initiator_group_portset_name = None
    @property
    def initiator_group_portset_name(self):
        """
        Name of the portset that is bound to the initiator
        group, if any.
        """
        return self._initiator_group_portset_name
    @initiator_group_portset_name.setter
    def initiator_group_portset_name(self, val):
        if val != None:
            self.validate('initiator_group_portset_name', val)
        self._initiator_group_portset_name = val
    
    _initiator_group_type = None
    @property
    def initiator_group_type(self):
        """
        Type of the initiators in this group.
        Possible values: "iscsi", "fcp", "mixed".
        """
        return self._initiator_group_type
    @initiator_group_type.setter
    def initiator_group_type(self, val):
        if val != None:
            self.validate('initiator_group_type', val)
        self._initiator_group_type = val
    
    _initiator_group_vsa_enabled = None
    @property
    def initiator_group_vsa_enabled(self):
        """
        Boolean value to indicate if this initiator group
        has Volume Set Addressing (VSA) enabled or disabled.
        """
        return self._initiator_group_vsa_enabled
    @initiator_group_vsa_enabled.setter
    def initiator_group_vsa_enabled(self, val):
        if val != None:
            self.validate('initiator_group_vsa_enabled', val)
        self._initiator_group_vsa_enabled = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of the vserver hosting this initiator group
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _initiator_group_throttle_reserve = None
    @property
    def initiator_group_throttle_reserve(self):
        """
        Percentage of filer SCSI command blocks reserved
        for this initiator group's exclusive usage.
        """
        return self._initiator_group_throttle_reserve
    @initiator_group_throttle_reserve.setter
    def initiator_group_throttle_reserve(self, val):
        if val != None:
            self.validate('initiator_group_throttle_reserve', val)
        self._initiator_group_throttle_reserve = val
    
    _initiator_group_os_type = None
    @property
    def initiator_group_os_type(self):
        """
        OS type of the initiator group
        """
        return self._initiator_group_os_type
    @initiator_group_os_type.setter
    def initiator_group_os_type(self, val):
        if val != None:
            self.validate('initiator_group_os_type', val)
        self._initiator_group_os_type = val
    
    _lun_id = None
    @property
    def lun_id(self):
        """
        LUN identifier to which the LUN is mapped at the host.
        This value is optional and is only returned for the
        lun-map-list-info api.
        """
        return self._lun_id
    @lun_id.setter
    def lun_id(self, val):
        if val != None:
            self.validate('lun_id', val)
        self._lun_id = val
    
    _initiators = None
    @property
    def initiators(self):
        """
        List of initiators belonging to this group.
        """
        return self._initiators
    @initiators.setter
    def initiators(self, val):
        if val != None:
            self.validate('initiators', val)
        self._initiators = val
    
    _initiator_group_name = None
    @property
    def initiator_group_name(self):
        """
        Name of this initiator group.
        """
        return self._initiator_group_name
    @initiator_group_name.setter
    def initiator_group_name(self, val):
        if val != None:
            self.validate('initiator_group_name', val)
        self._initiator_group_name = val
    
    _initiator_group_report_scsi_name_enabled = None
    @property
    def initiator_group_report_scsi_name_enabled(self):
        """
        Boolean value to indicate whether to report or hide
        SCSI Name String (8h) Descriptor to initiator's
        INQUIRY VPD 0x83 page command. This field is available in
        Data ONTAP 8.1.0 and later.
        """
        return self._initiator_group_report_scsi_name_enabled
    @initiator_group_report_scsi_name_enabled.setter
    def initiator_group_report_scsi_name_enabled(self, val):
        if val != None:
            self.validate('initiator_group_report_scsi_name_enabled', val)
        self._initiator_group_report_scsi_name_enabled = val
    
    _initiator_group_uuid = None
    @property
    def initiator_group_uuid(self):
        """
        This value is Universally-unique identifier (UUID) of this
        initiator group.
        <p>
        The UUIDs are formatted as 36-character strings.  These
        strings are composed of 32 hexadecimal characters
        broken up into five groupings separated by '-'s.  The
        first grouping has 8 hexadecimal characters, the second through
        fourth groupings have four hexadecimal characters each, and the
        fifth and final grouping has 12 hexadecimal characters.  Note
        that a leading '0x' is not used.
        <p>
        This field is available in Data ONTAP 7-mode 7.3.6, 8.0.2, 8.1.0 and later
        for the igroup-list-info API.
        This field is available in Data ONTAP Cluster-Mode 8.1.0 and later for
        the igroup-get-iter and lun-map-list-info APIs.
        <p>
        Here is an example of an actual UUID:
        <p>
        <dl>
        <dt><dd> 35d6ca90-c759-11df-8b6d-00a098132c6c </dd><br></dt>
        </dl>
        """
        return self._initiator_group_uuid
    @initiator_group_uuid.setter
    def initiator_group_uuid(self, val):
        if val != None:
            self.validate('initiator_group_uuid', val)
        self._initiator_group_uuid = val
    
    @staticmethod
    def get_api_name():
          return "initiator-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-group-alua-enabled',
            'initiator-group-throttle-borrow',
            'initiator-group-use-partner',
            'initiator-group-portset-name',
            'initiator-group-type',
            'initiator-group-vsa-enabled',
            'vserver',
            'initiator-group-throttle-reserve',
            'initiator-group-os-type',
            'lun-id',
            'initiators',
            'initiator-group-name',
            'initiator-group-report-scsi-name-enabled',
            'initiator-group-uuid',
        ]
    
    def describe_properties(self):
        return {
            'initiator_group_alua_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'initiator_group_throttle_borrow': { 'class': bool, 'is_list': False, 'required': 'required' },
            'initiator_group_use_partner': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'initiator_group_portset_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'initiator_group_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_vsa_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'initiator_group_throttle_reserve': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_group_os_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'lun_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'initiators': { 'class': InitiatorInfo, 'is_list': True, 'required': 'optional' },
            'initiator_group_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_report_scsi_name_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'initiator_group_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

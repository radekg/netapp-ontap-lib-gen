from netapp.lun.iscsi_pr_nexus import IscsiPrNexus
from netapp.lun.fcp_pr_nexus import FcpPrNexus
from netapp.netapp_object import NetAppObject

class PersistentReservationInfo(NetAppObject):
    """
    Information about the persistent reservation
    """
    
    _iscsi_pr_nexus = None
    @property
    def iscsi_pr_nexus(self):
        """
        This is the I_T_Nexus info for an iscsi type
        reservation.
        """
        return self._iscsi_pr_nexus
    @iscsi_pr_nexus.setter
    def iscsi_pr_nexus(self, val):
        if val != None:
            self.validate('iscsi_pr_nexus', val)
        self._iscsi_pr_nexus = val
    
    _reservation_type = None
    @property
    def reservation_type(self):
        """
        Type of persistent reservation. Possible values:
        "fcp", "iscsi".
        """
        return self._reservation_type
    @reservation_type.setter
    def reservation_type(self, val):
        if val != None:
            self.validate('reservation_type', val)
        self._reservation_type = val
    
    _reservation_type_code = None
    @property
    def reservation_type_code(self):
        """
        Type of persistent reservation held by the I_T_Nexus,
        if any.  Please refer to the SCSI Primary Command (SPC)
        specification for full details on reservation types.
        Possible values:
        <ul>
        <li> "read shared",</li>
        <li> "write exclusive",</li>
        <li> "exclusive access",</li>
        <li> "write exclusive registrants only",</li>
        <li> "exclusive access registrants only",</li>
        <li> "write exclusive all registrants",</li>
        <li> "exclusive access all registrants".</li>
        </ul>
        """
        return self._reservation_type_code
    @reservation_type_code.setter
    def reservation_type_code(self, val):
        if val != None:
            self.validate('reservation_type_code', val)
        self._reservation_type_code = val
    
    _fcp_pr_nexus = None
    @property
    def fcp_pr_nexus(self):
        """
        This is the I_T_Nexus info for an fcp type
        reservation.
        """
        return self._fcp_pr_nexus
    @fcp_pr_nexus.setter
    def fcp_pr_nexus(self, val):
        if val != None:
            self.validate('fcp_pr_nexus', val)
        self._fcp_pr_nexus = val
    
    _scsi_revision = None
    @property
    def scsi_revision(self):
        """
        The SCSI specification revision for the reservation.
        Possible values: "scsi2", "scsi3".
        """
        return self._scsi_revision
    @scsi_revision.setter
    def scsi_revision(self, val):
        if val != None:
            self.validate('scsi_revision', val)
        self._scsi_revision = val
    
    _reservation_key = None
    @property
    def reservation_key(self):
        """
        Value of persistent reservation key that is registered
        for the given lun.
        """
        return self._reservation_key
    @reservation_key.setter
    def reservation_key(self, val):
        if val != None:
            self.validate('reservation_key', val)
        self._reservation_key = val
    
    @staticmethod
    def get_api_name():
          return "persistent-reservation-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'iscsi-pr-nexus',
            'reservation-type',
            'reservation-type-code',
            'fcp-pr-nexus',
            'scsi-revision',
            'reservation-key',
        ]
    
    def describe_properties(self):
        return {
            'iscsi_pr_nexus': { 'class': IscsiPrNexus, 'is_list': False, 'required': 'optional' },
            'reservation_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'reservation_type_code': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fcp_pr_nexus': { 'class': FcpPrNexus, 'is_list': False, 'required': 'optional' },
            'scsi_revision': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'reservation_key': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

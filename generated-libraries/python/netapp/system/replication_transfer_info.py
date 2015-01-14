from netapp.netapp_object import NetAppObject

class ReplicationTransferInfo(NetAppObject):
    """
    Structure of each entry in the transfer accounting table
    """
    
    _replication_type = None
    @property
    def replication_type(self):
        """
        Type of replication operation.
        Qtree-snapmirror/SnapVault have two core data transfer mechanisms
        which they can utilize for data transfer. One is the legacy engine
        and the other is the newer engine. By default Data ONTAP enables
        the new engine. The user can choose to flip between the new engine
        and legacy engine. options-get api with an input of
        replication.logical.transfer_limits can be used to detect the
        type of engine. "current" implies a new engine while "previous"
        implies the legacy engine. Open Systems SnapVault (OSSV) always
        uses the legacy engine for transfers.
        Legacy volume-snapmirror limits are used when data resides on a
        traditional volume.
        Possible values of a replication operation are
        <ul>
        <li> "legacy_qtree_snapmirror_source";
        <li> "legacy_qtree_snapmirror_destination";
        <li> "qtree_snapmirror_source";
        <li> "qtree_snapmirror_destination";
        <li> "legacy_volume_snapmirror_source";
        <li> "legacy_volume_snapmirror_destination";
        <li> "volume_snapmirror_source";
        <li> "volume_snapmirror_destination";
        <li> "legacy_snapvault_source";
        <li> "legacy_snapvault_destination";
        <li> "snapvault_source";
        <li> "snapvault_destination";
        <li> "sync_snapmirror_source";
        <li> "sync_snapmirror_destination";
        <li> "volume_copy_source";
        <li> "volume_copy_destination";
        </ul>
        """
        return self._replication_type
    @replication_type.setter
    def replication_type(self, val):
        if val != None:
            self.validate('replication_type', val)
        self._replication_type = val
    
    _replication_available_transfers = None
    @property
    def replication_available_transfers(self):
        """
        Number of transfers that could be started at this point in
        time, if we choose only this particular replication type.
        Range:[0..2^32-1]
        """
        return self._replication_available_transfers
    @replication_available_transfers.setter
    def replication_available_transfers(self, val):
        if val != None:
            self.validate('replication_available_transfers', val)
        self._replication_available_transfers = val
    
    _replication_maximum_transfers = None
    @property
    def replication_maximum_transfers(self):
        """
        Maximum number of transfers that can be started, if we choose
        only this particular replication type.
        Range:[1..2^32-1]
        """
        return self._replication_maximum_transfers
    @replication_maximum_transfers.setter
    def replication_maximum_transfers(self, val):
        if val != None:
            self.validate('replication_maximum_transfers', val)
        self._replication_maximum_transfers = val
    
    @staticmethod
    def get_api_name():
          return "replication-transfer-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'replication-type',
            'replication-available-transfers',
            'replication-maximum-transfers',
        ]
    
    def describe_properties(self):
        return {
            'replication_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'replication_available_transfers': { 'class': int, 'is_list': False, 'required': 'required' },
            'replication_maximum_transfers': { 'class': int, 'is_list': False, 'required': 'required' },
        }

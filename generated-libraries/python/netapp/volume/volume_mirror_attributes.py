from netapp.netapp_object import NetAppObject

class VolumeMirrorAttributes(NetAppObject):
    """
    Information about the volume mirror.
    """
    
    _mirror_transfer_in_progress = None
    @property
    def mirror_transfer_in_progress(self):
        """
        True if a SnapMirror transfer is in progress on this
        mirrored volume.
        <p>
        This mirror's active filesystem can be inconsistent
        during snapmirror transfer.  As a result, snapshot create
        operation is temporary disabled on this mirror until the
        current transfer session finishes.
        <p>
        This field is set to true at the start of a SnapMirror
        transfer session and set to false at the end of that
        session.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._mirror_transfer_in_progress
    @mirror_transfer_in_progress.setter
    def mirror_transfer_in_progress(self, val):
        if val != None:
            self.validate('mirror_transfer_in_progress', val)
        self._mirror_transfer_in_progress = val
    
    _is_move_mirror = None
    @property
    def is_move_mirror(self):
        """
        True if this is a volume move mirror.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_move_mirror
    @is_move_mirror.setter
    def is_move_mirror(self, val):
        if val != None:
            self.validate('is_move_mirror', val)
        self._is_move_mirror = val
    
    _redirect_snapshot_id = None
    @property
    def redirect_snapshot_id(self):
        """
        If the volume is a logical mirror destination or is in
        the process of being made one, this field indicates the
        logical-id of the snapshot to which clients are to be
        redirected.
        <p>
        If modifiable, when setting this attribute, invalid
        snapshot id or a non-existent snapshot id specified will
        be rejected with error ESNAPSHOTDOESNOTEXIST. Failure to
        set ('stamp') the attribute in the volume will cause
        error ESTAMPREDIRECTSNAPIDERROR to be returned. This
        field can be set only for online volumes. This option is
        valid only in Cluster-Mode. The volume can be set to have
        no redirection snapshot by using a value of 0. This
        option can be set only for Cluster-Mode volumes
        participating in a logical-mirror relationship. Setting
        this field on a Cluster-Mode volume which is not a
        logical mirror destination (yet) will not have any impact
        on client access or the volume's behavior. The client
        access will be impacted with regard to this value only
        when the volume is converted to a logical-mirror
        destination.
        <p>
        When reading this attribute, the value of 0 indicates
        volume has no redirection snapshot. The field cannot be
        interpreted authoritatively if the volume is offline or
        restricted.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._redirect_snapshot_id
    @redirect_snapshot_id.setter
    def redirect_snapshot_id(self, val):
        if val != None:
            self.validate('redirect_snapshot_id', val)
        self._redirect_snapshot_id = val
    
    _is_replica_volume = None
    @property
    def is_replica_volume(self):
        """
        True if this is a read only replica volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_replica_volume
    @is_replica_volume.setter
    def is_replica_volume(self, val):
        if val != None:
            self.validate('is_replica_volume', val)
        self._is_replica_volume = val
    
    _is_data_protection_mirror = None
    @property
    def is_data_protection_mirror(self):
        """
        True if this is a data protection mirror.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_data_protection_mirror
    @is_data_protection_mirror.setter
    def is_data_protection_mirror(self, val):
        if val != None:
            self.validate('is_data_protection_mirror', val)
        self._is_data_protection_mirror = val
    
    _is_load_sharing_mirror = None
    @property
    def is_load_sharing_mirror(self):
        """
        True if this is a load sharing mirror.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_load_sharing_mirror
    @is_load_sharing_mirror.setter
    def is_load_sharing_mirror(self, val):
        if val != None:
            self.validate('is_load_sharing_mirror', val)
        self._is_load_sharing_mirror = val
    
    @staticmethod
    def get_api_name():
          return "volume-mirror-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'mirror-transfer-in-progress',
            'is-move-mirror',
            'redirect-snapshot-id',
            'is-replica-volume',
            'is-data-protection-mirror',
            'is-load-sharing-mirror',
        ]
    
    def describe_properties(self):
        return {
            'mirror_transfer_in_progress': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_move_mirror': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'redirect_snapshot_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_replica_volume': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_data_protection_mirror': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_load_sharing_mirror': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

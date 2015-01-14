from netapp.netapp_object import NetAppObject

class VolumeStateAttributes(NetAppObject):
    """
    Information about the state or status of a volume or its
    features.
    """
    
    _ignore_inconsistent = None
    @property
    def ignore_inconsistent(self):
        """
        If true, then the volume can be brought online when
        booting even if it is marked as inconsistent. The user is
        cautioned that bringing it online prior to running
        wafliron may result in further file system
        inconsistency.
        <p>
        By default, this field is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._ignore_inconsistent
    @ignore_inconsistent.setter
    def ignore_inconsistent(self, val):
        if val != None:
            self.validate('ignore_inconsistent', val)
        self._ignore_inconsistent = val
    
    _is_nvfail_enabled = None
    @property
    def is_nvfail_enabled(self):
        """
        If true, the controller performs additional work at boot
        and takeover times if it finds that there has been any
        potential data loss in this volume due to an NVRAM
        failure.
        <p>
        For 7-Mode volumes, it causes the invalidation of all NFS
        file handles on all volumes affected by the problem so
        that client-side users are forced to remount the affected
        file system (and thus not continue to use potentially
        incorrect data).
        <p>
        It is also possible to specify a set of files per volume
        that are to be renamed out of the way in these cases.
        The controller sends error messages to the console
        whenever such problems are found.
        <p>
        For Cluster-Mode volumes, the volume would be put in a
        special state called 'in-nvfailed-state' such that
        protocol access is blocked. This will cause the client
        applications to crash and thus prevent access to stale
        data on the volume.
        <p>
        To get out of this situation, the admin needs to manually
        clear the 'in-nvfailed-state' on the volume.
        <p>
        By default, this value is false.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._is_nvfail_enabled
    @is_nvfail_enabled.setter
    def is_nvfail_enabled(self, val):
        if val != None:
            self.validate('is_nvfail_enabled', val)
        self._is_nvfail_enabled = val
    
    _is_node_root = None
    @property
    def is_node_root(self):
        """
        If true, this volume is the root volume of the node in
        which it resides.
        <p>
        Only the node's internal logic can change this option's
        value from true to false; this happens when some other
        volume has the value set to true.
        <p>
        By default, this field is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_node_root
    @is_node_root.setter
    def is_node_root(self, val):
        if val != None:
            self.validate('is_node_root', val)
        self._is_node_root = val
    
    _in_nvfailed_state = None
    @property
    def in_nvfailed_state(self):
        """
        The user can only clear this state and never set it. The
        file system will set this state on the volume if NVFAIL
        event occurs. So long as the volume is in this state, all
        protocol Ops with a special SpinNP flag set are blocked.
        By clearing this state on the volume, the admin will
        allow protocol access to the data on the volume and can
        initiate the recovery process.
        <p>
        By default, this field is false.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._in_nvfailed_state
    @in_nvfailed_state.setter
    def in_nvfailed_state(self, val):
        if val != None:
            self.validate('in_nvfailed_state', val)
        self._in_nvfailed_state = val
    
    _state = None
    @property
    def state(self):
        """
        Volume State.
        <p>
        Possible values:
        <ul>
        <li> 'online',
        <li> 'restricted',
        <li> 'offline',
        <li> 'mixed'
        </ul>
        <p>
        If an Infinite Volumes constituents are not all in the
        same state,
        it will return 'mixed'. The 'mixed' state is read-only.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _is_vserver_root = None
    @property
    def is_vserver_root(self):
        """
        If true, this volume is the namespace root volume of the
        Vserver which owns this volume. The default value is
        false.
        <p>
        When creating a volume, if this field is set to true, the
        new volume is to become the new namespace root volume of
        the Vserver. This field can be used in a recovery
        scenario in which the namespace root volume of the
        Vserver becomes unrecoverable.
        <p>
        Attributes: optional-for-create, non-modifiable
        """
        return self._is_vserver_root
    @is_vserver_root.setter
    def is_vserver_root(self, val):
        if val != None:
            self.validate('is_vserver_root', val)
        self._is_vserver_root = val
    
    _become_node_root_after_reboot = None
    @property
    def become_node_root_after_reboot(self):
        """
        Whether this non node-root volume has been marked as the
        one that will become the node root volume the next time
        the hosting controller is rebooted.  Only one volume at a
        time may have this marking on any given controller.  This
        field is not directly settable.  Instead, a legal request
        to set the 'is-node-root' attribute (if modifiable)
        causes this field to be set.  Note that marking a volume
        that is already the node root volume as the new node root
        has no net effect.
        <p>
        By default, this field is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._become_node_root_after_reboot
    @become_node_root_after_reboot.setter
    def become_node_root_after_reboot(self, val):
        if val != None:
            self.validate('become_node_root_after_reboot', val)
        self._become_node_root_after_reboot = val
    
    _is_moving = None
    @property
    def is_moving(self):
        """
        Is the given volume moving? If true, this volume is
        moving from one aggregate to another aggregate in the
        cluster. The aggregates can be on different nodes of the
        cluster.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_moving
    @is_moving.setter
    def is_moving(self, val):
        if val != None:
            self.validate('is_moving', val)
        self._is_moving = val
    
    _is_inconsistent = None
    @property
    def is_inconsistent(self):
        """
        Whether or not there is known inconsistency in the file
        system associated with the volume. By default, the value
        is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_inconsistent
    @is_inconsistent.setter
    def is_inconsistent(self, val):
        if val != None:
            self.validate('is_inconsistent', val)
        self._is_inconsistent = val
    
    _is_unrecoverable = None
    @property
    def is_unrecoverable(self):
        """
        Whether or not there is known inconsistency in the
        associated file system and it is not recoverable. This
        field is valid only for flexible volumes.
        <p>
        By default, this field is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_unrecoverable
    @is_unrecoverable.setter
    def is_unrecoverable(self, val):
        if val != None:
            self.validate('is_unrecoverable', val)
        self._is_unrecoverable = val
    
    _is_junction_active = None
    @property
    def is_junction_active(self):
        """
        This field indicates whether the mounted volume is
        accessible. The default is true. If the mounted path is
        not accessible, the volume does not appear in the owning
        Vserver's namespace. This field applies only to
        Cluster-Mode volumes.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._is_junction_active
    @is_junction_active.setter
    def is_junction_active(self, val):
        if val != None:
            self.validate('is_junction_active', val)
        self._is_junction_active = val
    
    _is_quiesced_in_memory = None
    @property
    def is_quiesced_in_memory(self):
        """
        Is the given volume quiesced? If true, this volume is in
        an (in-memory) quiesced state in which most operations on
        the volume are blocked except for certain internal
        operations. By default, this value is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_quiesced_in_memory
    @is_quiesced_in_memory.setter
    def is_quiesced_in_memory(self, val):
        if val != None:
            self.validate('is_quiesced_in_memory', val)
        self._is_quiesced_in_memory = val
    
    _is_invalid = None
    @property
    def is_invalid(self):
        """
        Whether or not this volume is invalid. Volumes typically
        become invalid as a result of an aborted 'vol copy' or
        SnapMirror(R) initial transfer.  In such a case, a volume
        is in a half-created state and cannot be recovered. By
        default, the value is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_invalid
    @is_invalid.setter
    def is_invalid(self, val):
        if val != None:
            self.validate('is_invalid', val)
        self._is_invalid = val
    
    _is_cluster_volume = None
    @property
    def is_cluster_volume(self):
        """
        Indicates whether this volume is a Cluster-Mode volume,
        namely one that is owned by cluster authorities and
        agents.  These same clustering agents also provide all
        protocol services for this class of volume.
        <p>
        Cluster-Mode volumes are not supported in 7-Mode Data
        ONTAP deployments. All such volumes are forced offline
        whenever they are detected in that environment.
        <p>
        Similarly, all 7-Mode volumes on a Data ONTAP
        Cluster-Mode system (except each controller's root
        volume) are by default forced offline.  There are
        exceptions, in particular when a 7-Mode volume is being
        prepared to become that controller's new root volume in a
        recovery scenario.
        <p>
        At the moment, traditional volumes cannot be Cluster-Mode
        volumes.
        <p>
        By default, this field is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_cluster_volume
    @is_cluster_volume.setter
    def is_cluster_volume(self, val):
        if val != None:
            self.validate('is_cluster_volume', val)
        self._is_cluster_volume = val
    
    _is_constituent = None
    @property
    def is_constituent(self):
        """
        This field indicates if this volume is a constituent
        within another volume. For an Infinite Volume, this field
        is true for all its constituents (namespace as well as
        data). This field is set to false for volumes which are
        not the constituents of an Infinite Volume.
        <p>
        The default value is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_constituent
    @is_constituent.setter
    def is_constituent(self, val):
        if val != None:
            self.validate('is_constituent', val)
        self._is_constituent = val
    
    _is_volume_in_cutover = None
    @property
    def is_volume_in_cutover(self):
        """
        Is the given volume move operation in cutover phase? If
        true, this volume is moving from one aggregate to another
        aggregate in the cluster and is in cutover phase. The
        aggregates can be on different nodes of the cluster.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_volume_in_cutover
    @is_volume_in_cutover.setter
    def is_volume_in_cutover(self, val):
        if val != None:
            self.validate('is_volume_in_cutover', val)
        self._is_volume_in_cutover = val
    
    _is_quiesced_on_disk = None
    @property
    def is_quiesced_on_disk(self):
        """
        Is the given volume quiesced? If true, this volume is in
        an (on-disk) quiesced state in which most operations on
        the volume are blocked except for certain internal
        operations. By default, this value is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_quiesced_on_disk
    @is_quiesced_on_disk.setter
    def is_quiesced_on_disk(self, val):
        if val != None:
            self.validate('is_quiesced_on_disk', val)
        self._is_quiesced_on_disk = val
    
    @staticmethod
    def get_api_name():
          return "volume-state-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ignore-inconsistent',
            'is-nvfail-enabled',
            'is-node-root',
            'in-nvfailed-state',
            'state',
            'is-vserver-root',
            'become-node-root-after-reboot',
            'is-moving',
            'is-inconsistent',
            'is-unrecoverable',
            'is-junction-active',
            'is-quiesced-in-memory',
            'is-invalid',
            'is-cluster-volume',
            'is-constituent',
            'is-volume-in-cutover',
            'is-quiesced-on-disk',
        ]
    
    def describe_properties(self):
        return {
            'ignore_inconsistent': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nvfail_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_node_root': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'in_nvfailed_state': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_vserver_root': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'become_node_root_after_reboot': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_moving': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_inconsistent': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_unrecoverable': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_junction_active': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_quiesced_in_memory': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_invalid': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_cluster_volume': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_constituent': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_volume_in_cutover': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_quiesced_on_disk': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

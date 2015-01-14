from netapp.netapp_object import NetAppObject

class NfsInfo(NetAppObject):
    """
    Information about NFS server configuration
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _is_nfsv3_connection_drop_enabled = None
    @property
    def is_nfsv3_connection_drop_enabled(self):
        """
        If 'true', then connection is dropped when an NFSv3
        request is dropped. Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv3_connection_drop_enabled
    @is_nfsv3_connection_drop_enabled.setter
    def is_nfsv3_connection_drop_enabled(self, val):
        if val != None:
            self.validate('is_nfsv3_connection_drop_enabled', val)
        self._is_nfsv3_connection_drop_enabled = val
    
    _is_nfsv3_enabled = None
    @property
    def is_nfsv3_enabled(self):
        """
        If 'true', then NFS version 3 is enabled. Default value
        is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv3_enabled
    @is_nfsv3_enabled.setter
    def is_nfsv3_enabled(self, val):
        if val != None:
            self.validate('is_nfsv3_enabled', val)
        self._is_nfsv3_enabled = val
    
    _default_windows_user = None
    @property
    def default_windows_user(self):
        """
        The default windows user for CIFS access.
        Attributes: optional-for-create, modifiable
        """
        return self._default_windows_user
    @default_windows_user.setter
    def default_windows_user(self, val):
        if val != None:
            self.validate('default_windows_user', val)
        self._default_windows_user = val
    
    _is_nfsv41_acl_preserve_enabled = None
    @property
    def is_nfsv41_acl_preserve_enabled(self):
        """
        If 'true', the NFSv4 server will preserve and modify ACL
        when chmod <mode> is done. Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_acl_preserve_enabled
    @is_nfsv41_acl_preserve_enabled.setter
    def is_nfsv41_acl_preserve_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_acl_preserve_enabled', val)
        self._is_nfsv41_acl_preserve_enabled = val
    
    _is_nfsv40_referrals_enabled = None
    @property
    def is_nfsv40_referrals_enabled(self):
        """
        If 'true', then NFSv4.0 Referrals feature is enabled.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv40_referrals_enabled
    @is_nfsv40_referrals_enabled.setter
    def is_nfsv40_referrals_enabled(self, val):
        if val != None:
            self.validate('is_nfsv40_referrals_enabled', val)
        self._is_nfsv40_referrals_enabled = val
    
    _is_nfsv41_pnfs_enabled = None
    @property
    def is_nfsv41_pnfs_enabled(self):
        """
        If 'true', then Parallel NFS support for NFS version 4.1
        is enabled. Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_pnfs_enabled
    @is_nfsv41_pnfs_enabled.setter
    def is_nfsv41_pnfs_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_pnfs_enabled', val)
        self._is_nfsv41_pnfs_enabled = val
    
    _is_nfsv40_migration_enabled = None
    @property
    def is_nfsv40_migration_enabled(self):
        """
        If 'true', then NFSv4.0 Migration feature is enabled.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv40_migration_enabled
    @is_nfsv40_migration_enabled.setter
    def is_nfsv40_migration_enabled(self, val):
        if val != None:
            self.validate('is_nfsv40_migration_enabled', val)
        self._is_nfsv40_migration_enabled = val
    
    _chown_mode = None
    @property
    def chown_mode(self):
        """
        Vserver Change Ownership Mode. Possible values are
        'ignore', 'fail', 'use_export_policy'. If
        'use_export_policy' is set, export policy option is used.
        Default value is 'use_export_policy'.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "restricted"          ,
        <li> "unrestricted"        ,
        <li> "use_export_policy"
        </ul>
        """
        return self._chown_mode
    @chown_mode.setter
    def chown_mode(self, val):
        if val != None:
            self.validate('chown_mode', val)
        self._chown_mode = val
    
    _is_nfsv41_referrals_enabled = None
    @property
    def is_nfsv41_referrals_enabled(self):
        """
        If 'true', then NFSv4.1 Referrals feature is enabled.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_referrals_enabled
    @is_nfsv41_referrals_enabled.setter
    def is_nfsv41_referrals_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_referrals_enabled', val)
        self._is_nfsv41_referrals_enabled = val
    
    _nfsv41_implementation_id_domain = None
    @property
    def nfsv41_implementation_id_domain(self):
        """
        NFSv4.1 Implementation id domain. Default value is
        'defaultv41impliddomain.com'.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv41_implementation_id_domain
    @nfsv41_implementation_id_domain.setter
    def nfsv41_implementation_id_domain(self, val):
        if val != None:
            self.validate('nfsv41_implementation_id_domain', val)
        self._nfsv41_implementation_id_domain = val
    
    _nfsv41_implementation_id_name = None
    @property
    def nfsv41_implementation_id_name(self):
        """
        NFSv4.1 Implementation id name. Default value is
        'defaultv41implidname'.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv41_implementation_id_name
    @nfsv41_implementation_id_name.setter
    def nfsv41_implementation_id_name(self, val):
        if val != None:
            self.validate('nfsv41_implementation_id_name', val)
        self._nfsv41_implementation_id_name = val
    
    _is_nfsv4_numeric_ids_enabled = None
    @property
    def is_nfsv4_numeric_ids_enabled(self):
        """
        If 'true', then NFSv4 support for Numeric Owner IDs is
        enabled. Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv4_numeric_ids_enabled
    @is_nfsv4_numeric_ids_enabled.setter
    def is_nfsv4_numeric_ids_enabled(self, val):
        if val != None:
            self.validate('is_nfsv4_numeric_ids_enabled', val)
        self._is_nfsv4_numeric_ids_enabled = val
    
    _is_nfsv40_acl_enabled = None
    @property
    def is_nfsv40_acl_enabled(self):
        """
        If 'true', then NFSv4.0 ACL feature is enabled. Default
        value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv40_acl_enabled
    @is_nfsv40_acl_enabled.setter
    def is_nfsv40_acl_enabled(self, val):
        if val != None:
            self.validate('is_nfsv40_acl_enabled', val)
        self._is_nfsv40_acl_enabled = val
    
    _is_nfs_access_enabled = None
    @property
    def is_nfs_access_enabled(self):
        """
        If 'true',then NFS server access is enabled. Default
        value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfs_access_enabled
    @is_nfs_access_enabled.setter
    def is_nfs_access_enabled(self, val):
        if val != None:
            self.validate('is_nfs_access_enabled', val)
        self._is_nfs_access_enabled = val
    
    _rpcsec_ctx_idle = None
    @property
    def rpcsec_ctx_idle(self):
        """
        Time in seconds before an idle entry in RPCSEC_GSS
        context cache is deleted. Default value is 0.
        Attributes: optional-for-create, modifiable
        """
        return self._rpcsec_ctx_idle
    @rpcsec_ctx_idle.setter
    def rpcsec_ctx_idle(self, val):
        if val != None:
            self.validate('rpcsec_ctx_idle', val)
        self._rpcsec_ctx_idle = val
    
    _is_nfsv2_enabled = None
    @property
    def is_nfsv2_enabled(self):
        """
        Starting Data ONTAP 8.2, NFS v2 is no longer supported.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv2_enabled
    @is_nfsv2_enabled.setter
    def is_nfsv2_enabled(self, val):
        if val != None:
            self.validate('is_nfsv2_enabled', val)
        self._is_nfsv2_enabled = val
    
    _nfsv4_acl_max_aces = None
    @property
    def nfsv4_acl_max_aces(self):
        """
        Maximum Number of ACEs allowed in an ACL. Range is 192 to
        1024. Default value is 400.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv4_acl_max_aces
    @nfsv4_acl_max_aces.setter
    def nfsv4_acl_max_aces(self, val):
        if val != None:
            self.validate('nfsv4_acl_max_aces', val)
        self._nfsv4_acl_max_aces = val
    
    _is_nfsv4_fsid_change_enabled = None
    @property
    def is_nfsv4_fsid_change_enabled(self):
        """
        If 'true', then clients see change in FSID as NFSv4
        clients traverse filesystems. Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv4_fsid_change_enabled
    @is_nfsv4_fsid_change_enabled.setter
    def is_nfsv4_fsid_change_enabled(self, val):
        if val != None:
            self.validate('is_nfsv4_fsid_change_enabled', val)
        self._is_nfsv4_fsid_change_enabled = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _is_qtree_export_enabled = None
    @property
    def is_qtree_export_enabled(self):
        """
        If 'true', then the Vserver allows qtree exports
        (read-only). Default value is 'false'.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_qtree_export_enabled
    @is_qtree_export_enabled.setter
    def is_qtree_export_enabled(self, val):
        if val != None:
            self.validate('is_qtree_export_enabled', val)
        self._is_qtree_export_enabled = val
    
    _is_nfsv40_req_open_confirm_enabled = None
    @property
    def is_nfsv40_req_open_confirm_enabled(self):
        """
        If 'true', then the server will require an OPEN_CONFIRM
        operation for all NFSv4.0 clients. Default value is
        'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv40_req_open_confirm_enabled
    @is_nfsv40_req_open_confirm_enabled.setter
    def is_nfsv40_req_open_confirm_enabled(self, val):
        if val != None:
            self.validate('is_nfsv40_req_open_confirm_enabled', val)
        self._is_nfsv40_req_open_confirm_enabled = val
    
    _nfsv4_id_domain = None
    @property
    def nfsv4_id_domain(self):
        """
        NFSv4 ID mapping domain. Default value is
        'defaultv4iddomain.com'.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv4_id_domain
    @nfsv4_id_domain.setter
    def nfsv4_id_domain(self, val):
        if val != None:
            self.validate('nfsv4_id_domain', val)
        self._nfsv4_id_domain = val
    
    _is_nfsv40_read_delegation_enabled = None
    @property
    def is_nfsv40_read_delegation_enabled(self):
        """
        If 'true', NFSv4.0 read delegation feature is enabled.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv40_read_delegation_enabled
    @is_nfsv40_read_delegation_enabled.setter
    def is_nfsv40_read_delegation_enabled(self, val):
        if val != None:
            self.validate('is_nfsv40_read_delegation_enabled', val)
        self._is_nfsv40_read_delegation_enabled = val
    
    _is_nfs_rootonly_enabled = None
    @property
    def is_nfs_rootonly_enabled(self):
        """
        If 'true', then the vserver allows NFS protocol calls
        only from privileged ports (port numbers less than 1024).
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfs_rootonly_enabled
    @is_nfs_rootonly_enabled.setter
    def is_nfs_rootonly_enabled(self, val):
        if val != None:
            self.validate('is_nfs_rootonly_enabled', val)
        self._is_nfs_rootonly_enabled = val
    
    _is_nfsv41_pnfs_striped_volumes_enabled = None
    @property
    def is_nfsv41_pnfs_striped_volumes_enabled(self):
        """
        If 'true', Striped volume support for Parallel NFS is
        enabled . Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_pnfs_striped_volumes_enabled
    @is_nfsv41_pnfs_striped_volumes_enabled.setter
    def is_nfsv41_pnfs_striped_volumes_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_pnfs_striped_volumes_enabled', val)
        self._is_nfsv41_pnfs_striped_volumes_enabled = val
    
    _nfsv41_implementation_id_time = None
    @property
    def nfsv41_implementation_id_time(self):
        """
        NFSv4.1 Implementation id time.The number of seconds
        since January 1, 1970.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv41_implementation_id_time
    @nfsv41_implementation_id_time.setter
    def nfsv41_implementation_id_time(self, val):
        if val != None:
            self.validate('nfsv41_implementation_id_time', val)
        self._nfsv41_implementation_id_time = val
    
    _is_nfsv41_acl_enabled = None
    @property
    def is_nfsv41_acl_enabled(self):
        """
        If 'true', then NFSv4.1 ACL feature is enabled. Default
        value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_acl_enabled
    @is_nfsv41_acl_enabled.setter
    def is_nfsv41_acl_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_acl_enabled', val)
        self._is_nfsv41_acl_enabled = val
    
    _is_nfsv40_write_delegation_enabled = None
    @property
    def is_nfsv40_write_delegation_enabled(self):
        """
        If 'true', NFSv4.0 write delegation feature is enabled.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv40_write_delegation_enabled
    @is_nfsv40_write_delegation_enabled.setter
    def is_nfsv40_write_delegation_enabled(self, val):
        if val != None:
            self.validate('is_nfsv40_write_delegation_enabled', val)
        self._is_nfsv40_write_delegation_enabled = val
    
    _ntfs_unix_security_ops = None
    @property
    def ntfs_unix_security_ops(self):
        """
        Ignore/Fail unix security operations on NTFS volumes.
        Possible values are 'ignore', 'fail','use_export_policy'.
        If 'use_export_policy' is set, export policy option is
        used.  Default value is 'use_export_policy'.
        Attributes: optional-for-create, modifiable
        """
        return self._ntfs_unix_security_ops
    @ntfs_unix_security_ops.setter
    def ntfs_unix_security_ops(self, val):
        if val != None:
            self.validate('ntfs_unix_security_ops', val)
        self._ntfs_unix_security_ops = val
    
    _is_mount_rootonly_enabled = None
    @property
    def is_mount_rootonly_enabled(self):
        """
        If 'true', then the vserver allows MOUNT protocol calls
        only from privileged ports (port numbers less than 1024).
        Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_mount_rootonly_enabled
    @is_mount_rootonly_enabled.setter
    def is_mount_rootonly_enabled(self, val):
        if val != None:
            self.validate('is_mount_rootonly_enabled', val)
        self._is_mount_rootonly_enabled = val
    
    _nfsv4x_session_num_slots = None
    @property
    def nfsv4x_session_num_slots(self):
        """
        Number of Slots in the NFSv4.x Session Slot Tables.
        Default value is 180.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv4x_session_num_slots
    @nfsv4x_session_num_slots.setter
    def nfsv4x_session_num_slots(self, val):
        if val != None:
            self.validate('nfsv4x_session_num_slots', val)
        self._nfsv4x_session_num_slots = val
    
    _enable_ejukebox = None
    @property
    def enable_ejukebox(self):
        """
        If 'true', then the NFS server will send EJUKEBOX error
        on server delays.
        Attributes: optional-for-create, modifiable
        """
        return self._enable_ejukebox
    @enable_ejukebox.setter
    def enable_ejukebox(self, val):
        if val != None:
            self.validate('enable_ejukebox', val)
        self._enable_ejukebox = val
    
    _nfsv4x_session_slot_reply_cache_size = None
    @property
    def nfsv4x_session_slot_reply_cache_size(self):
        """
        Size of the Reply that will be Cached in Each NFSv4.x
        Session Slot (in bytes). Default value is 640.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv4x_session_slot_reply_cache_size
    @nfsv4x_session_slot_reply_cache_size.setter
    def nfsv4x_session_slot_reply_cache_size(self, val):
        if val != None:
            self.validate('nfsv4x_session_slot_reply_cache_size', val)
        self._nfsv4x_session_slot_reply_cache_size = val
    
    _rpcsec_ctx_high = None
    @property
    def rpcsec_ctx_high(self):
        """
        High water mark for the RPCSEC_GSS Context Cache.
        Default value is 0.
        Attributes: optional-for-create, modifiable
        """
        return self._rpcsec_ctx_high
    @rpcsec_ctx_high.setter
    def rpcsec_ctx_high(self, val):
        if val != None:
            self.validate('rpcsec_ctx_high', val)
        self._rpcsec_ctx_high = val
    
    _is_nfsv41_read_delegation_enabled = None
    @property
    def is_nfsv41_read_delegation_enabled(self):
        """
        If 'true', NFSv4.1 read delegation feature is enabled.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_read_delegation_enabled
    @is_nfsv41_read_delegation_enabled.setter
    def is_nfsv41_read_delegation_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_read_delegation_enabled', val)
        self._is_nfsv41_read_delegation_enabled = val
    
    _is_vstorage_enabled = None
    @property
    def is_vstorage_enabled(self):
        """
        If 'true', then enables the usage of vStorage protocol
        for server side copies, which is mostly used in
        hypervisors. Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_vstorage_enabled
    @is_vstorage_enabled.setter
    def is_vstorage_enabled(self, val):
        if val != None:
            self.validate('is_vstorage_enabled', val)
        self._is_vstorage_enabled = val
    
    _is_nfsv3_fsid_change_enabled = None
    @property
    def is_nfsv3_fsid_change_enabled(self):
        """
        If 'true', then NFSv3 clients see change in FSID as they
        traverse filesystems. Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv3_fsid_change_enabled
    @is_nfsv3_fsid_change_enabled.setter
    def is_nfsv3_fsid_change_enabled(self, val):
        if val != None:
            self.validate('is_nfsv3_fsid_change_enabled', val)
        self._is_nfsv3_fsid_change_enabled = val
    
    _nfsv4_grace_seconds = None
    @property
    def nfsv4_grace_seconds(self):
        """
        NFSv4 Grace timeout value in seconds. Default value is 45
        seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv4_grace_seconds
    @nfsv4_grace_seconds.setter
    def nfsv4_grace_seconds(self, val):
        if val != None:
            self.validate('nfsv4_grace_seconds', val)
        self._nfsv4_grace_seconds = val
    
    _nfsv4_lease_seconds = None
    @property
    def nfsv4_lease_seconds(self):
        """
        NFSv4 Lease timeout value in seconds. Default value is 30
        seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._nfsv4_lease_seconds
    @nfsv4_lease_seconds.setter
    def nfsv4_lease_seconds(self, val):
        if val != None:
            self.validate('nfsv4_lease_seconds', val)
        self._nfsv4_lease_seconds = val
    
    _is_nfsv41_write_delegation_enabled = None
    @property
    def is_nfsv41_write_delegation_enabled(self):
        """
        If 'true', NFSv4.1 write delegation feature is enabled.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_write_delegation_enabled
    @is_nfsv41_write_delegation_enabled.setter
    def is_nfsv41_write_delegation_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_write_delegation_enabled', val)
        self._is_nfsv41_write_delegation_enabled = val
    
    _is_nfsv41_migration_enabled = None
    @property
    def is_nfsv41_migration_enabled(self):
        """
        If 'true', then NFSv4.1 Migration feature is enabled.
        Default value is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_migration_enabled
    @is_nfsv41_migration_enabled.setter
    def is_nfsv41_migration_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_migration_enabled', val)
        self._is_nfsv41_migration_enabled = val
    
    _is_validate_qtree_export_enabled = None
    @property
    def is_validate_qtree_export_enabled(self):
        """
        If 'true', then the Vserver performs additional
        validation for qtree. Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_validate_qtree_export_enabled
    @is_validate_qtree_export_enabled.setter
    def is_validate_qtree_export_enabled(self, val):
        if val != None:
            self.validate('is_validate_qtree_export_enabled', val)
        self._is_validate_qtree_export_enabled = val
    
    _is_nfsv41_enabled = None
    @property
    def is_nfsv41_enabled(self):
        """
        If 'true', then NFS version 4.1 is enabled. Default value
        is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_enabled
    @is_nfsv41_enabled.setter
    def is_nfsv41_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_enabled', val)
        self._is_nfsv41_enabled = val
    
    _is_nfsv40_enabled = None
    @property
    def is_nfsv40_enabled(self):
        """
        If 'true', then NFS version 4.0 is enabled. Default value
        is 'false'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv40_enabled
    @is_nfsv40_enabled.setter
    def is_nfsv40_enabled(self, val):
        if val != None:
            self.validate('is_nfsv40_enabled', val)
        self._is_nfsv40_enabled = val
    
    _default_windows_group = None
    @property
    def default_windows_group(self):
        """
        The default windows group for CIFS access.
        Attributes: optional-for-create, modifiable
        """
        return self._default_windows_group
    @default_windows_group.setter
    def default_windows_group(self, val):
        if val != None:
            self.validate('default_windows_group', val)
        self._default_windows_group = val
    
    _is_nfsv41_state_protection_enabled = None
    @property
    def is_nfsv41_state_protection_enabled(self):
        """
        If 'true', then NFSv4.1 State Protection is enabled.
        Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfsv41_state_protection_enabled
    @is_nfsv41_state_protection_enabled.setter
    def is_nfsv41_state_protection_enabled(self, val):
        if val != None:
            self.validate('is_nfsv41_state_protection_enabled', val)
        self._is_nfsv41_state_protection_enabled = val
    
    @staticmethod
    def get_api_name():
          return "nfs-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-nfsv3-connection-drop-enabled',
            'is-nfsv3-enabled',
            'default-windows-user',
            'is-nfsv41-acl-preserve-enabled',
            'is-nfsv40-referrals-enabled',
            'is-nfsv41-pnfs-enabled',
            'is-nfsv40-migration-enabled',
            'chown-mode',
            'is-nfsv41-referrals-enabled',
            'nfsv41-implementation-id-domain',
            'nfsv41-implementation-id-name',
            'is-nfsv4-numeric-ids-enabled',
            'is-nfsv40-acl-enabled',
            'is-nfs-access-enabled',
            'rpcsec-ctx-idle',
            'is-nfsv2-enabled',
            'nfsv4-acl-max-aces',
            'is-nfsv4-fsid-change-enabled',
            'vserver',
            'is-qtree-export-enabled',
            'is-nfsv40-req-open-confirm-enabled',
            'nfsv4-id-domain',
            'is-nfsv40-read-delegation-enabled',
            'is-nfs-rootonly-enabled',
            'is-nfsv41-pnfs-striped-volumes-enabled',
            'nfsv41-implementation-id-time',
            'is-nfsv41-acl-enabled',
            'is-nfsv40-write-delegation-enabled',
            'ntfs-unix-security-ops',
            'is-mount-rootonly-enabled',
            'nfsv4x-session-num-slots',
            'enable-ejukebox',
            'nfsv4x-session-slot-reply-cache-size',
            'rpcsec-ctx-high',
            'is-nfsv41-read-delegation-enabled',
            'is-vstorage-enabled',
            'is-nfsv3-fsid-change-enabled',
            'nfsv4-grace-seconds',
            'nfsv4-lease-seconds',
            'is-nfsv41-write-delegation-enabled',
            'is-nfsv41-migration-enabled',
            'is-validate-qtree-export-enabled',
            'is-nfsv41-enabled',
            'is-nfsv40-enabled',
            'default-windows-group',
            'is-nfsv41-state-protection-enabled',
        ]
    
    def describe_properties(self):
        return {
            'is_nfsv3_connection_drop_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv3_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'default_windows_user': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_acl_preserve_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv40_referrals_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_pnfs_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv40_migration_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'chown_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_referrals_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nfsv41_implementation_id_domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nfsv41_implementation_id_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_nfsv4_numeric_ids_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv40_acl_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfs_access_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'rpcsec_ctx_idle': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_nfsv2_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nfsv4_acl_max_aces': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_nfsv4_fsid_change_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_qtree_export_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv40_req_open_confirm_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nfsv4_id_domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_nfsv40_read_delegation_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfs_rootonly_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_pnfs_striped_volumes_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nfsv41_implementation_id_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_acl_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv40_write_delegation_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ntfs_unix_security_ops': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_mount_rootonly_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nfsv4x_session_num_slots': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enable_ejukebox': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nfsv4x_session_slot_reply_cache_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'rpcsec_ctx_high': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_read_delegation_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_vstorage_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv3_fsid_change_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nfsv4_grace_seconds': { 'class': int, 'is_list': False, 'required': 'optional' },
            'nfsv4_lease_seconds': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_write_delegation_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_migration_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_validate_qtree_export_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nfsv40_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'default_windows_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_nfsv41_state_protection_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

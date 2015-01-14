from netapp.netapp_object import NetAppObject

class SnapmirrorInfo(NetAppObject):
    """
    Information about the SnapMirror Relationship.
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
    
    _relationship_progress = None
    @property
    def relationship_progress(self):
        """
        The total number of bytes that have been processed so far
        for the current activity of the relationship as returned
        in the relationship-status. This is set only when the
        relationship-status indicates that an activity is in
        progress.
        Attributes: non-creatable, non-modifiable
        """
        return self._relationship_progress
    @relationship_progress.setter
    def relationship_progress(self, val):
        if val != None:
            self.validate('relationship_progress', val)
        self._relationship_progress = val
    
    _newest_snapshot = None
    @property
    def newest_snapshot(self):
        """
        The name of the newest Snapshot copy on the destination
        volume.
        Attributes: non-creatable, non-modifiable
        """
        return self._newest_snapshot
    @newest_snapshot.setter
    def newest_snapshot(self, val):
        if val != None:
            self.validate('newest_snapshot', val)
        self._newest_snapshot = val
    
    _relationship_status = None
    @property
    def relationship_status(self):
        """
        Specifies the status of the SnapMirror relationship.
        Possible values  are:
        <ul>
        <li>'idle' - Transfers are enabled, and no transfer is
        in progress, <li>'transferring' - SnapMirror transfers
        are enabled and a transfer is in progress,
        <li>'checking'- The destination volume is undergoing a
        diagnostic check and no transfer is in progress. Only
        applicable for SnapMirror relationships with the
        relationship-control-plane field set to 'v1',
        <li>'quiescing' - A SnapMirror transfer is in progress,
        additional transfers are disabled,
        <li>'quiesced' - SnapMirror transfers are disabled, no
        transfer is in progress,
        <li>'queued' - SnapMirror transfers are enabled, and a
        transfer operation has been accepted and queued in the
        system,
        <li>'preparing' - SnapMirror transfers are enabled,
        currently in the pre-transfer phase for Vault incremental
        transfers,
        <li>'finalizing' - SnapMirror transfers are enabled,
        currently in the post-transfer phase for vault
        incremental transfers,
        <li>'aborting' - SnapMirror transfers are enabled,
        however a transfer abort operation that may include
        removal of the checkpoint is underway.
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._relationship_status
    @relationship_status.setter
    def relationship_status(self, val):
        if val != None:
            self.validate('relationship_status', val)
        self._relationship_status = val
    
    _last_transfer_type = None
    @property
    def last_transfer_type(self):
        """
        The type of the previous transfer for the relationship.
        This parameter is only available on Data ONTAP 8.2 or
        later operating in Cluster-Mode if the relationship
        control plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "initialize"     ,
        <li> "update"         ,
        <li> "resync"         ,
        <li> "restore"        ,
        <li> "check"
        </ul>
        """
        return self._last_transfer_type
    @last_transfer_type.setter
    def last_transfer_type(self, val):
        if val != None:
            self.validate('last_transfer_type', val)
        self._last_transfer_type = val
    
    _snapshot_checkpoint = None
    @property
    def snapshot_checkpoint(self):
        """
        The number of bytes transferred as recorded for the
        checkpoint of the current or most recent transfer
        snapshot.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_checkpoint
    @snapshot_checkpoint.setter
    def snapshot_checkpoint(self, val):
        if val != None:
            self.validate('snapshot_checkpoint', val)
        self._snapshot_checkpoint = val
    
    _exported_snapshot_timestamp = None
    @property
    def exported_snapshot_timestamp(self):
        """
        The timestamp of the exported Snapshot copy on the
        destination volume, in seconds since Jan 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._exported_snapshot_timestamp
    @exported_snapshot_timestamp.setter
    def exported_snapshot_timestamp(self, val):
        if val != None:
            self.validate('exported_snapshot_timestamp', val)
        self._exported_snapshot_timestamp = val
    
    _last_transfer_size = None
    @property
    def last_transfer_size(self):
        """
        The total number of bytes transferred as part of the last
        transfer. This parameter is available only on Data ONTAP
        8.2 or later operating in Cluster-Mode if the
        relationship control plane is 'v2', and if the last
        transfer was successful.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_transfer_size
    @last_transfer_size.setter
    def last_transfer_size(self, val):
        if val != None:
            self.validate('last_transfer_size', val)
        self._last_transfer_size = val
    
    _destination_vserver = None
    @property
    def destination_vserver(self):
        """
        Specifies the name of the destination Vserver for the
        SnapMirror relationship. If using this parameter, the
        following parameters should also be specified:
        <ul>
        <li> The name of destination volume.
        <li> The name of the destination cluster on Data ONTAP
        8.1, or on Data ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v1'.
        </ul>
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._destination_vserver
    @destination_vserver.setter
    def destination_vserver(self, val):
        if val != None:
            self.validate('destination_vserver', val)
        self._destination_vserver = val
    
    _destination_volume = None
    @property
    def destination_volume(self):
        """
        Specifies the name of the destination volume for the
        SnapMirror relationship. If using this parameter, the
        following parameters should also be specified:
        <ul>
        <li> The name of the destination Vserver.
        <li> The name of the destination cluster on Data ONTAP
        8.1 operating in Cluster-Mode, or on Data ONTAP 8.2 or
        later operating in Cluster-Mode if the relationship
        control plane is 'v1'.
        </ul>
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._destination_volume
    @destination_volume.setter
    def destination_volume(self, val):
        if val != None:
            self.validate('destination_volume', val)
        self._destination_volume = val
    
    _mirror_state = None
    @property
    def mirror_state(self):
        """
        Specifies the mirror state of the SnapMirror
        relationship. Possible values  are:
        <ul>
        <li>'uninitialized' - Destination volume has not been
        initialized,
        <li>'snapmirrored' - Destination volume has been
        initialized and is ready to receive SnapMirror updates,
        <li>'broken-off' - Destination volume is RW and
        snapshots are present.
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._mirror_state
    @mirror_state.setter
    def mirror_state(self, val):
        if val != None:
            self.validate('mirror_state', val)
        self._mirror_state = val
    
    _is_healthy = None
    @property
    def is_healthy(self):
        """
        False if the last manual or scheduled update failed or
        was aborted, or if the last scheduled update was delayed.
        Otherwise true.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_healthy
    @is_healthy.setter
    def is_healthy(self, val):
        if val != None:
            self.validate('is_healthy', val)
        self._is_healthy = val
    
    _last_transfer_duration = None
    @property
    def last_transfer_duration(self):
        """
        The amount of time in seconds it took for the last
        transfer to complete. This parameter is available only on
        Data ONTAP 8.2 or later operating in Cluster-Mode if the
        relationship control plane is 'v2', and if the last
        transfer was successful.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_transfer_duration
    @last_transfer_duration.setter
    def last_transfer_duration(self, val):
        if val != None:
            self.validate('last_transfer_duration', val)
        self._last_transfer_duration = val
    
    _last_transfer_error = None
    @property
    def last_transfer_error(self):
        """
        A message describing the cause of the last transfer
        failure. This parameter is only available on Data ONTAP
        8.2 or later operating in Cluster-Mode, if the
        relationship control plane is 'v2', and if the last
        transfer was unsuccessful.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_transfer_error
    @last_transfer_error.setter
    def last_transfer_error(self, val):
        if val != None:
            self.validate('last_transfer_error', val)
        self._last_transfer_error = val
    
    _destination_cluster = None
    @property
    def destination_cluster(self):
        """
        Specifies the destination cluster name for the SnapMirror
        relationship. The parameters for the name of the
        destination Vserver, and the name of the destination
        volume must also be specified if using this parameter.
        This parameter is available only on:
        <ul>
        <li> Data ONTAP 8.1 operating in Cluster-Mode.
        <li> Data ONTAP 8.2 or later operating in Cluster-Mode if
        the relationship control plane is 'v1'.
        </ul>
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._destination_cluster
    @destination_cluster.setter
    def destination_cluster(self, val):
        if val != None:
            self.validate('destination_cluster', val)
        self._destination_cluster = val
    
    _is_constituent = None
    @property
    def is_constituent(self):
        """
        Specifies whether or not the SnapMirror relationship is
        between Infinite Volume constituent volumes.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_constituent
    @is_constituent.setter
    def is_constituent(self, val):
        if val != None:
            self.validate('is_constituent', val)
        self._is_constituent = val
    
    _source_vserver = None
    @property
    def source_vserver(self):
        """
        Specifies the name of the source Vserver for the
        SnapMirror relationship. If using this parameter, the
        following parameters should also be specified:
        <ul>
        <li> The name of source volume.
        <li> The name of the source cluster on Data ONTAP 8.1, or
        on Data ONTAP 8.2 or later operating in Cluster-Mode if
        the relationship control plane is 'v1'.
        </ul>
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._source_vserver
    @source_vserver.setter
    def source_vserver(self, val):
        if val != None:
            self.validate('source_vserver', val)
        self._source_vserver = val
    
    _source_volume = None
    @property
    def source_volume(self):
        """
        Specifies the name of the source volume of the SnapMirror
        relationship. If using this parameter, the following
        parameters should also be specified:
        <ul>
        <li> The name of the source Vserver.
        <li> The name of the source cluster on Data ONTAP 8.1
        operating in Cluster-Mode, or on Data ONTAP 8.2 or later
        operating in Cluster-Mode if the relationship control
        plane is 'v1'.
        </ul>
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._source_volume
    @source_volume.setter
    def source_volume(self, val):
        if val != None:
            self.validate('source_volume', val)
        self._source_volume = val
    
    _newest_snapshot_timestamp = None
    @property
    def newest_snapshot_timestamp(self):
        """
        The timestamp of the newest Snapshot copy on the
        destination volume, in seconds since Jan 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._newest_snapshot_timestamp
    @newest_snapshot_timestamp.setter
    def newest_snapshot_timestamp(self, val):
        if val != None:
            self.validate('newest_snapshot_timestamp', val)
        self._newest_snapshot_timestamp = val
    
    _last_transfer_from = None
    @property
    def last_transfer_from(self):
        """
        The source endpoint of the last transfer. This parameter
        is available only on Data ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_transfer_from
    @last_transfer_from.setter
    def last_transfer_from(self, val):
        if val != None:
            self.validate('last_transfer_from', val)
        self._last_transfer_from = val
    
    _current_max_transfer_rate = None
    @property
    def current_max_transfer_rate(self):
        """
        The upper bound in kilobytes per second, at which data is
        transferred for the current transfer. This value can be
        the same as the 'max-transfer-rate' or different if
        overwritten when starting the transfer via the associated
        commands or APIs (snapmirror-initialize,
        snapmirror-update, snapmirror-resync,
        snapmirror-restore). This parameter is only valid when a
        transfer is in progress. This parameter is available only
        on Data ONTAP 8.2 or later operating in Cluster-Mode if
        the relationship control plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        """
        return self._current_max_transfer_rate
    @current_max_transfer_rate.setter
    def current_max_transfer_rate(self, val):
        if val != None:
            self.validate('current_max_transfer_rate', val)
        self._current_max_transfer_rate = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        If this optional parameter is specified, designates the
        managing Vserver. The managing Vserver is authorized to
        use snapmirror commands to manage the SnapMirror
        relationship. The vserver option is currently a reserved
        option and should not be used for queries. The
        destination-vserver parameter should be used to select
        the Vserver in a cluster context.
        Attributes: optional-for-create, modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _transfer_snapshot = None
    @property
    def transfer_snapshot(self):
        """
        The name of the current snapshot copy being transferred.
        This is set only when the relationship-status indicates
        that an activity is in progress.
        Attributes: non-creatable, non-modifiable
        """
        return self._transfer_snapshot
    @transfer_snapshot.setter
    def transfer_snapshot(self, val):
        if val != None:
            self.validate('transfer_snapshot', val)
        self._transfer_snapshot = val
    
    _destination_location = None
    @property
    def destination_location(self):
        """
        Specifies the destination endpoint of the SnapMirror
        relationship in one of the following formats:
        <ul>
        <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
        on Data ONTAP operating in 7-Mode.
        <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on
        Data ONTAP 8.1 operating in Cluster-Mode, and on Data
        ONTAP 8.2 operating in Cluster-Mode for relationships
        using a control plane compatible with Data ONTAP 8.1
        operating in Cluster-Mode.
        <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
        operating in Cluster-Mode except for relationships using
        a control plane compatible with Data ONTAP 8.1 operating
        in Cluster-Mode. This format depends on Vserver peering
        setup between the source and destination Vservers.
        </ul>
        This format may change in the future.
        The destination endpoint can be specified using the
        location formats above, or by specifying the parameters
        for the name of the destination Vserver, the name of the
        destination volume, and the name of the destination
        cluster. The name of the destination cluster is only
        required on Data ONTAP 8.1 operating in Cluster-Mode.
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._destination_location
    @destination_location.setter
    def destination_location(self, val):
        if val != None:
            self.validate('destination_location', val)
        self._destination_location = val
    
    _policy = None
    @property
    def policy(self):
        """
        Specifies the name of the snapmirror policy for the
        relationship. For SnapMirror relationships of type
        'vault', the policy will also have rules to select
        snapshot copies that must be transferred. If no policy is
        specified, a default policy will be applied depending on
        the type of the SnapMirror relationship. This parameter
        is only available on Data ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v2'.
        Attributes: optional-for-create, modifiable
        """
        return self._policy
    @policy.setter
    def policy(self, val):
        if val != None:
            self.validate('policy', val)
        self._policy = val
    
    _progress_last_updated = None
    @property
    def progress_last_updated(self):
        """
        A timestamp indicating when the progress of the transfer
        was last updated. This parameter is available only on
        Data ONTAP 8.2 or later operating in Cluster-Mode if the
        relationship control plane is 'v2', and if a transfer is
        in progress.
        Attributes: non-creatable, non-modifiable
        """
        return self._progress_last_updated
    @progress_last_updated.setter
    def progress_last_updated(self, val):
        if val != None:
            self.validate('progress_last_updated', val)
        self._progress_last_updated = val
    
    _relationship_id = None
    @property
    def relationship_id(self):
        """
        A unique identifier assigned to the SnapMirror
        relationship when it is created. This parameter is only
        available on Data ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        """
        return self._relationship_id
    @relationship_id.setter
    def relationship_id(self, val):
        if val != None:
            self.validate('relationship_id', val)
        self._relationship_id = val
    
    _source_cluster = None
    @property
    def source_cluster(self):
        """
        Specifies the name of the source cluster for the
        SnapMirror relationship. The parameters for the name of
        the source Vserver, and the name of the source volume
        must also be specified if using this parameter. This
        parameter is available only on:
        <ul>
        <li> Data ONTAP 8.1 operating in Cluster-Mode.
        <li> Data ONTAP 8.2 or later operating in Cluster-Mode if
        the relationship control plane is 'v1'.
        </ul>
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._source_cluster
    @source_cluster.setter
    def source_cluster(self, val):
        if val != None:
            self.validate('source_cluster', val)
        self._source_cluster = val
    
    _unhealthy_reason = None
    @property
    def unhealthy_reason(self):
        """
        The reason the relationship is not healthy. This
        parameter is available only on Data ONTAP 8.2 or later
        operating in Cluster-Mode if the relationship control
        plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        """
        return self._unhealthy_reason
    @unhealthy_reason.setter
    def unhealthy_reason(self, val):
        if val != None:
            self.validate('unhealthy_reason', val)
        self._unhealthy_reason = val
    
    _schedule = None
    @property
    def schedule(self):
        """
        Specifies the name of the cron schedule, which is used to
        update the SnapMirror relationship.
        Attributes: optional-for-create, modifiable
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    _destination_volume_node = None
    @property
    def destination_volume_node(self):
        """
        Node which owns the destination volume of the
        relationship. This parameter is available only on Data
        ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_volume_node
    @destination_volume_node.setter
    def destination_volume_node(self, val):
        if val != None:
            self.validate('destination_volume_node', val)
        self._destination_volume_node = val
    
    _tries = None
    @property
    def tries(self):
        """
        Specifies the maximum number of times to attempt each
        manual or scheduled transfer for a SnapMirror
        relationship. The default is eight times.
        Note: You can set the tries option to zero (0) to disable
        manual and scheduled updates for the SnapMirror
        relationship. This parameter is only relevant on Data
        ONTAP 8.1 operating in Cluster-Mode. On Data ONTAP 8.2
        operating in Cluster-Mode, the maximum number of times to
        attempt a transfer is an attribute of the SnapMirror
        policy. Therefore the value of this parameter is
        ignored.
        Attributes: optional-for-create, modifiable
        """
        return self._tries
    @tries.setter
    def tries(self, val):
        if val != None:
            self.validate('tries', val)
        self._tries = val
    
    _current_transfer_type = None
    @property
    def current_transfer_type(self):
        """
        The type of transfer taking place. This parameter is only
        available on Data ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "initialize"     ,
        <li> "update"         ,
        <li> "resync"         ,
        <li> "restore"        ,
        <li> "check"
        </ul>
        """
        return self._current_transfer_type
    @current_transfer_type.setter
    def current_transfer_type(self, val):
        if val != None:
            self.validate('current_transfer_type', val)
        self._current_transfer_type = val
    
    _exported_snapshot = None
    @property
    def exported_snapshot(self):
        """
        The name of the exported Snapshot copy on the destination
        volume.
        Attributes: non-creatable, non-modifiable
        """
        return self._exported_snapshot
    @exported_snapshot.setter
    def exported_snapshot(self, val):
        if val != None:
            self.validate('exported_snapshot', val)
        self._exported_snapshot = val
    
    _current_transfer_error = None
    @property
    def current_transfer_error(self):
        """
        A message describing the last retryable error encountered
        by the current transfer. This parameter is only available
        on Data ONTAP 8.2 or later operating in Cluster-Mode if
        the relationship control plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        """
        return self._current_transfer_error
    @current_transfer_error.setter
    def current_transfer_error(self, val):
        if val != None:
            self.validate('current_transfer_error', val)
        self._current_transfer_error = val
    
    _max_transfer_rate = None
    @property
    def max_transfer_rate(self):
        """
        Specifies the upper bound, in kilobytes per second, at
        which data is transferred. The default is unlimited (0)
        which permits the SnapMirror relationship to fully
        utilize the available network bandwidth.  The
        max-transfer-rate option does not affect load-sharing
        transfers and transfers for other relationships with
        Relationship Capability of Pre 8.2 confined to a single
        cluster.
        Attributes: optional-for-create, modifiable
        """
        return self._max_transfer_rate
    @max_transfer_rate.setter
    def max_transfer_rate(self, val):
        if val != None:
            self.validate('max_transfer_rate', val)
        self._max_transfer_rate = val
    
    _last_transfer_error_codes = None
    @property
    def last_transfer_error_codes(self):
        """
        List of codes providing additional information on the
        cause and context of the last transfer failure. These are
        Data ONTAP internal codes, not API errnos. This parameter
        is reserved for use only by vendor provided management
        tools, and is available only on Data ONTAP 8.2 or later
        operating in Cluster-Mode if the relationship control
        plane is 'v2', and if the last transfer was
        unsuccessful.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_transfer_error_codes
    @last_transfer_error_codes.setter
    def last_transfer_error_codes(self, val):
        if val != None:
            self.validate('last_transfer_error_codes', val)
        self._last_transfer_error_codes = val
    
    _relationship_type = None
    @property
    def relationship_type(self):
        """
        Specifies the type of the SnapMirror relationship.
        Attributes: optional-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "data_protection"               ,
        <li> "load_sharing"                  ,
        <li> "vault"                         ,
        <li> "restore"                       ,
        <li> "transition_data_protection"
        </ul>
        """
        return self._relationship_type
    @relationship_type.setter
    def relationship_type(self, val):
        if val != None:
            self.validate('relationship_type', val)
        self._relationship_type = val
    
    _current_transfer_priority = None
    @property
    def current_transfer_priority(self):
        """
        Priority assigned to the ongoing transfer. This parameter
        is only available on Data ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v2',
        and if a transfer is in progress.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "low"       ,
        <li> "normal"
        </ul>
        """
        return self._current_transfer_priority
    @current_transfer_priority.setter
    def current_transfer_priority(self, val):
        if val != None:
            self.validate('current_transfer_priority', val)
        self._current_transfer_priority = val
    
    _lag_time = None
    @property
    def lag_time(self):
        """
        The amount of time in seconds by which the data on the
        mirror lags behind the source. This parameter is
        available only on Data ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        """
        return self._lag_time
    @lag_time.setter
    def lag_time(self, val):
        if val != None:
            self.validate('lag_time', val)
        self._lag_time = val
    
    _source_location = None
    @property
    def source_location(self):
        """
        Specifies the source endpoint of the SnapMirror
        relationship in one of the following formats:
        <ul>
        <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
        on Data ONTAP operating in 7-Mode.
        <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on
        Data ONTAP 8.1 operating in Cluster-Mode, and on Data
        ONTAP 8.2 operating in Cluster-Mode for relationships
        using a control plane compatible with Data ONTAP 8.1
        operating in Cluster-Mode.
        <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
        operating in Cluster-Mode except for relationships using
        a control plane compatible with Data ONTAP 8.1 operating
        in Cluster-Mode. This format depends on Vserver peering
        setup between the source and destination Vservers.
        </ul>
        This format may change in the future.
        The source endpoint can be specified using the location
        formats above, or by specifying the parameters for the
        name of the source Vserver, the name of the source
        volume, and the name of the source cluster. The name of
        the source cluster is only required on Data ONTAP 8.1
        operating in Cluster-Mode.
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._source_location
    @source_location.setter
    def source_location(self, val):
        if val != None:
            self.validate('source_location', val)
        self._source_location = val
    
    _last_transfer_end_timestamp = None
    @property
    def last_transfer_end_timestamp(self):
        """
        The Timestamp of the end of the last transfer. This
        parameter is available only on Data ONTAP 8.2 or later
        operating in Cluster-Mode if the relationship control
        plane is 'v2'.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_transfer_end_timestamp
    @last_transfer_end_timestamp.setter
    def last_transfer_end_timestamp(self, val):
        if val != None:
            self.validate('last_transfer_end_timestamp', val)
        self._last_transfer_end_timestamp = val
    
    _snapshot_progress = None
    @property
    def snapshot_progress(self):
        """
        The number of bytes transferred for the transfer
        snapshot. This is set only when the relationship-status
        indicates that an activity is in progress.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_progress
    @snapshot_progress.setter
    def snapshot_progress(self, val):
        if val != None:
            self.validate('snapshot_progress', val)
        self._snapshot_progress = val
    
    _relationship_control_plane = None
    @property
    def relationship_control_plane(self):
        """
        The type of the control plane used for the relationship.
        Possible values are:
        <ul>
        <li> 'v1' -  Data ONTAP 8.1 compatible control plane.
        The endpoint location format
        [&lt;cluster&gt;:][//&lt;vserver&gt;/]&lt;volume&gt; must
        be used. Long operations such as initialize, update and
        resync will spawn a job, and return a job id. The job API
        must be used to track the progress of the operations.
        <li>'v2' -  Data ONTAP 8.2 and later compatible control
        plane.  The endpoint location format
        [&lt;vserver&gt;:]&lt;volume&gt; should be used. Long
        operations such as initialize, update, and resync do not
        spawn a job and do not return a job id.  The
        snapmirror-get API must be used to track the progress of
        these operations.
        </ul>
        This parameter is available only on Data ONTAP 8.2 or
        later operating in Cluster-Mode.'
        Attributes: non-creatable, non-modifiable
        """
        return self._relationship_control_plane
    @relationship_control_plane.setter
    def relationship_control_plane(self, val):
        if val != None:
            self.validate('relationship_control_plane', val)
        self._relationship_control_plane = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'relationship-progress',
            'newest-snapshot',
            'relationship-status',
            'last-transfer-type',
            'snapshot-checkpoint',
            'exported-snapshot-timestamp',
            'last-transfer-size',
            'destination-vserver',
            'destination-volume',
            'mirror-state',
            'is-healthy',
            'last-transfer-duration',
            'last-transfer-error',
            'destination-cluster',
            'is-constituent',
            'source-vserver',
            'source-volume',
            'newest-snapshot-timestamp',
            'last-transfer-from',
            'current-max-transfer-rate',
            'vserver',
            'transfer-snapshot',
            'destination-location',
            'policy',
            'progress-last-updated',
            'relationship-id',
            'source-cluster',
            'unhealthy-reason',
            'schedule',
            'destination-volume-node',
            'tries',
            'current-transfer-type',
            'exported-snapshot',
            'current-transfer-error',
            'max-transfer-rate',
            'last-transfer-error-codes',
            'relationship-type',
            'current-transfer-priority',
            'lag-time',
            'source-location',
            'last-transfer-end-timestamp',
            'snapshot-progress',
            'relationship-control-plane',
        ]
    
    def describe_properties(self):
        return {
            'relationship_progress': { 'class': int, 'is_list': False, 'required': 'optional' },
            'newest_snapshot': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'relationship_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_transfer_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snapshot_checkpoint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'exported_snapshot_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_transfer_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mirror_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_healthy': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'last_transfer_duration': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_transfer_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_cluster': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_constituent': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'source_vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'newest_snapshot_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_transfer_from': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_max_transfer_rate': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'transfer_snapshot': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'progress_last_updated': { 'class': int, 'is_list': False, 'required': 'optional' },
            'relationship_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_cluster': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'unhealthy_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'schedule': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_volume_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tries': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_transfer_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'exported_snapshot': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_transfer_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_transfer_rate': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_transfer_error_codes': { 'class': int, 'is_list': True, 'required': 'optional' },
            'relationship_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_transfer_priority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lag_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'source_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_transfer_end_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_progress': { 'class': int, 'is_list': False, 'required': 'optional' },
            'relationship_control_plane': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

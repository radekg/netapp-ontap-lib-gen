from netapp.connection import NaConnection
from snapvault_snapshot_schedule_status_info import SnapvaultSnapshotScheduleStatusInfo # 3 properties
from snapvault_configuration_info import SnapvaultConfigurationInfo # 10 properties
from snapvault_schedule_info import SnapvaultScheduleInfo # 2 properties
from snapvault_snapcreate_options import SnapvaultSnapcreateOptions # 1 properties
from snapvault_chained_destination_info import SnapvaultChainedDestinationInfo # 2 properties
from snapvault_primary_snapshot_schedule_info import SnapvaultPrimarySnapshotScheduleInfo # 8 properties
from snapshot_name import SnapshotName # 0 properties
from snapvault_status_info import SnapvaultStatusInfo # 22 properties
from snapvault_secondary_snapshot_schedule_info import SnapvaultSecondarySnapshotScheduleInfo # 8 properties
from snapvault_softlock_info import SnapvaultSoftlockInfo # 2 properties
from snapvault_schedule_options import SnapvaultScheduleOptions # 2 properties
from snapvault_destination_info import SnapvaultDestinationInfo # 3 properties

class SnapvaultConnection(NaConnection):
    
    def snapvault_secondary_modify_configuration(self, configuration):
        """
        Request change in one or more configuration parameters of
        an existing snapvault relationship identified by the
        secondary path provided. Only the parameters that are
        specified as input will be changed for this configuration.
        
        :param configuration: Relationship configuration
        """
        return self.request( "snapvault-secondary-modify-configuration", {
            'configuration': [ configuration, 'configuration', [ SnapvaultConfigurationInfo, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_set_snapshot_schedule(self, snapshot_schedule):
        """
        Request the primary system to configure the specified
        snapshot schedule. It can also update existing snapshot
        schedules. If the optional input schedule is skipped,
        the days-of-week is set to "mon-sun" and hours-of-day set
        to 0, i.e. midnight.
        @test
        
        :param snapshot_schedule: Specifies details of the schedule to be set.
        """
        return self.request( "snapvault-primary-set-snapshot-schedule", {
            'snapshot_schedule': [ snapshot_schedule, 'snapshot-schedule', [ SnapvaultPrimarySnapshotScheduleInfo, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_abort_snapshot_create(self, volume_name, schedule_name):
        """
        Request the primary to abort a snapshot creation that is
        already in progress.
        The snapshot schedule for which the snapshot creation is in
        progress must be specified as input.
        @test
        
        :param volume_name: Primary volume in which snapshot create is in progress.
        
        :param schedule_name: Name of the schedule used for snapshot creation.
        """
        return self.request( "snapvault-primary-abort-snapshot-create", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'schedule_name': [ schedule_name, 'schedule-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_relationship_status_list_iter_start(self):
        """
        Request the secondary to start an iteration through the
        list of the status entries for all relationships. This list
        will also include entries for snapvault restores from this
        secondary.
        @test
        """
        return self.request( "snapvault-secondary-relationship-status-list-iter-start", {
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def snapvault_get_softlocks(self, volume, snapshot):
        """
        List all snapvault softlocks on the given snapshot which
        are locked by external means.
        EONTAPI_EINVAL
        
        :param volume: Name of the volume where the snapshot exists.
        
        :param snapshot: Name of the snapshot for which softlocks to be
                listed.
        """
        return self.request( "snapvault-get-softlocks", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
            'snapvault-softlocks': [ SnapvaultSoftlockInfo, False ],
        } )
    
    def snapvault_secondary_initiate_incremental_transfer(self, secondary_path, max_transfer_rate=None, primary_snapshot=None, no_lun_clone_expansion=None):
        """
        Request the snapvault secondary system to begin an
        incremental transfer to the given secondary path. This API
        is equivalent to the 'snapvault update' Data ONTAP command.
        It is required that this secondary path has already been
        configured as part of a snapvault relationship. The
        primary system and path configured in that relationship
        will be used as the source for this transfer.
        The request will only start the transfer and return. The
        actual transfer will proceed asynchronously and there is
        no guarantee that it will succeed.
        The snapvault-secondary-get-relationship-status API should
        be used to check the status of the update.
        @test
        
        :param secondary_path: The secondary path that will be used as the destination
                for this update transfer.
                It is required that this secondary path is already a part
                of some configured snapvault relationship.
        
        :param max_transfer_rate: The maximum transfer rate in kilobytes (1024 bytes) per
                second to be applied only for this update transfer.
                If this option is not provided the default behavior will
                be to allow the transfer to proceed as fast as possible.
                Range:[1.. 2^31-2]
        
        :param primary_snapshot: Name of the primary snapshot to be used for this update
                transfer.
                This option is supported for only primary systems.
                If this option is not provided, the primary system will
                create a new source snapshot for this transfer.
        
        :param no_lun_clone_expansion: This option dictates how a lun clone would be transferred
                from source to destination. If this option is "false", a
                LUN clone would be transferred as a LUN and if it is "true",
                it will be transferred as a clone.
                By default the value of the option is "false".
        """
        return self.request( "snapvault-secondary-initiate-incremental-transfer", {
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
            'primary_snapshot': [ primary_snapshot, 'primary-snapshot', [ basestring, 'None' ], False ],
            'secondary_path': [ secondary_path, 'secondary-path', [ basestring, 'None' ], False ],
            'no_lun_clone_expansion': [ no_lun_clone_expansion, 'no-lun-clone-expansion', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_relationship_status_list_iter_next(self, tag, maximum):
        """
        Request the primary to continue the iteration set up with
        the snapvault-primary-relationship-status-list-iter-start API.
        A list consisting of a number of status entries, upto the
        specified maximum, will be returned.
        When snapvault primary and secondary are licensed on the
        same filer, output of this API is identical to the output
        of snapvault-secondary-relationship-status-list-iter-next
        @test
        
        :param tag: Tag from a previous
                primary-relationship-status-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
                Range:[0..2^32-1]
        """
        return self.request( "snapvault-primary-relationship-status-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'status-list': [ SnapvaultStatusInfo, True ],
            'records': [ int, False ],
        } )
    
    def snapvault_get_all_softlocked_snapshots(self, volume):
        """
        List all snapshots which are softlocked for snapvault by
        external means.
        EAPIMISSINGARGUMENT
        ESNAPVAULTRESOURCE
        EONTAPI_EINVAL
        
        :param volume: Name of the volume for which softlocked snapshots to be listed.
        """
        return self.request( "snapvault-get-all-softlocked-snapshots", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'snapshot-list': [ basestring, True ],
        } )
    
    def snapvault_secondary_resync_relationship(self, configuration, no_lun_clone_expansion=None):
        """
        Request to resynchronize the relationship for an existing
        secondary path. This API is equivalent to the 'snapvault
        start -r' Data ONTAP command.
        In addition the configuration entry for this relationship
        will be updated with any parameters that are provided as
        input. Finally an update transfer to this secondary path
        will be started.
        The resynchronization is commonly used when the primary
        dataset has been migrated to a different location for e.g.
        via snapvault restore. This functionality is also required
        if the secondary path was made writable for e.g. via wafl
        iron.
        This request will only start the resync process and
        return. The process will proceed asynchronously and there
        is no guarantee that it will succeed. The
        snapvault-secondary-get-relationship-status API should be
        used to check the status of this restore.
        
        :param configuration: Relationship configuration
        
        :param no_lun_clone_expansion: This option dictates how a lun clone would be transferred
                from source to destination. If this option is "false", a
                LUN clone would be transferred as a LUN and if it is "true",
                it will be transferred as a clone.
                By default the value of the option is "false".
        """
        return self.request( "snapvault-secondary-resync-relationship", {
            'no_lun_clone_expansion': [ no_lun_clone_expansion, 'no-lun-clone-expansion', [ bool, 'None' ], False ],
            'configuration': [ configuration, 'configuration', [ SnapvaultConfigurationInfo, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_relationship_status_list_iter_end(self, tag):
        """
        Terminate the status list iteration set up by the
        snapvault-secondary-relationship-status-list-iter-start
        API. The secondary will clean up any saved info for this
        iteration.
        @test
        
        :param tag: Tag from the previous
                secondary-relationship-status-list-iter-start.
        """
        return self.request( "snapvault-secondary-relationship-status-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def snapvault_secondary_snapshot_schedule_list_info(self, volume_name=None):
        """
        Request the secondary to return a list of configured
        snapshot schedules. Without any input arguments this
        request returns the list of all snapshot schedules
        configured on the secondary. If a volume is specified
        then only the list of schedules configured for that
        volume will be returned.
        When snapvault primary and secondary are licensed on the
        same filer, snapvault-primary-snapshot-schedule-list-info
        and this API return the same number of schedules.
        @test
        
        :param volume_name: The secondary volume for which the list of snapshot
                schedules are desired.
        """
        return self.request( "snapvault-secondary-snapshot-schedule-list-info", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'snapshot-schedules': [ SnapvaultSecondarySnapshotScheduleInfo, True ],
        } )
    
    def snapvault_add_softlock(self, volume, snapshot, softlock_name=None):
        """
        Request the system to add softlock for the specified snapshot.
        Softlocks can be added  to preserve the snapshots which user
        wants to retain down the cascade.
        EAPIMISSINGARGUMENT
        EONTAPI_EINVAL
        EONTAPI_ERANGE
        ESNAPVAULTRESOURCE
        
        :param volume: Name of the volume where the snapshot exists.
        
        :param snapshot: Name of the snapshot to be softlocked.
        
        :param softlock_name: Name of softlock which  uniquely identifies the softlock for
                the snapshot. When not specified, softlock will be added with
                default name. Name of softlock can contain letters, numbers,
                and underscore character (_), and can be up to 64 characters
                long.
        """
        return self.request( "snapvault-add-softlock", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'softlock_name': [ softlock_name, 'softlock-name', [ basestring, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_initiate_snapshot_create(self, volume_name, schedule_name, options=None, lock_backing_snapshot=None):
        """
        Request the secondary to force a snapshot creation for a
        specified snapshot schedule. The snapshot schedule must be
        identified by the volume name and the schedule name. All
        the properties of the specified schedule will be applied to
        the snapshot creation.
        This API should be used when it is desirable to create
        snapshots right away, without having to wait for the
        pre-configured scheduled time. This API returns after only
        initiating the snapshot creation, and there is no guarantee
        that the snapshot creation will succeed.
        The snapvault-secondary-snapshot-schedule-status-list-info
        API should be used to track progress of the snapshot
        creation.
        @test
        
        :param volume_name: The secondary volume in which the snapshot is to be
                created.
        
        :param schedule_name: The name of the schedule to be used for creating the
                snapshot. The schedule-name will be used as a prefix in the
                name of each snapshot created by this schedule.
                If an empty string is provided, the snapshot creation
                process will be started, but a snapshot will not be
                created. This is useful to bring all the relationships of
                a secondary volume to a consistent state.
        
        :param options: Describes options for snap create request.
        
        :param lock_backing_snapshot: When set to 'true' any snapshots backing the LUN clones
                present in the snapshot being created will be locked down. As
                a result, the locked backing snapshots can't be deleted as long
                as the snapshot that is locking them exists. The default value
                for this option is 'false', which doesn't lock any backing
                snapshots.
        """
        return self.request( "snapvault-secondary-initiate-snapshot-create", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'schedule_name': [ schedule_name, 'schedule-name', [ basestring, 'None' ], False ],
            'options': [ options, 'options', [ SnapvaultSnapcreateOptions, 'None' ], False ],
            'lock_backing_snapshot': [ lock_backing_snapshot, 'lock-backing-snapshot', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_configuration_list_info(self):
        """
        Request to return a list of all configuration entries found
        on the secondary system.
        @test
        """
        return self.request( "snapvault-secondary-configuration-list-info", {
        }, {
            'configurations': [ SnapvaultConfigurationInfo, True ],
        } )
    
    def snapvault_secondary_abort_snapshot_create(self, volume_name, schedule_name):
        """
        Request the secondary to abort a snapshot creation that is
        already in progress.
        The snapshot schedule for which the snapshot creation is in
        progress must be specified as input.
        @test
        
        :param volume_name: The secondary volume in which snapshot create is in
                progress.
        
        :param schedule_name: The name of the schedule used by the snapshot creation.
        """
        return self.request( "snapvault-secondary-abort-snapshot-create", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'schedule_name': [ schedule_name, 'schedule-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_delete_snapshot_schedule(self, volume_name, schedule_name=None):
        """
        Request the primary system to delete the specified
        snapshot schedules. The snapshot schedules that match the
        volume name and if specified the schedule name, will be
        deleted.
        @test
        
        :param volume_name: The primary volume for which the schedules are to be
                deleted.
        
        :param schedule_name: Name of the schedule to be deleted.
        """
        return self.request( "snapvault-primary-delete-snapshot-schedule", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'schedule_name': [ schedule_name, 'schedule-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_get_relationship_status(self, system_path):
        """
        Request the primary to return the status entries for
        desired relationships. The relationships whose status is
        desired must be specified using the system path.
        When snapvault primary and secondary are licensed on the
        same filer, output of this API is identical to the output
        of snapvault-secondary-get-relationship-status
        @test
        
        :param system_path: System path for relationships whose status
                is desired.
        """
        return self.request( "snapvault-primary-get-relationship-status", {
            'system_path': [ system_path, 'system-path', [ basestring, 'None' ], False ],
        }, {
            'status': [ SnapvaultStatusInfo, True ],
        } )
    
    def snapvault_secondary_destinations_list_info(self, source_path=None):
        """
        Request the secondary to list all snapvault destinations
        that have been replicated from any source path on this
        secondary system.
        If a source path is provided, then the secondary will
        return destinations information only for that source path.
        When snapvault primary and secondary are licensed on the
        same filer, output of this API is identical to the output
        of snapvault-primary-destinations-list-info
        @test
        
        :param source_path: Source path on this secondary for which the destination
                information is desired.
        """
        return self.request( "snapvault-secondary-destinations-list-info", {
            'source_path': [ source_path, 'source-path', [ basestring, 'None' ], False ],
        }, {
            'destinations': [ SnapvaultDestinationInfo, True ],
        } )
    
    def snapvault_secondary_create_relationship(self, configuration, no_lun_clone_expansion=None):
        """
        Request the secondary system to configure a new snapvault
        relationship with the given primary and secondary systems
        and paths. This API is equivalent to the 'snapvault start'
        Data ONTAP command.
        All the inputs provided with this request will
        be stored in the configuration entry maintained by the
        secondary system. These values will be used as default
        settings for further incremental update transfers for
        this relationship. The
        snapvault-secondary-modify-configuration API can be used
        to change these configured settings.
        A successful configuration will automatically be followed
        by a baseline transfer from the primary to the secondary.
        The secondary path will be created during the baseline
        transfer hence it is required that the secondary path must
        not exist when issuing this request.
        This request will only begin the baseline transfer and
        return. The transfer will proceed asynchronously and there
        is no guarantee that it will succeed. The
        snapvault-get-relationship-status API should be used to
        check the status of the transfer.
        @test
        
        :param configuration: Relationship configuration
        
        :param no_lun_clone_expansion: This option dictates how a lun clone would be transferred
                from source to destination. If this option is "false", a
                LUN clone would be transferred as a LUN and if it is "true",
                it will be transferred as a clone.
                By default the value of the option is "false".
        """
        return self.request( "snapvault-secondary-create-relationship", {
            'no_lun_clone_expansion': [ no_lun_clone_expansion, 'no-lun-clone-expansion', [ bool, 'None' ], False ],
            'configuration': [ configuration, 'configuration', [ SnapvaultConfigurationInfo, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_delete_snapshot_schedule(self, volume_name, schedule_name=None, delete_schedule_softlock=None):
        """
        Request the secondary system to delete the specified
        snapshot schedules. The snapshot schedules that match the
        volume name and the snapshot prefix when specified, will be
        deleted.
        @test
        
        :param volume_name: The secondary volume for which the schedule is to be
                deleted.
        
        :param schedule_name: The name of the schedule to be deleted.
        
        :param delete_schedule_softlock: When set to 'true', snapvault will delete ACS softlock set
                by this schedule. The default value for this option is 'false'.
        """
        return self.request( "snapvault-secondary-delete-snapshot-schedule", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'schedule_name': [ schedule_name, 'schedule-name', [ basestring, 'None' ], False ],
            'delete_schedule_softlock': [ delete_schedule_softlock, 'delete-schedule-softlock', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_get_relationship_status(self, system_path):
        """
        Request the secondary to return the status entries for
        desired relationships. The relationships whose status is
        desired must be specified using the system path.
        When snapvault primary and secondary are licensed on the
        same filer, output of this API is identical to the output
        of snapvault-primary-get-relationship-status
        @test
        
        :param system_path: System path for the relationships whose status is
                desired.
        """
        return self.request( "snapvault-secondary-get-relationship-status", {
            'system_path': [ system_path, 'system-path', [ basestring, 'None' ], False ],
        }, {
            'status': [ SnapvaultStatusInfo, True ],
        } )
    
    def snapvault_primary_destinations_list_info(self, source_path=None):
        """
        Request the primary to list all snapvault destinations
        that have been replicated from any source path on this
        primary system.
        If a source path is provided, then the primary will
        return destinations information only for that source path.
        When snapvault primary and secondary are licensed on the
        same filer, output of this API is identical to the output
        of snapvault-primary-destinations-list-info
        @test
        
        :param source_path: Source path on this primary for which the destination
                information is desired.
        """
        return self.request( "snapvault-primary-destinations-list-info", {
            'source_path': [ source_path, 'source-path', [ basestring, 'None' ], False ],
        }, {
            'destinations': [ SnapvaultDestinationInfo, True ],
        } )
    
    def snapvault_primary_initiate_incremental_restore_transfer(self, secondary_path, secondary_system, primary_path, secondary_snapshot=None, no_lun_clone_expansion=None, connection_mode=None, max_transfer_rate=None):
        """
        Request to initiate an incremental restore from a given
        secondary path to an existing primary path, using the
        specified secondary snapshot. The request will only
        initiate the restore and return. The actual restore operation
        will proceed asynchronously and there is no guarantee that
        it will succeed. The snapvault-primary-get-relationship-
        status API should be used to determine progress of the
        restore operation.
        If the dataset contains LUNs, the restore will attempt to
        prevent disruptions to clients using those LUNs.
        Upon success, the primary path will have the exact same
        contents as the specified secondary path in the specified
        secondary snapshot.
        @test
        
        :param secondary_path: The secondary path to restore from.
        
        :param secondary_system: The secondary system to restore from.
                This input will be used by the primary system to establish
                contact with the secondary. Therefore it is expected to be a
                hostname that the primary can resolve.
        
        :param primary_path: The pre-existing primary path to which data is being restored.
        
        :param secondary_snapshot: Name of the secondary snapshot to be used for this restore
                transfer.
        
        :param no_lun_clone_expansion: This option dictates how a lun clone would be transferred
                from source to destination. If this option is "flase", a
                LUN clone would be transferred as a LUN and if it is "true",
                it will be transferred as a clone.
                By default the value of the option is "false".
        
        :param connection_mode: This option specifies the mode to be used for establising
                connection between primary and secondary. If this option
                is set to "inet6", connections between primary and secondary
                will be established using IPv6 addresses only. If there are
                no IPv6 addressess configured, then the connection will fail.
                If the option is set to "inet", connections between primary
                and secondary will be established using IPv4 addresses only.
                If there are no IPv4 addresses configured, then the connection
                will fail.
                When this option is not specified, Connection will be tried
                using both "inet6" and "inet". "inet6" will have higher
                precedence than "inet". If connection request using "inet6"
                fails, SnapMirror will retry the connection using "inet".
                This argument is not effective when an IP address is specified
                instead of secondary hostname. If the IP address format and
                connection mode do not match, the operation will fail with
                proper error message.
        
        :param max_transfer_rate: The maximum transfer rate in kilobytes (1024 bytes) per
                second to be applied only for this transfer.
                If this option is not provided the default behavior will
                be to allow the transfer to proceed as fast as possible.
                Range:[1..2^31-2]
        """
        return self.request( "snapvault-primary-initiate-incremental-restore-transfer", {
            'secondary_path': [ secondary_path, 'secondary-path', [ basestring, 'None' ], False ],
            'secondary_snapshot': [ secondary_snapshot, 'secondary-snapshot', [ basestring, 'None' ], False ],
            'secondary_system': [ secondary_system, 'secondary-system', [ basestring, 'None' ], False ],
            'primary_path': [ primary_path, 'primary-path', [ basestring, 'None' ], False ],
            'no_lun_clone_expansion': [ no_lun_clone_expansion, 'no-lun-clone-expansion', [ bool, 'None' ], False ],
            'connection_mode': [ connection_mode, 'connection-mode', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_initiate_restore_transfer(self, secondary_path, secondary_system, primary_path, secondary_snapshot=None, overwrite_existing_content=None, no_lun_clone_expansion=None, connection_mode=None, max_transfer_rate=None):
        """
        Request the primary system to begin a baseline restore
        transfer from the given secondary path to the given
        primary path.
        If the primary path does not already exist, it will be
        created before starting the restore transfer. If it
        already exists, its contents will be overwritten by the
        restore transfer if overwrite-existing-content is set to true
        else an error is returned.
        If an existing primary path contains LUNs, then under certain
        conditions, restore will prevent disruptions to clients using
        those LUNs.
        The request will only start the restore transfer and
        return. The actual transfer will proceed asynchronously
        and there is no guarantee that it will succeed. The
        snapvault-primary-get-relationship-status API should be
        used to check the status of the restore.
        @test
        
        :param secondary_path: The secondary path to restore from.
        
        :param secondary_system: The secondary system to restore from.
                This input will be used by the primary system to
                establish contact with the secondary. Therefore it is
                expected to be a hostname that the primary can resolve.
        
        :param primary_path: The primary path to which data is being restored.
                The primary path will be created during the restore if it
                doesn't already exist.
        
        :param secondary_snapshot: Name of the secondary snapshot to be used for this restore
                transfer.
                If this option is not provided, the secondary system will
                choose the snapshot that contains the most recent back-up
                for this secondary path.
        
        :param overwrite_existing_content: This option specifies to overwrite an existing primary qtree
                or not.
                If specified primary qtree path already exists and the option
                is set to "true" the existing qtree will be overwritten and
                and previous data will be lost.
                If specified primary qtree path already exists and the option
                is set to "false" then an error is returned.
                The default value of the option is "true".
        
        :param no_lun_clone_expansion: This option dictates how a lun clone would be transferred
                from source to destination. If this option is "false", a
                LUN clone would be transferred as a LUN and if it is "true",
                it will be transferred as a clone.
                By default the value of the option is "false".
        
        :param connection_mode: This option specifies the mode to be used for establising
                connection between primary and secondary. If this option
                is set to "inet6", connections between primary and secondary
                will be established using IPv6 addresses only. If there are
                no IPv6 addressess configured, then the connection will fail.
                If the option is set to "inet", connections between primary
                and secondary will be established using IPv4 addresses only.
                If there are no IPv4 addresses configured, then the connection
                will fail.
                When this option is not specified, Connection will be tried
                using both "inet6" and "inet". "inet6" will have higher
                precedence than "inet". If connection request using "inet6"
                fails, SnapMirror will retry the connection using "inet".
                This argument is not effective when an IP address is specified
                instead of secondary hostname. If the IP address format and
                connection mode do not match, the operation will fail with
                proper error message.
        
        :param max_transfer_rate: The maximum transfer rate in kilobytes (1024 bytes) per
                second to be applied only for this update transfer.
                If this option is not provided the default behavior will
                be to allow the transfer to proceed as fast as possible.
                Range:[1..2^31-2]
        """
        return self.request( "snapvault-primary-initiate-restore-transfer", {
            'secondary_path': [ secondary_path, 'secondary-path', [ basestring, 'None' ], False ],
            'secondary_snapshot': [ secondary_snapshot, 'secondary-snapshot', [ basestring, 'None' ], False ],
            'secondary_system': [ secondary_system, 'secondary-system', [ basestring, 'None' ], False ],
            'primary_path': [ primary_path, 'primary-path', [ basestring, 'None' ], False ],
            'overwrite_existing_content': [ overwrite_existing_content, 'overwrite-existing-content', [ bool, 'None' ], False ],
            'no_lun_clone_expansion': [ no_lun_clone_expansion, 'no-lun-clone-expansion', [ bool, 'None' ], False ],
            'connection_mode': [ connection_mode, 'connection-mode', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
        }, {
        } )
    
    def snapvault_remove_softlock(self, volume, snapshot, softlock_name=None):
        """
        request the system to remove softlock for the given snapshot.
        EAPIMISSINGARGUMENT
        EONTAPI_ERANGE
        EONTAPI_ERANGE
        ESNAPVAULTRESOURCE
        
        :param volume: Name of the volume where the snapshot exists.
        
        :param snapshot: Name of the snapshot for which softlock to be removed.
        
        :param softlock_name: Name of softlock which uniquely identifies the softlock for the
                snapshot. When not specified, softlock with default name will
                be removed. When softlock-name has value "-all", all softlocks
                on the snapshot will be removed. Name of softlock can contain
                letters, numbers, and underscore character (_), and can be up
                to 64 characters long.
        """
        return self.request( "snapvault-remove-softlock", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'softlock_name': [ softlock_name, 'softlock-name', [ basestring, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_release_relationship(self, secondary_path, primary_path, secondary_system):
        """
        Request the release of a snapvault relationship formed
        by a "create-relationship" or "resync-relationship"
        operation.
        This operation deletes the registry entry and the
        softlocks on the source snapshot.
        @test
        
        :param secondary_path: The secondary path for the relationship.
        
        :param primary_path: The primary path for the relationship.
        
        :param secondary_system: The secondary system for the relationship.
        """
        return self.request( "snapvault-primary-release-relationship", {
            'secondary_path': [ secondary_path, 'secondary-path', [ basestring, 'None' ], False ],
            'primary_path': [ primary_path, 'primary-path', [ basestring, 'None' ], False ],
            'secondary_system': [ secondary_system, 'secondary-system', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_relationship_status_list_iter_end(self, tag):
        """
        Terminate the status list iteration set up by the
        snapvault-primary-relationship-status-list-iter-start API.
        The primary will clean up any saved info for this iteration.
        @test
        
        :param tag: Tag from the previous
                primary-relationship-status-list-iter-start.
        """
        return self.request( "snapvault-primary-relationship-status-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def snapvault_secondary_get_configuration(self, secondary_path):
        """
        Request the secondary to return the configuration entry
        for a relationship. The relationship must be specified
        by providing the secondary path as input.
        @test
        
        :param secondary_path: The secondary path for the relationship whose configuration
                entry is desired.
        """
        return self.request( "snapvault-secondary-get-configuration", {
            'secondary_path': [ secondary_path, 'secondary-path', [ basestring, 'None' ], False ],
        }, {
            'configuration': [ SnapvaultConfigurationInfo, False ],
        } )
    
    def snapvault_secondary_snapshot_schedule_status_list_info(self, volume_name=None):
        """
        Request the secondary to return status for all configured
        snapshot schedules. If a specific volume is provided as
        input, this API will return only the status for schedules
        within that volume.
        This API corresponds to the 'snapvault status -s' Data
        ONTAP command.
        When snapvault primary and secondary are licensed on the
        same filer, output of this API is identical to the output
        of snapvault-primary-snapshot-schedule-status-list-info
        @test
        
        :param volume_name: Secondary volume for which snapshot schedule status is
                desired.
        """
        return self.request( "snapvault-secondary-snapshot-schedule-status-list-info", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'snapshot-schedule-status': [ SnapvaultSnapshotScheduleStatusInfo, True ],
        } )
    
    def snapvault_secondary_delete_relationship(self, secondary_path):
        """
        Request the secondary system to unconfigure and delete
        the relationship permanently. The secondary path will be
        deleted. But none of the snapshots that capture this
        secondary path will be deleted.
        This API corresponds to the 'snapvault stop' Data ONTAP
        command.
        @test
        
        :param secondary_path: The secondary-path to be deleted. The path will be
                unconfigured and deleted.
        """
        return self.request( "snapvault-secondary-delete-relationship", {
            'secondary_path': [ secondary_path, 'secondary-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_relationship_status_list_iter_next(self, tag, maximum):
        """
        Request the secondary to continue the iteration set up with
        the snapvault-secondary-relationship-status-list-iter-start
        API. A list consisting of a number of status entries, upto
        the specified maximum, will be returned.
        When snapvault primary and secondary are licensed on the
        same filer, output of this API is identical to the output
        of snapvault-primary-relationship-status-list-iter-next
        @test
        
        :param tag: Tag from a previous
                secondary-relationship-status-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
                Range:[0..2^32-1]
        """
        return self.request( "snapvault-secondary-relationship-status-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'status-list': [ SnapvaultStatusInfo, True ],
            'records': [ int, False ],
        } )
    
    def snapvault_primary_abort_transfer(self, system_path, target_system=None, is_hard_abort=None):
        """
        Request the primary system to abort an active transfer.
        The abort can be hard abort, which means the transfer will
        not be restartable. Or it could be a soft abort, which
        will not clean the restart checkpoints. In that case the
        transfer may be restartable.
        An aborted transfer may be restarted by using the same API
        used to initiate the transfer in the previous attempt. If
        that request cannot restart the aborted transfer, then it
        will initiate a fresh new transfer.
        @test
        
        :param system_path: The system path which is the target of transfer.
        
        :param target_system: The system filer which is the target of transfer.
        
        :param is_hard_abort: When set to 'true' a hard abort is performed. In that case
                the restart checkpoints are cleared.
                Default value is 'false'.
        """
        return self.request( "snapvault-primary-abort-transfer", {
            'target_system': [ target_system, 'target-system', [ basestring, 'None' ], False ],
            'system_path': [ system_path, 'system-path', [ basestring, 'None' ], False ],
            'is_hard_abort': [ is_hard_abort, 'is-hard-abort', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_set_snapshot_schedule(self, snapshot_schedule):
        """
        Request the secondary system to configure the specified
        snapshot schedule. If this request is made for an existing
        snapshot schedule, then that snapshot schedule is updated
        with any new values specified. If the optional input
        schedule is skipped, the days-of-week is set to "mon-sun"
        and hours-of-day set to 0, i.e. midnight.
        @test
        
        :param snapshot_schedule: Specifies details of the schedule to be set.
        """
        return self.request( "snapvault-secondary-set-snapshot-schedule", {
            'snapshot_schedule': [ snapshot_schedule, 'snapshot-schedule', [ SnapvaultSecondarySnapshotScheduleInfo, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_initiate_snapshot_create(self, volume_name, schedule_name, options=None):
        """
        Request the primary to force a snapshot creation for a
        specified snapshot schedule. The snapshot schedule must be
        identified by the volume name and the snapshot prefix. All
        the properties of the specified schedule will be applied to
        the snapshot creation.
        This API should be used when it is desirable to create
        snapshots right away, without having to wait for the
        pre-configured scheduled time. This API returns after only
        initiating the snapshot creation, and there is no guarantee
        that the snapshot creation will succeed.
        The snapvault-primary-snapshot-schedule-status-list-info
        API should be used to track progress of the snapshot
        creation.
        @test
        
        :param volume_name: The primary volume for which the snapshot schedule was
                configured.
        
        :param schedule_name: The name of the schedule to be used for this snapshot
                creation.
        
        :param options: Describes options for snap create request.
        """
        return self.request( "snapvault-primary-initiate-snapshot-create", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'schedule_name': [ schedule_name, 'schedule-name', [ basestring, 'None' ], False ],
            'options': [ options, 'options', [ SnapvaultSnapcreateOptions, 'None' ], False ],
        }, {
        } )
    
    def snapvault_secondary_abort_transfer(self, system_path, target_system=None, is_hard_abort=None):
        """
        Request the secondary system to abort the current transfer.
        The abort can be hard abort, which means the transfer will
        not be restartable. By default, a soft abort is used,
        which means the transfer is restartable.
        An aborted transfer may be restarted by using the same API
        used to initiate the transfer in the previous attempt. If
        that request cannot restart the aborted transfer, then it
        will initiate a fresh new transfer.
        @test
        
        :param system_path: The system path which is the target of update.
        
        :param target_system: The system filer which is the target of transfer.
        
        :param is_hard_abort: When set to 'true' a hard abort is performed. In that case
                the restart checkpoints are cleared.
                Default value is 'false'.
        """
        return self.request( "snapvault-secondary-abort-transfer", {
            'target_system': [ target_system, 'target-system', [ basestring, 'None' ], False ],
            'system_path': [ system_path, 'system-path', [ basestring, 'None' ], False ],
            'is_hard_abort': [ is_hard_abort, 'is-hard-abort', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_snapshot_schedule_list_info(self, volume_name=None):
        """
        Request the primary to return a list of configured
        snapshot schedules. Without any input arguments this
        request returns the list of all snapshot schedules
        configured on the primary. If a volume is specified
        then only the list of schedules configured for that
        volume will be returned.
        When snapvault primary and secondary are licensed on the
        same filer, snapvault-secondary-snapshot-schedule-list-info
        and this API return the same number of schedules.
        @test
        
        :param volume_name: The primary volume for which the list of snapshot
                schedules are desired.
        """
        return self.request( "snapvault-primary-snapshot-schedule-list-info", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'snapshot-schedules': [ SnapvaultPrimarySnapshotScheduleInfo, True ],
        } )
    
    def snapvault_primary_relationship_status_list_iter_start(self):
        """
        Request the primary to start an iteration through the
        list of the status entries for all relationships.
        @test
        """
        return self.request( "snapvault-primary-relationship-status-list-iter-start", {
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def snapvault_secondary_release_relationship(self, primary_path, secondary_path, primary_system):
        """
        Request the release of a snapvault relationship formed
        after a restore operation on the primary system.
        This operation deletes the registry entry and removes the
        softlock on the source base snapshot.
        @test
        
        :param primary_path: The primary path that had been used for the restore.
        
        :param secondary_path: The secondary path that was used as source for restore.
        
        :param primary_system: The primary system which had performed the restore.
        """
        return self.request( "snapvault-secondary-release-relationship", {
            'primary_path': [ primary_path, 'primary-path', [ basestring, 'None' ], False ],
            'secondary_path': [ secondary_path, 'secondary-path', [ basestring, 'None' ], False ],
            'primary_system': [ primary_system, 'primary-system', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapvault_primary_snapshot_schedule_status_list_info(self, volume_name=None):
        """
        Request the primary to return status for all configured
        snapshot schedules. If a specific volume is provided as
        input, this API will return only the status for schedules
        within that volume.
        When snapvault primary and secondary are licensed on the
        same filer, output of this API is identical to the output
        of snapvault-secondary-snapshot-schedule-status-list-info
        @test
        
        :param volume_name: Primary volume for which snapshot schedule status is
                desired.
        """
        return self.request( "snapvault-primary-snapshot-schedule-status-list-info", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'snapshot-schedule-status': [ SnapvaultSnapshotScheduleStatusInfo, True ],
        } )

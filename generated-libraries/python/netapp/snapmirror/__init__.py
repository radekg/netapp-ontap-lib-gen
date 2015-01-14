from netapp.connection import NaConnection
from snapmirror_promote_iter_info import SnapmirrorPromoteIterInfo # 3 properties
from snapmirror_initialize_iter_key_td import SnapmirrorInitializeIterKeyTd # 14 properties
from snapmirror_release_iter_info import SnapmirrorReleaseIterInfo # 3 properties
from snapmirror_resume_iter_info import SnapmirrorResumeIterInfo # 3 properties
from snapmirror_modify_iter_key_td import SnapmirrorModifyIterKeyTd # 14 properties
from snapmirror_modify_iter_info import SnapmirrorModifyIterInfo # 3 properties
from snapmirror_break_iter_key_td import SnapmirrorBreakIterKeyTd # 14 properties
from snapmirror_destroy_iter_info import SnapmirrorDestroyIterInfo # 3 properties
from snapmirror_destination_info import SnapmirrorDestinationInfo # 13 properties
from snapmirror_error import SnapmirrorError # 2 properties
from snapmirror_promote_iter_key_td import SnapmirrorPromoteIterKeyTd # 14 properties
from snapmirror_resume_iter_key_td import SnapmirrorResumeIterKeyTd # 14 properties
from snapmirror_initialize_iter_info import SnapmirrorInitializeIterInfo # 5 properties
from snapmirror_quiesce_iter_key_td import SnapmirrorQuiesceIterKeyTd # 14 properties
from snapmirror_abort_iter_info import SnapmirrorAbortIterInfo # 3 properties
from snapmirror_destroy_iter_key_td import SnapmirrorDestroyIterKeyTd # 14 properties
from snapmirror_resync_iter_info import SnapmirrorResyncIterInfo # 5 properties
from snapmirror_status_info import SnapmirrorStatusInfo # 17 properties
from snapmirror_get_destination_iter_key_td import SnapmirrorGetDestinationIterKeyTd # 7 properties
from address_pair import AddressPair # 2 properties
from snapmirror_update_iter_info import SnapmirrorUpdateIterInfo # 5 properties
from snapmirror_sync_schedule_info import SnapmirrorSyncScheduleInfo # 9 properties
from snapmirror_resync_iter_key_td import SnapmirrorResyncIterKeyTd # 14 properties
from snapmirror_info import SnapmirrorInfo # 43 properties
from snapmirror_update_iter_key_td import SnapmirrorUpdateIterKeyTd # 14 properties
from snapmirror_check_iter_key_td import SnapmirrorCheckIterKeyTd # 14 properties
from snapmirror_schedule_info import SnapmirrorScheduleInfo # 10 properties
from snapshot_owner_name import SnapshotOwnerName # 0 properties
from snapmirror_abort_iter_key_td import SnapmirrorAbortIterKeyTd # 14 properties
from snapmirror_connection_info import SnapmirrorConnectionInfo # 5 properties
from snapmirror_break_iter_info import SnapmirrorBreakIterInfo # 3 properties
from snapmirror_release_iter_key_td import SnapmirrorReleaseIterKeyTd # 7 properties
from snapmirror_quiesce_iter_info import SnapmirrorQuiesceIterInfo # 3 properties
from snapmirror_get_iter_key_td import SnapmirrorGetIterKeyTd # 14 properties
from snapmirror_check_iter_info import SnapmirrorCheckIterInfo # 5 properties
from destination_info import DestinationInfo # 3 properties

class SnapmirrorConnection(NaConnection):
    
    def snapmirror_get_status(self, location=None):
        """
        Return the SnapMirror status.  This API can be issued
        on either the source or destination filer.
        
        :param location: The source location or destination location of the
                SnapMirror pair. Possible types are volume or qtree only.
                If this input is provided, only the SnapMirror relationships
                with a matching source or destination will be reported.
                The argument is invalid if the named location doesn't exist.
                In this case, snapmirror-status-info output will not be present.
                The argument can also be invalid if it is a flexclone name.
                (Be aware that the snapmirror-list-destinations API can return
                flexclone names.) Then snapmirror-get-status API will return
                a snapmirror-status output value with a "state" of "unknown".
                If the argument is not specified, all source, destination
                SnapMirror pairs are returned.
        """
        return self.request( "snapmirror-get-status", {
            'location': [ location, 'location', [ basestring, 'None' ], False ],
        }, {
            'snapmirror-status': [ SnapmirrorStatusInfo, True ],
            'is-available': [ bool, False ],
        } )
    
    def snapmirror_list_destinations(self, source_location=None):
        """
        Returns a list of destination locations and information
        about SnapMirror relationships for given source
        locations, which can be a volume name or qtree path.
        This API must be issued on the source filer.
        
        :param source_location: Source location of the SnapMirror pair.  The source
                location is of the volume form: &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
                If the source-location is not specified, then all source,
                destination SnapMirror pairs are returned.
        """
        return self.request( "snapmirror-list-destinations", {
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
        }, {
            'destinations': [ DestinationInfo, True ],
        } )
    
    def snapmirror_get(self, source_vserver=None, source_volume=None, desired_attributes=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        The snapmirror-get API returns information for a SnapMirror
        relationship.
        <p>
        On Data ONTAP 8.1 operating in Cluster-Mode this API can be
        issued on the source cluster or destination cluster of the
        relatonship.
        On Data ONTAP 8.2 operating in Cluster-Mode, this API must be
        issued on the destination Vserver or the destination cluster of
        the relationship.
        The destination endpoint must be specified when using the
        snapmirror-get API.
        </p>
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-get", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapmirrorInfo, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ SnapmirrorInfo, False ],
        } )
    
    def snapmirror_resume(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        Enables future transfers for a SnapMirror relationship that
        has been quiesced. If there is a scheduled transfer, it will
        be triggered on the next schedule. If there is a restart
        checkpoint, it will be re-used if possible.
        On Data ONTAP Cluster-Mode, If applied on a load-sharing
        SnapMirror relationship, transfers will resume for all the
        relationships of the set.
        When a quiesced SnapMirror relationship is resumed, it remains in
        that state across reboots and fail-overs.
        The relationship must exist on the destination and you must
        specify the destination end point when using snapmirror-resume.
        This API must be issued on the destination storage system on
        Data ONTAP operating in 7-Mode, on the destination cluster on
        Data ONTAP 8.1 operating in Cluster-Mode, and on the destination
        Vserver on Data ONTAP 8.2 or later operating in Cluster-Mode.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source volume.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship. The
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter.
        
        :param destination_vserver: Specifies the destination Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, when specifying a
                destination endpoint, you must use either the destination
                location, or the destination cluster, destination Vserver,
                and destination volume.
                This parameter is mandatory on Data ONTAP operating in 7-mode.
        
        :param destination_volume: Specifies the destination volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, When specifying a
                source endpoint, you must use either the source location, or the
                source cluster, source Vserver, and source volume.
        
        :param destination_cluster: Specifies the destination cluster of the SnapMirror relationship.
                The destination Vserver and destination volume must also be
                specified if using this parameter.
        """
        return self.request( "snapmirror-resume", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_promote_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        The snapmirror-promote-iter API performs failover for one or more
        SnapMirror relationships.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "snapmirror-promote-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorPromoteIterInfo, True ],
            'failure-list': [ SnapmirrorPromoteIterInfo, True ],
        } )
    
    def snapmirror_initialize(self, source_vserver=None, source_volume=None, destination_snapshot=None, transfer_priority=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, source_snapshot=None, max_transfer_rate=None, destination_cluster=None):
        """
        Performs the initial update of a SnapMirror relationship.
        You must specify the destination endpoint when using
        snapmirror-initialize.
        This API must be used from the destination storage system on
        Data ONTAP operating in 7-Mode, from the destination cluster
        on Data ONTAP 8.1 operating in Cluster-Mode, and from the
        destination Vserver on Data ONTAP 8.2 or later operating
        in Cluster-Mode.
        <p>
        On Data ONTAP operating in 7-Mode, If the destination endpoint
        is a volume, the volume must be in the restricted state.
        If the destination endpoint is a qtree, the qtree must not
        already exist.
        <p>
        On Data ONTAP operating in Cluster-Mode, this API is usually
        used after the snapmirror-create API, but it can be used alone,
        that is, without the snapmirror-create API, to create and
        initially update a SnapMirror relationship.
        <p>
        On Data ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP
        8.2 operating in Cluster-Mode for relationships using
        a control plane compatible with Data ONTAP 8.1 operating
        Cluster-Mode (The relationship-control-plane field is set to
        'v1'), a job will be spawned to operate on the SnapMirror
        relationship, and the job id will be returned. The progress of
        the job can be tracked using the job APIs.
        <p>
        On Data ONTAP 8.2 or later operating in Cluster-Mode, for
        vault relationships, a 32-bit volume cannot be the source
        or destination of the relationship.
        <p>
        On Data ONTAP 8.2 or later operating in Cluster-Mode, you
        can track the progress of the operation using the
        snapmirror-get API, except for relationships using a control
        plane compatible with  Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source volume.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship. The
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_snapshot: Creates the specified snapshot (in addition to the regular
                SnapMirror snapshot) on the destination after the qtree
                SnapMirror transfer is over.
        
        :param transfer_priority: Specifies the priority at which the transfer runs.
                Possible values are: "normal", and "low".  The default
                value is the value specified in the snapmirror policy which
                is associated with the relationship.
                <p>This parameter only applies on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane
                is 'v2'.
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter.
        
        :param destination_vserver: Specifies the destination Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, when specifying a
                destination endpoint, you must use either the destination
                location, or the destination cluster, destination Vserver, and
                destination volume.
                On Data ONTAP operating in 7-Mode, if the destination endpoint
                is a volume, the volume must be in the restricted state.
                If the destination endpoint is a qtree, the qtree must not
                already exist.
                <p> This parameter is mandatory on Data ONTAP operating in
                7-mode.
        
        :param destination_volume: Specifies the destination volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode when specifying a
                source endpoint, you must use either the source location, or the
                source  cluster, source Vserver, and source volume.
                On Data ONTAP operating in 7-Mode, If the source-location is not
                specified, then the source in /etc/snapmirror.conf for the
                destination path is used.
        
        :param source_snapshot: Designates the source snapshot to use for a qtree update
                on Data ONTAP operating in 7-mode, and the snapshot on the
                source volume to use for the baseline transfer
                on Data ONTAP 8.2 or later operating in
                Cluster-Mode.
                The default creates new snapshot on the source for the
                transfer.
                <p>This parameter only applies on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v2'.
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth.
                On Data ONTAP operating in Cluster-Mode, the max-transfer-rate
                option does not affect load-sharing transfers and transfers for
                other relationships with Relationship Capability of Pre 8.2
                confined to a single cluster.
        
        :param destination_cluster: Specifies the destination cluster of the SnapMirror relationship.
                The destination Vserver and destination volume must also be
                specified if using this parameter.
        """
        return self.request( "snapmirror-initialize", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'destination_snapshot': [ destination_snapshot, 'destination-snapshot', [ basestring, 'None' ], False ],
            'transfer_priority': [ transfer_priority, 'transfer-priority', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'source_snapshot': [ source_snapshot, 'source-snapshot', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_promote(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        The snapmirror-promote API performs a failover to the destination
        volume of a load-sharing SnapMirror relationship. This API
        changes the destination volume from a load-sharing volume to a
        read-write volume and makes the destination volume assume the
        identity of the source volume. The API then destroys the original
        source volume. The destination volume must be a load-sharing
        volume. However, you can still perform 'snapmirror-promote' on a
        destination load-sharing volume that has been left in read-write
        state by a previously failed promote operation.
        You must specify the destination endpoint when using
        snapmirror-promote.
        Note: The source volume and destination volume must be on the
        same Vserver for the promote to work.
        Client accesses are redirected from the original source volume to
        the promoted destination volume. The view clients see on the
        promoted destination volume is the latest transferred Snapshot
        copy, which might lag behind the view clients had of the original
        source volume before the promote.
        The SnapMirror relationship is usually deleted as part of the
        promotion process. This is not true for a set of load-sharing
        mirrors that contain more than one destination volume. In this
        case, the promoted destination volume becomes the new source
        volume to the set of load-sharing mirrors.
        It is possible that the original source volume is the source of
        multiple SnapMirror relationships. For such a configuration, the
        promoted destination volume becomes the new source volume of the
        other SnapMirror relationships.
        The snapmirror-promote API fails if a SnapMirror transfer is in
        progress for any SnapMirror relationship involving the original
        source volume.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-promote", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_restore(self, disable_storage_efficiency=None, source_vserver=None, source_volume=None, transfer_priority=None, source_cluster=None, tries=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, source_snapshot=None, max_transfer_rate=None, clean_up_failure=None, destination_cluster=None):
        """
        The snapmirror-restore API restores the contents of a selected
        Snapshot copy from the source volume to the active file system of
        the destination volume.  The destination volume is read write
        after the data is restored.
        The snapmirror-restore API creates a temporary SnapMirror
        relationship of the type RST. For this reason the destination
        volume cannot be the destination volume of another SnapMirror
        relationship. The temporary RST relationship is deleted after the
        operation completes successfully.
        If the destination volume is an empty data protection volume, the
        snapmirror-restore API performs a baseline restore. The baseline
        restore transfers the contents of the selected Snapshot copy from
        the source volume to the destination volume.
        If the destination volume is read-write and has at least one
        Snapshot which also appears on the source volume, an incremental
        restore is performed.
        The destination volume is made read only, if is not already read
        only. When the destination volume is made read only the latest
        snapshot on destination volume is made the exported snapshot.
        Note, that any data written to the destination volume since the
        last snapshot is lost during this operation. To save the contents
        of the active file system on the destination volume, stop all
        client access and take a snapshot before starting this
        operation.
        During an incremental restore a common Snapshot copy is selected.
        The snapshot chosen as the common snapshot must be on the source
        and destination volumes. The contents of the common Snapshot copy
        on the destination volume are copied to the active file system of
        the destination volume. Then the contents of the Snapshot copy to
        be restored are transferred from the source volume to the
        destination volume.
        Unless 'source-snapshot' is specified the most recent Snapshot
        copy on the source volume is restored.
        This API may be used to restart a failed snapmirror-restore
        operation.
        This API may be used to terminate an aborted or failed
        snapmirror-restore operation by specifying the 'clean-up-failure'
        parameter set to 'true'. Terminating an aborted or failed
        snapmirror-restore operation deletes any residual temporary RST
        relationship and converts the destination volume back to
        read-write if the destination volume was read-write prior to
        initial snapmirror-restore operation while removing any data
        transferred or copied during the snapmirror-restore operation.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param disable_storage_efficiency: The default behavior of restore is to preserve storage efficiency
                when possible. Use this parameter with a value of 'true' to turn
                off storage efficiency for data transferred over the wire and
                written to the destination volume. The default value for this
                parameter is false.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param transfer_priority: Specifies the priority at which the transfer runs.  Possible
                values are: 'normal', and 'low'. The default value for this
                parameter is 'normal'.
                Possible values:
                <ul>
                <li> "low"       ,
                <li> "normal"
                </ul>
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param tries: Specifies the total number of attempts to transfer data. Valid
                input is a positive integer or 'unlimited'. The default is '8'.
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param source_snapshot: Specifies the Snapshot from the source to be restored.
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth. The max-transfer-rate option does not affect
                load-sharing transfers and transfers for other relationships with
                Relationship Capability of Pre 8.2 confined to a single cluster.
        
        :param clean_up_failure: Use this parameter with the value of 'true' to recover from an
                aborted or failed restore operation. If the destination volume
                was read-write prior to the failed or aborted restore operation,
                it is converted back to read-write if necessary while removing
                all data transferred or copied during the restore operation. Any
                residual temporary RST relationship is also removed from the
                destination Vserver.  An attempt is made to remove any residual
                temporary RST relationship from the source Vserver. The default
                value for this parameter is 'false'.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-restore", {
            'disable_storage_efficiency': [ disable_storage_efficiency, 'disable-storage-efficiency', [ bool, 'None' ], False ],
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'transfer_priority': [ transfer_priority, 'transfer-priority', [ basestring, 'sm-transfer-priority-enum' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'tries': [ tries, 'tries', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'source_snapshot': [ source_snapshot, 'source-snapshot', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
            'clean_up_failure': [ clean_up_failure, 'clean-up-failure', [ bool, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_initialize_ls_set(self, source_cluster=None, source_vserver=None, source_location=None, source_volume=None):
        """
        The snapmirror-initialize-ls-set API performs the initial manual
        update of a set of load-sharing mirrors. This API is usually used
        after the snapmirror-create API is used to create a SnapMirror
        relationship for each of the destination volumes in the set of
        load-sharing mirrors.
        You must specify the source endpoint when using
        snapmirror-initialize-ls-set.
        Data and Snapshot copies are transferred from the source volume
        to all up-to-date destination volumes in the set of load-sharing
        mirrors.
        Use the snapmirror-initialize API to add and initialize a new
        destination volume to an existing set of load-sharing mirrors.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter. This parameter is supported only in cluster
                context.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship. The
                source cluster and source volume must also be specified if using
                this parameter.
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship.
                When specifying a source endpoint, you must use either the source
                location, or the source cluster, source Vserver, and source
                volume.
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship. The
                source cluster and source Vserver must also be specified if using
                this parameter. This parameter may be optional if executed
                outside cluster context.
        """
        return self.request( "snapmirror-initialize-ls-set", {
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_get_total_records(self):
        """
        Obtain the total number of SnapMirror relationships.  This is a
        point in time estimate and may be different on subsequent calls.
        """
        return self.request( "snapmirror-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def snapmirror_quiesce_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Disables future transfers for one or more SnapMirror
        relationships.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "snapmirror-quiesce-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorQuiesceIterInfo, True ],
            'failure-list': [ SnapmirrorQuiesceIterInfo, True ],
        } )
    
    def snapmirror_snapshot_owner_get_snapshots(self, vserver, volume):
        """
        List all Snapshot copies that are preserved for a SnapMirror
        mirror-to-vault cascade configuration.
        
        :param vserver: Vserver Name
        
        :param volume: Volume Name
        """
        return self.request( "snapmirror-snapshot-owner-get-snapshots", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
        }, {
            'snapshots': [ basestring, True ],
        } )
    
    def snapmirror_break_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        The snapmirror-break-iter API breaks one or more SnapMirror
        relationships.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "snapmirror-break-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorBreakIterInfo, True ],
            'failure-list': [ SnapmirrorBreakIterInfo, True ],
        } )
    
    def snapmirror_modify(self, source_vserver=None, source_volume=None, schedule=None, vserver=None, source_cluster=None, tries=None, destination_vserver=None, destination_location=None, policy=None, destination_volume=None, source_location=None, max_transfer_rate=None, destination_cluster=None):
        """
        The snapmirror-modify API changes one or more parameters of a
        SnapMirror relationship. The key parameter that identifies any
        SnapMirror  relationship is the destination volume.
        <p>
        You must specify the destination endpoint when using the
        snapmirror-modify API.
        For load-sharing mirrors, a change to a parameter affects all of
        the SnapMirror relationships in the set of load-sharing mirrors.
        Destination volumes in a set of load-sharing mirrors do not have
        individual parameter settings.
        Changes made by the snapmirror-modify API do not take effect
        until the next manual or scheduled update of the SnapMirror
        relationship. Changes do not affect updates that have started and
        have not finished yet.
        On Data ONTAP 8.1 operating in Cluster-Mode this API must be
        issued on the destination Cluster.
        On Data ONTAP 8.2 operating in Cluster-Mode, this API must be
        issued on the destination Vserver if operating in a Vserver
        context and on the destination cluster if operating in a cluster
        context.
        This API is not supported on Infinite Volume constituents.</p>
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param schedule: Specifies the name of the cron schedule, used to update the
                SnapMirror relationship.
        
        :param vserver: If this optional parameter is specified, designates the managing
                Vserver. The managing Vserver is authorized to use snapmirror
                commands to manage the SnapMirror relationship. The vserver
                option is currently a reserved option.
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param tries: Specifies the maximum number of times to attempt each manual or
                scheduled transfer for a SnapMirror relationship. The default is
                eight times.
                Note: You can set the tries option to zero (0) to disable manual
                and scheduled updates for the SnapMirror relationship. This
                parameter is only relevant on Data ONTAP 8.1 operating in
                Cluster-Mode. On Data ONTAP 8.2 operating in Cluster-Mode, the
                maximum number of times to attempt a transfer is an attribute of
                the SnapMirror policy. Therefore the value of this parameter is
                ignored.
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param policy: Specifies the name of the SnapMirror policy that applies to this
                relationship.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth.  The max-transfer-rate option does not affect
                load-sharing transfers and transfers for other relationships with
                Relationship Capability of Pre 8.2 confined to a single cluster.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-modify", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'tries': [ tries, 'tries', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'policy': [ policy, 'policy', [ basestring, 'sm-policy' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_abort_iter(self, query, check_only=None, max_failure_count=None, clear_checkpoint=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        The snapmirror-abort-iter API aborts SnapMirror transfers for one
        or more SnapMirror relationships. This API is not supported on
        Infinite Volume constituents.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param check_only: If this option is specified true, only snapmirror-check
                operations active on the relationship will be aborted.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param clear_checkpoint: If this option is specified true, the restart checkpoint is
                discarded and the destination volume is restored to the last
                Snapshot copy that was successfully transferred. You can use the
                clear-checkpoint option to discard the restart checkpoint of a
                previous transfer attempt which forces the subsequent transfer to
                start with a fresh Snapshot copy on the destination volume.
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "snapmirror-abort-iter", {
            'check_only': [ check_only, 'check-only', [ bool, 'None' ], False ],
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'clear_checkpoint': [ clear_checkpoint, 'clear-checkpoint', [ bool, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorAbortIterInfo, True ],
            'failure-list': [ SnapmirrorAbortIterInfo, True ],
        } )
    
    def snapmirror_throttle(self, destination_location, max_transfer_rate):
        """
        Changes the max transfer rate of an active transfer.
        The API can be issued to either the source or the
        destination filer.
        
        :param destination_location: The destination location of the active transfer.  The
                destination location is of the volume form:
                &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        
        :param max_transfer_rate: Maximum transfer rate in kilobytes per second.  A value '0'
                disables the throttle, ie. the filer will transfer as fast
                as it can. Range: 0..2^32-1
        """
        return self.request( "snapmirror-throttle", {
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_check_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None, target_snapshot=None):
        """
        The snapmirror-check-iter API checks one or more SnapMirror
        relationships.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on or
                scheduled to be worked on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        
        :param target_snapshot: Specifies the Snapshot copy on the destination endpoint to
                check.
        """
        return self.request( "snapmirror-check-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'target_snapshot': [ target_snapshot, 'target-snapshot', [ basestring, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorCheckIterInfo, True ],
            'failure-list': [ SnapmirrorCheckIterInfo, True ],
        } )
    
    def snapmirror_delete_schedule(self, destination_location):
        """
        Delete the schedule for a given destination.  This API
        must be executed on the destination filer.
        
        :param destination_location: The destination location of a schedule to delete.  The
                destination location is of the volume form:
                &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        """
        return self.request( "snapmirror-delete-schedule", {
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_snapshot_owner_destroy(self, vserver, volume, snapshot, snapshot_owner_name=None):
        """
        Delete an owner used to preserve a Snapshot copy for a SnapMirror
        mirror-to-vault cascade configuration.
        
        :param vserver: Vserver Name
        
        :param volume: Volume Name
        
        :param snapshot: Snapshot Copy Name
        
        :param snapshot_owner_name: The specified owner is removed from the Snapshot copy. If no
                owner name is provided, the system will look for and remove the
                internal default name for the owner. A specified owner of '*'
                removes all owners from the Snapshot copy.
        """
        return self.request( "snapmirror-snapshot-owner-destroy", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'snapshot-id' ], False ],
            'snapshot_owner_name': [ snapshot_owner_name, 'snapshot-owner-name', [ basestring, 'snapshot-owner-name' ], False ],
        }, {
        } )
    
    def snapmirror_delete_connection(self, connection):
        """
        Deletes a connection specified by connection.
        This API must be executed on the destination filer.
        Currently, the connections are in: /etc/snapmirror.conf.
        
        :param connection: Connection name to delete.  The name is in ASCII and
                must begin with an alpha character.
        """
        return self.request( "snapmirror-delete-connection", {
            'connection': [ connection, 'connection', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_destroy(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        The snapmirror-destroy API removes only the SnapMirror
        relationship of a source volume and a destination volume, the
        volumes are not destroyed and Snapshot copies on the volumes are
        not removed.
        You must specify the destination endpoint when using
        snapmirror-destroy.
        On Data ONTAP 8.1 operating in Cluster-Mode, the
        snapmirror-destroy API fails if a SnapMirror transfer for the
        SnapMirror relationship is in progress.
        On Data ONTAP 8.2 operating in Cluster-Mode, the
        snapmirror-destroy API will attempt to abort any ongoing
        transfer. However, failure to abort the transfer will not cause
        the API to fail.
        A set of load-sharing mirrors might contain multiple destination
        volumes, each destination volume having a separate SnapMirror
        relationship with the common source volume. When used on one of
        the SnapMirror relationships from the set of load-sharing
        mirrors, the snapmirror-destroy API deletes the specified
        SnapMirror relationship from the set of load-sharing mirrors.
        The snapmirror-destroy API preserves the read-write or read-only
        attributes of the volumes of a SnapMirror relationship after the
        relationship is deleted. Therefore, a read-write volume that was
        the source of a SnapMirror relationship  retains its read-write
        attributes, and a data protection volume or a load-sharing volume
        that was a destination of a SnapMirror relationship retains its
        read-only attributes.
        Note: When a SnapMirror relationship from a set of load-sharing
        mirrors is deleted, the destination volume becomes a data
        protection volume and retains the read-only attributes of a data
        protection volume.
        On Data ONTAP 8.2 operating in Cluster-Mode, this API can only be
        issued on the destination Vserver. The SnapMirror relationship
        information is deleted from destination Vserver, but no cleanup
        or deletion is performed on the source Vserver. The
        snapmirror-release API must be issued on the source Vserver to
        delete the relationship information on the source Vserver.
        On Data ONTAP 8.1 operating in Cluster-Mode, this API can be
        issued on the source or on the destination cluster. When issued
        on the destination cluster, the SnapMirror relationship
        information on the source and destination clusters is deleted.
        When issued on the source cluster, only the SnapMirror
        relationship information on the source cluster is deleted.
        Note: If the SnapMirror relationship identified by the
        destination endpoint does not exist, this API will return
        success.
        This API is not supported if the destination end point is a
        Infinite Volume.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-destroy", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Removes one or several SnapMirror relationships. This API is not
        supported on Infinite Volume constituents.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "snapmirror-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorDestroyIterInfo, True ],
            'failure-list': [ SnapmirrorDestroyIterInfo, True ],
        } )
    
    def snapmirror_set_schedule(self, hours, destination_location, days_of_month, source_location, minutes, days_of_week, is_compressed=None, max_transfer_rate=None, tcp_window_size=None, restart=None, connection_mode=None):
        """
        Sets the schedule for a given destination.  The API must
        be executed on the destination filer.  Currently,
        the schedule is in /etc/snapmirror.conf.
        
        :param hours: Hours in the day for which the schedule is set.
                The form is crontab-like, with possible values of:
                <ul>
                <li> -       := match nothing;
                <li> 1       := match hour 1;
                <li> 1,3     := match hour 1 and 3;
                <li> 2-5     := match hour 2,3,4,5;
                <li> 1-24/3  := match hour 1,4,7,10,13,16,19,22;
                <li> *       := matches all possible legal values;
                </ul>
        
        :param destination_location: The destination location of a schedule to set.  The
                destination location is of the volume form:
                &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        
        :param days_of_month: Minutes in the hour for which the schedule is set.
                The form is crontab-like, with possible values of:
                <ul>
                <li> -       := match nothing;
                <li> 1       := match day 1;
                <li> 1,3     := match day 1 and 3;
                <li> 2-5     := match day 2,3,4,5;
                <li> 1-30/7  := match day 1,8,15,22,29;
                <li> *       := matches all possible legal values;
                </ul>
        
        :param source_location: The source location of a schedule to set.  The source
                location is of the volume form: &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        
        :param minutes: Minutes in the hour for which the schedule is set.
                The form is crontab-like, with possible values of:
                <ul>
                <li> -       := match nothing;
                <li> 1       := match minute 1;
                <li> 1,3     := match minute 1 and 3;
                <li> 2-5     := match minute 2,3,4,5;
                <li> 1-12/3  := match minute 1,4,7,10;
                <li> 0-55/5  := match minute 0,5,10,15,20,25,30,35,40,45,50,55;
                <li> *       := matches all possible legal values;
                </ul>
        
        :param days_of_week: Days in the week for which the schedule is set.
                0 represents Sunday, and 6 represents Saturday.
                The form is crontab-like, with possible values of:
                <ul>
                <li> -       := match nothing;
                <li> 1       := match day 1 (Mon);
                <li> 1,3     := match day 1 and 3 (Mon and Wed);
                <li> 2-5     := match day 2,3,4,5 (Tue,Wed,Thu,Fri);
                <li> *       := matches all possible legal values;
                </ul>
        
        :param is_compressed: If true SnapMirror will compress/decompress the data that is
                transferred between the source and destination storage system.
                If false, transferred data will not be compressed. Upon initial
                configuration, default is false. On subsequent requests, the
                current configured setting is retained if not provided.
                This argument can only be used when a connection definition is
                used for the relationship entry. Using this argument without a
                connection definition will throw an error message.
        
        :param max_transfer_rate: Maximum transfer rate in kilobytes per second. If specified as 0,
                transfer happens as fast as the storage system can. If not
                specified, the previous value is retained. If nothing was
                mentioned previously, it is set to the default value.
        
        :param tcp_window_size: TCP window size in bytes. If specified as 0, size is set to
                an internally determined default value. If not specified, the
                previous value is retained.
        
        :param restart: restart mode when transfer is interrupted. Possible values are
                "always", "never" and "default". If  value is  set to "always",
                then  an interrupted transfer will always restart, if it has a
                restart check point and the conditions are the same as before
                the transfer was interrupted. If value  is set to "never", then
                an interrupted transfer will never restart, even if it has a
                restart checkpoint. If not specified, the previous value is
                retained. If nothing was mentioned previously, then it is set to
                default, where SnapMirror behaves like the "always" case, unless
                it has passed the next scheduled transfer time, in which case it
                will begin that scheduled transfer instead of restarting.
        
        :param connection_mode: This option specifies the mode to be used for establishing
                connection between source and destination. Possible values are
                "inet", "inet6" and "default". If this option is set to "inet6",
                connections between source and destination will be established
                using IPv6 addresses only. If there are no IPv6 addresses
                configured, then the connection will fail. If the option is set
                to "inet", connections between source and destination will be
                established using IPv4 addresses only. If there are no IPv4
                addresses configured, then the connection will fail.
                <p>
                If not specified, the previous value is retained. If nothing was
                mentioned previously, it is set as default, where connection will
                be tried using both "inet6" and "inet". "inet6" will have higher
                precedence than "inet". If connection request using "inet6" fails,
                SnapMirror will retry the connection using "inet".
                <p>
                This argument is not effective when an IP address is specified
                instead of source hostname. If the IP address format and
                connection mode do not match, the operation will fail with proper
                error message.
        """
        return self.request( "snapmirror-set-schedule", {
            'is_compressed': [ is_compressed, 'is-compressed', [ bool, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
            'hours': [ hours, 'hours', [ basestring, 'None' ], False ],
            'tcp_window_size': [ tcp_window_size, 'tcp-window-size', [ int, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'restart': [ restart, 'restart', [ basestring, 'None' ], False ],
            'connection_mode': [ connection_mode, 'connection-mode', [ basestring, 'None' ], False ],
            'days_of_month': [ days_of_month, 'days-of-month', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'minutes': [ minutes, 'minutes', [ basestring, 'None' ], False ],
            'days_of_week': [ days_of_week, 'days-of-week', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_update_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None, source_snapshot=None, max_transfer_rate=None):
        """
        The snapmirror-update-iter API updates the destination volumes of
        one or more SnapMirror relationships. This API is not supported
        on Infinite Volume constituents.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on or
                scheduled to be worked on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        
        :param source_snapshot: Source Snapshot
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth. The max-transfer-rate option does not affect
                load-sharing transfers and transfers for other relationships with
                Relationship Capability of Pre 8.2 confined to a single cluster.
        """
        return self.request( "snapmirror-update-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
            'source_snapshot': [ source_snapshot, 'source-snapshot', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorUpdateIterInfo, True ],
            'failure-list': [ SnapmirrorUpdateIterInfo, True ],
        } )
    
    def snapmirror_initialize_iter(self, query, max_failure_count=None, transfer_priority=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None, source_snapshot=None, max_transfer_rate=None):
        """
        The snapmirror-initialize-iter API initializes the destination
        volume of one or more SnapMirror relationships.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param transfer_priority: Transfer Priority
                Possible values:
                <ul>
                <li> "low"       ,
                <li> "normal"
                </ul>
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on or
                scheduled to be worked on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        
        :param source_snapshot: Source Snapshot
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth. The max-transfer-rate option does not affect
                load-sharing transfers and transfers for other relationships with
                Relationship Capability of Pre 8.2 confined to a single cluster.
        """
        return self.request( "snapmirror-initialize-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'transfer_priority': [ transfer_priority, 'transfer-priority', [ basestring, 'sm-transfer-priority-enum' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
            'source_snapshot': [ source_snapshot, 'source-snapshot', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorInitializeIterInfo, True ],
            'failure-list': [ SnapmirrorInitializeIterInfo, True ],
        } )
    
    def snapmirror_set_sync_schedule(self, visibility_frequency, destination_location, source_location, is_compressed=None, ops_throttle=None, sync_mode=None, tcp_window_size=None, connection_mode=None, is_data_motion_schedule=None):
        """
        Establishes a synchronous or semi-synchronous schedule.
        Currently, the schedules are in: /etc/snapmirror.conf.
        Semi-synchronous mode is determined by specifying
        semi-sync.
        
        :param visibility_frequency: Controls how often the source snapspot will be visible
                on the destination mirror. This input is used to control
                the value of visibility_interval in the snapmirror.conf file.
                The units are in seconds. A typical value to use for this
                input is 180.
        
        :param destination_location: The destination location of a schedule to set.  The
                destination location is of the volume form:
                &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        
        :param source_location: The source location of a schedule to set.  The source
                location is of the volume form: &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        
        :param is_compressed: If true SnapMirror will compress/decompress the data that is
                transferred between the source and destination storage system.
                If false, transferred data will not be compressed. Upon initial
                configuration, default is false. On subsequent requests, the
                current configured setting is retained if not provided.
                This argument can only be used when a connection definition is
                used for the relationship entry. Using this argument without a
                connection definition will throw an error message.
        
        :param ops_throttle: The number of outstanding operations allowed before
                blocking on the source.  The format is a number
                followed by the one of the following
                units: "ops", "s", or "ms".
                If the specified value is less than 10s, the mirror
                is configured to run in a fully synchronous mode.
                If the specified value is greater than or equal to
                10s, the mirror is configured to run in semi-synchronous
                mode. If not specified, the previous value is retained.
                This is a deprecated parameter. Use the sync-mode
                parameter instead to specify the sync mode.
        
        :param sync_mode: This specifies whether the mirror should be configured
                in sync or in semi-sync mode. Possible values are:
                "full_sync" and "semi_sync".
                If the user wants to configure the mirror to run in fully
                synchronous mode, the user must specify "full_sync" as the
                value for this parameter. If the user wants to configure the
                mirror to run in semi-synchronous mode, the user must specify
                "semi_sync" as the value of this parameter. If not specified,
                the mirror will be configured to run in full synchronous mode.
                This parameter overrides the deprecated ops-throttle
                parameter.
        
        :param tcp_window_size: TCP window size in bytes. If specified as 0, size is set to an
                internally determined default value. If not specified, the previous
                value is retained.
        
        :param connection_mode: This option specifies the mode to be used for establishing
                connection between source and destination. If this option is
                set to "inet6", connections between source and destination will
                be established using IPv6 addresses only. If there are no IPv6
                addresses configured, then the connection will fail. If the
                option is set to "inet", connections between source and
                destination will be established using IPv4 addresses only. If
                there are no IPv4 addresses configured, then the connection
                will fail.
                <p>
                If not specified, the previous value is retained. If nothing was
                mentioned previously, it is set as default, where connection will
                be tried using both "inet6" and "inet". "inet6" will have higher
                precedence than "inet". If connection request using "inet6" fails,
                SnapMirror will retry the connection using "inet".
                <p>
                This argument is not effective when an IP address is specified
                instead of source hostname. If the IP address format and
                connection-mode do not match, the operation will fail with proper
                error message.
        
        :param is_data_motion_schedule: If true, indicates the schedule entry is part of a vfiler
                migration (Data Motion). Upon initial configuration, default
                value is false. On subsequent requests, the current configured
                setting is retained if not provided.
                <p>
                Semi-sync SnapMirror uses this input to provide Data Motion
                specific behavior.
        """
        return self.request( "snapmirror-set-sync-schedule", {
            'is_compressed': [ is_compressed, 'is-compressed', [ bool, 'None' ], False ],
            'ops_throttle': [ ops_throttle, 'ops-throttle', [ basestring, 'None' ], False ],
            'sync_mode': [ sync_mode, 'sync-mode', [ basestring, 'None' ], False ],
            'visibility_frequency': [ visibility_frequency, 'visibility-frequency', [ int, 'None' ], False ],
            'tcp_window_size': [ tcp_window_size, 'tcp-window-size', [ int, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'connection_mode': [ connection_mode, 'connection-mode', [ basestring, 'None' ], False ],
            'is_data_motion_schedule': [ is_data_motion_schedule, 'is-data-motion-schedule', [ bool, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_resume_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Enables future transfers for one or more SnapMirror
        relationships.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "snapmirror-resume-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorResumeIterInfo, True ],
            'failure-list': [ SnapmirrorResumeIterInfo, True ],
        } )
    
    def snapmirror_delete_sync_schedule(self, destination_location):
        """
        Delete a synchronous  schedule for a given destination.
        This API must be executed on the destination filer.
        
        :param destination_location: The destination location of a schedule to delete.  The
                destination location is of the volume form:
                &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        """
        return self.request( "snapmirror-delete-sync-schedule", {
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_break_async(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        The snapmirror-break-async API breaks an Infinite Volume
        SnapMirror relationship between a source and destination volume
        of a data protection mirror. When Data ONTAP breaks the
        relationship, the destination volume is made a read-write volume
        and can diverge from the source volume, client redirection is
        turned off on the destination volume, the restart checkpoint is
        cleared, and the clients can see the latest Snapshot copy.
        You must specify the destination endpoint when using
        snapmirror-break-async.
        Subsequent manual or scheduled SnapMirror updates to the broken
        relationship will fail until the SnapMirror relationship is
        reestablished using the snapmirror-resync API.
        This API applies only to data protection mirrors for Infinite
        Volume.
        You must use the snapmirror-break-async API from the destination
        cluster. This API is not supported on Infinite Volume
        constituents.
        This API is not supported if the destination end point is a
        flexible volume.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-break-async", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_list_schedule(self, destination_location=None):
        """
        Returns the schedule for a given destination or all
        destinations.  The API must be executed on the destination
        filer.  Currently, the schedules is in /etc/snapmirror.conf.
        
        :param destination_location: The destination location of a schedule to obtain.  The
                destination location is of the volume form:
                &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
                The &lt;filer&gt; must match the destination filer.  If
                the destination-location is not specified, then all the
                destination schedules are returned.
        """
        return self.request( "snapmirror-list-schedule", {
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
        }, {
            'snapmirror-schedules': [ SnapmirrorScheduleInfo, True ],
        } )
    
    def snapmirror_snapshot_owner_get(self, vserver, volume, snapshot):
        """
        List all owners used to preserve a Snapshot copy for a SnapMirror
        mirror-to-vault cascade configuration.
        
        :param vserver: Vserver Name
        
        :param volume: Volume Name
        
        :param snapshot: Snapshot Copy Name
        """
        return self.request( "snapmirror-snapshot-owner-get", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'snapshot-id' ], False ],
        }, {
            'snapshot-owner-names': [ basestring, True ],
        } )
    
    def snapmirror_check(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, target_snapshot=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        The snapmirror-check API starts an operation to compare the
        contents of a snapshot between the source volume and destination
        volume.
        You must specify the destination endpoint when using
        snapmirror-check.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param target_snapshot: Specifies the Snapshot copy on the destination endpoint to
                check.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-check", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'target_snapshot': [ target_snapshot, 'target-snapshot', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_set_connection(self, connection, address_pair1, address_pair2=None, mode=None):
        """
        Sets up a connection.  snapmirror-set-connection will
        add a new connection or modify an existing one.
        This API must be executed on the destination filer.
        Currently, the connections are in: /etc/snapmirror.conf.
        
        :param connection: Name of the connection to add or modify.  The name is
                in ASCII and must begin with an alpha character.
        
        :param address_pair1: The connection's first source and destination
                address pair.  In multi mode, the first address
                pair provides a connection path; while in
                failover mode, the first address pair provides
                the prefer connection path.
        
        :param address_pair2: The connection's second source and destination
                address pair.  In multi mode the second address
                pair provides another connection path, while in
                failover mode, the second address pair provides
                a connection path in case the first path fails.
        
        :param mode: Possible mode values are "multi" or "failover".
                If not specified, the default is "multi".
        """
        return self.request( "snapmirror-set-connection", {
            'address_pair2': [ address_pair2, 'address-pair2', [ AddressPair, 'None' ], False ],
            'connection': [ connection, 'connection', [ basestring, 'None' ], False ],
            'address_pair1': [ address_pair1, 'address-pair1', [ AddressPair, 'None' ], False ],
            'mode': [ mode, 'mode', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_abort(self, source_vserver=None, source_volume=None, check_only=None, clear_checkpoint=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        The snapmirror-abort API stops ongoing transfers for a
        SnapMirror relationship. The relationship is identified by its
        destination endpoint.
        You must specify the destination endpoint when using
        snapmirror-abort.
        On Data ONTAP operating in Cluster-Mode, the snapmirror-abort
        API stops all of the active transfers to each associated volume
        on the  receiving side in a set of load-sharing mirrors.
        Load-sharing mirrors are either up to date and serving data to
        clients, or they are lagging and not serving data to clients. If
        the snapmirror-abort API identifies an up-to-date load-sharing
        mirror, then SnapMirror transfers to associated up-to-date
        load-sharing mirrors in the set of load-sharing mirrors are also
        aborted. If the snapmirror-abort API identifies a lagging
        load-sharing mirror, then only the SnapMirror transfer associated
        with the lagging load-sharing mirror is aborted.
        After the snapmirror-abort API successfully completes its
        operation, the volume on the receiving side of the transfer might
        contain a restart checkpoint. The restart checkpoint can be used
        by a subsequent transfer to restart and continue the aborted
        SnapMirror transfer.
        Snapmirror-abort API must be used from the destination storage
        system on Data ONTAP operating in 7-Mode, from the destination
        cluster on Data ONTAP 8.1 operating in Cluster-Mode, from the
        destination Vserver or cluster on Data ONTAP 8.2 or later
        operating in Cluster-Mode.
        <p>
        This API is not supported if the destination end point is
        an Infinite Volume.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source volume.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param check_only: If this option is specified true, only snapmirror-check
                operations active on the relationship will be aborted.
        
        :param clear_checkpoint: If true, the restart checkpoint is cleared.  The default is
                false, not cleared.
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter.
        
        :param destination_vserver: Specifies the destination Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, when specifying a
                destination endpoint, you must use either the destination
                location, or the destination cluster, destination Vserver,
                and destination volume.
                This parameter is mandatory on Data ONTAP operating in 7-mode.
        
        :param destination_volume: Specifies the destination volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, When specifying a
                source endpoint, you must use either the source location, or the
                source cluster, source Vserver, and source volume.
        
        :param destination_cluster: Specifies the destination cluster of the SnapMirror relationship.
                The destination Vserver and destination volume must also be
                specified if using this parameter.
        """
        return self.request( "snapmirror-abort", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'check_only': [ check_only, 'check-only', [ bool, 'None' ], False ],
            'clear_checkpoint': [ clear_checkpoint, 'clear-checkpoint', [ bool, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_get_volume_status(self, volume):
        """
        Returns SnapMirror status values for a given volume. Including
        whether: the volume is a source of a SnapMirror relationship;
        the volume is a destination of a SnapMirror relationship;
        a transfer is in progress; the relationship is broken off.
        On Data ONTAP 8.1 operating in Cluster-Mode, this API is
        provided for backward compatibility only. It will fail if
        the volume is the source or destination of a load-sharing
        SnapMirror relationship. It is recommended to use the
        snapmirror-get-iter API to get the same information.
        On Data ONTAP 8.1 operating in Cluster-Mode, this API must be
        issued on the cluster the volume belongs to.
        This API is not supported On Data ONTAP 8.2 or later operating
        in Cluster-Mode. You must use the snapmirror-get-iter and
        snapmirror-get-destination-iter APIs. If issued on Data ONTAP
        8.2 or later operating in Cluster-Mode, this API will return
        EOPNOTSUPPORTED error.
        
        :param volume: Name of the volume to be queried.
                On Data ONTAP operating in Cluster-Mode, specifies the location
                of the volume the  following formats:
                [&lt;cluster&gt;:][//&lt;vserver&gt;/]&lt;volume&gt;
        """
        return self.request( "snapmirror-get-volume-status", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'is-destination': [ bool, False ],
            'is-transfer-in-progress': [ bool, False ],
            'is-transfer-broken': [ bool, False ],
            'is-source': [ bool, False ],
        } )
    
    def snapmirror_off(self):
        """
        Disables SnapMirror data transfers and turns off the
        SnapMirror scheduler.  Check the SnapMirror status
        with the snapmirror-get-status API for results.
        """
        return self.request( "snapmirror-off", {
        }, {
        } )
    
    def snapmirror_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        The snapmirror-get-iter API returns information for one or
        several SnapMirror relationships.
        <p>
        On Data ONTAP 8.1 operating in Cluster-Mode, this API can be
        issued on a cluster. It returns all SnapMirror relationships that
        have a source or destination endpoint in that cluster, and that
        match the parameters specified.
        On Data ONTAP 8.2 operating in Cluster-Mode, this API can be
        issued on a Vserver or a cluster. It returns all the SnapMirror
        relationships, which have a destination endpoint in that Vserver
        or cluster, and that match the parameters specified.
        <p>
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                snapmirror object.
                All snapmirror objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "snapmirror-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapmirrorInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SnapmirrorInfo, True ],
        } )
    
    def snapmirror_release(self, source_vserver=None, source_volume=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, relationship_id=None, relationship_info_only=None):
        """
        The snapmirror-release API removes a SnapMirror relationship
        on the source endpoint. It unlocks and cleanups the snapshots
        pertaining to the relationship. It does not destroy any volume.
        You must specify the destination endpoint when using
        snapmirror-release.
        Unless relationship-info-only is specified, this operation
        will fail if it is unable to reach the source volume and
        clean up snapshots.
        On Data ONTAP 8.2 or later operating in Cluster-Mode,
        this API must be executed on the source Vserver or source
        cluster following the deletion of the relationship on the
        destination Vserver or destination cluster.
        It is possible to issue snapmirror-release on the source
        Vserver without deleting the relationship on the destination
        Vserver. However, the relationship will continue to exist
        because the destination is the authority. The relationship will
        reappear on the source on the next transfer.
        On Data ONTAP operating in 7-Mode, this API must be issued on
        the source storage system. On Data ONTAP 8.2 or later operating
        in Cluster-Mode, this API must be issued on  the source Vserver
        if operating in Vserver context and on the source cluster if
        operating in a cluster context.
        This API is not supported on Data ONTAP 8.1 operating in
        Cluster-Mode, or Data ONTAP 8.2 or later operating in
        Cluster-Mode if the relationship control plane is 'v1'.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship.
                If using this parameter, the source volume must also be
                specified.
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship.
                If using this parameter, the source Vserver must also be
                specified:
        
        :param destination_vserver: Specifies the destination Vserver of the SnapMirror relationship.
                If using this parameter, the destination volume must also be
                specified.
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, when specifying a
                destination endpoint, you must use either the destination
                location, or destination Vserver and destination volume.
                This parameter is mandatory on Data ONTAP operating in 7-mode
        
        :param destination_volume: Specifies the destination volume of the SnapMirror relationship.
                If using this parameter, the destination Vserver must also be
                specified.
        
        :param source_location: Specifies the source endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, When specifying a
                source endpoint, you must use either the source location, or the
                source Vserver, and source volume.
        
        :param relationship_id: Specifies the relationship unique identifier of the
                SnapMirror relationship.
        
        :param relationship_info_only: If relationship-info-only is set to true then only
                relationship information is removed. By default it is false.
        """
        return self.request( "snapmirror-release", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'relationship_id': [ relationship_id, 'relationship-id', [ basestring, 'None' ], False ],
            'relationship_info_only': [ relationship_info_only, 'relationship-info-only', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_list_connections(self, connection=None):
        """
        Returns connection information for a given connection or
        all connections.  The API must be executed on the
        destination filer.  Currently, the connections are in:
        /etc/snapmirror.conf.
        
        :param connection: Connection name of the connection information to obtain.
                If the connections is not specified, then the
                connection information for all the connections is returned.
        """
        return self.request( "snapmirror-list-connections", {
            'connection': [ connection, 'connection', [ basestring, 'None' ], False ],
        }, {
            'snapmirror-connections': [ SnapmirrorConnectionInfo, True ],
        } )
    
    def snapmirror_resync(self, preserve=None, source_vserver=None, source_volume=None, destination_snapshot=None, transfer_priority=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, source_snapshot=None, max_transfer_rate=None, destination_cluster=None):
        """
        Re-establishes a mirroring relationship between a source volume
        and a destination volume, typically in the following cases:
        <ul>
        <li> The destination mirror is broken (that is, the destination
        volume is a read-write volume and no longer a data protection
        mirror). After the snapmirror-resync API completes, the
        destination volume is made a data protection mirror and the
        mirror can be manually updated or scheduled for updates.
        <li> A snapmirror-update API failed because the required common
        Snapshot copy was deleted on the source volume.
        </ul>
        After the operation  completes, the destination volume is made a
        data protection mirror and the mirror can be manually updated
        or scheduled for updates.
        <b>Attention:</b> The snapmirror-resync API can cause data loss
        on the destination volume because the API can remove the exported
        Snapshot copy on the destination volume.
        <p>
        The default behavior of the snapmirror-resync API is defined as follows:
        <ul>
        <li> Finds the most recent common Snapshot copy between the source and
        destination volumes, removes Snapshot copies on the destination volume
        that are newer than the common Snapshot copy and mounts the destination
        volume as a DP volume with the common Snapshot copy as the exported
        Snapshot copy.
        <li> For data protection relationships, takes a Snapshot copy of the
        source volume to capture the current image and transfers Snapshot copies
        that are newer than the common Snapshot copy from the source volume to
        the destination volume. For vault relationships, transfers Snapshot copies
        newer than the common Snapshot copy according to the relationship policy,
        i.e., Snapshot copies will match rules associated with the policy as
        defined by the snapmirror-policy API.
        </ul>
        On Data ONTAP 8.2 or later operating in Cluster-Mode, the snapmirror-resync
        API supports an optional parameter 'preserve'.
        The parameter 'preserve' is only supported for vault relationships.
        When used, the parameter 'preserve' changes the behavior of the
        snapmirror-resync API. The changed behavior can be described as follows:
        <ul>
        <li> Finds the most recent common Snapshot copy between the source
        and destination volumes, preserves all Snapshot copies on the destination
        volume that are newer than the common Snapshot copy, and mounts the
        destination volume as a DP volume with the common Snapshot copy as the
        exported Snapshot copy.
        <li> Performs a local rollback transfer to make a copy of the common
        Snapshot copy on the destination volume and establish it as the latest
        Snapshot copy on the destination volume. The command then transfers all
        Snapshot copies that are newer than the common Snapshot copy, from the
        source volume to the destination volume. The command only transfers
        Snapshot copies that match the vault relationship's policy, i.e.,
        Snapshot copies will match rules associated with the policy as defined
        by the snapmirror-policy APIs.
        </ul>
        The snapmirror-resync API fails if the destination volume does
        not have a Snapshot copy in common with the source volume.
        <p>
        On Data ONTAP 8.1 operating in Cluster-Mode, or on Data ONTAP
        8.2 operating in Cluster-Mode for relationships using a control
        plane compatible with Data ONTAP 8.1 operating in Cluster-Mode,
        a job is spawned to operate for the SnapMirror relationship and
        the job id is returned. The progress of the operation can be
        tracked using the job APIs.
        <p>
        On Data ONTAP 8.2 or later operating in Cluster-Mode, you can
        track the progress of the operation using the snapmirror-get
        API except for  relationships using a control plane compatible
        with Data ONTAP 8.1 operating in Cluster-Mode.
        <p>
        On Data ONTAP operating in 7-Mode, the update is asynchronously
        handled, and there is no guarantee that it succeeds.
        This requires that a schedule in /etc/snapmirror.conf is set
        for the destination.
        <p>
        The API must be issued on the destination storage system  on
        Data ONTAP operating in 7-Mode, on the destination cluster
        on Data ONTAP 8.1 operating in Cluster-Mode, and on the
        destination Vserver on Data ONTAP 8.2 or later operating in
        Cluster-Mode.
        
        :param preserve: This parameter is only available for Vault relationships.
                The default value is false which means all snapshots on the
                destination that are newer than the latest common snapshot
                will be deleted. If preserve is specified, newer snapshots
                are retained.  If preserve is specified for a non-Vault
                relationship the API will fail.
                <p>This parameter only applies on Data ONTAP 8.2 or later
                operating in Cluster-Mode and for vault relationships.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source volume.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_snapshot: Creates the specified snapshot (in addition to the regular
                SnapMirror snapshot) on the destination after the qtree
                SnapMirror transfer is over.
        
        :param transfer_priority: Specifies the priority at which the transfer runs.
                Possible values are: "normal", and "low".  The default
                value is the value specified in the snapmirror policy which
                is associated with the relationship.
                <p>This parameter only applies on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane
                is 'v2'.
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter.
        
        :param destination_vserver: Specifies the destination Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, when specifying a
                destination endpoint, you must use either the destination
                location, or the destination cluster, destination Vserver,
                and destination volume.
                This parameter is mandatory on Data ONTAP operating in 7-mode
        
        :param destination_volume: Specifies the destination volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP Cluster-Mode when specifying a source endpoint,
                you must use either the source location, or the source
                cluster, source Vserver, and source volume.
                On Data ONTAP operating in 7-Mode, If the source-location is
                not specified, then the source in /etc/snapmirror.conf for
                the destination path is used.
        
        :param source_snapshot: Designates the source snapshot to use for a qtree update
                on Data ONTAP operating in 7-Mode, and the snapshot on the
                source volume to use for the transfer on Data ONTAP 8.2 or
                later operating in Cluster-Mode.
                <p>For data protection mirror relationships, Data ONTAP
                Cluster-Mode does not create a new Snapshot copy. It will
                use the specified Snapshot copy as if it were the most recent
                one; that is, all copies between the most recent common one and
                the specified one are transferred, but no copies newer than the
                specified one are transferred.
                <p>For vault relationships, Data ONTAP Cluster-Mode transfers the
                specified Snapshot copy instead of the ones that match its policy's rules.
                <p>This parameter only applies on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane
                is 'v2'.
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth.
                On Data ONTAP operating in Cluster-Mode, the max-transfer-rate
                option does not affect load-sharing transfers and transfers for
                other relationships with Relationship Capability of Pre 8.2
                confined to a single cluster.
        
        :param destination_cluster: Specifies the destination cluster of the SnapMirror relationship.
                The destination Vserver and destination volume must also be
                specified if using this parameter.
        """
        return self.request( "snapmirror-resync", {
            'preserve': [ preserve, 'preserve', [ bool, 'None' ], False ],
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'destination_snapshot': [ destination_snapshot, 'destination-snapshot', [ basestring, 'None' ], False ],
            'transfer_priority': [ transfer_priority, 'transfer-priority', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'source_snapshot': [ source_snapshot, 'source-snapshot', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_on(self):
        """
        Enables SnapMirror data transfers and turns on the
        SnapMirror scheduler.  Check the SnapMirror status
        with the snapmirror-get-status API for results.
        """
        return self.request( "snapmirror-on", {
        }, {
        } )
    
    def snapmirror_get_destination_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        The snapmirror-get-destination-iter API returns information
        about, one or more SnapMirror relationships whose source
        endpoints are in the  Vserver or the cluster the API is issued
        on.
        <p>
        The information returned can be stale. Stale information
        corresponds to a SnapMirror relationship that has been deleted on
        its destination cluster or Vserver. Stale information may result
        to several entries being returned with the same source and
        destination endpoints, but with different relationship IDs.
        <p>
        Note that the information for a SnapMirror relationship will not
        be available on its source Vserver or source cluster until at
        least one transfer is initiated.
        <p>
        This API is only supported on Data ONTAP 8.2 and above operating
        in Cluster-Mode.  It can be issued on a Vserver or a Cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                snapmirror object.
                All snapmirror objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "snapmirror-get-destination-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SnapmirrorDestinationInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapmirrorDestinationInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SnapmirrorDestinationInfo, True ],
        } )
    
    def snapmirror_list_sync_schedule(self, destination_location=None):
        """
        Returns a synchronous schedule for a given destination or
        all destinations.  The API must be executed on the
        destination filer.
        Currently, the schedules is in /etc/snapmirror.conf.
        
        :param destination_location: The destination location of a schedule to obtain.  The
                destination location is of the volume form:
                &lt;filer&gt;:&lt;volume&gt;
                or the qtree form:
                &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
                The &lt;filer&gt; must match the destination filer.  If
                the destination-location is not specified, then all the
                destination schedules are returned.
        """
        return self.request( "snapmirror-list-sync-schedule", {
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
        }, {
            'snapmirror-sync-schedules': [ SnapmirrorSyncScheduleInfo, True ],
        } )
    
    def snapmirror_cache_rebuild_relationship(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        auto generated : Rebuild the cache for a SnapMirror
        relationship.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-cache-rebuild-relationship", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_quiesce(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        Disables future transfers to a SnapMirror destination.
        If there is no transfer in progress, the SnapMirror
        relationship becomes 'Quiesced'. If there is a transfer in
        progress, the SnapMirror relationship becomes 'Quiescing' until
        the transfer completes. If the current transfer aborts, it will
        be treated like a future transfer and will not restart.
        When a SnapMirror relationship is quiesced, it remains in that
        state across reboots and fail-overs.
        The relationship must exist on the destination and you must
        specify the destination endpoint when using snapmirror-quiesce.
        On Data ONTAP 8.1 operating in Cluster-Mode, if applied
        to a load-sharing (LS) SnapMirror relationship, all the
        relationships in the set will be quiesced.
        This API must be issued from the destination storage system on
        Data ONTAP operating in 7-Mode, on the destination cluster on
        Data ONTAP 8.1 operating in Cluster-Mode, and the destination
        Vserver on Data ONTAP 8.2 or later operating in Cluster-Mode.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source volume.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter.
        
        :param destination_vserver: Specifies the destination Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, when specifying a
                destination endpoint, you must use either the destination
                location, or the destination cluster, destination Vserver,
                and destination volume.
                This parameter is mandatory on Data ONTAP 7-mode
        
        :param destination_volume: Specifies the destination volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, When specifying a
                source endpoint, you must use either the source location, or the
                source cluster, source Vserver, and source volume.
        
        :param destination_cluster: Specifies the destination cluster of the SnapMirror relationship.
                The destination Vserver and destination volume must also be
                specified if using this parameter.
        """
        return self.request( "snapmirror-quiesce", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_destroy_async(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        The snapmirror-destroy-async API removes only the SnapMirror
        relationship of a source and a destination Infinite Volume, the
        volumes are not destroyed and Snapshot copies on the volumes are
        not removed.
        You must specify the destination endpoint when using
        snapmirror-destroy-async.
        The snapmirror-destroy-async API fails if a SnapMirror transfer
        for the SnapMirror relationship is in progress.
        The snapmirror-destroy-async API preserves the read-write or
        read-only attributes of the volumes of a SnapMirror relationship
        after the relationship is deleted. Therefore, a read-write volume
        that was the source of a SnapMirror relationship retains its
        read-write attributes, and a data protection volume that was a
        destination of a SnapMirror relationship retains its read-only
        attributes.
        The snapmirror-destroy-async API should be used from the
        destination cluster. When used in this fashion, the
        destination-side information will be cleaned up. The destination
        will also attempt to cleanup source-side information. If the
        source cluster is not available, the destination-side information
        will still be cleaned up.
        This API is not supported if the destination end point is a
        flexible volume or an Infinite Volume constituent.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-destroy-async", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_update(self, source_vserver=None, source_volume=None, destination_snapshot=None, transfer_priority=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, source_snapshot=None, max_transfer_rate=None, destination_cluster=None):
        """
        Updates the destination endpoint of the SnapMirror relationship.
        The update is asynchronously handled, and there is no
        guarantee that it will succeed.
        <p>
        On Data ONTAP operating in 7-Mode the snapmirror-get-status API
        can be used to check the status of the update.  The API must
        be issued on the destination storage system.
        <p>
        On Data ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP
        8.2 operating in Cluster-Mode and for relationships using
        a control plane compatible with Data 8.1 operating Cluster-Mode
        (relationship-control-plane set 'v1'), a job will be spawned to
        operate on the SnapMirror relationship, and the job id will be
        returned. The progress of the job can be tracked using the job
        APIs.
        <p>
        On Data ONTAP 8.2 or later operating in Cluster-Mode, you
        can track the progress of the operation using the
        snapmirror-get API, except for relationships using a control
        plane compatible with  Data ONTAP 8.1 operating Cluster-Mode.
        <p>
        You must specify the destination endpoint when using
        snapmirror-update.
        <p>
        The API makes the destination volume an up-to-date mirror of the
        source volume.
        <p>
        This API must be used from the destination storage system on
        Data ONTAP 7-Mode, or from the destination cluster on Data
        ONTAP 8.1 operating in Cluster-Mode, and from the destination
        Vserver on Data ONTAP 8.2 or later operating in Cluster-Mode.
        <p>
        On Data ONTAP operating in 7-Mode, if the destination endpoint
        is a volume, the volume must be in the restricted state. If the
        destination endpoint is a qtree, the qtree must not already
        exist.
        <p>
        On Data ONTAP Cluster-Mode if the destination volume is empty,
        the snapmirror-update API will fail. The snapmirror-initialize
        API must be called to perform the baseline transfer before the
        the snapmirror-update can be called.
        <p>
        For data protection relationships, the snapmirror-update API
        makes the destination volume an up-to-date mirror of the source
        volume with the following steps:</p>
        <ul>
        <li>If the source volume is read-write, takes a Snapshot copy on
        the source volume to capture the current image of the source volume.
        <li>Finds the most recent Snapshot copy on the destination volume
        and validates that the corresponding Snapshot copy is on the source.
        <li>Incrementally transfers Snapshot copies that are newer than
        the corresponding Snapshot copy to the destination volume.
        </ul>
        <p>
        For vault relationships, the snapmirror-update API does not take
        a Snapshot copy on the source volume but transfers only selected
        Snapshot copies that are newer than the common Snapshot copy to
        the destination volume. Snapshot copies are selected by matching
        their 'snapmirror-label' with the 'snapmirror-label' of one of
        the rules from the corresponding SnapMirror policy associated
        to the SnapMirror relationship.
        All matching Snapshot copies are incrementally transferred to the
        destination volume.
        <p>
        For vault relationships, the snapmirror-update API also manages
        expiration of Snapshot copies on the destination volume. It does
        so by deleting Snapshot copies that have exceeded the value of
        'keep' for the matching rule from the corresponding SnapMirror
        policy associated with the SnapMirror relationship. Snapshot copies
        that match the same 'snapmirror-label' will be deleted in
        oldest-first order.
        <p>
        For data protection relationships, the parameter 'source-snapshot'
        is optional and allows for the transfer of Snapshot copies newer than
        the common Snapshot copy up to the specified 'source-snapshot'.
        <p>
        For vault relationships, the parameter 'source-snapshot' is optional
        and allows transfer of a Snapshot copy that is older than the common
        Snapshot copy and/or may not be selected for transfer based on
        policy-based selection of a scheduled update transfer.
        <p>
        After the snapmirror-update API successfully completes, the last
        Snapshot copy transferred is made the new exported Snapshot copy
        on the destination volume. If an update to a vault relationship
        specifies a Snapshot copy using the 'source-snapshot' parameter
        that is older than the common snapshot, after the snapmirror-update
        API successfully completes, the exported Snapshot copy on the
        destination volume will remain unchanged.
        <p>
        If the snapmirror-update does not finish successfully, due to a
        network failure or because a snapmirror-abort API was issued for
        example, a restart checkpoint might be recorded on the
        destination volume. If a restart checkpoint is recorded, the
        next update restarts and continues the transfer from the restart
        checkpoint. For vault relationships, the next update will restart
        and continue the old transfer regardless of whether it is a
        matching Snapshot copy or not.
        <p>
        On Data ONTAP 8.1 operating in Cluster-Mode, you can
        use the snapmirror-update API to update a specific load-sharing
        mirror that lags behind up-to-date destination  volumes in the
        set of load-sharing mirrors. An update to the lagging
        load-sharing mirror should bring it up to date with the other
        up-to-date destination volumes in the set of load-sharing
        mirrors.
        Note: You might have to run the snapmirror-update API more than
        once if the command does not finish before the next scheduled
        update of the set of load-sharing mirrors.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source volume.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_snapshot: Creates the specified snapshot (in addition to the regular
                SnapMirror snapshot) on the destination after the qtree
                SnapMirror transfer is over.
        
        :param transfer_priority: Specifies the priority at which the transfer runs.
                Possible values are: "normal", and "low".  The default
                value is the value specified in the snapmirror policy which is
                associated with the relationship.
                <p>This parameter only applies on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane
                is 'v2'.
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter.
        
        :param destination_vserver: Specifies the destination Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP Cluster-Mode, when specifying a destination
                endpoint, you must use either the destination location, or
                the destination cluster, destination Vserver, and destination
                volume.
                On Data ONTAP 7-Mode, if the destination endpoint is a volume,
                the volume must be in the restricted state.  If the destination
                endpoint is a qtree, the qtree must not already exist.
                This parameter is mandatory on Data ONTAP 7-mode
        
        :param destination_volume: Specifies the destination volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP Cluster-Mode when specifying a source endpoint,
                you must use either the source location, or the source
                cluster, source Vserver, and source volume.
                On Data ONTAP 7-Mode, If the source-location is not specified,
                then the source in /etc/snapmirror.conf for the destination
                path is used.
        
        :param source_snapshot: Specifies the Snapshot copy on the source to use as the basis
                for the update. It is used for updates to Data ONTAP 7-mode
                qtree relationships and Data ONTAP Cluster-Mode relationships.
                <p>For a qtree relationship, Data ONTAP 7-mode does not create a
                new Snapshot copy and transfers the specified Snapshot copy
                instead.
                <p>For data protection mirror relationships, Data ONTAP
                Cluster-Mode does not create a new Snapshot copy. It will use
                the specified Snapshot copy as if it were the most recent one;
                that is, all copies between the most recent common one and the
                specified one are transferred, but no copies newer than the
                specified one are transferred.
                <p>For vault relationships, Data ONTAP Cluster-Mode transfers
                the specified Snapshot copy instead of the ones that match its
                policy's rules.
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth.
                On Data ONTAP operating in Cluster-Mode, the max-transfer-rate
                option does not affect load-sharing transfers and transfers for
                other relationships with Relationship Capability of Pre 8.2
                confined to a single cluster.
        
        :param destination_cluster: Specifies the destination cluster of the SnapMirror relationship.
                The destination Vserver and destination volume must also be
                specified if using this parameter.
        """
        return self.request( "snapmirror-update", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'destination_snapshot': [ destination_snapshot, 'destination-snapshot', [ basestring, 'None' ], False ],
            'transfer_priority': [ transfer_priority, 'transfer-priority', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'source_snapshot': [ source_snapshot, 'source-snapshot', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_abort_async(self, source_vserver=None, source_volume=None, check_only=None, clear_checkpoint=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        The snapmirror-abort-async API stops ongoing transfer for a
        SnapMirror relationship on Infinite Volume. The relationship is
        identified by its destination endpoint.
        You must specify the destination endpoint when using the
        snapmirror-abort-async API.
        After the snapmirror-abort-async API successfully aborted the
        transfer, the volume on the receiving side of the transfer might
        contain a restart checkpoint. The restart checkpoint can be used
        by a subsequent transfer to restart and continue the aborted
        SnapMirror transfer.
        Snapmirror-abort-async API must be used from the destination
        cluster on Data ONTAP Cluster-Mode.
        This API is not supported if the destination end point is a
        flexible volume or an Infinite Volume constituent.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param check_only: If this option is specified true, only snapmirror-check
                operations active on the relationship will be aborted.
        
        :param clear_checkpoint: If this option is specified true, the restart checkpoint is
                discarded and the destination volume is restored to the last
                Snapshot copy that was successfully transferred. You can use the
                clear-checkpoint option to discard the restart checkpoint of a
                previous transfer attempt which forces the subsequent transfer to
                start with a fresh Snapshot copy on the destination volume.
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-abort-async", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'check_only': [ check_only, 'check-only', [ bool, 'None' ], False ],
            'clear_checkpoint': [ clear_checkpoint, 'clear-checkpoint', [ bool, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_release_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        releases one or a group of SnapMirror relationships.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "snapmirror-release-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorDestinationInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorReleaseIterInfo, True ],
            'failure-list': [ SnapmirrorReleaseIterInfo, True ],
        } )
    
    def snapmirror_update_ls_set(self, source_cluster=None, source_vserver=None, source_location=None, source_volume=None):
        """
        The snapmirror-update-ls-set API updates destination volumes of
        the set of load-sharing mirrors. The API makes destination
        volumes, in the group of load-sharing mirrors, up-to-date mirrors
        of the source volume.
        You must specify the source endpoint when using
        snapmirror-update-ls-set.
        Separate SnapMirror transfers are performed from the source
        volume to each of the up-to-date destination volumes in the set
        of load-sharing mirrors.
        Load-sharing mirrors that lag behind the up-to-date destination
        volumes might not be updated by the snapmirror-update-ls-set API.
        Use the snapmirror-update API to update a lagging load-sharing
        mirror.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter. This parameter is supported only in cluster
                context.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship. The
                source cluster and source volume must also be specified if using
                this parameter.
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship.
                When specifying a source endpoint, you must use either the source
                location, or the source cluster, source Vserver, and source
                volume.
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship. The
                source cluster and source Vserver must also be specified if using
                this parameter.
        """
        return self.request( "snapmirror-update-ls-set", {
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapmirror_resync_iter(self, query, preserve=None, max_failure_count=None, transfer_priority=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None, source_snapshot=None, max_transfer_rate=None):
        """
        The snapmirror-resync-iter API reestablishes one or more
        previously broken SnapMirror relationships. This API is not
        supported on Infinite Volume constituents.
        A job will be spawned to operate on the snapmirror and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param preserve: Preserve
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param transfer_priority: Transfer Priority
                Possible values:
                <ul>
                <li> "low"       ,
                <li> "normal"
                </ul>
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on or
                scheduled to be worked on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        
        :param source_snapshot: Source Snapshot
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred between clusters. The default is unlimited (0)
                which permits the SnapMirror relationship to fully utilize the
                available network bandwidth. The max-transfer-rate option does
                not affect load-sharing transfers and transfers for other
                relationships with Relationship Capability of Pre 8.2 confined to
                a single cluster.
        """
        return self.request( "snapmirror-resync-iter", {
            'preserve': [ preserve, 'preserve', [ bool, 'None' ], False ],
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'transfer_priority': [ transfer_priority, 'transfer-priority', [ basestring, 'sm-transfer-priority-enum' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
            'source_snapshot': [ source_snapshot, 'source-snapshot', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorResyncIterInfo, True ],
            'failure-list': [ SnapmirrorResyncIterInfo, True ],
        } )
    
    def snapmirror_modify_iter(self, query, max_records=None, max_failure_count=None, schedule=None, return_success_list=None, vserver=None, tries=None, tag=None, continue_on_failure=None, return_failure_list=None, policy=None, max_transfer_rate=None):
        """
        The snapmirror-modify-iter API allows to change one or more
        parameters of one or more SnapMirror relationships.  This API is
        not supported on Infinite Volume constituents.
        
        :param query: If operating on a specific snapmirror, this input element must
                specify all keys.
                If operating on snapmirror objects based on query, this input
                element must specify a query.
        
        :param max_records: The maximum number of snapmirror objects to be operated in this
                call.
                Default: 20
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching snapmirror
                even when the operation on a previous matching snapmirror fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param schedule: Specifies the name of the cron schedule, used to update the
                SnapMirror relationship.
        
        :param return_success_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were successfully operated on.
                If set to false, the list of snapmirror objects operated on will
                not be returned.
                Default: true
        
        :param vserver: If this optional parameter is specified, designates the managing
                Vserver. The managing Vserver is authorized to use snapmirror
                commands to manage the SnapMirror relationship. The vserver
                option is currently a reserved option.
        
        :param tries: Specifies the maximum number of times to attempt each manual or
                scheduled transfer for a SnapMirror relationship. The default is
                eight times.
                Note: You can set the tries option to zero (0) to disable manual
                and scheduled updates for the SnapMirror relationship. This
                parameter is only relevant on Data ONTAP 8.1 operating in
                Cluster-Mode. On Data ONTAP 8.2 operating in Cluster-Mode, the
                maximum number of times to attempt a transfer is an attribute of
                the SnapMirror policy. Therefore the value of this parameter is
                ignored.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapmirror objects
                match a given query.
                If set to true, the API will continue with the next matching
                snapmirror even when the operation fails for the snapmirror.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapmirror
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of snapmirror objects not operated on
                will not be returned.
                Default: true
        
        :param policy: Specifies the name of the SnapMirror policy that applies to this
                relationship.
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth.  The max-transfer-rate option does not affect
                load-sharing transfers and transfers for other relationships with
                Relationship Capability of Pre 8.2 confined to a single cluster.
        """
        return self.request( "snapmirror-modify-iter", {
            'max_records': max_records,
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'tries': [ tries, 'tries', [ basestring, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'policy': [ policy, 'policy', [ basestring, 'sm-policy' ], False ],
            'query': [ query, 'query', [ SnapmirrorInfo, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapmirrorModifyIterInfo, True ],
            'failure-list': [ SnapmirrorModifyIterInfo, True ],
        } )
    
    def snapmirror_break(self, source_vserver=None, source_volume=None, source_cluster=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None, destination_cluster=None):
        """
        Breaks a SnapMirror relationship between a source and
        destination volume of a data protection mirror. When
        Data ONTAP breaks the relationship, the destination volume is
        made a read-write volume and can diverge from the source volume,
        client redirection is turned off on the destination volume, the
        restart checkpoint is cleared, and the clients can see the latest
        Snapshot copy.
        <p>
        On Data ONTAP operating in 7-Mode, no check is done to
        determine whether the operation is legal or successful.
        You need to query the status afterward by using the
        snapmirror-get-status API.
        <p>
        Subsequent manual or scheduled SnapMirror updates to the broken
        relationship will fail until the SnapMirror relationship is
        re-established using the snapmirror-resync API.
        <p>
        On Data ONTAP operating in Cluster-Mode, this API applies
        only to data protection mirrors and not to load-sharing mirrors.
        <p>
        The snapmirror-break API must be issued on destination storage
        system on Data ONTAP operating in 7-Mode, and on the destination
        cluster on Data ONTAP 8.1 operating in Cluster-Mode, and on
        the destination cluster or Vserver on Data ONTAP 8.2 or later
        operating in Cluster-Mode.
        <p>
        This API is not supported if the destination end point is an
        Infinite Volume.
        
        :param source_vserver: Specifies the source Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source volume.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the source volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_cluster: Specifies the source cluster of the SnapMirror relationship. The
                source Vserver and source volume must also be specified if using
                this parameter.
        
        :param destination_vserver: Specifies the destination Vserver of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, when specifying a
                destination endpoint, you must use either the destination
                location, or the destination cluster, destination Vserver,
                and destination volume.
                On Data ONTAP operating in 7-Mode, If the destination
                endpoint is a qtree, it must be quiesced using
                snapmirror-quiesce.
                This parameter is mandatory on Data ONTAP 7-mode
        
        :param destination_volume: Specifies the destination volume of the SnapMirror relationship.
                If using this parameter, the following parameters must also be
                specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2
                operating in Cluster-Mode if the relationship control
                plane is 'v1'.
                </ul>
        
        :param source_location: Specifies source endpoint of the SnapMirror
                relationship in the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;]
                On Data ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt;
                On Data ONTAP 8.1 operating in Cluster-Mode, and on Data
                ONTAP 8.2 operating in Cluster-Mode for relationships using
                a control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode.
                <li> &lt;[vserver:]volume&gt;
                On Data ONTAP 8.2 or later operating in Cluster-Mode except
                for relationships using a control plane compatible with Data
                ONTAP 8.1 operating in Cluster-Mode. This format depends
                on the Vserver peering setup between the source and
                destination Vservers.
                <ul>
                This format may change in the future.
                On Data ONTAP operating in Cluster-Mode, When specifying a
                source endpoint, you must use either the source location, or the
                source cluster, source Vserver, and source volume.
        
        :param destination_cluster: Specifies the destination cluster of the SnapMirror relationship.
                The destination Vserver and destination volume must also be
                specified if using this parameter.
        """
        return self.request( "snapmirror-break", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_create(self, source_vserver=None, source_volume=None, schedule=None, vserver=None, relationship_type=None, return_record=None, source_cluster=None, tries=None, destination_vserver=None, destination_location=None, policy=None, destination_volume=None, source_location=None, max_transfer_rate=None, destination_cluster=None):
        """
        The snapmirror-create API creates a SnapMirror relationship
        between a source  and destination volumes. The following types of
        relationships can be created:
        <ul>
        <li>'data_protection' - For Disater Recovery (DR);
        <li>'load_sharing' - For load-sharing within the same Vserver;
        <li>'vault' - For Vault;
        <li>'transition_data_protection' -  For 7-mode to Cluster-Mode
        transition;
        <li>'restore' - For restoring a data protection (DP) volume
        data;
        </ul>
        On Data ONTAP 8.1 operating in Cluster-Mode, only
        'data_protection' and 'load_sharing' type are supported.
        Relationships of type 'restore' are created temporary during a
        restore operation initiated using the snapmirror-restore API or
        the corresponding command.
        The source and destination endpoints must be specified when using
        the snapmirror-create API.
        This API will fail if the destination volume does not exist.
        On Data ONTAP 8.2 operating in Cluster-Mode, the API does not
        validate the attributes and the existence of the source volume.
        It will succeed even if the source volume does not exist. The
        validation will be done at the first transfer time.
        On Data ONTAP 8.1 operating in Cluster-Mode, the API will fail if
        the source volume is not in online state and read-write (RW)
        type, or the destination volume is not in online state and a DP
        (Data Protection) type.
        Note: The source volume might contain data and Snapshot copies
        prior to creating the Snapmirror relationship. If the destination
        volume is not empty, it must have a Snapshot copy in common with
        the source volume, that is, it must have once been a copy of the
        source volume. On Data ONTAP 8.1 operating in Cluster-Mode, the
        API will fail if there is no common Snapshot copy. On Data ONTAP
        8.2 operating in Cluster-Mode the API will succeed, but all
        subsequent transfers will fail if there is no common snapshot
        copy.
        Load-sharing mirrors have the following restrictions:
        - They only use FlexVol volumes.
        - They are confined to a single Vserver; they are not allowed to
        span Vservers.
        - The source or destination of a load-sharing relationship cannot
        be the source or destination of any other SnapMirror
        relationship.
        A set of load-sharing mirrors can have one or more destination
        volumes. You create separate SnapMirror relationships between the
        common source volume and each destination volume to create the
        set of load-sharing mirrors.
        If the destination volume is empty, it must be initialized using
        the snapmirror-initialize API. Destination volumes in a set of
        load-sharing mirrors must be initialized using the
        snapmirror-initialize-ls-set API.
        The snapmirror-create API must be issued on the destination
        cluster on Data ONTAP 8.1 operating in Cluster-Mode, and on the
        destination Vserver on Data ONTAP 8.2 operating in Cluster-Mode.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of source volume.
                <li> The name of the source cluster on Data ONTAP 8.1, or on Data
                ONTAP 8.2 or later operating in Cluster-Mode if the relationship
                control plane is 'v1'.
                </ul>
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the source Vserver.
                <li> The name of the source cluster on Data ONTAP 8.1 operating
                in Cluster-Mode, or on Data ONTAP 8.2 or later operating in
                Cluster-Mode if the relationship control plane is 'v1'.
                </ul>
        
        :param schedule: Specifies the name of the cron schedule, which is used to update
                the SnapMirror relationship.
        
        :param vserver: If this optional parameter is specified, designates the managing
                Vserver. The managing Vserver is authorized to use snapmirror
                commands to manage the SnapMirror relationship. The vserver
                option is currently a reserved option and should not be used for
                queries. The destination-vserver parameter should be used to
                select the Vserver in a cluster context.
        
        :param relationship_type: Specifies the type of the SnapMirror relationship.
                Possible values:
                <ul>
                <li> "data_protection"               ,
                <li> "load_sharing"                  ,
                <li> "vault"                         ,
                <li> "restore"                       ,
                <li> "transition_data_protection"
                </ul>
        
        :param return_record: If set to true, returns the snapmirror on successful creation.
                Default: false
        
        :param source_cluster: Specifies the name of the source cluster for the SnapMirror
                relationship. The parameters for the name of the source Vserver,
                and the name of the source volume must also be specified if using
                this parameter. This parameter is available only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param tries: Specifies the maximum number of times to attempt each manual or
                scheduled transfer for a SnapMirror relationship. The default is
                eight times.
                Note: You can set the tries option to zero (0) to disable manual
                and scheduled updates for the SnapMirror relationship. This
                parameter is only relevant on Data ONTAP 8.1 operating in
                Cluster-Mode. On Data ONTAP 8.2 operating in Cluster-Mode, the
                maximum number of times to attempt a transfer is an attribute of
                the SnapMirror policy. Therefore the value of this parameter is
                ignored.
        
        :param destination_vserver: Specifies the name of the destination Vserver for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of destination volume.
                <li> The name of the destination cluster on Data ONTAP 8.1, or on
                Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        
        :param destination_location: Specifies the destination endpoint of the SnapMirror relationship
                in one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The destination endpoint can be specified using the location
                formats above, or by specifying the parameters for the name of
                the destination Vserver, the name of the destination volume, and
                the name of the destination cluster. The name of the destination
                cluster is only required on Data ONTAP 8.1 operating in
                Cluster-Mode.
        
        :param policy: Specifies the name of the snapmirror policy for the relationship.
                For SnapMirror relationships of type 'vault', the policy will
                also have rules to select snapshot copies that must be
                transferred. If no policy is specified, a default policy will be
                applied depending on the type of the SnapMirror relationship.
                This parameter is only available on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v2'.
        
        :param destination_volume: Specifies the name of the destination volume for the SnapMirror
                relationship. If using this parameter, the following parameters
                should also be specified:
                <ul>
                <li> The name of the destination Vserver.
                <li> The name of the destination cluster on Data ONTAP 8.1
                operating in Cluster-Mode, or on Data ONTAP 8.2 or later
                operating in Cluster-Mode if the relationship control plane is
                'v1'.
                </ul>
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                one of the following formats:
                <ul>
                <li> &lt;system&gt;:/vol/&lt;volume&gt;[/&lt;qtree&gt;] on Data
                ONTAP operating in 7-Mode.
                <li> [&lt;cluster&gt:]//&ltvserver&gt/&ltvolume&gt; on Data
                ONTAP 8.1 operating in Cluster-Mode, and on Data ONTAP 8.2
                operating in Cluster-Mode for relationships using a control plane
                compatible with Data ONTAP 8.1 operating in Cluster-Mode.
                <li> &lt;[vserver:]volume&gt; on Data ONTAP 8.2 or later
                operating in Cluster-Mode except for relationships using a
                control plane compatible with Data ONTAP 8.1 operating in
                Cluster-Mode. This format depends on Vserver peering setup
                between the source and destination Vservers.
                </ul>
                This format may change in the future.
                The source endpoint can be specified using the location formats
                above, or by specifying the parameters for the name of the source
                Vserver, the name of the source volume, and the name of the
                source cluster. The name of the source cluster is only required
                on Data ONTAP 8.1 operating in Cluster-Mode.
        
        :param max_transfer_rate: Specifies the upper bound, in kilobytes per second, at which data
                is transferred. The default is unlimited (0) which permits the
                SnapMirror relationship to fully utilize the available network
                bandwidth.  The max-transfer-rate option does not affect
                load-sharing transfers and transfers for other relationships with
                Relationship Capability of Pre 8.2 confined to a single cluster.
        
        :param destination_cluster: Specifies the destination cluster name for the SnapMirror
                relationship. The parameters for the name of the destination
                Vserver, and the name of the destination volume must also be
                specified if using this parameter. This parameter is available
                only on:
                <ul>
                <li> Data ONTAP 8.1 operating in Cluster-Mode.
                <li> Data ONTAP 8.2 or later operating in Cluster-Mode if the
                relationship control plane is 'v1'.
                </ul>
        """
        return self.request( "snapmirror-create", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'relationship_type': [ relationship_type, 'relationship-type', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'source_cluster': [ source_cluster, 'source-cluster', [ basestring, 'None' ], False ],
            'tries': [ tries, 'tries', [ basestring, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'policy': [ policy, 'policy', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
            'max_transfer_rate': [ max_transfer_rate, 'max-transfer-rate', [ int, 'None' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'None' ], False ],
        }, {
            'result': [ SnapmirrorInfo, False ],
        } )
    
    def snapmirror_get_destination(self, source_vserver=None, source_volume=None, desired_attributes=None, destination_vserver=None, destination_location=None, destination_volume=None, source_location=None):
        """
        The snapmirror-get-destination API returns information about a
        SnapMirror relationship whose source endpoint is on the cluster
        or Vserver it is issued on. The destination endpoint must be
        specified when using this API. The source endpoint can also be
        specified.
        <p>
        The cluster or Vserver may have several entries for the specified
        endpoints, but with different relationship IDs. In this case the
        API returns information about the first entry. To get information
        about all the SnapMirror relationships  matching the specified
        endpoints, the snapmirror-get-destination-iter API must be used.
        <p>
        Note that the information for a SnapMirror relationship will not
        be available on its source Vserver or source cluster until at
        least one transfer is initiated.
        <p>
        The information returned can be stale. Stale information
        corresponds to a SnapMirror relationship that has been deleted on
        its destination cluster or Vserver.
        <p>
        This API is only supported on Data ONTAP 8.2 and above operating
        in Cluster-Mode.
        <p>
        This API must be issued on the source Vserver or the source
        cluster of the relationship.
        
        :param source_vserver: Specifies the name of the source Vserver for the SnapMirror
                relationship. The name of the source volume must also be
                specified if using this parameter.
        
        :param source_volume: Specifies the name of the source volume of the SnapMirror
                relationship. The name of the source Vserver must also be
                specified if using this parameter.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param destination_vserver: Specifies the name of the destination Vserver for the
                relationship. The name of the destination volume must also be
                specified if using this parameter.
        
        :param destination_location: Specifies the destination endpoint of the  SnapMirror
                relationship in the format [vserver:]volume. This format may
                change in the future.
                The destination endpoint can be specified using the location
                format above, or by specifying the parameters for the name of the
                destination Vserver and the name of the destination volume.
        
        :param destination_volume: Specifies the name of destination volume for the SnapMirror
                relationshp. The name of the destination Vserver must also be
                specified if using this parameter.
        
        :param source_location: Specifies the source endpoint of the SnapMirror relationship in
                the format [vserver:]volume. This format may change in the
                future.
                The source endpoint can be specified using the location format
                above, or by specifying the parameters for the name of the source
                Vserver and the name of the source volume.
        """
        return self.request( "snapmirror-get-destination", {
            'source_vserver': [ source_vserver, 'source-vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapmirrorDestinationInfo, 'None' ], False ],
            'destination_vserver': [ destination_vserver, 'destination-vserver', [ basestring, 'None' ], False ],
            'destination_location': [ destination_location, 'destination-location', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_location': [ source_location, 'source-location', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ SnapmirrorDestinationInfo, False ],
        } )
    
    def snapmirror_snapshot_owner_create(self, vserver, volume, snapshot, snapshot_owner_name=None):
        """
        Add an owner to preserve a Snapshot copy for a SnapMirror
        mirror-to-vault cascade configuration.
        
        :param vserver: Vserver Name
        
        :param volume: Volume Name
        
        :param snapshot: Snapshot Copy Name
        
        :param snapshot_owner_name: Specifies the name of the owner to preserve a Snapshot copy for a
                SnapMirror mirror-to-vault cascade configuration. An owner can
                contain letters, numbers, and the underscore character (_), and
                can be at most 32 characters long. If no owner is specified, the
                system will assign an internal default owner to preserve the
                Snapshot copy.
        """
        return self.request( "snapmirror-snapshot-owner-create", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'snapshot-id' ], False ],
            'snapshot_owner_name': [ snapshot_owner_name, 'snapshot-owner-name', [ basestring, 'snapshot-owner-name' ], False ],
        }, {
        } )

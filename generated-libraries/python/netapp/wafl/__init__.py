from netapp.connection import NaConnection
from wafl_sync_handle import WaflSyncHandle # 3 properties

class WaflConnection(NaConnection):
    
    def wafl_sync(self, volume_uuids=None, volumes=None):
        """
        Forces a WAFL consistency point (CP) in order to reduce
        the time for succeeding fence and snapshot related
        operations.
        In Data ONTAP 7-Mode this call is synchronous and will
        not return until the CP has completed.
        In Data ONTAP Cluster-Mode this API is asynchronous and
        will return immediately as soon as the CP is scheduled.
        The wafl-get-sync-status API can be used to check status
        of the previously scheduled CP.
        Two uses of this API are
        <ul>
        <li> to predict how fast a successive consistency
        group based operation will finish,</li>
        <li> to improve performance of succeeding consistency
        group primitives.</li>
        </ul>
        
        :param volume_uuids: A list of volume UUIDs in this filer to take a CP on.
        
        :param volumes: A list of volume names to take a CP on.
                In Data ONTAP 7-Mode, the CP operation will be performed on
                all the volumes on the controller if no volumes are specified.
                In Data ONTAP Cluster-Mode, "volumes" is a required input and
                all specified volumes must belong to the same Vserver.
                If an error is encountered when processing the sync request for
                a volume, the operation is aborted and sync operation will
                not be performed on the rest of the volumes specified.
        """
        return self.request( "wafl-sync", {
            'volume_uuids': [ volume_uuids, 'volume-uuids', [ basestring, 'uuid' ], True ],
            'volumes': [ volumes, 'volumes', [ basestring, 'volume-name' ], True ],
        }, {
            'handles': [ WaflSyncHandle, True ],
        } )
    
    def wafl_get_sync_status(self, sync_handle):
        """
        Returns the status of the previously issued asynchronous
        Consistency Point operations.
        
        :param sync_handle: Handle representing a previously issued wafl-sync operation.
        """
        return self.request( "wafl-get-sync-status", {
            'sync_handle': [ sync_handle, 'sync-handle', [ WaflSyncHandle, 'None' ], False ],
        }, {
            'status': [ basestring, False ],
        } )

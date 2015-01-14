from netapp.connection import NaConnection
from cg_timeout_enum import CgTimeoutEnum # 0 properties

class CgConnection(NaConnection):
    
    def cg_commit(self, cg_id):
        """
        Commits the snapshots that were started during
        the preceeding cg-start call that returned the
        cg-id key, and unfences the volumes that were fenced.
        If cg-commit API times out, then it means that either too
        many volumes were specified to the cg-start api or the timeout
        value for the cg-start api was very small. In this situation,
        the caller should try to perform the cg-start operation by
        specifying lesser volumes or by specifying higher timeout
        value.
        
        :param cg_id: Key to identify the ongoing cg operation.
        """
        return self.request( "cg-commit", {
            'cg_id': [ cg_id, 'cg-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def cg_delete(self, snapshot, volume_uuids, volumes):
        """
        Deletes the snaps associated with a CG checkpoint
        in this filer. This API is deprecated as of Data ONTAP 8.2.
        Applications using this API should transition to
        snapshot-multidelete API as appropriate.
        
        :param snapshot: The name of the snapshot that is deleted in each volume.
        
        :param volume_uuids: The identities of the volumes in which to create
                the snapshot.
                <p>
                The volume identity string is its 128-bit universally-unique
                identifier (UUID) or its DSID.
                <p>
                UUIDs are formatted as 36-character strings.  These
                strings are composed of 32 hexadecimal characters
                broken up into five groupings separated by '-'s.  The
                first grouping has 8 hex characters, the second through
                fourth groupings have four hex characters each, and the
                fifth and final grouping has 12 hex characters.  Note
                that a leading '0x' is not used.
                <p>
                Here is an example of an actual UUID:
                <p>
                <dl>
                <dt><dd> 49e370d6-5b5a-11d9-9eb5-000100000529 </dd><br></dt>
                </dl>
        
        :param volumes: A list of volumes in this filer that is part of this CG
                operation.
        """
        return self.request( "cg-delete", {
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'volume_uuids': [ volume_uuids, 'volume-uuids', [ basestring, 'UUID' ], True ],
            'volumes': [ volumes, 'volumes', [ basestring, 'volume-name' ], True ],
        }, {
        } )
    
    def cg_start(self, snapshot, volumes, volume_uuids, user_timeout=None, timeout=None, incoming_cg_id=None):
        """
        Starts the checkpoint cycle for externally synchronized
        checkpoints in the filer. This operation fences the
        specified volumes and returns "success" (if successful).
        If the API returns "success", the call starts a snapshot
        create operation in these volumes.
        If the API returns "success", this  operation
        SHOULD be followed by a call to cg-commit (below).
        <p>
        This API is not supported on Infinite Volume.
        
        :param snapshot: The provided name of the snapshot that is created in each
                volume. This name is the unique identifier by which the
                calling agent identifies the snapshots that constitute a
                checkpoint.
                The maximum length is 255 characters. (= MAXNAMLEN)
        
        :param volumes: A list of volumes in this filer that is part of this CG
                operation.
        
        :param volume_uuids: The identities of the volumes in which to create
                the snapshot.
                <p>
                The volume identity string is its 128-bit universally-unique
                identifier (UUID) or its DSID.
                <p>
                UUIDs are formatted as 36-character strings.  These
                strings are composed of 32 hexadecimal characters
                broken up into five groupings separated by '-'s.  The
                first grouping has 8 hex characters, the second through
                fourth groupings have four hex characters each, and the
                fifth and final grouping has 12 hex characters.  Note
                that a leading '0x' is not used.
                <p>
                Here is an example of an actual UUID:
                <p>
                <dl>
                <dt><dd> 49e370d6-5b5a-11d9-9eb5-000100000529 </dd><br></dt>
                </dl>
        
        :param user_timeout: User specified timeout value in seconds. This option can be
                set if the user	wants to specify timeout value other than the
                default timeouts. The API will return failure if both
                'timeout' and 'user-timeout' are specified. The minimum value
                for this field is equal to the "urgent" timeout. The maximum
                timeout which can be specified is 120 seconds.
        
        :param timeout: Timeout selector. Possible vaules are "urgent", "medium"
                or "relaxed". If no value is specified, the default value
                is "medium". Following are the timeout values:
                <p>
                <dl>
                <dt><dd>"urgent"  : 5 seconds </dd><br></dt>
                <dt><dd>"medium"  : 7 seconds </dd><br></dt>
                <dt><dd>"relaxed" : 20 seconds </dd><br></dt>
                </dl>
                </p>
        
        :param incoming_cg_id: This is the common cg-id which the M-host generates internally
                to keep track of all the D-blades on which this API is
                executed. When this field is not present, D-blade will
                generates its own cg-id.
        """
        return self.request( "cg-start", {
            'user_timeout': [ user_timeout, 'user-timeout', [ int, 'None' ], False ],
            'timeout': [ timeout, 'timeout', [ basestring, 'None' ], False ],
            'incoming_cg_id': [ incoming_cg_id, 'incoming-cg-id', [ int, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'volumes': [ volumes, 'volumes', [ basestring, 'volume-name' ], True ],
            'volume_uuids': [ volume_uuids, 'volume-uuids', [ basestring, 'UUID' ], True ],
        }, {
            'cg-id': [ int, False ],
        } )

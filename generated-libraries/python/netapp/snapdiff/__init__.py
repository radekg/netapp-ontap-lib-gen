from netapp.connection import NaConnection
from change_rec import ChangeRec # 14 properties

class SnapdiffConnection(NaConnection):
    
    def snapdiff_iter_next(self, session_id):
        """
        List the first or next set of changes between two snapshots
        in the same volume.  This is either the first
        set or a continuation of the changes from the previous
        call to this function.
        When finding changed file information takes a long time, to
        prevent the ZAPI session from timing out zero changes may be
        reported with 'end-of-diff' flag set to 'false'. In such
        situations it is expected that the client keeps sending this
        ZAPI until it receives a response where 'end-of-diff' set to
        'true'.
        
        :param session_id: This is the session identifier returned from the
                snapdiff-iter-start request.
        """
        return self.request( "snapdiff-iter-next", {
            'session_id': [ session_id, 'session-id', [ basestring, 'None' ], False ],
        }, {
            'progress': [ int, False ],
            'end-of-diff': [ bool, False ],
            'num-changes': [ int, False ],
            'snapshot-changes': [ ChangeRec, True ],
            'restart-cookie': [ basestring, False ],
        } )
    
    def snapdiff_iter_end(self, session_id):
        """
        Close or Abort a snapdiff operation.  If there is no
        outstanding snapdiff-iter-next request from the client
        then this function will close the current session
        regardless of the number of diffs received.  If a
        snapdiff-iter-next request is currently outstanding from
        this client then this function is considered an abort and
        will cause the current request to abort.  In the case of
        abort, the snapdiff-iter-next function may or may not
        return.  This function will always return.  An aborted
        session could be restarted from the checkpoint by calling
        snapdiff-iter-start with restart-cookie.
        
        :param session_id: This is the session id returned from the
                snapdiff-iter-start request.
        """
        return self.request( "snapdiff-iter-end", {
            'session_id': [ session_id, 'session-id', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapdiff_iter_status(self, session_id):
        """
        Report status of current session.  This is used to
        determine if the filer is still responding and/or
        working on the current request.  This is needed because
        some operations can take a long time and the client
        needs a way to maintain the session.
        
        :param session_id: This is the session id returned from the snapdiff-iter-start
                request.
        """
        return self.request( "snapdiff-iter-status", {
            'session_id': [ session_id, 'session-id', [ basestring, 'None' ], False ],
        }, {
            'session-status': [ basestring, False ],
            'failure-reason': [ basestring, False ],
        } )
    
    def snapdiff_iter_start(self, application_type, application_name, diff_snapshot, max_diffs, volume, namespace_diff_snapshot_id=None, diff_snapshot_id=None, volume_dsid=None, file_access_protocol=None, constituent_role=None, namespace_constituent_orig_msid=None, namespace_base_snapshot_id=None, namespace_constituent_dsid=None, base_snapshot=None, base_snapshot_id=None, atime=None, include_file_attributes=None, mhost_session_id=None, restart_cookie=None):
        """
        Establish a session for a snapdiff operation.
        
        :param application_type: Type of the application specified in 'application-name' field.
                Examples:  "indexing", "backup", "srm", etc.
        
        :param application_name: Complete name of the application using the API.
        
        :param diff_snapshot: This is the name of the difference snapshot.
                The diff-snapshot is the end time for the difference operation.
        
        :param max_diffs: This is the maximum number of changes to be returned by
                each call to snapdiff-iter-next.
                range: [256..4096]
        
        :param volume: This is the name of the volume containing the base and
                diff snapshots.  The name should not have "/vol/"
                prepended to it.
        
        :param namespace_diff_snapshot_id: The logical-snapshot-id of the diff-snapshot in the volume with
                namespace-constituent-dsid.
        
        :param diff_snapshot_id: The logical-snapshot-id of the diff-snapshot in the volume with
                volume-dsid. This should be set only for Infinite Volume.
        
        :param volume_dsid: DSID of the volume containing the base and diff snapshots.
                DSIDs are formatted as 18-character strings composed of 16 hex
                characters prefixed with '0x'.  If this volume-dsid is for
                a data constituent volume of an Infinite Volume then the
                namespace-* fields also must be set.
        
        :param file_access_protocol: This is the file access protocol that the filenames, returned in
                responses to the snapdiff-iter-next API, are guaranteed to work
                over, if and when the caller attempts to access the changed
                files from the filer.
                Possible values are "nfs", "nfsv4" and "cifs". The default is "nfs".
        
        :param constituent_role: Indicates the role of the volume represented by the
                volume-dsid if that volume is a constituent of an Infinite
                Volume. This is set only for Infinite Volume and the possible
                alues are:
                "namespace"
                "data"
                "objectlocator"
        
        :param namespace_constituent_orig_msid: If the volume(represented by volume-dsid) on which the snapdiff
                operation is running is a data constituent volume of the
                Infinite Volume, then this field indicates the original MSID of
                the namespace constituent of that Infinite Volume.
        
        :param namespace_base_snapshot_id: The logical-snapshot-id of the base-snapshot in the volume with
                namespace-constituent-dsid.
        
        :param namespace_constituent_dsid: If the volume(represented by volume-dsid) on which the snapdiff
                operation is running is a data constituent volume of the
                Infinite Volume, then this field indicates the DSID of the
                namespace constituent or its mirror of that Infinite Volume
                which is on the same node as the data constituent volume.
                This is set only if the constituent-role is "data".
        
        :param base_snapshot: This is the name of the base snapshot.  This describes the
                beginning time for the difference operation. The name is a
                snapshot for the volume. If this snapshot is not specified,
                then all files in the difference snapshot will be returned.
        
        :param base_snapshot_id: The logical-snapshot-id of the base-snapshot in the volume with
                volume-dsid. This should be set only for Infinite Volume.
        
        :param atime: Report files which have access time changes. Default value is true.
        
        :param include_file_attributes: Report the attributes of a file. If this flag is not set, then
                only the inode number, change-type, filename and ftype is reported.
                Default value is true.
        
        :param mhost_session_id: This is the mhost session-id passed to the d-blade session which
                is used in the d-blade performance counters for easy association
                of m-host counter object with the corresponding d-blade counter
                object(s).
        
        :param restart_cookie: This is the cookie returned from snapdiff-iter-next which can be
                used to restart a session from the last aborted point.
        """
        return self.request( "snapdiff-iter-start", {
            'namespace_diff_snapshot_id': [ namespace_diff_snapshot_id, 'namespace-diff-snapshot-id', [ int, 'None' ], False ],
            'application_type': [ application_type, 'application-type', [ basestring, 'None' ], False ],
            'application_name': [ application_name, 'application-name', [ basestring, 'None' ], False ],
            'diff_snapshot_id': [ diff_snapshot_id, 'diff-snapshot-id', [ int, 'None' ], False ],
            'volume_dsid': [ volume_dsid, 'volume-dsid', [ basestring, 'None' ], False ],
            'diff_snapshot': [ diff_snapshot, 'diff-snapshot', [ basestring, 'None' ], False ],
            'max_diffs': [ max_diffs, 'max-diffs', [ int, 'None' ], False ],
            'file_access_protocol': [ file_access_protocol, 'file-access-protocol', [ basestring, 'None' ], False ],
            'constituent_role': [ constituent_role, 'constituent-role', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'namespace_constituent_orig_msid': [ namespace_constituent_orig_msid, 'namespace-constituent-orig-msid', [ basestring, 'None' ], False ],
            'namespace_base_snapshot_id': [ namespace_base_snapshot_id, 'namespace-base-snapshot-id', [ int, 'None' ], False ],
            'namespace_constituent_dsid': [ namespace_constituent_dsid, 'namespace-constituent-dsid', [ basestring, 'None' ], False ],
            'base_snapshot': [ base_snapshot, 'base-snapshot', [ basestring, 'None' ], False ],
            'base_snapshot_id': [ base_snapshot_id, 'base-snapshot-id', [ int, 'None' ], False ],
            'atime': [ atime, 'atime', [ bool, 'None' ], False ],
            'include_file_attributes': [ include_file_attributes, 'include-file-attributes', [ bool, 'None' ], False ],
            'mhost_session_id': [ mhost_session_id, 'mhost-session-id', [ basestring, 'None' ], False ],
            'restart_cookie': [ restart_cookie, 'restart-cookie', [ basestring, 'None' ], False ],
        }, {
            'session-id': [ basestring, False ],
            'session-status': [ basestring, False ],
        } )

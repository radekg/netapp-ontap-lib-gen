from netapp.connection import NaConnection
from hole_range_info import HoleRangeInfo # 2 properties
from file_hole_range_query_iter_key_td import FileHoleRangeQueryIterKeyTd # 2 properties
from file_copy_info import FileCopyInfo # 23 properties
from sfod_operation_path import SfodOperationPath # 0 properties
from file_copy_get_iter_key_td import FileCopyGetIterKeyTd # 2 properties
from file_info import FileInfo # 20 properties
from file_list_directory_iter_key_td import FileListDirectoryIterKeyTd # 3 properties
from digest_algorithm import DigestAlgorithm # 0 properties
from volume_inode import VolumeInode # 3 properties
from inode_parent_info import InodeParentInfo # 4 properties
from sfod_scanner_status import SfodScannerStatus # 0 properties
from file_scope import FileScope # 0 properties
from fingerprint_info import FingerprintInfo # 25 properties
from file_fingerprint_info import FileFingerprintInfo # 22 properties
from failed_delete_info import FailedDeleteInfo # 3 properties

class FileConnection(NaConnection):
    
    def file_usage_result_get(self, cookie):
        """
        Used to poll and retrieve results for a previous
        file-usage-start call. EINPROGRESS indicates that the
        background job has not finished yet.
        
        :param cookie: Cookie that was returned in an earlier
                file-usage-start call.
        """
        return self.request( "file-usage-result-get", {
            'cookie': [ cookie, 'cookie', [ basestring, 'None' ], False ],
        }, {
            'unique-bytes': [ int, False ],
            'total-bytes': [ int, False ],
        } )
    
    def file_get_file_info(self, path):
        """
        Obtains the file information or properties.
        
        :param path: Pathname of the directory to list.
                The value is expected to begin with /vol/<volumename>.
        """
        return self.request( "file-get-file-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'file-info': [ FileInfo, False ],
        } )
    
    def file_rename_file(self, from_path, to_path):
        """
        Rename a file or directory. Note that this API cannot be used
        to rename to a different volume.
        
        :param from_path: Original path of the file.
                The value must begin with /vol/<volumename>.
        
        :param to_path: Final path of the file.
                The value must begin with /vol/<volumename>. All path
                components except the final file name must already
                exist.
        """
        return self.request( "file-rename-file", {
            'from_path': [ from_path, 'from-path', [ basestring, 'None' ], False ],
            'to_path': [ to_path, 'to-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_delete_directory_all(self, dirpath, continue_on_error=None):
        """
        Delete a directory and its contents, including
        subdirectories and their contents. It is possible for this
        API to fail if the directory or one of its subdirectories
        is a CIFS share	and resides in a qtree with ntfs or mixed
        security. It is possible for this API to fail if the
        directory or one of its subdirectories contains a LUN. It
        is possible for this API to fail if the specified storage
        belongs to another vfiler. It is possible for this API to
        fail if the delete encounters nested subdirectories
        deep enough to cause the API's process stack to be
        consumed.
        Warning: This API is potentially dangerous. Use it
        with appropriate care and caution.
        
        :param dirpath: Path of the directory to delete.
                The value must begin with /vol/<volumename>.
                Deletion of an entire volume is not supported, the path
                must contain at least one directory within a volume.
                Deletion of files and subdirectories under
                /vol/<rootVolume>/etc is not supported.
        
        :param continue_on_error: If false, the API will stop if it encounters a directory
                or subdirectory that it	cannot delete. If true, the API
                will skip the directory	it cannot delete and continue
                deleting other files, directories and subdirectories.
                The default value is false.
        """
        return self.request( "file-delete-directory-all", {
            'continue_on_error': [ continue_on_error, 'continue-on-error', [ bool, 'None' ], False ],
            'dirpath': [ dirpath, 'dirpath', [ basestring, 'None' ], False ],
        }, {
            'failed-delete-errors': [ FailedDeleteInfo, True ],
        } )
    
    def file_get_space_reservation_info(self, volume_id, path):
        """
        Queries the space reservation settings for the
        named file.
        
        :param volume_id: The identifier of the volume in which the named file exists.
                <p>
                There are two legal choices for a volume identifier,
                either a DSID or a UUID.
                <p>
                DSIDs are formatted as 18-character strings composed
                of 16 hex characters, zero filled if required and prefixed
                with '0x'.
                <p>
                Here is an example of an actual DSID:
                <p>
                0x0000000000000401
                <p>
                UUIDs are formatted as 36-character strings. These strings
                are composed of 32 hexadecimal characters broken up into
                five groupings separated by '-'s. The first grouping has 8
                hex characters, the second through fourth groupings have
                four hex characters each, and the fifth and final grouping
                has 12 hex characters. Note that a leading '0x' is not used.
                <p>
                Here is an example of an actual UUID:
                <p>
                49e370d6-5b5a-11d9-9eb5-000100000529
        
        :param path: File to be queried.
        """
        return self.request( "file-get-space-reservation-info", {
            'volume_id': [ volume_id, 'volume-id', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'is-fill-enabled': [ bool, False ],
            'is-overwrite-enabled': [ bool, False ],
        } )
    
    def file_punch_hole_iter(self, path, attributes_list, max_records=None, tag=None):
        """
        Punch hole in the file. Hole punching involves reclaiming of
        blocks in a file by unallocating them and then direct or
        indirect blocks can be made to point to 0.
        
        :param path: Path of the file. Format must be of the following:
                /vol/my_vol/path-to-file
        
        :param attributes_list: This is the array containing the ranges that need to be
                hole punched.
        
        :param max_records: Here for future conformance with smfgen
                Default: 1
        
        :param tag: Do not set on first iteration. Use value of next-tag
                on subseguent iterations.
        """
        return self.request( "file-punch-hole-iter", {
            'max_records': max_records,
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'attributes_list': [ attributes_list, 'attributes-list', [ HoleRangeInfo, 'None' ], True ],
            'tag': tag,
        }, {
        } )
    
    def file_list_directory_iter_next(self, tag, maximum):
        """
        Obtain a list of files in a given directory.
        
        :param tag: Tag from a previous file-list-directory-iter-start.
        
        :param maximum: Maximum number of directory entries to retrieve.
        """
        return self.request( "file-list-directory-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'files': [ FileInfo, True ],
            'records': [ int, False ],
        } )
    
    def file_copy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Query the status of a file-copy operation
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                file object.
                All file objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "file-copy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FileCopyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FileCopyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FileCopyInfo, True ],
        } )
    
    def file_check(self, volume_inode=None, snapshot=None, file_path=None):
        """
        Check L0 (level 0) blocks of a file for RAID errors.
        It starts a background WAFL L0 block scanner for the file.
        The scanner status can be checked by 'wafl scan status'.
        Results are saved to an output file
        in the format '/etc/file_check.VOL.SNAPID.FILEID'.
        Existing output file of the same name will be overwritten.
        Example Output File - '/vol/vv1/messages' in snapshot 'hourly.4'
        File check started
        Volume: vv1
        Snapshot: hourly.4
        Inode 693 has 1 name(s):
        /vol/vv1/.snapshot/hourly.4/messages
        Lost block(s): 135333 135336 135412 135422 135539
        Lost block(s): 135635
        Total 6 lost block(s)
        The following snapshots contain any of the listed blocks:
        snap1 Wed Jul 16 23:59:44 GMT 2008
        nightly.1 Thu Jul 17 00:00:31 GMT 2008
        hourly.5 Thu Jul 17 08:00:46 GMT 2008
        hourly.4 Thu Jul 17 12:00:46 GMT 2008
        hourly.3 Thu Jul 17 16:00:46 GMT 2008
        snap3 Thu Jul 17 23:24:56 GMT 2008
        snap99 Thu Jul 17 23:47:26 GMT 2008
        nightly.0 Fri Jul 18 00:00:16 GMT 2008
        hourly.2 Fri Jul 18 08:00:17 GMT 2008
        hourly.1 Fri Jul 18 12:00:16 GMT 2008
        Total 184 block(s) scanned
        File check completed
        
        :param volume_inode: A file path in volume and inode format.
                Either file-path or volume-inode-path must be specified, but not both.
        
        :param snapshot: Snapshot name or ID.
        
        :param file_path: The path of the file to be checked.
                The format is: /vol/<volume>/<dir>/<file>.
                Either file-path or volume-inode-path must be specified, but not both.
        """
        return self.request( "file-check", {
            'volume_inode': [ volume_inode, 'volume-inode', [ VolumeInode, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'file_path': [ file_path, 'file-path', [ basestring, 'None' ], False ],
        }, {
            'output-file': [ basestring, False ],
        } )
    
    def file_copy_start(self, source_paths, destination_paths, cutover_time=None, report_time=None, max_throughput=None):
        """
        Start copying a file
        
        :param source_paths: Source file, in the form <volume>/<path>/<filename>. The volume
                must be within the authenticated vserver.
        
        :param destination_paths: Destination file, in the form <volume>/<path>/<filename>. The
                volume must be within the authenticated vserver. If the terminal
                path component is a directory, then the source file's basename is
                replicated in that directory.
        
        :param cutover_time: The maximum amount of time (in seconds) that the source
                can be quiesced before a destination file must be made available
                for read-write traffic. Lower values allow near- immediate
                presentation of the destination file, at the cost of potentially
                preventing the destination volume from taking snapshots for a
                short period of time. Higher values ensure that the destination's
                snapshot schedules are not impacted, at the cost of potentially
                delaying presentation of the destination file. Default is 10
                seconds.
        
        :param report_time: Amount of time in seconds that the job should remain visible for
                reporting purposes.
        
        :param max_throughput: The maximum amount of data (in bytes) that can be transferred per
                second in support of this operation. This mechanism can be used
                to throttle a transfer, to reduce its impact on the performance
                of the source and destination nodes.  Default value is zero,
                indicating no throttling.
        """
        return self.request( "file-copy-start", {
            'source_paths': [ source_paths, 'source-paths', [ basestring, 'sfod-operation-path' ], True ],
            'cutover_time': [ cutover_time, 'cutover-time', [ int, 'None' ], False ],
            'destination_paths': [ destination_paths, 'destination-paths', [ basestring, 'sfod-operation-path' ], True ],
            'report_time': [ report_time, 'report-time', [ int, 'None' ], False ],
            'max_throughput': [ max_throughput, 'max-throughput', [ int, 'size' ], False ],
        }, {
            'job-uuid': [ basestring, False ],
        } )
    
    def file_list_directory_iter_end(self, tag):
        """
        Terminate a directory iteration.
        
        :param tag: Tag from a previous file-list-directory-iter-start.
        """
        return self.request( "file-list-directory-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def file_hole_range_query_iter(self, offset, length, path, desired_attributes=None, max_records=None, tag=None, query=None):
        """
        Return ranges of holes in a file
        
        :param offset: The starting offset of the file from where the scan for holes
                should begin. If the offset is not an integral multiple of
                the block size it will be rounded down to the start of the block.
                Range :		[0..2^63-1]
        
        :param length: The number of bytes to scan. If this is zero scan until end
                of file. If the length is not an integral multiple of the block
                size it will be rounded up to the end of the block.
                Range :		[0..2^63-1]
        
        :param path: The full path of the file for which hole information is to be
                queried. Format must be of the following: /vol/my_vol/my_file
        
        :param desired_attributes: Required to satisfy smfgen and is not used by callers.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 64
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param query: Required to satisfy smfgen and is not used by callers.
        """
        return self.request( "file-hole-range-query-iter", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ HoleRangeInfo, 'None' ], False ],
            'offset': [ offset, 'offset', [ int, 'None' ], False ],
            'max_records': max_records,
            'length': [ length, 'length', [ int, 'None' ], False ],
            'tag': tag,
            'query': [ query, 'query', [ HoleRangeInfo, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'attributes-list': [ HoleRangeInfo, True ],
        } )
    
    def file_rename_directory(self, from_path, to_path):
        """
        Rename a directory. Note that this API cannot be used
        to rename a directory to a different volume.
        
        :param from_path: Original path of the directory.
                The value must begin with /vol/<volumename>.
        
        :param to_path: Final path of the directory.
                The value must begin with /vol/<volumename>. All path
                components except the final directory name must already
                exist.
        """
        return self.request( "file-rename-directory", {
            'from_path': [ from_path, 'from-path', [ basestring, 'None' ], False ],
            'to_path': [ to_path, 'to-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_set_space_reservation_info(self, volume_id, path, is_fill_enabled=None, is_overwrite_enabled=None):
        """
        Sets the space reservation settings for the named
        file. is-overwrite-enabled and is-fill-enabled both must
        be the same value.
        
        :param volume_id: The identifier of the volume in which the named file exists.
                <p>
                There are two legal choices for a volume identifier,
                either a DSID or a UUID.
                <p>
                DSIDs are formatted as 18-character strings composed
                of 16 hex characters, zero filled if required and prefixed
                with '0x'.
                <p>
                Here is an example of an actual DSID:
                <p>
                0x0000000000000401
                <p>
                UUIDs are formatted as 36-character strings. These strings
                are composed of 32 hexadecimal characters broken up into
                five groupings separated by '-'s. The first grouping has 8
                hex characters, the second through fourth groupings have
                four hex characters each, and the fifth and final grouping
                has 12 hex characters. Note that a leading '0x' is not used.
                <p>
                Here is an example of an actual UUID:
                <p>
                49e370d6-5b5a-11d9-9eb5-000100000529
                <p>
                Space reservations are not supported on any volume within
                a Vserver with Infinite Volume, whether on the Infinite
                Volume itself or any of its constituents.
        
        :param path: File to be queried.
        
        :param is_fill_enabled: Whether or not to set the file with fill.
        
        :param is_overwrite_enabled: Whether or not to set the file with overwrite.
        """
        return self.request( "file-set-space-reservation-info", {
            'volume_id': [ volume_id, 'volume-id', [ basestring, 'None' ], False ],
            'is_fill_enabled': [ is_fill_enabled, 'is-fill-enabled', [ bool, 'None' ], False ],
            'is_overwrite_enabled': [ is_overwrite_enabled, 'is-overwrite-enabled', [ bool, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_create_directory(self, path, perm):
        """
        Create a directory.
        
        :param path: Path of the directory to be created.
                The value is expected to begin with /vol/<volumename>.
        
        :param perm: Permission of the directory to be created.
                It's similar to Unix style permission bits: 0755 gives
                read/write/execute permissions to owner and  read/execute
                to group and other users. It consists of 4 octal digits
                derived by adding up bits 4, 2 and 1. Omitted digits are
                assumed to be zeros. First digit selects the set user ID(4),
                set group ID (2) and sticky (1) attributes. The second digit
                selects permission for the owner of the file: read (4),
                write (2) and execute (1); the third selects permissions for
                other users in the same group; the fourth for other users not
                in the group.
                Note: Prior to Data ONTAP 7.3.1 this value was
                treated as a base-10 number.
        """
        return self.request( "file-create-directory", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'perm': [ perm, 'perm', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_read_symlink(self, path):
        """
        Read the contents of a symlink.
        
        :param path: Path of the symlink file to read.
                The value is expected to begin with /vol/<volumename>.
        """
        return self.request( "file-read-symlink", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'symlink': [ basestring, False ],
        } )
    
    def file_delete_directory(self, path):
        """
        Delete a directory.
        
        :param path: Path of the directory to delete.
                The value is expected to begin with /vol/<volumename>.
                The directory must be empty in order for this API to succeed.
        """
        return self.request( "file-delete-directory", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_write_file(self, path, data, offset, stream_name=None, overwrite=None):
        """
        Write data into a named file.  If the file/stream does
        not previously exist, it will be created -
        the owner of the file will be root and
        it will not be readable or writable by non-root users.
        API will fail if data exceeds 1 MB.
        This API should only be used on normal files or streams
        associated with files.. The results for other file types such as
        LUNs is undefined.
        
        :param path: Pathname of the file to write. For example:
                "/vol/&lt;volume&gt;/&lt;file&gt;".
        
        :param data: Data to be written.  The format of the data is
                ASCII hex characters, two characters representing
                one byte.  Whitespace characters, for convenience in
                formatting, can be present in the value and are ignored.
        
        :param offset: Offset into file at which to start writing.
                If the offset is -1, the data is appended to the file.
                The valid maximum value for (offset + data length) is the
                maximum total file size which is Data ONTAP version and file
                system dependent.
                If the value of the (offset + data length) is beyond the maximum
                total file size, the API will fail with EAPIERROR.
        
        :param stream_name: A stream is an on disk structure which contains a sequence of
                bytes, analogous to a file.  A stream is always associated with
                exactly one file.  Characters that are valid for a file name are
                also valid for the stream-name.  e.g., "meta",
                "resource1".
                Use this option if the data should be written to the named
                stream associated with file specified by &lt;path&gt;
                Default is empty stream name, in which case the data is written
                to file specified by &lt;path&gt;
                This field is available in Data ONTAP 8.2 or later.
        
        :param overwrite: If false, and the file already exists, then the
                API will fail, with an errno of EEXIST.
                This allows the client to ensure that it
                was the exclusive creator of the file.
                The default value is true.
        """
        return self.request( "file-write-file", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'stream_name': [ stream_name, 'stream-name', [ basestring, 'None' ], False ],
            'data': [ data, 'data', [ basestring, 'None' ], False ],
            'overwrite': [ overwrite, 'overwrite', [ bool, 'None' ], False ],
            'offset': [ offset, 'offset', [ int, 'None' ], False ],
        }, {
            'length': [ int, False ],
        } )
    
    def file_usage_get(self, path, length=None, start_offset=None):
        """
        Reports unique bytes held in a file.
        
        :param path: File name to generate report: E.g., /vol/vol1/file1
        
        :param length: Length of the range in bytes. If it is not specified, the range
                that is reported is from start-offset to end-of-file.
                Range : [0..2^63-1].
        
        :param start_offset: Start range of file in bytes. If this is not specified, it is
                assumed to be beginning of file (offset 0).
                Range : [0..2^63-1].
        """
        return self.request( "file-usage-get", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'length': [ length, 'length', [ int, 'None' ], False ],
            'start_offset': [ start_offset, 'start-offset', [ int, 'None' ], False ],
        }, {
            'unique-bytes': [ int, False ],
            'total-bytes': [ int, False ],
        } )
    
    def file_inode_info(self, inode_number, logical_snap_id=None, snap_id=None, report_cifs_paths=None, generation=None, volume_name=None, volume_fsid=None, volume_uuid=None, report_leaf_name=None, snap_name=None, encoded=None, report_parent_data=None, volume_dsid=None, report_no_pathname=None, report_other_parents=None):
        """
        Get parent information for a given inode.
        <p>
        This API corresponds to the "inodepath" diagnostic-level CLI
        in ONTAP-Classic, and has the same defaults.
        </p>
        <p>
        The input is:<ul>
        <li>Required, a volume identifier.  A volume may be specified
        by name, fsid, or (in some ONTAP products) UUID/DSID.</li>
        <li>Required, an inode number.</li>
        <li>Optional, a snapshot identifier to get information from
        a snapshot rather than the active volume.  A snapshot may
        be specified by name or by id.</li>
        <li>Optional, various reporting flags (see below) to enable or
        disable optional output information.</li></ul>
        </p>
        <p>
        The output is:<ul>
        <li>All volume identifiers, the one used as input plus
        the values of the others.</li>
        <li>Optionally, all snapshot identifiers; the one used as
        input plus the value of the other.</li>
        <li>The number of parents for the inode. </li>
        <li>Optionally, one or more volume relative pathnames to the
        inode </li>
        <li>Optionally, one or more leaf names for the inode. </li>
        <li>Optionally, one or more of the actual parent info stored
        for the inode, in the form of the parent dir inode number
        and the parent directory cookie (fbn and offset into the
        fbn) used to find the dir entry that refers to the inode
        in the parent directory (ie. the info used to get the leaf
        name).</li></ul>
        </p>
        
        :param inode_number: The inode number for which information is desired.
        
        :param logical_snap_id: All snapshots are associated with an internal index. "logical-snap-id" is the
                client-visible index that maps the the underlying internal index.
                <p>
                Range: [1..255].
                <p>
        
        :param snap_id: The snapshot number within the given volume in which the
                given inode is to be referenced.  At most, one of snap-id
                or snap-name can be provided.  If neither is provided, we
                reference the given inode within the active file system of
                the given volume.  Valid snapshot ids have a range of 0 to
                (WAFL_SNAP_CNT - 1) (currently 255).  A value of 0 will
                refer to the active file system of the given volume.
                This refers to the physical snapshot identifier.
        
        :param report_cifs_paths: Flag for indicating if the paths returned should be cifs-paths
        
        :param generation: The generation number for this inode.
                <p>
                Range: [1..2^32-1]
        
        :param volume_name: The name of the volume containing the given inode.  Exactly
                one of volume-fsid, volume-name, volume-uuid, or volume-dsid
                must be specified.
        
        :param volume_fsid: The FSID (file system identifier) of the volume containing
                the given inode.  Exactly one of volume-fsid, volume-name,
                volume-uuid, or volume-dsid must be specified.  An FSID may
                have any uint32_t value.
        
        :param volume_uuid: The UUID (Universally Unique IDentifier) of the volume
                containing the given inode.  Exactly one of volume-fsid,
                volume-name, volume-uuid or volume-dsid must be specified.
                <p>
                UUIDs are formatted as 36-character strings.  These strings
                are composed of 32 hexadecimal characters broken up into five
                groupings separated by '-'s.  The first grouping has 8 hex
                characters, the second through fourth groupings have four hex
                characters each, and the fifth and final grouping has 12 hex
                characters.  Note that a leading '0x' is not used.
                <p>
                An example UUID is 532ad684-c8ec-11d9-945f-00065b8c8a1e.
                NOTE: This form of volume identification is only supported
                in some ONTAP products (ONTAP-NG).
        
        :param report_leaf_name: If set to true, report the leaf name of the given inode.  The
                leaf name is equivalent to the final component of a full
                pathname.  For example, the leaf name of:
                <p>
                /vol/vol0/foo/bar/baz
                <br>
                is:
                <br>
                baz
                <p>
                By default, the inode's leaf name is not shown.
        
        :param snap_name: A snapshot name within the given volume in which the given
                inode is to be referenced.  At most, one of snap-id or
                snap-name can be provided.  If neither is provided, we
                reference the given inode within the active file system of
                the given volume.
        
        :param encoded: Specifies if non ASCII characters present in the filename will be hex
                encoded or not. If set to true, then all non-ASCII characters present
                in the filename are transformed to \XX where XX is the hex equivalent
                of the character. For example, if the filename has a non-ASCII
                character whose hex equivalent is 0x5C then the character would be
                encoded as a three byte sequence of '\','5' and 'C' & returned
                as "\5C". By default, the value is false.
        
        :param report_parent_data: If set to true, report various other pieces of information
                about the given inode.  This information includes the inode
                of the parent directory containing the given inode, along
                with the directory cookie by which the given inode is known
                in that parent directory inode.  By default, this other
                information is not reported for the given inode.
        
        :param volume_dsid: The DSID (Data Set IDentifier) of the volume containing the
                given inode.  Exactly one of volume-fsid, volume-name,
                volume-uuid or volume-dsid must be specified.
                <p>
                DSIDs are formatted as 18-character strings composed of 16
                hex characters prefixed with '0x'.
                NOTE: This form of volume identification is only supported
                in some ONTAP products (ONTAP-NG).
        
        :param report_no_pathname: If set to true, do not report on the given inode's full
                pathname.  By default, the inode's full pathname is reported.
        
        :param report_other_parents: If set to true, report the requested information for all of
                the parents for the given inode.  By default, only information
                about one of the given inode's parents is reported.
        """
        return self.request( "file-inode-info", {
            'logical_snap_id': [ logical_snap_id, 'logical-snap-id', [ int, 'None' ], False ],
            'snap_id': [ snap_id, 'snap-id', [ int, 'None' ], False ],
            'report_cifs_paths': [ report_cifs_paths, 'report-cifs-paths', [ bool, 'None' ], False ],
            'generation': [ generation, 'generation', [ int, 'None' ], False ],
            'inode_number': [ inode_number, 'inode-number', [ int, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'volume_fsid': [ volume_fsid, 'volume-fsid', [ int, 'None' ], False ],
            'volume_uuid': [ volume_uuid, 'volume-uuid', [ basestring, 'None' ], False ],
            'report_leaf_name': [ report_leaf_name, 'report-leaf-name', [ bool, 'None' ], False ],
            'snap_name': [ snap_name, 'snap-name', [ basestring, 'None' ], False ],
            'encoded': [ encoded, 'encoded', [ bool, 'None' ], False ],
            'report_parent_data': [ report_parent_data, 'report-parent-data', [ bool, 'None' ], False ],
            'volume_dsid': [ volume_dsid, 'volume-dsid', [ basestring, 'None' ], False ],
            'report_no_pathname': [ report_no_pathname, 'report-no-pathname', [ bool, 'None' ], False ],
            'report_other_parents': [ report_other_parents, 'report-other-parents', [ bool, 'None' ], False ],
        }, {
            'logical-snap-id': [ int, False ],
            'snapshot-id': [ int, False ],
            'volume-name': [ basestring, False ],
            'volume-fsid': [ int, False ],
            'volume-uuid': [ basestring, False ],
            'inode-number': [ int, False ],
            'inode-paths': [ InodeParentInfo, True ],
            'number-of-parents': [ int, False ],
            'volume-dsid': [ basestring, False ],
            'snapshot-name': [ basestring, False ],
        } )
    
    def file_create_symlink(self, path, symlink):
        """
        Create a symlink.
        
        :param path: Path of the symlink file to create.
                The value is expected to begin with /vol/<volumename>.
        
        :param symlink: Value of the symlink.
        """
        return self.request( "file-create-symlink", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'symlink': [ symlink, 'symlink', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_read_file(self, path, length, offset, stream_name=None):
        """
        Read data from a named file.
        API will fail if length exceeds 1 MB.
        This API should only be used on normal files or streams
        associated with files.
        The results for other file types such as LUNs is undefined.
        
        :param path: Name of the file to read. For example:
                "/vol/&lt;volume&gt;/&lt;file&gt;".
        
        :param length: Number of bytes to read from the file.
        
        :param offset: Offset into file to start reading from.
                If the value of offset is beyond the eof, the API will fail
                with EAPIERROR.
        
        :param stream_name: A stream is an on disk structure which contains a sequence of
                bytes, analogous to a file.  A stream is always associated with
                exactly one file.  Characters that are valid for a file name are
                also valid for the stream-name.  e.g., "meta",
                "resource1".
                Use this option if the data should be read from the named stream
                associated with file specified by &lt;path&gt;
                Default is empty stream name, in which case the data is read
                from file specified by &lt;path&gt;
                This field is available in Data ONTAP 8.2 or later.
        """
        return self.request( "file-read-file", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'length': [ length, 'length', [ int, 'None' ], False ],
            'stream_name': [ stream_name, 'stream-name', [ basestring, 'None' ], False ],
            'offset': [ offset, 'offset', [ int, 'None' ], False ],
        }, {
            'length': [ int, False ],
            'data': [ basestring, False ],
        } )
    
    def file_get_fingerprint(self, path, fingerprint_scope=None, fingerprint_algorithm=None):
        """
        Get the fingerprint or digest of a file.
        Fingerprint is calculated using md5 or sha-256 digest algorithm
        depending on the algorithm specified.
        Fingerprint is calculated over the file data or metadata or on
        both data and metadata depending on the scope selected.
        Data fingerprint is calculated over file contents.
        Metadata fingerprint is calculated over the selected attributes
        of the file.
        Attributes used for metadata fingerprint calculations are file
        type (file-type), file size (file-size), file crtime
        (creation-time), file mtime (modified-time), file ctime
        (changed-time), file retention time (retention-time,
        is-wraparound), file uid (owner-id), file gid (group-id).
        File retention time is applicable to worm protected files only.
        The fingerprints are base64 encoded.
        
        :param path: Full path of the file to be fingerprinted.
                The value is expected to begin with /vol/<volumename>.
        
        :param fingerprint_scope: Default value:  "data_and_metadata".
        
        :param fingerprint_algorithm: Default value: "sha-256".
        """
        return self.request( "file-get-fingerprint", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'fingerprint_scope': [ fingerprint_scope, 'fingerprint-scope', [ basestring, 'file-scope' ], False ],
            'fingerprint_algorithm': [ fingerprint_algorithm, 'fingerprint-algorithm', [ basestring, 'digest-algorithm' ], False ],
        }, {
            'fingerprint': [ FingerprintInfo, False ],
        } )
    
    def file_list_directory_iter(self, path, max_records=None, tag=None, desired_attributes=None, query=None):
        """
        list of files in a given directory.
        
        :param path: Pathname of the directory to list.
                The value is expected to begin with /vol/<volumename>.
        
        :param max_records: Maximum number of directory entries to retrieve.
        
        :param tag: Should be empty for first call. For subsequent calls
                should be the value returned by next-tag below.
        
        :param desired_attributes: Specify which attributes to return. If not set
                return all of them.
        
        :param query: not used - here to satisfy smfgen
        """
        return self.request( "file-list-directory-iter", {
            'max_records': max_records,
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FileInfo, 'None' ], True ],
            'query': [ query, 'query', [ FileInfo, 'None' ], True ],
        }, {
            'attributes-list': [ FileInfo, True ],
        } )
    
    def file_delete_file(self, path):
        """
        Delete a file.
        
        :param path: Path of the file or symlink to delete.
                The value is expected to begin with /vol/<volumename>.
        """
        return self.request( "file-delete-file", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_list_directory_iter_start(self, path, encoded=None):
        """
        Start in iteration through the
        list of files in a given directory.
        
        :param path: Pathname of the directory to list.
                The value is expected to begin with /vol/<volumename>.
        
        :param encoded: Specifies if non ASCII characters present in the filename
                will be hex encoded or not. If set to true, then all
                non-ASCII characters present in the filename are transformed
                to \XX where XX is the hex equivalent of the character.
                For example, if the filename has a non-ASCII character whose
                hex equivalent is 0x5C then the character would be encoded
                as a three byte sequence of '\','5' and 'C' & returned as "\5C".
                By default, the value is false.
        """
        return self.request( "file-list-directory-iter-start", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'encoded': [ encoded, 'encoded', [ bool, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def file_truncate_file(self, path, size=None):
        """
        Truncate a file.  Any data past the truncation
        point will be lost, of course.
        
        :param path: Path of the file to truncate.
                The value is expected to begin with /vol/<volumename>.
        
        :param size: If provided, the file size in bytes is set to this value.
                The default value is 0.
        """
        return self.request( "file-truncate-file", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ int, 'None' ], False ],
        }, {
        } )
    
    def file_assign_qos(self, vserver, volume, qos_policy_group_name, file):
        """
        Manage the association of QoS policy group to a specified file.
        QoS Policy groups define measurable Service Level Objectives
        (SLOs) that apply to the storage object with which the policy
        group is associated. In Data ONTAP 8.2 hierarchical QoS is not
        supported i.e. QoS policy groups cannot be assigned to multiple
        objects in the file's storage hierarchy - such as the parent LUN,
        volume or Vserver.
        
        :param vserver: Name of the Vserver in which the volume that hosts the file
                resides.
        
        :param volume: Name of the Volume in which the file resides.
        
        :param qos_policy_group_name: The QoS Policy Group Name that is to be associated with this
                file in order to enforce Service Level Objectives (SLO). NOTE:
                none is a reserved keyword for deleting the association of the
                file with a QoS policy group.
        
        :param file: Complete file path of the file without a trailing slash.
        """
        return self.request( "file-assign-qos", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'qos_policy_group_name': [ qos_policy_group_name, 'qos-policy-group-name', [ basestring, 'None' ], False ],
            'file': [ file, 'file', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_usage_start(self, path, length=None, start_offset=None):
        """
        Starts a background job to compute unique bytes held
        in a file. The result can be obtained by passing the
        cookie to file-usage-result-get call.
        
        :param path: File name to generate report: E.g., /vol/vol1/file1
        
        :param length: Length of the range in bytes. If it is not specified, the range
                that is reported is from start-offset to end-of-file.
                Range : [0..2^63-1].
        
        :param start_offset: Start range of file in bytes. If this is not specified, it is
                assumed to be beginning of file (offset 0).
                Range : [0..2^63-1].
        """
        return self.request( "file-usage-start", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'length': [ length, 'length', [ int, 'None' ], False ],
            'start_offset': [ start_offset, 'start-offset', [ int, 'None' ], False ],
        }, {
            'cookie': [ basestring, False ],
        } )
    
    def file_punch_hole(self, path, hole_info):
        """
        Punch hole in the file. Hole punching involves reclaiming of
        blocks in a file by unallocating them and then direct or
        indirect blocks can be made to point to 0.
        
        :param path: Path of the file. Format must be of the following:
                /vol/my_vol/path-to-file
        
        :param hole_info: This is the array containing the ranges that need to be
                hole punched. Punching up to 16 holes is supported.
        """
        return self.request( "file-punch-hole", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'hole_info': [ hole_info, 'hole-info', [ HoleRangeInfo, 'None' ], True ],
        }, {
        } )
    
    def file_copy_destroy(self, file_index, job_uuid):
        """
        Destroy an incomplete file copy operation.
        
        :param file_index: An additional unique element identifying one file among many that
                could be possibly copied as part of a job. For file copy
                operations that involve only one file, the file-index value of
                zero is always correct.
        
        :param job_uuid: The UUID which uniquely identifies the job that started this copy
                operation.
        """
        return self.request( "file-copy-destroy", {
            'file_index': [ file_index, 'file-index', [ int, 'None' ], False ],
            'job_uuid': [ job_uuid, 'job-uuid', [ basestring, 'uuid' ], False ],
        }, {
        } )
    
    def file_hole_range_query(self, path, length, offset):
        """
        Returns an array of holes in a file for a given range. Each
        array contains the starting offset and length of the hole.
        
        :param path: The full path of the file for which hole information is to be
                queried. Format must be of the following: /vol/my_vol/my_file
        
        :param length: The number of bytes to scan. If this is zero, scan until end
                of file. If the length is not an integral multiple of the block
                size it will be rounded up to the end of the block. Note that
                if the offset is modified the length will be adjusted to compensate.
        
        :param offset: The starting offset of the file from where the scan for holes
                should begin. If the offset is not an integral multiple of
                the block size it will be rounded down to the start of the block.
        """
        return self.request( "file-hole-range-query", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'length': [ length, 'length', [ int, 'None' ], False ],
            'offset': [ offset, 'offset', [ int, 'None' ], False ],
        }, {
            'next-offset': [ int, False ],
            'hole-info': [ HoleRangeInfo, True ],
        } )

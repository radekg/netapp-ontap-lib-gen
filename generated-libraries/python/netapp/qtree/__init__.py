from netapp.connection import NaConnection
from qtree_list_iter_key_td import QtreeListIterKeyTd # 2 properties
from qtree_path import QtreePath # 0 properties
from unix_perm import UnixPerm # 0 properties
from qtree_info import QtreeInfo # 10 properties

class QtreeConnection(NaConnection):
    
    def qtree_prepare_for_downgrade(self):
        """
        auto generated : Disable qtree exports
        """
        return self.request( "qtree-prepare-for-downgrade", {
        }, {
        } )
    
    def qtree_rename(self, qtree, new_qtree_name):
        """
        Renames the specified qtree to a new name specified by
        "new-qtree-name".
        <p>
        For unclustered volumes, if the qtree is referenced in the file
        /etc/exportfs, use NFS API nfs-exportfs-append-rules to modify
        the file so that the affected file system can be exported by the
        filer immediately.  The "qtree-rename" command does not
        automatically update the /etc/exports file.  Also, if the qtree
        is referenced in the file /etc/quotas, use the quota management
        APIs to delete and re-create the quota rule with the new qtree
        name.
        <p>
        For clustered volumes, the qtree name in the quota rules will be
        automatically updated with the new qtree name.
        
        :param qtree: Path of an existing qtree. The path should be
                in this format: /vol/< volume name >/< src qtree name >.
        
        :param new_qtree_name: Path of new qtree. The path should be in
                this format: /vol/< volume name >/< dst qtree name >.
        """
        return self.request( "qtree-rename", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'new_qtree_name': [ new_qtree_name, 'new-qtree-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def qtree_delete_async(self, qtree, force=None):
        """
        Delete the specified qtree by spawning a background job.
        The jobid will be returned. The progress of the job can be
        tracked using the job APIs. All the quota rules that reference
        this qtree will be automatically deleted.
        
        :param qtree: Path of an existing qtree. The path should be
                in this format: /vol/< volume name >/< qtree name >.
        
        :param force: Force the deletion of the qtree even if it not empty.
                Default: false
        """
        return self.request( "qtree-delete-async", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def qtree_delete(self, qtree, force=None):
        """
        Delete the specified qtree.
        <p>
        For unclustered volumes, use the quota management APIs to delete
        the quota rules that reference this qtree in the /etc/quotas
        file.
        <p>
        For clustered volumes, all the quota rules that reference this
        qtree will be automatically deleted.
        
        :param qtree: Path of an existing qtree. The path should be
                in this format: /vol/< volume name >/< qtree name >.
        
        :param force: Force the deletion of the qtree even if it not
                empty. On using "force" option, ZAPI may
                take a long time to complete because the contents of
                the entire qtree will have to be deleted before it returns.
                Default: false
                <p>
                For clustered volumes, if the qtree has a large number of files,
                it is recommended that the qtree-delete-async API be used.
        """
        return self.request( "qtree-delete", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def qtree_list(self, volume=None):
        """
        Return list of qtrees
        
        :param volume: Name of the volume to be queried.
                Do not include a "/vol/" prefix.
        """
        return self.request( "qtree-list", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'qtrees': [ QtreeInfo, True ],
        } )
    
    def qtree_list_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of qtrees in the cluster.
        
        :param max_records: The maximum number of records to return in this response.
        
        :param query: A query that specifies which qtrees need to be returned.
                A query could be specified on any number of attributes in the
                qtree-info object. All qtree objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the previous iteration.
                It is usually not specified for the first iteration. For subsequent
                iterations, copy the value from the 'next-tag' obtained from the previous
                iteration.
        
        :param desired_attributes: Specify the attributes that should be returned in the qtree-info
                object. If not present, all attributes for which information is
                available will be returned. If present, only the desired attributes
                for which information is available will be returned.
        """
        return self.request( "qtree-list-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ QtreeInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QtreeInfo, 'None' ], False ],
        }, {
            'attributes-list': [ QtreeInfo, True ],
        } )
    
    def qtree_list_iter_next(self, tag, maximum):
        """
        Continues an iteration through the list of qtrees
        
        :param tag: Tag from a previous qtree-list-iter-start.
        
        :param maximum: The maximum number of qtrees to retrieve.
        """
        return self.request( "qtree-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'qtrees': [ QtreeInfo, True ],
        } )
    
    def qtree_list_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous qtree-list-iter-start.
        """
        return self.request( "qtree-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def qtree_modify(self, qtree, volume, export_policy=None, security_style=None, oplocks=None, mode=None):
        """
        Modify the attributes of a qtree. If values are not provided
        for any of the fields, then that field will not be modified.
        
        :param qtree: Name of the qtree.
        
        :param volume: Name of the volume containing the qtree to be modified.
        
        :param export_policy: Export policy of the qtree. If empty string, the qtree will
                inherit the export policy of the parent volume.
        
        :param security_style: Security style of the qtree.
                Possible values: "unix", "ntfs", or "mixed".
                Changing the security style of a qtree will change the visibility
                of existing Windows security descriptors (i.e. ACLs). This may
                affect the disk space usage values in the quota database.
                Turn quotas off and then on to re-compute disk space usage.
        
        :param oplocks: Opportunistic locks mode of the qtree.
                Possible values: "enabled", "disabled".
        
        :param mode: The file permission bits of the qtree.
                Similar to UNIX permission bits: 0755 gives read/write/execute
                permissions to owner and read/execute to group and other users.
                It consists of 4 octal digits derived by adding up
                bits 4, 2, and 1.
                Omitted digits are assumed to be zeros.
                First digit selects the set user ID (4), set group ID (2), and
                sticky (1) attributes. The second digit selects permissions for
                the owner of the file: read (4), write (2), and execute (1);
                the third selects permissions for other users in the same group;
                the fourth for other users not in the group.
        """
        return self.request( "qtree-modify", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'export_policy': [ export_policy, 'export-policy', [ basestring, 'None' ], False ],
            'security_style': [ security_style, 'security-style', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'oplocks': [ oplocks, 'oplocks', [ basestring, 'None' ], False ],
            'mode': [ mode, 'mode', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def qtree_list_iter_start(self):
        """
        Starts an iteration through the list of qtrees.
        """
        return self.request( "qtree-list-iter-start", {
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def qtree_create(self, qtree, volume, export_policy=None, security_style=None, oplocks=None, mode=None):
        """
        Create a new qtree.
        
        :param qtree: The path of the qtree, relative to the volume.
        
        :param volume: Name of the volume on which to create the qtree
        
        :param export_policy: Export policy of the qtree.
                If this input is not specified, the qtree will inherit
                the export policy of the parent volume.
        
        :param security_style: Security style of the qtree.
                Possible values: "unix", "ntfs", or "mixed".
                Default value is the security style of the volume.
        
        :param oplocks: Opportunistic locks mode of the qtree.
                Possible values: "enabled", "disabled".
                Default value is the oplock mode of the volume.
        
        :param mode: The file permission bits of the qtree.
                Similar to UNIX permission bits: 0755 gives read/write/execute
                permissions to owner and read/execute to group and other users.
                It consists of 4 octal digits derived by adding up
                bits 4, 2, and 1.
                Omitted digits are assumed to be zeros.
                First digit selects the set user ID (4), set group ID (2), and
                sticky (1) attributes. The second digit selects permissions for
                the owner of the file: read (4), write (2), and execute (1);
                the third selects permissions for other users in the same group;
                the fourth for other users not in the group.
                <p>
                For unclustered volumes, if this argument is missing, use the
                value specified in the option "wafl.default_qtree_mode".
                <p>
                For clustered volumes, if this argument is missing, the
                permissions of the volume is used.
        """
        return self.request( "qtree-create", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'export_policy': [ export_policy, 'export-policy', [ basestring, 'None' ], False ],
            'security_style': [ security_style, 'security-style', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'oplocks': [ oplocks, 'oplocks', [ basestring, 'None' ], False ],
            'mode': [ mode, 'mode', [ basestring, 'None' ], False ],
        }, {
        } )

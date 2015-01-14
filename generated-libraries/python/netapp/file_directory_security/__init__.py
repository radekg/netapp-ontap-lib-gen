from netapp.connection import NaConnection
from access_rights import AccessRights # 0 properties
from security_type import SecurityType # 0 properties
from file_directory_security_policy_get_iter_key_td import FileDirectorySecurityPolicyGetIterKeyTd # 2 properties
from name_or_sid import NameOrSid # 0 properties
from file_directory_security_policy import FileDirectorySecurityPolicy # 2 properties
from fsecurity_acl import FsecurityAcl # 0 properties
from audit_access_type import AuditAccessType # 0 properties
from file_directory_security_ntfs_dacl import FileDirectorySecurityNtfsDacl # 9 properties
from file_directory_security_policy_task_get_iter_key_td import FileDirectorySecurityPolicyTaskGetIterKeyTd # 4 properties
from file_directory_security_ntfs_get_iter_key_td import FileDirectorySecurityNtfsGetIterKeyTd # 2 properties
from file_directory_security_ntfs_dacl_get_iter_key_td import FileDirectorySecurityNtfsDaclGetIterKeyTd # 4 properties
from ntfs_propagation_mode import NtfsPropagationMode # 0 properties
from file_directory_security_ntfs_sacl import FileDirectorySecurityNtfsSacl # 9 properties
from fsecurity_ntfs_sd import FsecurityNtfsSd # 0 properties
from inheritance_level import InheritanceLevel # 0 properties
from file_directory_security_ntfs import FileDirectorySecurityNtfs # 5 properties
from file_directory_security_ntfs_sacl_get_iter_key_td import FileDirectorySecurityNtfsSaclGetIterKeyTd # 4 properties
from access_type import AccessType # 0 properties
from fsecurity_policy_name import FsecurityPolicyName # 0 properties
from advanced_access_rights import AdvancedAccessRights # 0 properties
from file_directory_security_policy_task import FileDirectorySecurityPolicyTask # 7 properties
from cifs_share_name import CifsShareName # 0 properties

class FileDirectorySecurityConnection(NaConnection):
    
    def file_directory_security_set(self, policy_name):
        """
        Apply security descriptors on files and directories defined in a
        policy to a Vserver
        
        :param policy_name: Specifies the name of the policy whose security settings have to
                be applied.
        """
        return self.request( "file-directory-security-set", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'fsecurity-policy-name' ], False ],
        }, {
        } )
    
    def file_directory_security_policy_delete(self, policy_name):
        """
        Deletes a file/folder security policy. To preserve the security
        configuration of a file(or, folder) or set of files(or, folders)
        security policy has been defined. Policy is a container for tasks
        and a task associates a file/folder path name and the security
        descriptor that needs to be set on the file/folder. Every task in
        a policy is uniquely identified by the file/folder path. Policy
        can't have duplicate task entries and there is only one task per
        path.
        
        :param policy_name: Specifies the name of the policy. To preserve the security
                configuration of a file(or, folder) or set of files(or, folders)
                security policy has been defined. Policy is a container for tasks
                and a task associates a file/folder path name and the security
                descriptor that needs to be set on the file/folder. Every task in
                a policy is uniquely identified by the file/folder path. Policy
                can't have duplicate task entries and there is only one task per
                path.
        """
        return self.request( "file-directory-security-policy-delete", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'fsecurity-policy-name' ], False ],
        }, {
        } )
    
    def file_directory_security_policy_create(self, policy_name, return_record=None):
        """
        Creates a new file/folder security policy configuration. To
        preserve the security configuration of a file(or, folder) or set
        of files(or, folders) security policy has been defined. Policy is
        a container for tasks and a task associates a file/folder path
        name and the security descriptor that needs to be set on the
        file/folder. Every task in a policy is uniquely identified by the
        file/folder path. Policy can't have duplicate task entries and
        there is only one task per path.
        
        :param policy_name: Specifies the name of the policy. To preserve the security
                configuration of a file(or, folder) or set of files(or, folders)
                security policy has been defined. Policy is a container for tasks
                and a task associates a file/folder path name and the security
                descriptor that needs to be set on the file/folder. Every task in
                a policy is uniquely identified by the file/folder path. Policy
                can't have duplicate task entries and there is only one task per
                path.
        
        :param return_record: If set to true, returns the file-directory-security-policy on
                successful creation.
                Default: false
        """
        return self.request( "file-directory-security-policy-create", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'fsecurity-policy-name' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ FileDirectorySecurityPolicy, False ],
        } )
    
    def file_directory_security_ntfs_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns information about one or more NTFS security descriptor
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                file-directory-security-ntfs object.
                All file-directory-security-ntfs objects matching this query up
                to 'max-records' will be returned.
        
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
        return self.request( "file-directory-security-ntfs-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FileDirectorySecurityNtfs, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FileDirectorySecurityNtfs, 'None' ], False ],
        }, {
            'attributes-list': [ FileDirectorySecurityNtfs, True ],
        } )
    
    def file_directory_security_policy_task_add(self, policy_name, path, ntfs_mode=None, task_index_number=None, ntfs_sd=None, security_type=None):
        """
        Add a file security policy task. A task maps security descriptor
        with a file or folder.
        
        :param policy_name: Specifies the name of the policy to which the task needs to be
                added.
        
        :param path: Specifies the file or folder path of the task.
        
        :param ntfs_mode: Specifies NTFS propagation mode.
                Possible values:
                <ul>
                <li> "propagate" ,
                <li> "ignore"    ,
                <li> "replace"
                </ul>
        
        :param task_index_number: Specifies the target index/position of this task in the policy.
                If a policy has already 5 tasks and this is the 6th task you are
                adding and you want to add this task as 2nd task, you can
                specifiy the index 2. By default the task gets added as last
                task. If the index number exceeds the number of positions, it
                will go at the end.
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param security_type: Specifies the type of security.
                Possible values:
                <ul>
                <li> "ntfs"      ,
                <li> "nfsv4"
                </ul>
        """
        return self.request( "file-directory-security-policy-task-add", {
            'ntfs_mode': [ ntfs_mode, 'ntfs-mode', [ basestring, 'ntfs-propagation-mode' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'fsecurity-policy-name' ], False ],
            'task_index_number': [ task_index_number, 'task-index-number', [ int, 'None' ], False ],
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'security_type': [ security_type, 'security-type', [ basestring, 'security-type' ], False ],
        }, {
        } )
    
    def file_directory_security_ntfs_dacl_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns information about one or more discretionary access
        control entries
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                file-directory-security-ntfs-dacl object.
                All file-directory-security-ntfs-dacl objects matching this query
                up to 'max-records' will be returned.
        
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
        return self.request( "file-directory-security-ntfs-dacl-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FileDirectorySecurityNtfsDacl, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FileDirectorySecurityNtfsDacl, 'None' ], False ],
        }, {
            'attributes-list': [ FileDirectorySecurityNtfsDacl, True ],
        } )
    
    def file_directory_security_ntfs_sacl_add(self, account, ntfs_sd, audit_access_type, advanced_rights=None, rights_raw=None, rights=None, apply_to=None):
        """
        Add a system/audit access control entry to NTFS security
        descriptor.
        
        :param account: Specifies SACL ACE's SID or domain account name of NTFS security
                descriptor.
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param audit_access_type: Specifies SACL ACE's access type.
                Possible values:
                <ul>
                <li> "failure"   ,
                <li> "success"
                </ul>
        
        :param advanced_rights: Specifies SACL ACE's access rights. Mutually exclusive with
                rights-raw field.
                Possible values:
                <ul>
                <li> "read_data"      ,
                <li> "write_data"     ,
                <li> "append_data"    ,
                <li> "read_ea"        ,
                <li> "write_ea"       ,
                <li> "execute_file"   ,
                <li> "delete_child"   ,
                <li> "read_attr"      ,
                <li> "write_attr"     ,
                <li> "delete"         ,
                <li> "read_perm"      ,
                <li> "write_perm"     ,
                <li> "write_owner"    ,
                <li> "full_control"
                </ul>
        
        :param rights_raw: Specifies SACL ACE's access rights in raw. This field is similar
                to advanced-rights fields. 'advanced-rights' specifies the value
                in enum but rights-raw specifies the access rights in integer
                format. Mutually exclusive with rights and advanced-rights
                fields.
        
        :param rights: Specifies SACL ACE's access rights.
                Possible values:
                <ul>
                <li> "no_access"           ,
                <li> "full_control"        ,
                <li> "modify"              ,
                <li> "read_and_execute"    ,
                <li> "read"                ,
                <li> "write"
                </ul>
        
        :param apply_to: Specifies how this ACE has to be applied on this folder and it's
                subfolders and files. This field is ignored if the security is
                mapped with a path which is not a folder.
                Possible values:
                <ul>
                <li> "this_folder"    ,
                <li> "sub_folders"    ,
                <li> "files"
                </ul>
        """
        return self.request( "file-directory-security-ntfs-sacl-add", {
            'advanced_rights': [ advanced_rights, 'advanced-rights', [ basestring, 'advanced-access-rights' ], True ],
            'account': [ account, 'account', [ basestring, 'name-or-sid' ], False ],
            'rights_raw': [ rights_raw, 'rights-raw', [ int, 'None' ], False ],
            'rights': [ rights, 'rights', [ basestring, 'access-rights' ], False ],
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'audit_access_type': [ audit_access_type, 'audit-access-type', [ basestring, 'audit-access-type' ], False ],
            'apply_to': [ apply_to, 'apply-to', [ basestring, 'inheritance-level' ], True ],
        }, {
        } )
    
    def file_directory_security_get(self, path, cifs_share_name=None, expand_mask=None, lookup_names=None, volume_name=None):
        """
        Returns security information of a file/folder
        
        :param path: Specifies the file or folder path whose security information
                needs to be read. If volume-name or cifs-share-name is not
                specified, path name lookup starts from the root path of the
                vserver
        
        :param cifs_share_name: Specifies that the given path name lookup starts from cifs share
                map path. Mutually exclusive with volume-name field.
        
        :param expand_mask: Specifies whether to expand the bit mask of DOS attributes,
                security descriptor's control flags and every ACE.
        
        :param lookup_names: Specifies whether the SID needs to be converted to user/group
                name.
        
        :param volume_name: Specifies that the given path name lookup starts from volume
                junction path. Mutually exclusive with cifs-share-name field.
        """
        return self.request( "file-directory-security-get", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'cifs_share_name': [ cifs_share_name, 'cifs-share-name', [ basestring, 'cifs-share-name' ], False ],
            'expand_mask': [ expand_mask, 'expand-mask', [ bool, 'None' ], False ],
            'lookup_names': [ lookup_names, 'lookup-names', [ bool, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'volume-name' ], False ],
        }, {
            'security-style': [ basestring, False ],
            'unix-mode-bits': [ int, False ],
            'dos-attributes': [ int, False ],
            'expanded-dos-attr': [ basestring, False ],
            'effective-style': [ basestring, False ],
            'acls': [ basestring, True ],
            'unix-user-id': [ int, False ],
            'text-dos-attr': [ basestring, False ],
            'unix-group-id': [ int, False ],
        } )
    
    def file_directory_security_ntfs_sacl_remove(self, ntfs_sd, audit_access_type, account):
        """
        Remove an system/audit access control entry from NTFS security
        descriptor.
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param audit_access_type: Specifies SACL ACE's access type.
                Possible values:
                <ul>
                <li> "failure"   ,
                <li> "success"
                </ul>
        
        :param account: Specifies SACL ACE's SID or domain account name of NTFS security
                descriptor.
        """
        return self.request( "file-directory-security-ntfs-sacl-remove", {
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'audit_access_type': [ audit_access_type, 'audit-access-type', [ basestring, 'audit-access-type' ], False ],
            'account': [ account, 'account', [ basestring, 'name-or-sid' ], False ],
        }, {
        } )
    
    def file_directory_security_ntfs_modify(self, ntfs_sd, owner=None, group=None, control_flags_raw=None):
        """
        Modifies an NTFS security descriptor
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param owner: Specifies owner's SID or domain account name of NTFS security
                descriptor.
        
        :param group: Specifies group's SID or domain account name of NTFS security
                descriptor.
        
        :param control_flags_raw: Specifies the security descriptor control flags in hexa decimal.
                The following are the bit fields of control flags.
                <br>1... .... .... .... = Self Relative
                <br>.0.. .... .... .... = RM Control Valid
                <br>..0. .... .... .... = SACL Protected
                <br>...0 .... .... .... = DACL Protected
                <br>.... 0... .... .... = SACL Inherited
                <br>.... .0.. .... .... = DACL Inherited
                <br>.... ..0. .... .... = SACL Inherit Required
                <br>.... ...0 .... .... = DACL Inherit Required
                <br>.... .... ..0. .... = SACL Defaulted
                <br>.... .... ...0 .... = SACL Present
                <br>.... .... .... 0... = DACL Defaulted
                <br>.... .... .... .1.. = DACL Present
                <br>.... .... .... ..0. = Group Defaulted
                <br>.... .... .... ...0 = Owner Defaulted
                <br>
                <br>At present only the following flags are honored. Others
                are ignored.
                <br>..0. .... .... .... = SACL Protected
                <br>...0 .... .... .... = DACL Protected
                <br>.... .... ..0. .... = SACL Defaulted
                <br>.... .... .... 0... = DACL Defaulted
                <br>.... .... .... ..0. = Group Defaulted
                <br>.... .... .... ...0 = Owner Defaulted
        """
        return self.request( "file-directory-security-ntfs-modify", {
            'owner': [ owner, 'owner', [ basestring, 'name-or-sid' ], False ],
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'group': [ group, 'group', [ basestring, 'name-or-sid' ], False ],
            'control_flags_raw': [ control_flags_raw, 'control-flags-raw', [ int, 'None' ], False ],
        }, {
        } )
    
    def file_directory_security_ntfs_delete(self, ntfs_sd):
        """
        Deletes an NTFS security descriptor information
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        """
        return self.request( "file-directory-security-ntfs-delete", {
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
        }, {
        } )
    
    def file_directory_security_ntfs_dacl_modify(self, account, ntfs_sd, access_type, advanced_rights=None, rights_raw=None, rights=None, apply_to=None):
        """
        Modify an discretionary access control entry of a file security
        descriptor
        
        :param account: Specifies DACL ACE's SID or domain account name of NTFS security
                descriptor.
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param access_type: Specifies DACL ACE's access type.
                Possible values:
                <ul>
                <li> "deny"      ,
                <li> "allow"
                </ul>
        
        :param advanced_rights: Specifies DACL ACE's Advanced access rights. Mutually exclusive
                with rights and rights-raw fields.
                Possible values:
                <ul>
                <li> "read_data"      ,
                <li> "write_data"     ,
                <li> "append_data"    ,
                <li> "read_ea"        ,
                <li> "write_ea"       ,
                <li> "execute_file"   ,
                <li> "delete_child"   ,
                <li> "read_attr"      ,
                <li> "write_attr"     ,
                <li> "delete"         ,
                <li> "read_perm"      ,
                <li> "write_perm"     ,
                <li> "write_owner"    ,
                <li> "full_control"
                </ul>
        
        :param rights_raw: Specifies DACL ACE's access rights in raw. This field is similar
                to advanced-rights fields. 'advanced-rights' specifies the value
                in enum but rights-raw specifies the access rights in integer
                format. Mutually exclusive with rights and advanced-rights
                fields.
        
        :param rights: Specifies DACL ACE's access rights. Mutually exclusive with
                advanced-rights and rights-raw fields.
                Possible values:
                <ul>
                <li> "no_access"           ,
                <li> "full_control"        ,
                <li> "modify"              ,
                <li> "read_and_execute"    ,
                <li> "read"                ,
                <li> "write"
                </ul>
        
        :param apply_to: Specifies this ACE has to be applied on.
                Possible values:
                <ul>
                <li> "this_folder"    ,
                <li> "sub_folders"    ,
                <li> "files"
                </ul>
        """
        return self.request( "file-directory-security-ntfs-dacl-modify", {
            'advanced_rights': [ advanced_rights, 'advanced-rights', [ basestring, 'advanced-access-rights' ], True ],
            'account': [ account, 'account', [ basestring, 'name-or-sid' ], False ],
            'rights_raw': [ rights_raw, 'rights-raw', [ int, 'None' ], False ],
            'rights': [ rights, 'rights', [ basestring, 'access-rights' ], False ],
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'apply_to': [ apply_to, 'apply-to', [ basestring, 'inheritance-level' ], True ],
            'access_type': [ access_type, 'access-type', [ basestring, 'access-type' ], False ],
        }, {
        } )
    
    def file_directory_security_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns information about one or more security policies. To
        preserve the security configuration of a file(or, folder) or set
        of files(or, folders) security policy has been defined. Policy is
        a container for tasks and a task associates a file/folder path
        name and the security descriptor that needs to be set on the
        file/folder. Every task in a policy is uniquely identified by the
        file/folder path. Policy can't have duplicate task entries and
        there is only one task per path.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                file-directory-security-policy object.
                All file-directory-security-policy objects matching this query up
                to 'max-records' will be returned.
        
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
        return self.request( "file-directory-security-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FileDirectorySecurityPolicy, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FileDirectorySecurityPolicy, 'None' ], False ],
        }, {
            'attributes-list': [ FileDirectorySecurityPolicy, True ],
        } )
    
    def file_directory_security_policy_task_modify(self, policy_name, path, ntfs_mode=None, task_index_number=None, ntfs_sd=None, security_type=None):
        """
        Modify a file security policy task
        
        :param policy_name: Specifies the name of the policy who has the task.
        
        :param path: Specifies the file or folder path of a task.
        
        :param ntfs_mode: Specifies the NTFS propagation mode.
                Possible values:
                <ul>
                <li> "propagate" ,
                <li> "ignore"    ,
                <li> "replace"
                </ul>
        
        :param task_index_number: Specifies the target index/position of this task in the policy.
                If the task is currently placed in 5th position in a policy and
                you want to reorder this task as 2nd task, you can set the
                index-num to 2. If the index number exceeds the number of
                positions, it will go at the end.
        
        :param ntfs_sd: Specifies the NTFS security descriptor identifier.
        
        :param security_type: Specifies the type of security.
                Possible values:
                <ul>
                <li> "ntfs"      ,
                <li> "nfsv4"
                </ul>
        """
        return self.request( "file-directory-security-policy-task-modify", {
            'ntfs_mode': [ ntfs_mode, 'ntfs-mode', [ basestring, 'ntfs-propagation-mode' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'fsecurity-policy-name' ], False ],
            'task_index_number': [ task_index_number, 'task-index-number', [ int, 'None' ], False ],
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'security_type': [ security_type, 'security-type', [ basestring, 'security-type' ], False ],
        }, {
        } )
    
    def file_directory_security_policy_task_remove(self, policy_name, path):
        """
        Remove a task from the policy of a vserver.
        
        :param policy_name: Specifies the name of the policy from which the task has been
                removed.
        
        :param path: Specifies the file or folder path of the task.
        """
        return self.request( "file-directory-security-policy-task-remove", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'fsecurity-policy-name' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def file_directory_security_ntfs_dacl_remove(self, ntfs_sd, access_type, account):
        """
        Remove a discretionary access control entry from NTFS security
        descriptor.
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param access_type: Specifies DACL ACE's access type.
                Possible values:
                <ul>
                <li> "deny"      ,
                <li> "allow"
                </ul>
        
        :param account: Specifies DACL ACE's SID or domain account name of NTFS security
                descriptor.
        """
        return self.request( "file-directory-security-ntfs-dacl-remove", {
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'access_type': [ access_type, 'access-type', [ basestring, 'access-type' ], False ],
            'account': [ account, 'account', [ basestring, 'name-or-sid' ], False ],
        }, {
        } )
    
    def file_directory_security_ntfs_dacl_add(self, account, ntfs_sd, access_type, advanced_rights=None, rights_raw=None, rights=None, apply_to=None):
        """
        Add a discretionary access control entry to NTFS security
        descriptor.
        
        :param account: Specifies DACL ACE's SID or domain account name of NTFS security
                descriptor.
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param access_type: Specifies DACL ACE's access type.
                Possible values:
                <ul>
                <li> "deny"      ,
                <li> "allow"
                </ul>
        
        :param advanced_rights: Specifies DACL ACE's Advanced access rights. Mutually exclusive
                with rights and rights-raw fields.
                Possible values:
                <ul>
                <li> "read_data"      ,
                <li> "write_data"     ,
                <li> "append_data"    ,
                <li> "read_ea"        ,
                <li> "write_ea"       ,
                <li> "execute_file"   ,
                <li> "delete_child"   ,
                <li> "read_attr"      ,
                <li> "write_attr"     ,
                <li> "delete"         ,
                <li> "read_perm"      ,
                <li> "write_perm"     ,
                <li> "write_owner"    ,
                <li> "full_control"
                </ul>
        
        :param rights_raw: Specifies DACL ACE's access rights in raw. This field is similar
                to advanced-rights fields. 'advanced-rights' specifies the value
                in enum but rights-raw specifies the access rights in integer
                format. Mutually exclusive with rights and advanced-rights
                fields.
        
        :param rights: Specifies DACL ACE's access rights. Mutually exclusive with
                advanced-rights and rights-raw fields.
                Possible values:
                <ul>
                <li> "no_access"           ,
                <li> "full_control"        ,
                <li> "modify"              ,
                <li> "read_and_execute"    ,
                <li> "read"                ,
                <li> "write"
                </ul>
        
        :param apply_to: Specifies apply DACL entry.
                Possible values:
                <ul>
                <li> "this_folder"    ,
                <li> "sub_folders"    ,
                <li> "files"
                </ul>
        """
        return self.request( "file-directory-security-ntfs-dacl-add", {
            'advanced_rights': [ advanced_rights, 'advanced-rights', [ basestring, 'advanced-access-rights' ], True ],
            'account': [ account, 'account', [ basestring, 'name-or-sid' ], False ],
            'rights_raw': [ rights_raw, 'rights-raw', [ int, 'None' ], False ],
            'rights': [ rights, 'rights', [ basestring, 'access-rights' ], False ],
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'apply_to': [ apply_to, 'apply-to', [ basestring, 'inheritance-level' ], True ],
            'access_type': [ access_type, 'access-type', [ basestring, 'access-type' ], False ],
        }, {
        } )
    
    def file_directory_security_ntfs_create(self, ntfs_sd, owner=None, group=None, control_flags_raw=None, return_record=None):
        """
        Creates a new NTFS security descriptor
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param owner: Specifies owner's SID or domain account name of NTFS security
                descriptor.
        
        :param group: Specifies group's SID or domain account name of NTFS security
                descriptor.
        
        :param control_flags_raw: Specifies the security descriptor control flags in hexa decimal.
                The following are the bit fields of control flags.
                <br>1... .... .... .... = Self Relative
                <br>.0.. .... .... .... = RM Control Valid
                <br>..0. .... .... .... = SACL Protected
                <br>...0 .... .... .... = DACL Protected
                <br>.... 0... .... .... = SACL Inherited
                <br>.... .0.. .... .... = DACL Inherited
                <br>.... ..0. .... .... = SACL Inherit Required
                <br>.... ...0 .... .... = DACL Inherit Required
                <br>.... .... ..0. .... = SACL Defaulted
                <br>.... .... ...0 .... = SACL Present
                <br>.... .... .... 0... = DACL Defaulted
                <br>.... .... .... .1.. = DACL Present
                <br>.... .... .... ..0. = Group Defaulted
                <br>.... .... .... ...0 = Owner Defaulted
                <br>
                <br>At present only the following flags are honored. Others
                are ignored.
                <br>..0. .... .... .... = SACL Protected
                <br>...0 .... .... .... = DACL Protected
                <br>.... .... ..0. .... = SACL Defaulted
                <br>.... .... .... 0... = DACL Defaulted
                <br>.... .... .... ..0. = Group Defaulted
                <br>.... .... .... ...0 = Owner Defaulted
        
        :param return_record: If set to true, returns the file-directory-security-ntfs on
                successful creation.
                Default: false
        """
        return self.request( "file-directory-security-ntfs-create", {
            'owner': [ owner, 'owner', [ basestring, 'name-or-sid' ], False ],
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'group': [ group, 'group', [ basestring, 'name-or-sid' ], False ],
            'control_flags_raw': [ control_flags_raw, 'control-flags-raw', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ FileDirectorySecurityNtfs, False ],
        } )
    
    def file_directory_security_ntfs_sacl_modify(self, account, ntfs_sd, audit_access_type, advanced_rights=None, rights_raw=None, rights=None, apply_to=None):
        """
        Modify an system/audit access control entry of a file security
        descriptor
        
        :param account: Specifies SACL ACE's SID or domain account name of NTFS security
                descriptor.
        
        :param ntfs_sd: Specifies NTFS security descriptor identifier.
        
        :param audit_access_type: Specifies SACL ACE's access type.
                Possible values:
                <ul>
                <li> "failure"   ,
                <li> "success"
                </ul>
        
        :param advanced_rights: Specifies SACL ACE's access rights. Mutually exclusive with
                rights-raw field.
                Possible values:
                <ul>
                <li> "read_data"      ,
                <li> "write_data"     ,
                <li> "append_data"    ,
                <li> "read_ea"        ,
                <li> "write_ea"       ,
                <li> "execute_file"   ,
                <li> "delete_child"   ,
                <li> "read_attr"      ,
                <li> "write_attr"     ,
                <li> "delete"         ,
                <li> "read_perm"      ,
                <li> "write_perm"     ,
                <li> "write_owner"    ,
                <li> "full_control"
                </ul>
        
        :param rights_raw: Specifies SACL ACE's access rights in raw. This field is similar
                to advanced-rights fields. 'advanced-rights' specifies the value
                in enum but rights-raw specifies the access rights in integer
                format. Mutually exclusive with rights and advanced-rights
                fields.
        
        :param rights: Specifies SACL ACE's access rights.
                Possible values:
                <ul>
                <li> "no_access"           ,
                <li> "full_control"        ,
                <li> "modify"              ,
                <li> "read_and_execute"    ,
                <li> "read"                ,
                <li> "write"
                </ul>
        
        :param apply_to: Specifies how this ACE has to be applied on this folder and it's
                subfolders and files. This field is ignored if the security is
                mapped with a path which is not a folder.
                Possible values:
                <ul>
                <li> "this_folder"    ,
                <li> "sub_folders"    ,
                <li> "files"
                </ul>
        """
        return self.request( "file-directory-security-ntfs-sacl-modify", {
            'advanced_rights': [ advanced_rights, 'advanced-rights', [ basestring, 'advanced-access-rights' ], True ],
            'account': [ account, 'account', [ basestring, 'name-or-sid' ], False ],
            'rights_raw': [ rights_raw, 'rights-raw', [ int, 'None' ], False ],
            'rights': [ rights, 'rights', [ basestring, 'access-rights' ], False ],
            'ntfs_sd': [ ntfs_sd, 'ntfs-sd', [ basestring, 'fsecurity-ntfs-sd' ], False ],
            'audit_access_type': [ audit_access_type, 'audit-access-type', [ basestring, 'audit-access-type' ], False ],
            'apply_to': [ apply_to, 'apply-to', [ basestring, 'inheritance-level' ], True ],
        }, {
        } )
    
    def file_directory_security_ntfs_sacl_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns information about one or more system/audit access control
        entries
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                file-directory-security-ntfs-sacl object.
                All file-directory-security-ntfs-sacl objects matching this query
                up to 'max-records' will be returned.
        
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
        return self.request( "file-directory-security-ntfs-sacl-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FileDirectorySecurityNtfsSacl, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FileDirectorySecurityNtfsSacl, 'None' ], False ],
        }, {
            'attributes-list': [ FileDirectorySecurityNtfsSacl, True ],
        } )
    
    def file_directory_security_policy_task_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns information about one or more policy tasks. Policy is a
        container for tasks and a task associates a file/folder path name
        and the security descriptor that needs to be set on the
        file/folder. Every task in a policy is uniquely identified by the
        file/folder path. Policy can't have duplicate task entries and
        there is only one task per path.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                file-directory-security-policy-task object.
                All file-directory-security-policy-task objects matching this
                query up to 'max-records' will be returned.
        
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
        return self.request( "file-directory-security-policy-task-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FileDirectorySecurityPolicyTask, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FileDirectorySecurityPolicyTask, 'None' ], False ],
        }, {
            'attributes-list': [ FileDirectorySecurityPolicyTask, True ],
        } )

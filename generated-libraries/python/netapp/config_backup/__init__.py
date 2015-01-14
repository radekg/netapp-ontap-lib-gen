from netapp.connection import NaConnection
from config_backup_info_type import ConfigBackupInfoType # 11 properties
from backup_type import BackupType # 0 properties
from config_backup_settings_type import ConfigBackupSettingsType # 8 properties
from config_backup_info_get_iter_key_td import ConfigBackupInfoGetIterKeyTd # 2 properties

class ConfigBackupConnection(NaConnection):
    
    def config_backup_info_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return a list of configuration backups in the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                config-backup-info object.
                All config-backup-info objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "config-backup-info-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ConfigBackupInfoType, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ConfigBackupInfoType, 'None' ], False ],
        }, {
            'attributes-list': [ ConfigBackupInfoType, True ],
        } )
    
    def config_backup_create(self, node, backup_type=None, backup_name=None):
        """
        Create a configuration backup. A job will be queued to create the
        configuration backup in the background. Creation of configuration
        backup may take several minutes. This ZAPI creates an on demand
        backup.
        A job will be spawned to operate on the config-backup and the job
        id will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param node: The node to own the configuration backup. This is the node that
                will have the backup file on its root volume.
        
        :param backup_type: Indicates if the backup is a node or a cluster backup. A node
                backup contains only node-specific configuration of a particular
                node in the cluster. A cluster backup contains cluster-wide
                replicas in addition to node backup of each node in the cluster.
                Possible values:
                <ul>
                <li> "node"      - Node Backup,
                <li> "cluster"   - Cluster Backup
                </ul>
        
        :param backup_name: The name of the configuration backup. It must be a valid file
                name. An extension of .7z will be added if the given backup-name
                doesn't have that extension. If backup-name is not provided,
                software will generate the name for configuration backup.
        """
        return self.request( "config-backup-create", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'backup_type': [ backup_type, 'backup-type', [ basestring, 'backup-type' ], False ],
            'backup_name': [ backup_name, 'backup-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def config_backup_rename(self, node, new_backup_name, backup_name):
        """
        Rename a configuration backup. Renamed backup stays on the same
        node.
        
        :param node: The node that owns the configuration backup. This is the node
                that has the backup file on its root volume.
        
        :param new_backup_name: The new name for the configuration backup. It must be a valid
                file name. An extension of .7z will be added if the given
                new-name doesn't have that extension.
        
        :param backup_name: The name of the configuration backup.
        """
        return self.request( "config-backup-rename", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'new_backup_name': [ new_backup_name, 'new-backup-name', [ basestring, 'None' ], False ],
            'backup_name': [ backup_name, 'backup-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def config_backup_settings_password_set(self, password_for_destination_url=None):
        """
        Modify the password for destination URL.
        
        :param password_for_destination_url: Password for the destination URL.
        """
        return self.request( "config-backup-settings-password-set", {
            'password_for_destination_url': [ password_for_destination_url, 'password-for-destination-url', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def config_backup_settings_modify(self, username_for_destination_url=None, backup_count2=None, backup_count1=None, backup_count3=None, destination_url=None):
        """
        Modify the settings for configuration backup operations.
        
        :param username_for_destination_url: The username for the destination URL.
        
        :param backup_count2: The number of configuration backups to keep in the cluster for
                schedule 2.
        
        :param backup_count1: The number of configuration backups to keep in the cluster for
                schedule 1.
        
        :param backup_count3: The number of configuration backups to keep in the cluster for
                schedule 3.
        
        :param destination_url: The destination URL for uploading the configuration backups. URL
                is specified following the syntax described in RFC 3986. Only
                'ftp', 'http' and 'https' protocols are supported.
        """
        return self.request( "config-backup-settings-modify", {
            'username_for_destination_url': [ username_for_destination_url, 'username-for-destination-url', [ basestring, 'None' ], False ],
            'backup_count2': [ backup_count2, 'backup-count2', [ int, 'None' ], False ],
            'backup_count1': [ backup_count1, 'backup-count1', [ int, 'None' ], False ],
            'backup_count3': [ backup_count3, 'backup-count3', [ int, 'None' ], False ],
            'destination_url': [ destination_url, 'destination-url', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def config_backup_upload(self, node, backup_name, destination_url):
        """
        Upload a configuration backup to a URL.
        
        :param node: The node that owns the configuration backup. This is the node
                that has the backup file on its root volume.
        
        :param backup_name: The name of the configuration backup.
        
        :param destination_url: The destination URL. URL is specified following the syntax
                described in RFC 3986. Only 'ftp', 'http' and 'https' protocols
                are supported.
        """
        return self.request( "config-backup-upload", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'backup_name': [ backup_name, 'backup-name', [ basestring, 'None' ], False ],
            'destination_url': [ destination_url, 'destination-url', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def config_backup_info_get(self, node, backup_name, desired_attributes=None):
        """
        Return information about a specified configuration backup.
        
        :param node: The node that owns the configuration backup. This is the node
                that has the backup file on its root volume.
        
        :param backup_name: The name of the configuration backup.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "config-backup-info-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'backup_name': [ backup_name, 'backup-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ConfigBackupInfoType, 'None' ], False ],
        }, {
            'attributes': [ ConfigBackupInfoType, False ],
        } )
    
    def config_backup_delete(self, node, backup_name):
        """
        Delete a configuration backup.
        
        :param node: The node that owns the configuration backup. This is the node
                that has the backup file on its root volume.
        
        :param backup_name: The name of the configuration backup.
        """
        return self.request( "config-backup-delete", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'backup_name': [ backup_name, 'backup-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def config_backup_copy(self, from_node, backup_name, to_node):
        """
        Copy a configuration backup. A job will be queued to copy the
        configuration backup.
        A job will be spawned to operate on the config-backup and the job
        id will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param from_node: The source node to copy the configuration backup from. This is
                the node that has the backup file on its root volume.
        
        :param backup_name: The name of the configuration backup.
        
        :param to_node: The destination node to copy the configuration backup to.
        """
        return self.request( "config-backup-copy", {
            'from_node': [ from_node, 'from-node', [ basestring, 'None' ], False ],
            'backup_name': [ backup_name, 'backup-name', [ basestring, 'None' ], False ],
            'to_node': [ to_node, 'to-node', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def config_backup_settings_get(self, desired_attributes=None):
        """
        Return information about the configuration backup settings.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "config-backup-settings-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ConfigBackupSettingsType, 'None' ], False ],
        }, {
            'attributes': [ ConfigBackupSettingsType, False ],
        } )
    
    def config_backup_download(self, node, source_url, backup_name=None):
        """
        Download a configuration backup from a URL.
        
        :param node: The node to own the configuration backup. The backup file will be
                downloaded to the root volume of this node.
        
        :param source_url: The source URL. URL is specified following the syntax described
                in RFC 3986. Only 'ftp', 'http' and 'https' protocols are
                supported.
        
        :param backup_name: The name of the configuration backup. It must be a valid file
                name. An extension of .7z will be added if the given backup-name
                doesn't have that extension. If backup-name is not provided,
                software will generate a name for configuration backup.
        """
        return self.request( "config-backup-download", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'source_url': [ source_url, 'source-url', [ basestring, 'None' ], False ],
            'backup_name': [ backup_name, 'backup-name', [ basestring, 'None' ], False ],
        }, {
        } )

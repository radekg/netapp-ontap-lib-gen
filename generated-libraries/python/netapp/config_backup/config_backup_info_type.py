from netapp.netapp_object import NetAppObject

class ConfigBackupInfoType(NetAppObject):
    """
    Configuration Backup Information
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
    
    _node = None
    @property
    def node(self):
        """
        The node that owns the configuration backup. This is the
        node that has the backup file on its root volume.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _backup_type = None
    @property
    def backup_type(self):
        """
        Indicates if the backup is a node or a cluster backup. A
        node backup contains only node-specific configuration of
        a particular node in the cluster. A cluster backup
        contains cluster-wide replicas in addition to node backup
        of each node in the cluster. If backup-type is not
        provided, cluster backup is assumed by default.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "node"      - Node Backup,
        <li> "cluster"   - Cluster Backup
        </ul>
        """
        return self._backup_type
    @backup_type.setter
    def backup_type(self, val):
        if val != None:
            self.validate('backup_type', val)
        self._backup_type = val
    
    _backup_size = None
    @property
    def backup_size(self):
        """
        The size of configuration backup file in number of
        bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._backup_size
    @backup_size.setter
    def backup_size(self, val):
        if val != None:
            self.validate('backup_size', val)
        self._backup_size = val
    
    _schedule = None
    @property
    def schedule(self):
        """
        The name of the job schedule for scheduled backups.
        Possible values are: '8hour', 'daily', and 'weekly'. This
        field is not set for on demand backups created via
        management CLI or ZAPI.
        Attributes: non-creatable, non-modifiable
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    _is_auto = None
    @property
    def is_auto(self):
        """
        True indicates that configuration backup is a scheduled
        backup that was created automatically by a schedule.
        False indicates that configuration backup was created on
        demand.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_auto
    @is_auto.setter
    def is_auto(self, val):
        if val != None:
            self.validate('is_auto', val)
        self._is_auto = val
    
    _cluster_uuid = None
    @property
    def cluster_uuid(self):
        """
        The UUID of the cluster which the configuration backup
        was created for. This field is set only for cluster
        backups.
        Attributes: non-creatable, non-modifiable
        """
        return self._cluster_uuid
    @cluster_uuid.setter
    def cluster_uuid(self, val):
        if val != None:
            self.validate('cluster_uuid', val)
        self._cluster_uuid = val
    
    _version = None
    @property
    def version(self):
        """
        The software version which the configuration backup was
        created with.
        Attributes: non-creatable, non-modifiable
        """
        return self._version
    @version.setter
    def version(self, val):
        if val != None:
            self.validate('version', val)
        self._version = val
    
    _cluster_name = None
    @property
    def cluster_name(self):
        """
        The name of the cluster which the configuration backup
        was created for. This field is set only for cluster
        backups. For node backups, the nodes-in-backup field
        indicates the name of the node.
        Attributes: non-creatable, non-modifiable
        """
        return self._cluster_name
    @cluster_name.setter
    def cluster_name(self, val):
        if val != None:
            self.validate('cluster_name', val)
        self._cluster_name = val
    
    _backup_name = None
    @property
    def backup_name(self):
        """
        The name of the configuration backup.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._backup_name
    @backup_name.setter
    def backup_name(self, val):
        if val != None:
            self.validate('backup_name', val)
        self._backup_name = val
    
    _backup_creation_time = None
    @property
    def backup_creation_time(self):
        """
        The time of the configuration backup creation. The time
        value is in seconds since January 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._backup_creation_time
    @backup_creation_time.setter
    def backup_creation_time(self, val):
        if val != None:
            self.validate('backup_creation_time', val)
        self._backup_creation_time = val
    
    _nodes_in_backup = None
    @property
    def nodes_in_backup(self):
        """
        The names of the nodes included in the configuration
        backup.
        Attributes: non-creatable, non-modifiable
        """
        return self._nodes_in_backup
    @nodes_in_backup.setter
    def nodes_in_backup(self, val):
        if val != None:
            self.validate('nodes_in_backup', val)
        self._nodes_in_backup = val
    
    @staticmethod
    def get_api_name():
          return "config-backup-info-type"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'backup-type',
            'backup-size',
            'schedule',
            'is-auto',
            'cluster-uuid',
            'version',
            'cluster-name',
            'backup-name',
            'backup-creation-time',
            'nodes-in-backup',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'backup_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'backup_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'schedule': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_auto': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'cluster_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cluster_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'backup_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'backup_creation_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'nodes_in_backup': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }

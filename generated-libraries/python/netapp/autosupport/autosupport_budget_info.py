from netapp.netapp_object import NetAppObject

class AutosupportBudgetInfo(NetAppObject):
    """
    AutoSupport budget data
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
    
    _subsystem = None
    @property
    def subsystem(self):
        """
        The name of a subsystem from which AutoSupport collects
        data.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "platform"                 - Hardware information
        about the node,
        <li> "mhost"                    - User Space
        application information for a node,
        <li> "log_files"                - Log files for a
        node,
        <li> "performance"              - This subsystem
        gathers the .cm_stats_hourly_done file and user space
        counters,
        <li> "performance_asup"         - Performance specific
        information for a node,
        <li> "nht"                      - This subsystem
        gathers the /mroot/etc/log/nht_info content,
        <li> "san"                      - SAN specific
        information for a node,
        <li> "snapvault"                - SNAPVAULT specific
        information for a node,
        <li> "snapmirror"               - Snapmirror specific
        information for a node,
        <li> "dedupe"                   - Dedupe specific
        information for a node,
        <li> "nfs"                      - NFS specific
        information for a node,
        <li> "wafl"                     - WAFL specific
        information for a node,
        <li> "mot"                      - MOT specific
        information for a node,
        <li> "ha"                       - HA specific
        information for a node,
        <li> "networking"               - Networking specific
        information for a node,
        <li> "cifs"                     - CIFS specific
        information for a node,
        <li> "fpolicy"                  - Fpolicy specific
        information for a node,
        <li> "multistore"               - Multistore specific
        information for a node,
        <li> "raid"                     - RAID specific
        information for a node,
        <li> "storage"                  - Storage specific
        information for a node,
        <li> "asup_ems"                 - ASUP EMS specific
        information for a node,
        <li> "tape"                     - Tape specific
        information for a node,
        <li> "kernel"                   - kernel specific
        information for a node,
        <li> "secd"                     - SECD specific
        information for a node,
        <li> "metrocluster"             - Metrocluster specific
        information for a node,
        <li> "mandatory"                - Mandatory Basic
        information for a node,
        <li> "repository"               - Repository specific
        information for a node,
        <li> "splog_downcontroller"     - SPLOG saved when
        ontap is abnormal down,
        <li> "splog_latest"             - Up-to-date SPLOG from
        Service Processor FW  ,
        <li> "splog_before_spreboot"    - Up-to-date SPLOG from
        Service Processor FW before SP reboot,
        <li> "hm"                       - Health Monitor Alerts
        specific information,
        <li> "kcs"                      - Kernel Cluster
        Services information for a node,
        <li> "av"                       - Antivirus specific
        information for a node,
        <li> "san_ffdc"                 - SAN specific trace
        dumps for a node,
        <li> "nwd"                      - Node Watchdog
        specific information for a node,
        <li> "vscan"                    - Vscan specific
        information for a node
        </ul>
        """
        return self._subsystem
    @subsystem.setter
    def subsystem(self, val):
        if val != None:
            self.validate('subsystem', val)
        self._subsystem = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The name of a filer on which the AutoSupport tool is
        running.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _size_limit = None
    @property
    def size_limit(self):
        """
        The maximum allowable collection size (in bytes) for the
        subsystem.
        Attributes: non-creatable, modifiable
        """
        return self._size_limit
    @size_limit.setter
    def size_limit(self, val):
        if val != None:
            self.validate('size_limit', val)
        self._size_limit = val
    
    _time_limit = None
    @property
    def time_limit(self):
        """
        The maximum allowable collection time (in seconds ) for
        the subsystem.
        Attributes: non-creatable, modifiable
        """
        return self._time_limit
    @time_limit.setter
    def time_limit(self, val):
        if val != None:
            self.validate('time_limit', val)
        self._time_limit = val
    
    @staticmethod
    def get_api_name():
          return "autosupport-budget-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'subsystem',
            'node-name',
            'size-limit',
            'time-limit',
        ]
    
    def describe_properties(self):
        return {
            'subsystem': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'time_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

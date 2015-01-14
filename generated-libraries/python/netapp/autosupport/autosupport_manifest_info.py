from netapp.netapp_object import NetAppObject

class AutosupportManifestInfo(NetAppObject):
    """
    AutoSupport manifest data
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
        Subsystem
        Attributes: non-creatable, non-modifiable
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
    
    _cmd_tgt = None
    @property
    def cmd_tgt(self):
        """
        Execution Domain for Command
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "bsd"            - Command executed by BSD,
        <li> "smf_table"      - Command selects SMF table,
        <li> "file"           - Command indicates file to
        collect,
        <li> "dblade"         - Collect from dbladecli,
        <li> "dblade_file"    - Collect a file from dblade.
        Could be partner file,
        <li> "zapi_xml"       - Response in XML format,
        <li> "custom_fx"      - Collect custom function output
        file
        </ul>
        """
        return self._cmd_tgt
    @cmd_tgt.setter
    def cmd_tgt(self, val):
        if val != None:
            self.validate('cmd_tgt', val)
        self._cmd_tgt = val
    
    _cmd = None
    @property
    def cmd(self):
        """
        Actual Data Being Collected
        Attributes: non-creatable, non-modifiable
        """
        return self._cmd
    @cmd.setter
    def cmd(self, val):
        if val != None:
            self.validate('cmd', val)
        self._cmd = val
    
    _seq_num = None
    @property
    def seq_num(self):
        """
        AutoSupport Sequence Number
        Attributes: key, non-creatable, non-modifiable
        """
        return self._seq_num
    @seq_num.setter
    def seq_num(self, val):
        if val != None:
            self.validate('seq_num', val)
        self._seq_num = val
    
    _prio_num = None
    @property
    def prio_num(self):
        """
        Priority Order of Collection
        Attributes: key, non-creatable, non-modifiable
        """
        return self._prio_num
    @prio_num.setter
    def prio_num(self, val):
        if val != None:
            self.validate('prio_num', val)
        self._prio_num = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        Node
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _size_collected = None
    @property
    def size_collected(self):
        """
        Number of Bytes Collected
        Attributes: non-creatable, non-modifiable
        """
        return self._size_collected
    @size_collected.setter
    def size_collected(self, val):
        if val != None:
            self.validate('size_collected', val)
        self._size_collected = val
    
    _status = None
    @property
    def status(self):
        """
        Status of this Data Item
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "requested"                               - ASUP
        request has been added to the queue and is waiting
        processing by the collector,
        <li> "working"                                 - ASUP
        Collector is actively gathering the needed data,
        <li> "file_not_found"                          - ASUP
        collection failed, a needed file is missing,
        <li> "no_such_table"                           - ASUP
        collection was unable to find the requested SMF table,
        <li> "collection_truncated_size_limit"         - ASUP
        collection truncated due to size limits and partial data
        is available,
        <li> "collection_skipped_size_limit"           - ASUP
        collection skipped due to size limits and no data is
        available,
        <li> "collection_truncated_time_limit"         - ASUP
        collection truncated due to time limits and partial data
        is available,
        <li> "collection_skipped_time_limit"           - ASUP
        collection skipped due to time limits and no data is
        available,
        <li> "delivery_skipped_size_limit"             - ASUP
        data was skipped at delivery time due to size limits,
        <li> "general_error"                           - ASUP
        collection failed, additional information if any will be
        in the Error String field,
        <li> "completed"                               - ASUP
        collection is complete, ready for delivery,
        <li> "content_not_collected_mode"              - ASUP
        content was not collected, incompatible operational
        mode,
        <li> "content_not_collected_precheck"          - ASUP
        content was not collected, pre-check function violation,
        <li> "content_not_collected_privacy"           - ASUP
        content was not collected, the operation is disabled in
        privacy mode,
        <li> "content_empty"                           - ASUP
        content was collected successfully, but output was
        empty,
        <li> "collection_aborted"                      - ASUP
        collection aborted,
        <li> "collection_truncated_file_size_limit"    - ASUP
        file truncated due to size limits and partial data is
        available
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _body_file = None
    @property
    def body_file(self):
        """
        The AutoSupport Content Filename for this Data
        Attributes: non-creatable, non-modifiable
        """
        return self._body_file
    @body_file.setter
    def body_file(self, val):
        if val != None:
            self.validate('body_file', val)
        self._body_file = val
    
    _error = None
    @property
    def error(self):
        """
        Textual Description of Error
        Attributes: non-creatable, non-modifiable
        """
        return self._error
    @error.setter
    def error(self, val):
        if val != None:
            self.validate('error', val)
        self._error = val
    
    _query = None
    @property
    def query(self):
        """
        Table Query for XML Collection
        Attributes: non-creatable, non-modifiable
        """
        return self._query
    @query.setter
    def query(self, val):
        if val != None:
            self.validate('query', val)
        self._query = val
    
    _time_collected = None
    @property
    def time_collected(self):
        """
        Collection Time for this Data Item (ms)
        Attributes: non-creatable, non-modifiable
        """
        return self._time_collected
    @time_collected.setter
    def time_collected(self, val):
        if val != None:
            self.validate('time_collected', val)
        self._time_collected = val
    
    _content_type = None
    @property
    def content_type(self):
        """
        AutoSupport Content Type for this Data
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "basic"               - ASUP will contain minimal
        set of data for this subsystem,
        <li> "troubleshooting"     - ASUP will contain detailed
        collection of data for this subsystem
        </ul>
        """
        return self._content_type
    @content_type.setter
    def content_type(self, val):
        if val != None:
            self.validate('content_type', val)
        self._content_type = val
    
    @staticmethod
    def get_api_name():
          return "autosupport-manifest-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'subsystem',
            'cmd-tgt',
            'cmd',
            'seq-num',
            'prio-num',
            'node-name',
            'size-collected',
            'status',
            'body-file',
            'error',
            'query',
            'time-collected',
            'content-type',
        ]
    
    def describe_properties(self):
        return {
            'subsystem': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cmd_tgt': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cmd': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'seq_num': { 'class': int, 'is_list': False, 'required': 'optional' },
            'prio_num': { 'class': int, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size_collected': { 'class': int, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'body_file': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'query': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time_collected': { 'class': int, 'is_list': False, 'required': 'optional' },
            'content_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

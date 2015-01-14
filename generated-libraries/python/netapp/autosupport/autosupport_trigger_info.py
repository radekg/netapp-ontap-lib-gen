from netapp.netapp_object import NetAppObject

class AutosupportTriggerInfo(NetAppObject):
    """
    AutoSupport trigger data
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
    
    _to_enabled = None
    @property
    def to_enabled(self):
        """
        Deliver to AutoSupport -to Addresses. Possible values
        are: enabled or disabled.
        Attributes: non-creatable, modifiable
        """
        return self._to_enabled
    @to_enabled.setter
    def to_enabled(self, val):
        if val != None:
            self.validate('to_enabled', val)
        self._to_enabled = val
    
    _troubleshooting_default = None
    @property
    def troubleshooting_default(self):
        """
        Default Subsystems Reporting Troubleshooting Info
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
        return self._troubleshooting_default
    @troubleshooting_default.setter
    def troubleshooting_default(self, val):
        if val != None:
            self.validate('troubleshooting_default', val)
        self._troubleshooting_default = val
    
    _noteto_enabled = None
    @property
    def noteto_enabled(self):
        """
        Deliver to AutoSupport -noteto Addresses. Possible values
        are: enabled or disabled.
        Attributes: non-creatable, modifiable
        """
        return self._noteto_enabled
    @noteto_enabled.setter
    def noteto_enabled(self, val):
        if val != None:
            self.validate('noteto_enabled', val)
        self._noteto_enabled = val
    
    _time_limit = None
    @property
    def time_limit(self):
        """
        The data collection time budget for this trigger (in
        seconds).  Content not collected will be marked as
        collection-truncated-time-limit in the manifest.
        Attributes: non-creatable, modifiable
        """
        return self._time_limit
    @time_limit.setter
    def time_limit(self, val):
        if val != None:
            self.validate('time_limit', val)
        self._time_limit = val
    
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
    
    _trigger = None
    @property
    def trigger(self):
        """
        EMS Message
        Attributes: key, non-creatable, non-modifiable
        """
        return self._trigger
    @trigger.setter
    def trigger(self, val):
        if val != None:
            self.validate('trigger', val)
        self._trigger = val
    
    _basic_additional = None
    @property
    def basic_additional(self):
        """
        Additional Subsystems Reporting Basic Info
        Attributes: non-creatable, modifiable
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
        return self._basic_additional
    @basic_additional.setter
    def basic_additional(self, val):
        if val != None:
            self.validate('basic_additional', val)
        self._basic_additional = val
    
    _troubleshooting_additional = None
    @property
    def troubleshooting_additional(self):
        """
        Additional Subsystems Reporting Troubleshooting Info
        Attributes: non-creatable, modifiable
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
        return self._troubleshooting_additional
    @troubleshooting_additional.setter
    def troubleshooting_additional(self, val):
        if val != None:
            self.validate('troubleshooting_additional', val)
        self._troubleshooting_additional = val
    
    _basic_default = None
    @property
    def basic_default(self):
        """
        Default Subsystems Reporting Basic Info
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
        return self._basic_default
    @basic_default.setter
    def basic_default(self, val):
        if val != None:
            self.validate('basic_default', val)
        self._basic_default = val
    
    _additional_content = None
    @property
    def additional_content(self):
        """
        Additional Content Flag
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "basic"               - ASUP will contain minimal
        set of data for this subsystem,
        <li> "troubleshooting"     - ASUP will contain detailed
        collection of data for this subsystem
        </ul>
        """
        return self._additional_content
    @additional_content.setter
    def additional_content(self, val):
        if val != None:
            self.validate('additional_content', val)
        self._additional_content = val
    
    @staticmethod
    def get_api_name():
          return "autosupport-trigger-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'to-enabled',
            'troubleshooting-default',
            'noteto-enabled',
            'time-limit',
            'node-name',
            'trigger',
            'basic-additional',
            'troubleshooting-additional',
            'basic-default',
            'additional-content',
        ]
    
    def describe_properties(self):
        return {
            'to_enabled': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'troubleshooting_default': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'noteto_enabled': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'trigger': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'basic_additional': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'troubleshooting_additional': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'basic_default': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'additional_content': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }

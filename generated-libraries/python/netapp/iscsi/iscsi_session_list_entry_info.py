from netapp.iscsi.iscsi_session_connection_list_entry_info import IscsiSessionConnectionListEntryInfo
from netapp.iscsi.iscsi_sesssion_cmd_list_entry_info import IscsiSesssionCmdListEntryInfo
from netapp.netapp_object import NetAppObject

class IscsiSessionListEntryInfo(NetAppObject):
    """
    Information about a single iSCSI session.
    In Data ONTAP 7-Mode, sessions are uniquely identified by the
    'target-session-id'.
    In Data ONTAP Cluster-Mode, sessions are uniquely identified within
    a Vserver by the combination of 'tpgroup-name' and 'target-session-id'.
    """
    
    _initiator_aliasname = None
    @property
    def initiator_aliasname(self):
        """
        The user-friendly name assigned to initiator.
        This field is only present if the initiator
        provided an alias during login.
        """
        return self._initiator_aliasname
    @initiator_aliasname.setter
    def initiator_aliasname(self, val):
        if val != None:
            self.validate('initiator_aliasname', val)
        self._initiator_aliasname = val
    
    _tpgroup_name = None
    @property
    def tpgroup_name(self):
        """
        The name of the target portal group associated
        with this session.
        """
        return self._tpgroup_name
    @tpgroup_name.setter
    def tpgroup_name(self, val):
        if val != None:
            self.validate('tpgroup_name', val)
        self._tpgroup_name = val
    
    _max_burst_length = None
    @property
    def max_burst_length(self):
        """
        The MaxBurstLength of the session as defined
        in RFC 3720, in bytes.
        """
        return self._max_burst_length
    @max_burst_length.setter
    def max_burst_length(self, val):
        if val != None:
            self.validate('max_burst_length', val)
        self._max_burst_length = val
    
    _iscsi_session_connection_list_entries = None
    @property
    def iscsi_session_connection_list_entries(self):
        """
        List of TCP/IP connections associated with this session
        """
        return self._iscsi_session_connection_list_entries
    @iscsi_session_connection_list_entries.setter
    def iscsi_session_connection_list_entries(self, val):
        if val != None:
            self.validate('iscsi_session_connection_list_entries', val)
        self._iscsi_session_connection_list_entries = val
    
    _initiator_nodename = None
    @property
    def initiator_nodename(self):
        """
        Name of initiator. The initiator name must
        conform to RFC 3720, for example:
        "iqn.1987-06.com.initvendor1:appsrv.sn.2346".
        """
        return self._initiator_nodename
    @initiator_nodename.setter
    def initiator_nodename(self, val):
        if val != None:
            self.validate('initiator_nodename', val)
        self._initiator_nodename = val
    
    _target_session_id = None
    @property
    def target_session_id(self):
        """
        The iSCSI session identifier assigned by the
        storage system.
        """
        return self._target_session_id
    @target_session_id.setter
    def target_session_id(self, val):
        if val != None:
            self.validate('target_session_id', val)
        self._target_session_id = val
    
    _immediate_data_enabled = None
    @property
    def immediate_data_enabled(self):
        """
        True if this session has immediate data enabled,
        false otherwise.
        """
        return self._immediate_data_enabled
    @immediate_data_enabled.setter
    def immediate_data_enabled(self, val):
        if val != None:
            self.validate('immediate_data_enabled', val)
        self._immediate_data_enabled = val
    
    _data_sequence_in_order = None
    @property
    def data_sequence_in_order(self):
        """
        The DataSequenceInOrder of the session
        as defined in RFC 3720.
        """
        return self._data_sequence_in_order
    @data_sequence_in_order.setter
    def data_sequence_in_order(self, val):
        if val != None:
            self.validate('data_sequence_in_order', val)
        self._data_sequence_in_order = val
    
    _default_time_to_wait = None
    @property
    def default_time_to_wait(self):
        """
        The DefaultTime2Wait of the session as defined
        in RFC 3720, in seconds.
        """
        return self._default_time_to_wait
    @default_time_to_wait.setter
    def default_time_to_wait(self, val):
        if val != None:
            self.validate('default_time_to_wait', val)
        self._default_time_to_wait = val
    
    _data_pdu_in_order = None
    @property
    def data_pdu_in_order(self):
        """
        The DataPDUInOrder of the session as defined
        in RFC 3720.
        """
        return self._data_pdu_in_order
    @data_pdu_in_order.setter
    def data_pdu_in_order(self, val):
        if val != None:
            self.validate('data_pdu_in_order', val)
        self._data_pdu_in_order = val
    
    _max_outstanding_r2t = None
    @property
    def max_outstanding_r2t(self):
        """
        The MaxOutstandingR2T of the session as defined
        in RFC 3720.
        """
        return self._max_outstanding_r2t
    @max_outstanding_r2t.setter
    def max_outstanding_r2t(self, val):
        if val != None:
            self.validate('max_outstanding_r2t', val)
        self._max_outstanding_r2t = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the vserver containing this
        session.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _default_time_to_retain = None
    @property
    def default_time_to_retain(self):
        """
        The DefaultTime2Retain of the session as defined
        in RFC 3720, in seconds.
        """
        return self._default_time_to_retain
    @default_time_to_retain.setter
    def default_time_to_retain(self, val):
        if val != None:
            self.validate('default_time_to_retain', val)
        self._default_time_to_retain = val
    
    _session_type = None
    @property
    def session_type(self):
        """
        Possible values: "normal" or "discovery".
        """
        return self._session_type
    @session_type.setter
    def session_type(self, val):
        if val != None:
            self.validate('session_type', val)
        self._session_type = val
    
    _cmd_window_size = None
    @property
    def cmd_window_size(self):
        """
        Command window size.
        """
        return self._cmd_window_size
    @cmd_window_size.setter
    def cmd_window_size(self, val):
        if val != None:
            self.validate('cmd_window_size', val)
        self._cmd_window_size = val
    
    _error_recovery_level = None
    @property
    def error_recovery_level(self):
        """
        iSCSI ErrorRecoveryLevel as defined in
        RFC 3720.
        """
        return self._error_recovery_level
    @error_recovery_level.setter
    def error_recovery_level(self, val):
        if val != None:
            self.validate('error_recovery_level', val)
        self._error_recovery_level = val
    
    _first_burst_length = None
    @property
    def first_burst_length(self):
        """
        The FirstBurstLength of the session as defined
        in RFC 3720, in bytes.
        """
        return self._first_burst_length
    @first_burst_length.setter
    def first_burst_length(self, val):
        if val != None:
            self.validate('first_burst_length', val)
        self._first_burst_length = val
    
    _iscsi_sesssion_cmd_list_entries = None
    @property
    def iscsi_sesssion_cmd_list_entries(self):
        """
        List of active commands associated with this session
        """
        return self._iscsi_sesssion_cmd_list_entries
    @iscsi_sesssion_cmd_list_entries.setter
    def iscsi_sesssion_cmd_list_entries(self, val):
        if val != None:
            self.validate('iscsi_sesssion_cmd_list_entries', val)
        self._iscsi_sesssion_cmd_list_entries = val
    
    _max_connections = None
    @property
    def max_connections(self):
        """
        Maximum number of connections for this session.
        """
        return self._max_connections
    @max_connections.setter
    def max_connections(self, val):
        if val != None:
            self.validate('max_connections', val)
        self._max_connections = val
    
    _tpgroup_tag = None
    @property
    def tpgroup_tag(self):
        """
        The tag of the target portal group associated
        with this session.
        """
        return self._tpgroup_tag
    @tpgroup_tag.setter
    def tpgroup_tag(self, val):
        if val != None:
            self.validate('tpgroup_tag', val)
        self._tpgroup_tag = val
    
    _isid = None
    @property
    def isid(self):
        """
        ISID for this session selected by initiator
        represented as 6 hexadecimal octets separated by
        colons, for example: "40:01:37:00:00:00".
        """
        return self._isid
    @isid.setter
    def isid(self, val):
        if val != None:
            self.validate('isid', val)
        self._isid = val
    
    _initial_r2t_enabled = None
    @property
    def initial_r2t_enabled(self):
        """
        True if this session has R2T enabled,
        false otherwise.
        """
        return self._initial_r2t_enabled
    @initial_r2t_enabled.setter
    def initial_r2t_enabled(self, val):
        if val != None:
            self.validate('initial_r2t_enabled', val)
        self._initial_r2t_enabled = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-session-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-aliasname',
            'tpgroup-name',
            'max-burst-length',
            'iscsi-session-connection-list-entries',
            'initiator-nodename',
            'target-session-id',
            'immediate-data-enabled',
            'data-sequence-in-order',
            'default-time-to-wait',
            'data-pdu-in-order',
            'max-outstanding-r2t',
            'vserver',
            'default-time-to-retain',
            'session-type',
            'cmd-window-size',
            'error-recovery-level',
            'first-burst-length',
            'iscsi-sesssion-cmd-list-entries',
            'max-connections',
            'tpgroup-tag',
            'isid',
            'initial-r2t-enabled',
        ]
    
    def describe_properties(self):
        return {
            'initiator_aliasname': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tpgroup_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'max_burst_length': { 'class': int, 'is_list': False, 'required': 'required' },
            'iscsi_session_connection_list_entries': { 'class': IscsiSessionConnectionListEntryInfo, 'is_list': True, 'required': 'required' },
            'initiator_nodename': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_session_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'immediate_data_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'data_sequence_in_order': { 'class': bool, 'is_list': False, 'required': 'required' },
            'default_time_to_wait': { 'class': int, 'is_list': False, 'required': 'required' },
            'data_pdu_in_order': { 'class': bool, 'is_list': False, 'required': 'required' },
            'max_outstanding_r2t': { 'class': int, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'default_time_to_retain': { 'class': int, 'is_list': False, 'required': 'required' },
            'session_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'cmd_window_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'error_recovery_level': { 'class': int, 'is_list': False, 'required': 'required' },
            'first_burst_length': { 'class': int, 'is_list': False, 'required': 'required' },
            'iscsi_sesssion_cmd_list_entries': { 'class': IscsiSesssionCmdListEntryInfo, 'is_list': True, 'required': 'optional' },
            'max_connections': { 'class': int, 'is_list': False, 'required': 'required' },
            'tpgroup_tag': { 'class': int, 'is_list': False, 'required': 'required' },
            'isid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initial_r2t_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
        }

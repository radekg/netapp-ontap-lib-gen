from netapp.netapp_object import NetAppObject

class SnapvaultConfigurationInfo(NetAppObject):
    """
    Describes the elements of the snapvault configuration
    entry.
    """
    
    _is_access_time_change_ignored = None
    @property
    def is_access_time_change_ignored(self):
        """
        Sets the ignore_atime option in snapvault configuration
        entry. When set to 'true', snapvault primary does not
        send files with only access time changes during
        incremental transfers.
        The default value is 'false'
        """
        return self._is_access_time_change_ignored
    @is_access_time_change_ignored.setter
    def is_access_time_change_ignored(self, val):
        if val != None:
            self.validate('is_access_time_change_ignored', val)
        self._is_access_time_change_ignored = val
    
    _use_compression = None
    @property
    def use_compression(self):
        """
        Specifies whether to compress the network data stream.
        Possible values are 'on', 'off', and 'default'. When
        the value is set to 'on', stream compression will be
        enabled. When the value is set to 'off', stream compression
        will be disabled. When the value is set to 'default' then
        the default value will be used.
        In case of snapvault create relationship API, when this
        option is not specified, the default value will be used.
        In case of snapvault modify API, when this option is not
        specified, the last configured value for this relationship
        will be used.
        The default value for this option is the value of global
        compression option.
        """
        return self._use_compression
    @use_compression.setter
    def use_compression(self, val):
        if val != None:
            self.validate('use_compression', val)
        self._use_compression = val
    
    _secondary_path = None
    @property
    def secondary_path(self):
        """
        The secondary path that will be used as destination for
        this relationship as well as baseline transfer.
        The secondary path will be created during the baseline
        transfer and hence it must not exist when issuing this
        request.
        """
        return self._secondary_path
    @secondary_path.setter
    def secondary_path(self, val):
        if val != None:
            self.validate('secondary_path', val)
        self._secondary_path = val
    
    _primary_system = None
    @property
    def primary_system(self):
        """
        The primary system for this relationship as well as for
        the baseline transfer.
        This input will be used by the secondary system to
        establish contact with the primary. Therefore this
        input is expected to be a hostname that the primary can
        resolve.
        """
        return self._primary_system
    @primary_system.setter
    def primary_system(self, val):
        if val != None:
            self.validate('primary_system', val)
        self._primary_system = val
    
    _primary_path = None
    @property
    def primary_path(self):
        """
        The primary path that will be used as the source for
        this relationship as well as for baseline transfer. This
        can be either in UTF8 or ASCII/extended ASCII depending
        on whether or not 'is-primary-path-utf8-encoded'  flag is
        set. If option 'is-primary-path-utf8-encoded' is not
        specified, then the primary-path considered as in
        ASCII/extended ASCII.
        """
        return self._primary_path
    @primary_path.setter
    def primary_path(self, val):
        if val != None:
            self.validate('primary_path', val)
        self._primary_path = val
    
    _is_open_file_backup_allowed = None
    @property
    def is_open_file_backup_allowed(self):
        """
        Sets the back_up_open_files option in the snapvault
        configuration entry. This option is used to allow or
        disallow the inclusion of open files on the primary
        system at the time of the transfer. This option is
        currently applicable only for OSSV relationships. When
        set to 'false' the OSSV primary agents will exclude
        files that are open from the transfer.
        The default value for this parameter is 'true'.
        """
        return self._is_open_file_backup_allowed
    @is_open_file_backup_allowed.setter
    def is_open_file_backup_allowed(self, val):
        if val != None:
            self.validate('is_open_file_backup_allowed', val)
        self._is_open_file_backup_allowed = val
    
    _tries_count = None
    @property
    def tries_count(self):
        """
        The maximum number of times a transfer will be tried.
        Transfers that are retried using this mechanism may be
        capable of restarting from where the previous attempt
        failed.
        If a transfer does not succeed even after those many
        attempts, then the secondary will give up. All the data
        that was transferred during previous tries for this
        transfer will be discarded.
        The default value for this parameter is 2.
        When set to 0, the relationship will become dormant.
        In other words no transfers will be allowed to this
        secondary path.
        The maximum value accepted for this input is 120.
        Range:[0..120]
        """
        return self._tries_count
    @tries_count.setter
    def tries_count(self, val):
        if val != None:
            self.validate('tries_count', val)
        self._tries_count = val
    
    _connection_mode = None
    @property
    def connection_mode(self):
        """
        This option specifies the mode to be used for establising
        connection between primary and secondary. If this option
        is set to "inet6", connections between primary and
        secondary will be established using IPv6 addresses only.
        If there are no IPv6 addressess configured, then the
        connection will fail. If the option is set to "inet",
        connections between primary and secondary will be
        established using IPv4 addresses only. If there are no IPv4
        addresses configured, then the connection will fail.
        When this option is not specified, Connection will be tried
        using both "inet6" and "inet". "inet6" will have higher
        precedence than "inet". If connection request using "inet6"
        fails, SnapMirror will retry the connection using "inet".
        This argument is not effective when an IP address is
        specified instead of primary hostname. If the IP address
        format and connection mode do not match, the operation will
        fail with proper error message.
        """
        return self._connection_mode
    @connection_mode.setter
    def connection_mode(self, val):
        if val != None:
            self.validate('connection_mode', val)
        self._connection_mode = val
    
    _is_primary_path_utf8_encoded = None
    @property
    def is_primary_path_utf8_encoded(self):
        """
        Specifies encoding format for the primary pathname. A 'true'
        value indicates that the primary pathname is in UTF8 format.
        The default encoding format is ASCII/extended ASCII.
        The default value is 'false'.
        """
        return self._is_primary_path_utf8_encoded
    @is_primary_path_utf8_encoded.setter
    def is_primary_path_utf8_encoded(self, val):
        if val != None:
            self.validate('is_primary_path_utf8_encoded', val)
        self._is_primary_path_utf8_encoded = val
    
    _max_transfer_rate = None
    @property
    def max_transfer_rate(self):
        """
        The maximum transfer rate in kilobytes (1024 bytes) per
        second that will be used for this relationship as well
        as baseline transfer.
        The default value for this parameter will allow
        transfers to proceed as fast as possible.
        Range:[1..2^31-2]
        """
        return self._max_transfer_rate
    @max_transfer_rate.setter
    def max_transfer_rate(self, val):
        if val != None:
            self.validate('max_transfer_rate', val)
        self._max_transfer_rate = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-configuration-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-access-time-change-ignored',
            'use-compression',
            'secondary-path',
            'primary-system',
            'primary-path',
            'is-open-file-backup-allowed',
            'tries-count',
            'connection-mode',
            'is-primary-path-utf8-encoded',
            'max-transfer-rate',
        ]
    
    def describe_properties(self):
        return {
            'is_access_time_change_ignored': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'use_compression': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'secondary_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'primary_system': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'primary_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_open_file_backup_allowed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'tries_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'connection_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_primary_path_utf8_encoded': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'max_transfer_rate': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

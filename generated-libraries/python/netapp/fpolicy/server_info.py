from netapp.netapp_object import NetAppObject

class ServerInfo(NetAppObject):
    """
    Structure containing information pertaining to servers.
    """
    
    _is_snapid_required = None
    @property
    def is_snapid_required(self):
        """
        True if the server is registered to receive file
        snapshot ID with every Fpolicy request.
        """
        return self._is_snapid_required
    @is_snapid_required.setter
    def is_snapid_required(self, val):
        if val != None:
            self.validate('is_snapid_required', val)
        self._is_snapid_required = val
    
    _smb_req_pipe_name = None
    @property
    def smb_req_pipe_name(self):
        """
        The name of the FPolicy request pipe name on which FPolicy
        server is recieving the screen requests from the storage
        system. This name is sent by the FPolicy server at the time
        of the FPolicy server registration.
        """
        return self._smb_req_pipe_name
    @smb_req_pipe_name.setter
    def smb_req_pipe_name(self, val):
        if val != None:
            self.validate('smb_req_pipe_name', val)
        self._smb_req_pipe_name = val
    
    _is_size_and_owner_required = None
    @property
    def is_size_and_owner_required(self):
        """
        True if the server is registered to receive file size
        and file owner information with every Fpolicy request.
        """
        return self._is_size_and_owner_required
    @is_size_and_owner_required.setter
    def is_size_and_owner_required(self, val):
        if val != None:
            self.validate('is_size_and_owner_required', val)
        self._is_size_and_owner_required = val
    
    _number_of_screen_failures = None
    @property
    def number_of_screen_failures(self):
        """
        Number of failed (denied) screens since server
        registrations.
        Range : [0..2^32-1].
        """
        return self._number_of_screen_failures
    @number_of_screen_failures.setter
    def number_of_screen_failures(self, val):
        if val != None:
            self.validate('number_of_screen_failures', val)
        self._number_of_screen_failures = val
    
    _server_id = None
    @property
    def server_id(self):
        """
        The unique server ID assigned to the Fpolicy server
        at the time of Fpolicy server registration.
        Range : [0..2^32-1].
        """
        return self._server_id
    @server_id.setter
    def server_id(self, val):
        if val != None:
            self.validate('server_id', val)
        self._server_id = val
    
    _is_version2 = None
    @property
    def is_version2(self):
        """
        True if the server is registered with version2 support
        enabled. version2 refers to the version of the
        FP_ScreenRequest(). When version2 is true the FPolicy
        server is enabled to receive FP_ScreenRequest2() RPC.
        """
        return self._is_version2
    @is_version2.setter
    def is_version2(self, val):
        if val != None:
            self.validate('is_version2', val)
        self._is_version2 = val
    
    _is_asynchronous = None
    @property
    def is_asynchronous(self):
        """
        Shows if the server is registered as asynchronous,
        i.e. doesn't send reply to the filer.
        """
        return self._is_asynchronous
    @is_asynchronous.setter
    def is_asynchronous(self, val):
        if val != None:
            self.validate('is_asynchronous', val)
        self._is_asynchronous = val
    
    _server_ip = None
    @property
    def server_ip(self):
        """
        The ip address, in dotted-decimal format, of the server.
        """
        return self._server_ip
    @server_ip.setter
    def server_ip(self, val):
        if val != None:
            self.validate('server_ip', val)
        self._server_ip = val
    
    _idl_version = None
    @property
    def idl_version(self):
        """
        Version of the Interface Definition Language(IDL) used by
        the Fpolicy server.
        Range : [0..2^32-1].
        """
        return self._idl_version
    @idl_version.setter
    def idl_version(self, val):
        if val != None:
            self.validate('idl_version', val)
        self._idl_version = val
    
    _offline_filter_bit = None
    @property
    def offline_filter_bit(self):
        """
        Shows the setting of offline filter.
        Supported values: "none", "on-set".
        """
        return self._offline_filter_bit
    @offline_filter_bit.setter
    def offline_filter_bit(self, val):
        if val != None:
            self.validate('offline_filter_bit', val)
        self._offline_filter_bit = val
    
    _number_of_screened_files = None
    @property
    def number_of_screened_files(self):
        """
        Number of screened files since server registration.
        Range : [0..2^32-1].
        """
        return self._number_of_screened_files
    @number_of_screened_files.setter
    def number_of_screened_files(self, val):
        if val != None:
            self.validate('number_of_screened_files', val)
        self._number_of_screened_files = val
    
    @staticmethod
    def get_api_name():
          return "server-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-snapid-required',
            'smb-req-pipe-name',
            'is-size-and-owner-required',
            'number-of-screen-failures',
            'server-id',
            'is-version2',
            'is-asynchronous',
            'server-ip',
            'idl-version',
            'offline-filter-bit',
            'number-of-screened-files',
        ]
    
    def describe_properties(self):
        return {
            'is_snapid_required': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'smb_req_pipe_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_size_and_owner_required': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'number_of_screen_failures': { 'class': int, 'is_list': False, 'required': 'required' },
            'server_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_version2': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_asynchronous': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'server_ip': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'idl_version': { 'class': int, 'is_list': False, 'required': 'required' },
            'offline_filter_bit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'number_of_screened_files': { 'class': int, 'is_list': False, 'required': 'required' },
        }

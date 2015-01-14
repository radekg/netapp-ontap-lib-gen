from netapp.netapp_object import NetAppObject

class CifsSession(NetAppObject):
    """
    Displays the established CIFS sessions
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
        The name of the node on which the session listing is
        done.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _session_id = None
    @property
    def session_id(self):
        """
        The unique identifier for the session.
        Attributes: non-creatable, non-modifiable
        """
        return self._session_id
    @session_id.setter
    def session_id(self, val):
        if val != None:
            self.validate('session_id', val)
        self._session_id = val
    
    _connected_time = None
    @property
    def connected_time(self):
        """
        The time duration since the session was established.
        Attributes: non-creatable, non-modifiable
        """
        return self._connected_time
    @connected_time.setter
    def connected_time(self, val):
        if val != None:
            self.validate('connected_time', val)
        self._connected_time = val
    
    _unix_user = None
    @property
    def unix_user(self):
        """
        The name of the UNIX user for which the session is
        established.
        Attributes: non-creatable, non-modifiable
        """
        return self._unix_user
    @unix_user.setter
    def unix_user(self, val):
        if val != None:
            self.validate('unix_user', val)
        self._unix_user = val
    
    _protocol_version = None
    @property
    def protocol_version(self):
        """
        The CIFS protocol version that is used to establish the
        session.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "smb1"      - SMB 1.0,
        <li> "smb2"      - SMB 2.0,
        <li> "smb2_1"    - SMB 2.1,
        <li> "smb3"      - SMB 3.0
        </ul>
        """
        return self._protocol_version
    @protocol_version.setter
    def protocol_version(self, val):
        if val != None:
            self.validate('protocol_version', val)
        self._protocol_version = val
    
    _lif_address = None
    @property
    def lif_address(self):
        """
        The data lif that is used to establish the session.
        Attributes: non-creatable, non-modifiable
        """
        return self._lif_address
    @lif_address.setter
    def lif_address(self, val):
        if val != None:
            self.validate('lif_address', val)
        self._lif_address = val
    
    _shares = None
    @property
    def shares(self):
        """
        The number of the CIFS shares that are opened under the
        session.
        Attributes: non-creatable, non-modifiable
        """
        return self._shares
    @shares.setter
    def shares(self, val):
        if val != None:
            self.validate('shares', val)
        self._shares = val
    
    _idle_time = None
    @property
    def idle_time(self):
        """
        The time duration since there was last activity on the
        session.
        Attributes: non-creatable, non-modifiable
        """
        return self._idle_time
    @idle_time.setter
    def idle_time(self, val):
        if val != None:
            self.validate('idle_time', val)
        self._idle_time = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The Vserver name on which the session listing is done.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _continuously_available = None
    @property
    def continuously_available(self):
        """
        The type of continuous avalability protection provided to
        the session.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "no"        - The open file is not continuously
        available. For sessions, it contains one or more open
        file but none of them are continuously available.,
        <li> "yes"       - The open file is continuously
        available. For sessions, it contains one or more open
        files and all of them are continuously available.,
        <li> "partial"   - This value is used for sessions
        only. It contains at least one continuously available
        open file but other open files that are not.
        </ul>
        """
        return self._continuously_available
    @continuously_available.setter
    def continuously_available(self, val):
        if val != None:
            self.validate('continuously_available', val)
        self._continuously_available = val
    
    _other = None
    @property
    def other(self):
        """
        The number of the special files that are opened under the
        session.
        Attributes: non-creatable, non-modifiable
        """
        return self._other
    @other.setter
    def other(self, val):
        if val != None:
            self.validate('other', val)
        self._other = val
    
    _address = None
    @property
    def address(self):
        """
        The ip address of the workstation from which the session
        is opened.
        Attributes: non-creatable, non-modifiable
        """
        return self._address
    @address.setter
    def address(self, val):
        if val != None:
            self.validate('address', val)
        self._address = val
    
    _auth_mechanism = None
    @property
    def auth_mechanism(self):
        """
        The authentication mechanism used to establish the
        session.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "none"      ,
        <li> "ntlmv1"    ,
        <li> "ntlmv2"    ,
        <li> "kerberos"  ,
        <li> "anonymous"
        </ul>
        """
        return self._auth_mechanism
    @auth_mechanism.setter
    def auth_mechanism(self, val):
        if val != None:
            self.validate('auth_mechanism', val)
        self._auth_mechanism = val
    
    _connection_id = None
    @property
    def connection_id(self):
        """
        The connection that is used to establish the session.
        Attributes: non-creatable, non-modifiable
        """
        return self._connection_id
    @connection_id.setter
    def connection_id(self, val):
        if val != None:
            self.validate('connection_id', val)
        self._connection_id = val
    
    _windows_user = None
    @property
    def windows_user(self):
        """
        The name of the CIFS user for which the session is
        established.
        Attributes: non-creatable, non-modifiable
        """
        return self._windows_user
    @windows_user.setter
    def windows_user(self, val):
        if val != None:
            self.validate('windows_user', val)
        self._windows_user = val
    
    _files = None
    @property
    def files(self):
        """
        The number of the regular files that are opened under the
        session.
        Attributes: non-creatable, non-modifiable
        """
        return self._files
    @files.setter
    def files(self, val):
        if val != None:
            self.validate('files', val)
        self._files = val
    
    @staticmethod
    def get_api_name():
          return "cifs-session"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'session-id',
            'connected-time',
            'unix-user',
            'protocol-version',
            'lif-address',
            'shares',
            'idle-time',
            'vserver',
            'continuously-available',
            'other',
            'address',
            'auth-mechanism',
            'connection-id',
            'windows-user',
            'files',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'session_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'connected_time': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'unix_user': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'protocol_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lif_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'shares': { 'class': int, 'is_list': False, 'required': 'optional' },
            'idle_time': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'continuously_available': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'other': { 'class': int, 'is_list': False, 'required': 'optional' },
            'address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'auth_mechanism': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connection_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'windows_user': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'files': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

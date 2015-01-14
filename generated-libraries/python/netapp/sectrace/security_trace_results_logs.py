from netapp.netapp_object import NetAppObject

class SecurityTraceResultsLogs(NetAppObject):
    """
    List of security tracing results.
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
        The cluster node on which the permission tracing event
        occured.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _index = None
    @property
    def index(self):
        """
        The index of the filter corresponding to the permission
        tracing event.
        Attributes: required-for-create, non-modifiable
        """
        return self._index
    @index.setter
    def index(self, val):
        if val != None:
            self.validate('index', val)
        self._index = val
    
    _user_name = None
    @property
    def user_name(self):
        """
        Windows or Unix user who triggered the permission tracing
        event.
        Attributes: required-for-create, non-modifiable
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    _client_ip = None
    @property
    def client_ip(self):
        """
        The IP address of the client that triggered the
        permission tracing event.
        Attributes: required-for-create, non-modifiable
        """
        return self._client_ip
    @client_ip.setter
    def client_ip(self, val):
        if val != None:
            self.validate('client_ip', val)
        self._client_ip = val
    
    _security_style = None
    @property
    def security_style(self):
        """
        The security style of the file system where the
        persmission tracing event occured.
        Attributes: required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "security_none"            - Security not Set,
        <li> "security_unix_modebits"   - UNIX and UNIX
        permissions,
        <li> "security_unix_acl"        - UNIX and NFSv4 ACL,
        <li> "security_unix_sd"         - UNIX and NT ACL,
        <li> "security_mixed_modebits"  - MIXED and UNIX
        permissions,
        <li> "security_mixed_acl"       - MIXED and NFSv4 ACL,
        <li> "security_mixed_sd"        - MIXED and NT ACL,
        <li> "security_ntfs_modebits"   - NTFS and UNIX
        permissions,
        <li> "security_ntfs_acl"        - NTFS and NT ACL,
        <li> "security_ntfs_sd"         - NTFS and NT ACL,
        <li> "security_unix"            - UNIX,
        <li> "security_mixed"           - MIXED,
        <li> "security_ntfs"            - NTFS,
        <li> "security_modebits"        - UNIX permissions,
        <li> "security_acl"             - ACL,
        <li> "security_sd"              - SD
        </ul>
        """
        return self._security_style
    @security_style.setter
    def security_style(self, val):
        if val != None:
            self.validate('security_style', val)
        self._security_style = val
    
    _seqnum = None
    @property
    def seqnum(self):
        """
        The sequence number of the permission tracing event.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._seqnum
    @seqnum.setter
    def seqnum(self, val):
        if val != None:
            self.validate('seqnum', val)
        self._seqnum = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The Vserver on which the permission tracing event
        occured.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _result = None
    @property
    def result(self):
        """
        A brief explanation of the result of the security check.
        Attributes: required-for-create, non-modifiable
        """
        return self._result
    @result.setter
    def result(self, val):
        if val != None:
            self.validate('result', val)
        self._result = val
    
    _path = None
    @property
    def path(self):
        """
        The path of the file whose access triggered the
        permission tracing event.
        Attributes: required-for-create, non-modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _keytime = None
    @property
    def keytime(self):
        """
        The date and time of day when the persmission tracing
        event occured.
        Attributes: required-for-create, non-modifiable
        """
        return self._keytime
    @keytime.setter
    def keytime(self, val):
        if val != None:
            self.validate('keytime', val)
        self._keytime = val
    
    @staticmethod
    def get_api_name():
          return "security-trace-results-logs"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'index',
            'user-name',
            'client-ip',
            'security-style',
            'seqnum',
            'vserver',
            'result',
            'path',
            'keytime',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'index': { 'class': int, 'is_list': False, 'required': 'optional' },
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'client_ip': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'security_style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'seqnum': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'result': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'keytime': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

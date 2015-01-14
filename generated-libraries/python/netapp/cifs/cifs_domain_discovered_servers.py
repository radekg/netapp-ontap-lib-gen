from netapp.netapp_object import NetAppObject

class CifsDomainDiscoveredServers(NetAppObject):
    """
    List of servers discovered by the cluster.
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
        The name of the node on which server discovery was done.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _prefer_type = None
    @property
    def prefer_type(self):
        """
        The preference level of the server that was discovered.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "unknown"   - The preference level of this server
        is unknown.,
        <li> "preferred" - This server was administratively
        marked as a preferred server due to its presence in the
        list of preferred servers.,
        <li> "favored"   - This server was marked as favored by
        the server discovery process by virtue of site
        membership.,
        <li> "adequate"  - This server was discovered by the
        server discovery process and can be used, but has no
        preference associated with it.
        </ul>
        """
        return self._prefer_type
    @prefer_type.setter
    def prefer_type(self, val):
        if val != None:
            self.validate('prefer_type', val)
        self._prefer_type = val
    
    _domain = None
    @property
    def domain(self):
        """
        The Active Directory domain that the discovered server is
        a member of.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._domain
    @domain.setter
    def domain(self, val):
        if val != None:
            self.validate('domain', val)
        self._domain = val
    
    _name = None
    @property
    def name(self):
        """
        The hostname of the server that was discovered.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _server_type = None
    @property
    def server_type(self):
        """
        The type of the server that was discovered.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "unknown"   - The server type is not known,
        <li> "kerberos"  - Kerberos server,
        <li> "ms_ldap"   - Microsoft Lightweight Directory
        Access Protocol (LDAP) server,
        <li> "ms_dc"     - Microsoft Domain Controller,
        <li> "ldap"      - Lightweight Directory Access
        Protocol (LDAP) server,
        <li> "nis"       - Network Information Service (NIS)
        server
        </ul>
        """
        return self._server_type
    @server_type.setter
    def server_type(self, val):
        if val != None:
            self.validate('server_type', val)
        self._server_type = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver which scopes the discovered
        servers.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _status = None
    @property
    def status(self):
        """
        The status of the connection to the server that was
        discovered.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "ok"             - The connection to this server
        is usable.,
        <li> "unavailable"    - This server is currently
        unavailable for use.,
        <li> "slow"           - The connection to this server
        is usable but slow.,
        <li> "expired"        - The connection to this server
        has expired.,
        <li> "undetermined"   - A connection to this server has
        not been attempted.,
        <li> "unreachable"    - This server is currently
        unreachable.
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _address = None
    @property
    def address(self):
        """
        The IP address of the server that was discovered.
        Attributes: non-creatable, non-modifiable
        """
        return self._address
    @address.setter
    def address(self, val):
        if val != None:
            self.validate('address', val)
        self._address = val
    
    @staticmethod
    def get_api_name():
          return "cifs-domain-discovered-servers"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'prefer-type',
            'domain',
            'name',
            'server-type',
            'vserver',
            'status',
            'address',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'prefer_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

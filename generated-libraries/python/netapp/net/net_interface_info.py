from netapp.netapp_object import NetAppObject

class NetInterfaceInfo(NetAppObject):
    """
    Network interface information
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
    
    _use_failover_group = None
    @property
    def use_failover_group(self):
        """
        Specifies whether failover rules are automatically
        created, manually created by the administrator, or
        disabled.
        For FCP and iSCSI LIFs, the default policy is 'disabled';
        for NFS, CIFs and fcache LIFs, the default policy is
        'system_defined'.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "system_defined" - Failover targets generated
        automatically by the system,
        <li> "disabled"       - Failover targets generated
        manually by the admin,
        <li> "enabled"        - Failover targets defined by
        failover-group
        </ul>
        """
        return self._use_failover_group
    @use_failover_group.setter
    def use_failover_group(self, val):
        if val != None:
            self.validate('use_failover_group', val)
        self._use_failover_group = val
    
    _comment = None
    @property
    def comment(self):
        """
        Comment
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _is_ipv4_link_local = None
    @property
    def is_ipv4_link_local(self):
        """
        If true, automatically configure an interface with an
        IPv4 address.
        User can configure an interface by explicitly specifying
        &lt;address&gt; and &lt;netmask&gt (or
        &lt;netmask-length&gt;); or by enabling
        is-ipv4-link-local to true.
        Attributes: optional-for-create, modifiable
        """
        return self._is_ipv4_link_local
    @is_ipv4_link_local.setter
    def is_ipv4_link_local(self, val):
        if val != None:
            self.validate('is_ipv4_link_local', val)
        self._is_ipv4_link_local = val
    
    _data_protocols = None
    @property
    def data_protocols(self):
        """
        Specifies the list of data protocols configured on the
        LIF.
        By default, the values in this element are nfs, cifs and
        fcache. Other supported protocols are iscsi and fcp.
        A LIF can be configured to not support any data protocols
        by specifying 'none'.
        Protocol values of none, iscsi or fcp can't be combined
        with any other data protocol(s).
        Attributes: optional-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "nfs"       - Used for NFS connections,
        <li> "cifs"      - Used for CIFS connections,
        <li> "iscsi"     - Used for iSCSI connections,
        <li> "fcp"       - Used for Fibre Channel connections,
        <li> "fcache"    - Used for FlexCache connections,
        <li> "none"      - Used for management. Does not serve
        any file protocols.
        </ul>
        """
        return self._data_protocols
    @data_protocols.setter
    def data_protocols(self, val):
        if val != None:
            self.validate('data_protocols', val)
        self._data_protocols = val
    
    _home_node = None
    @property
    def home_node(self):
        """
        Specifies the LIF's home node.
        Attributes: required-for-create, modifiable
        """
        return self._home_node
    @home_node.setter
    def home_node(self, val):
        if val != None:
            self.validate('home_node', val)
        self._home_node = val
    
    _dns_domain_name = None
    @property
    def dns_domain_name(self):
        """
        Specifies the unique, fully qualified domain name of the
        DNS zone of this LIF.
        Attributes: optional-for-create, modifiable
        """
        return self._dns_domain_name
    @dns_domain_name.setter
    def dns_domain_name(self, val):
        if val != None:
            self.validate('dns_domain_name', val)
        self._dns_domain_name = val
    
    _is_auto_revert = None
    @property
    def is_auto_revert(self):
        """
        If true, data LIF will revert to its home node under
        certain circumstances such as startup, and load balancing
        migration capability is disabled automatically.
        Default: false
        Attributes: optional-for-create, modifiable
        """
        return self._is_auto_revert
    @is_auto_revert.setter
    def is_auto_revert(self, val):
        if val != None:
            self.validate('is_auto_revert', val)
        self._is_auto_revert = val
    
    _lif_uuid = None
    @property
    def lif_uuid(self):
        """
        Available in Data ONTAP 8.2 and later.
        Attributes: non-creatable, non-modifiable
        """
        return self._lif_uuid
    @lif_uuid.setter
    def lif_uuid(self, val):
        if val != None:
            self.validate('lif_uuid', val)
        self._lif_uuid = val
    
    _firewall_policy = None
    @property
    def firewall_policy(self):
        """
        Specifies the firewall policy for the LIF.
        Default firewall-policy is set as per the following
        table:
        <ul>
        <li> 'LIF Role    Protocols   Default policy',
        <li> '-------     ---------   --------------',
        <li> 'data         none             mgmt',
        <li> 'data         any              data',
        <li> 'node_mgmt    any              mgmt',
        <li> 'cluster_mgmt any              mgmt',
        <li> 'cluster      any              cluster',
        <li> 'intercluster any              intercluster'
        </ul>
        Attributes: optional-for-create, modifiable
        """
        return self._firewall_policy
    @firewall_policy.setter
    def firewall_policy(self, val):
        if val != None:
            self.validate('firewall_policy', val)
        self._firewall_policy = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Specifies the Vserver name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _role = None
    @property
    def role(self):
        """
        Specifies the role of the LIF.
        Default: data
        Attributes: required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "undef"          - No defined role,
        <li> "cluster"        - Used for communication using
        the private cluster network,
        <li> "data"           - Used for communicating with
        file service clients,
        <li> "node_mgmt"      - Used by administrators to
        configure the node,
        <li> "intercluster"   - Used for communication with a
        different cluster,
        <li> "cluster_mgmt"   - Used by administrators to
        configure the cluster
        </ul>
        """
        return self._role
    @role.setter
    def role(self, val):
        if val != None:
            self.validate('role', val)
        self._role = val
    
    _netmask_length = None
    @property
    def netmask_length(self):
        """
        Specifies number of bits in the netmask.
        Attributes: optional-for-create, modifiable
        """
        return self._netmask_length
    @netmask_length.setter
    def netmask_length(self, val):
        if val != None:
            self.validate('netmask_length', val)
        self._netmask_length = val
    
    _operational_status = None
    @property
    def operational_status(self):
        """
        Specifies the operational status of the LIF.
        Possible values:
        <ul>
        <li> 'up',
        <li> 'down',
        <li> 'unknown'
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._operational_status
    @operational_status.setter
    def operational_status(self, val):
        if val != None:
            self.validate('operational_status', val)
        self._operational_status = val
    
    _netmask = None
    @property
    def netmask(self):
        """
        Specifies the LIF's netmask.
        This element is valid for all data protocols except FCP.
        Attributes: optional-for-create, modifiable
        """
        return self._netmask
    @netmask.setter
    def netmask(self, val):
        if val != None:
            self.validate('netmask', val)
        self._netmask = val
    
    _failover_policy = None
    @property
    def failover_policy(self):
        """
        Specifies the failover policy for the LIF.
        For FCP and iSCSI LIFs, the only failover policy is
        'disabled'; for NFS, CIFs and fcache LIFs, the default
        policy is 'nextavail'.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "nextavail" - Next failover target selected based
        on next port in failover targets list, preferring local
        ports first,
        <li> "priority"  - Next failover target selected based
        on first available port in failover targets list,
        <li> "disabled"  - Failover disabled
        </ul>
        """
        return self._failover_policy
    @failover_policy.setter
    def failover_policy(self, val):
        if val != None:
            self.validate('failover_policy', val)
        self._failover_policy = val
    
    _address = None
    @property
    def address(self):
        """
        Specifies the LIF's IP address.
        This element is valid for all data protocols except FCP.
        Attributes: optional-for-create, modifiable
        """
        return self._address
    @address.setter
    def address(self, val):
        if val != None:
            self.validate('address', val)
        self._address = val
    
    _address_family = None
    @property
    def address_family(self):
        """
        Address family
        Attributes: non-creatable, non-modifiable
        """
        return self._address_family
    @address_family.setter
    def address_family(self, val):
        if val != None:
            self.validate('address_family', val)
        self._address_family = val
    
    _current_port = None
    @property
    def current_port(self):
        """
        The port on which the LIF currently resides.
        Upon LIF migration 'current-port' may be different from
        'home-port'.
        Attributes: non-creatable, non-modifiable
        """
        return self._current_port
    @current_port.setter
    def current_port(self, val):
        if val != None:
            self.validate('current_port', val)
        self._current_port = val
    
    _current_node = None
    @property
    def current_node(self):
        """
        The node on which the LIF currently resides.
        Upon LIF migration 'current-node' may be different from
        'home-node'.
        Attributes: non-creatable, non-modifiable
        """
        return self._current_node
    @current_node.setter
    def current_node(self, val):
        if val != None:
            self.validate('current_node', val)
        self._current_node = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Specifies the logical interface (LIF) name.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    _routing_group_name = None
    @property
    def routing_group_name(self):
        """
        Specifies the routing group, which enables multiple
        logical interfaces to share a set of routing table
        entries.
        For example:
        d192.168.1.0/24 ('d' stands for data LIF and
        192.168.1.0/24 is subnet)
        c192.168.1.0/24 ('c' stands for cluster LIF and
        192.168.1.0/24 is subnet)
        n192.168.1.0/24 ('n' stands for node management LIF and
        192.168.1.0/24 is subnet)
        dfd20:13::0/50  ('d' stands for data LIF and
        fd20:13::0/50 is IPv6 subnet)
        Attributes: optional-for-create, modifiable
        """
        return self._routing_group_name
    @routing_group_name.setter
    def routing_group_name(self, val):
        if val != None:
            self.validate('routing_group_name', val)
        self._routing_group_name = val
    
    _listen_for_dns_query = None
    @property
    def listen_for_dns_query(self):
        """
        If True, this IP address will listen for DNS queries for
        the dns-zone specified.
        Attributes: optional-for-create, modifiable
        """
        return self._listen_for_dns_query
    @listen_for_dns_query.setter
    def listen_for_dns_query(self, val):
        if val != None:
            self.validate('listen_for_dns_query', val)
        self._listen_for_dns_query = val
    
    _administrative_status = None
    @property
    def administrative_status(self):
        """
        Specifies the administrative status of the LIF.
        The administrative status can differ from the operational
        status; for instance, if you specify the status as up but
        a network problem prevents the interface from
        functioning, the operational status remains as down.
        Possible values:
        <ul>
        <li> 'up',
        <li> 'down',
        <li> 'unknown'
        </ul>
        Attributes: optional-for-create, modifiable
        """
        return self._administrative_status
    @administrative_status.setter
    def administrative_status(self, val):
        if val != None:
            self.validate('administrative_status', val)
        self._administrative_status = val
    
    _failover_group = None
    @property
    def failover_group(self):
        """
        Specifies the failover group name.
        Attributes: optional-for-create, modifiable
        """
        return self._failover_group
    @failover_group.setter
    def failover_group(self, val):
        if val != None:
            self.validate('failover_group', val)
        self._failover_group = val
    
    _home_port = None
    @property
    def home_port(self):
        """
        Specifies the LIF's home port.
        Attributes: required-for-create, modifiable
        """
        return self._home_port
    @home_port.setter
    def home_port(self, val):
        if val != None:
            self.validate('home_port', val)
        self._home_port = val
    
    _is_home = None
    @property
    def is_home(self):
        """
        True if LIF is currently on 'home-node' and 'home-port'.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_home
    @is_home.setter
    def is_home(self, val):
        if val != None:
            self.validate('is_home', val)
        self._is_home = val
    
    @staticmethod
    def get_api_name():
          return "net-interface-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'use-failover-group',
            'comment',
            'is-ipv4-link-local',
            'data-protocols',
            'home-node',
            'dns-domain-name',
            'is-auto-revert',
            'lif-uuid',
            'firewall-policy',
            'vserver',
            'role',
            'netmask-length',
            'operational-status',
            'netmask',
            'failover-policy',
            'address',
            'address-family',
            'current-port',
            'current-node',
            'interface-name',
            'routing-group-name',
            'listen-for-dns-query',
            'administrative-status',
            'failover-group',
            'home-port',
            'is-home',
        ]
    
    def describe_properties(self):
        return {
            'use_failover_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_ipv4_link_local': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'data_protocols': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'home_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dns_domain_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_auto_revert': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'lif_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'firewall_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'role': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'netmask_length': { 'class': int, 'is_list': False, 'required': 'optional' },
            'operational_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'netmask': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'failover_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'address_family': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'routing_group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'listen_for_dns_query': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'administrative_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'failover_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'home_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_home': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }

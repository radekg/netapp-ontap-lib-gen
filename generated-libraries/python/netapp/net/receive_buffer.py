from netapp.netapp_object import NetAppObject

class ReceiveBuffer(NetAppObject):
    """
    Receive buffer window size configuration
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
    
    _receive_buffer = None
    @property
    def receive_buffer(self):
        """
        If receive-auto-tune is false, receive buffer size in
        kilobytes (1024).  If receive-auto-tune flag is true,
        this value has no effect.  The default value is 2048 for
        the ctlopcp service using the WAN network type, and 256
        in other cases.
        Attributes: required-for-create, modifiable
        """
        return self._receive_buffer
    @receive_buffer.setter
    def receive_buffer(self, val):
        if val != None:
            self.validate('receive_buffer', val)
        self._receive_buffer = val
    
    _receive_auto_tune = None
    @property
    def receive_auto_tune(self):
        """
        If true, allow the system to automatically adjust the
        receive buffer size.  The default value is false for the
        ctlopcp service using the LAN network type, and true in
        all other cases.
        Attributes: required-for-create, modifiable
        """
        return self._receive_auto_tune
    @receive_auto_tune.setter
    def receive_auto_tune(self, val):
        if val != None:
            self.validate('receive_auto_tune', val)
        self._receive_auto_tune = val
    
    _protocol = None
    @property
    def protocol(self):
        """
        The network layer 4 protocol type
        Attributes: key, required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "udp"  - UDP,
        <li> "tcp"  - TCP,
        <li> "na"   - not_available
        </ul>
        """
        return self._protocol
    @protocol.setter
    def protocol(self, val):
        if val != None:
            self.validate('protocol', val)
        self._protocol = val
    
    _network = None
    @property
    def network(self):
        """
        The network topology classification
        Attributes: key, required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "wan"       ,
        <li> "lan"       ,
        <li> "undefined"
        </ul>
        """
        return self._network
    @network.setter
    def network(self, val):
        if val != None:
            self.validate('network', val)
        self._network = val
    
    _service = None
    @property
    def service(self):
        """
        The stream protocol connection classification
        Attributes: key, required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "mount"          - Mount stream protocol,
        <li> "nfs"            - NFS stream protocol,
        <li> "nfs_v2"         - NFS version 2 stream protocol,
        <li> "nfs_v3"         - NFS version 3 stream protocol,
        <li> "nlm_v4"         - Network lock manager stream
        protocol,
        <li> "sm"             - Session Manager stream
        protocol,
        <li> "ftp_ctrl"       - FTP control stream protocol,
        <li> "ftp_data"       - FTP data stream protocol,
        <li> "http_1_0"       - HTTP version 1 stream
        protocol,
        <li> "http_1_1"       - HTTP version 1.1 stream
        protocol,
        <li> "iscsi"          - ISCSI stream protocol,
        <li> "cifs_srv"       - CIFS server stream protocol,
        <li> "cifs_nam"       - CIFS name server stream
        protocol,
        <li> "loopback"       - loopback stream protocol,
        <li> "rf"             - RC stream protocol,
        <li> "rawscp"         - Raw secure copy stream
        protocol,
        <li> "discard"        - Descard stream protocol,
        <li> "port_map"       - Port map stream protocol,
        <li> "pass_thru"      - Passthru stream protocol,
        <li> "rclopcp"        - Rc connection stream protocol,
        <li> "nfs_v4"         - NFS version 4 stream protocol,
        <li> "fcache"         - Flex cache stream protocol,
        <li> "ctlopcp"        - Ct connection stream protocol,
        <li> "rquota"         - Rquota stream protocol,
        <li> "cifs_msrpc"     - CIFS MsRpc stream protocol,
        <li> "unknown"        - unknown protocol
        </ul>
        """
        return self._service
    @service.setter
    def service(self, val):
        if val != None:
            self.validate('service', val)
        self._service = val
    
    @staticmethod
    def get_api_name():
          return "receive-buffer"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'receive-buffer',
            'receive-auto-tune',
            'protocol',
            'network',
            'service',
        ]
    
    def describe_properties(self):
        return {
            'receive_buffer': { 'class': int, 'is_list': False, 'required': 'optional' },
            'receive_auto_tune': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'network': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'service': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

from netapp.netapp_object import NetAppObject

class CertificateFileInfo(NetAppObject):
    """
    Information about location of certificate
    files
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
    
    _certificate_authority = None
    @property
    def certificate_authority(self):
        """
        Certificate Authority.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._certificate_authority
    @certificate_authority.setter
    def certificate_authority(self, val):
        if val != None:
            self.validate('certificate_authority', val)
        self._certificate_authority = val
    
    _protocol = None
    @property
    def protocol(self):
        """
        Protocol
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "ssl"
        </ul>
        """
        return self._protocol
    @protocol.setter
    def protocol(self, val):
        if val != None:
            self.validate('protocol', val)
        self._protocol = val
    
    _file = None
    @property
    def file(self):
        """
        Type of file.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "certificate"    - Public Key,
        <li> "key"            - Private Key,
        <li> "crl"            - Certificate Revocation List
        </ul>
        """
        return self._file
    @file.setter
    def file(self, val):
        if val != None:
            self.validate('file', val)
        self._file = val
    
    _exists = None
    @property
    def exists(self):
        """
        Certificate File Exists
        Attributes: non-creatable, non-modifiable
        """
        return self._exists
    @exists.setter
    def exists(self, val):
        if val != None:
            self.validate('exists', val)
        self._exists = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of vserver.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The node on which the file exists.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Serial number of certificate.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _common_name = None
    @property
    def common_name(self):
        """
        Represents the domain name in FQDN form that specifies
        its exact location in the tree hierarchy of the Domain
        Name System (DNS).
        Attributes: key, non-creatable, non-modifiable
        """
        return self._common_name
    @common_name.setter
    def common_name(self, val):
        if val != None:
            self.validate('common_name', val)
        self._common_name = val
    
    _path = None
    @property
    def path(self):
        """
        Path of the file in the file system.
        Attributes: non-creatable, non-modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _type = None
    @property
    def type(self):
        """
        Type of certificate.
        <p>
        Possible values:
        <ul>
        <li> 'server'       - Server certificate,
        <li> 'root_ca'      - Self-Signed Root CA,
        <li> 'client_ca'    - CA who signed user certificates
        on client',
        <li> 'server_ca'    - CA who signed user certificates
        on server',
        <li> 'server_chain' - Intermediate certificate for
        server authentication
        </ul>
        Attributes: key, non-creatable, non-modifiable
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    @staticmethod
    def get_api_name():
          return "certificate-file-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'certificate-authority',
            'protocol',
            'file',
            'exists',
            'vserver',
            'node-name',
            'serial-number',
            'common-name',
            'path',
            'type',
        ]
    
    def describe_properties(self):
        return {
            'certificate_authority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'exists': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'common_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

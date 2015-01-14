from netapp.netapp_object import NetAppObject

class CifsSymlink(NetAppObject):
    """
    CIFS symbolic link path mapping configuration.
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
    
    _unix_path = None
    @property
    def unix_path(self):
        """
        This field specifies the UNIX path prefix to be matched
        for the mapping. If the prefix of the target path in the
        symbolic link matches against this field, this entry of
        symbolic link path mapping would be used. The path is a
        UTF-8 string and supports localization. The path must
        start and end with a forward slash ('/'). For example
        '/usr/local/'.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._unix_path
    @unix_path.setter
    def unix_path(self, val):
        if val != None:
            self.validate('unix_path', val)
        self._unix_path = val
    
    _cifs_server = None
    @property
    def cifs_server(self):
        """
        This field specifies the destination CIFS server name for
        the mapping to which the symbolic link is mapped. The
        default is the local CIFS server. The field needs to be
        specified if the locality of the symbolic link is
        'widelink'. This can be either a DNS name, NetBIOS name
        or an IP address. If a DNS name or a NetBIOS name are
        specified, the CIFS client configuration should be such
        that it is capable of resolving the CIFS server name to
        the correct IP address.
        Attributes: optional-for-create, modifiable
        """
        return self._cifs_server
    @cifs_server.setter
    def cifs_server(self, val):
        if val != None:
            self.validate('cifs_server', val)
        self._cifs_server = val
    
    _locality = None
    @property
    def locality(self):
        """
        This field specifies whether the CIFS symbolic link is a
        local link or wide link. A local symbolic link maps to
        the local CIFS share, whereas a wide symbolic link maps
        to any CIFS share on the network. If the CIFS server
        matches the VServer's NetBIOS name then the default value
        is local otherwise widelink.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "local"     - Share On This VServer,
        <li> "widelink"  - Share On Another CIFS Server
        </ul>
        """
        return self._locality
    @locality.setter
    def locality(self, val):
        if val != None:
            self.validate('locality', val)
        self._locality = val
    
    _share_name = None
    @property
    def share_name(self):
        """
        This field specifies the CIFS share name on the
        destination CIFS server to which the symbolic link is
        mapped. This is a UTF-8 string and supports
        localization.
        Attributes: required-for-create, modifiable
        """
        return self._share_name
    @share_name.setter
    def share_name(self, val):
        if val != None:
            self.validate('share_name', val)
        self._share_name = val
    
    _cifs_path = None
    @property
    def cifs_path(self):
        """
        This field specifies the CIFS path on the destination to
        which the symbolic link maps. The final path is generated
        by concatenating the CIFS server name, the share name,
        the cifs-path and the remaining path in the symbolic link
        left after the prefix match. This value is specified by
        using a UNIX-style path name. The trailing forward slash
        is required for the full path name to be properly
        interpreted. This is a UTF-8 string and supports
        localization.
        Attributes: required-for-create, modifiable
        """
        return self._cifs_path
    @cifs_path.setter
    def cifs_path(self, val):
        if val != None:
            self.validate('cifs_path', val)
        self._cifs_path = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver associated with this CIFS
        server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    @staticmethod
    def get_api_name():
          return "cifs-symlink"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'unix-path',
            'cifs-server',
            'locality',
            'share-name',
            'cifs-path',
            'vserver',
        ]
    
    def describe_properties(self):
        return {
            'unix_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cifs_server': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'locality': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'share_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cifs_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

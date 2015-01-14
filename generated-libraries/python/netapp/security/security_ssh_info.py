from netapp.netapp_object import NetAppObject

class SecuritySshInfo(NetAppObject):
    """
    Provide SSH configuration
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
    
    _ciphers = None
    @property
    def ciphers(self):
        """
        List of SSH Ciphers enabled.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "aes256_ctr"     ,
        <li> "aes192_ctr"     ,
        <li> "aes128_ctr"     ,
        <li> "aes256_cbc"     ,
        <li> "aes192_cbc"     ,
        <li> "aes128_cbc"     ,
        <li> "3des_cbc"
        </ul>
        """
        return self._ciphers
    @ciphers.setter
    def ciphers(self, val):
        if val != None:
            self.validate('ciphers', val)
        self._ciphers = val
    
    _vserver_name = None
    @property
    def vserver_name(self):
        """
        Name of Vserver.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver_name
    @vserver_name.setter
    def vserver_name(self, val):
        if val != None:
            self.validate('vserver_name', val)
        self._vserver_name = val
    
    _key_exchange_algorithms = None
    @property
    def key_exchange_algorithms(self):
        """
        List of SSH key exchange algorithms enabled.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "diffie_hellman_group_exchange_sha256"    ,
        <li> "diffie_hellman_group_exchange_sha1"      ,
        <li> "diffie_hellman_group14_sha1"             ,
        <li> "diffie_hellman_group1_sha1"
        </ul>
        """
        return self._key_exchange_algorithms
    @key_exchange_algorithms.setter
    def key_exchange_algorithms(self, val):
        if val != None:
            self.validate('key_exchange_algorithms', val)
        self._key_exchange_algorithms = val
    
    @staticmethod
    def get_api_name():
          return "security-ssh-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ciphers',
            'vserver-name',
            'key-exchange-algorithms',
        ]
    
    def describe_properties(self):
        return {
            'ciphers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_exchange_algorithms': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }

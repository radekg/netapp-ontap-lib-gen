from netapp.nfs.exports_hostname_info import ExportsHostnameInfo
from netapp.nfs.sec_flavor_info import SecFlavorInfo
from netapp.netapp_object import NetAppObject

class SecurityRuleInfo(NetAppObject):
    """
    Information on hostnames and security availability for the
    hosts. ORDER MATTERS for the hostnames in 'read-only' and
    'read-write' privileges. Please see documentation for exportfs
    command or etc/exports file for complete details.
    """
    
    _root = None
    @property
    def root(self):
        """
        Array of hostnames which have roots with 'read-write' or
        'read-only' privileges.
        """
        return self._root
    @root.setter
    def root(self, val):
        if val != None:
            self.validate('root', val)
        self._root = val
    
    _sec_flavor = None
    @property
    def sec_flavor(self):
        """
        List of possible security flavors this rule supports.
        Default security is &quot;sys&quot;.
        In Data ONTAP Cluster-Mode, all the security flavors
        supported by 7-Mode are not supported. Hence the security
        flavors supported in both the ONTAP versions
        [for reference: 'none','sys','krb5']  will be
        considered valid.
        """
        return self._sec_flavor
    @sec_flavor.setter
    def sec_flavor(self, val):
        if val != None:
            self.validate('sec_flavor', val)
        self._sec_flavor = val
    
    _read_write = None
    @property
    def read_write(self):
        """
        An array of hostnames which have read and write
        privileges for all the security flavors found in the
        'sec-flavor list'. Any hostname in 'read-only' must not
        be in 'read-write' also. By default, if no 'read-only' or
        'read-write' hosts are given, then 'read-write' contains
        a hostname of 'all-hosts'.
        """
        return self._read_write
    @read_write.setter
    def read_write(self, val):
        if val != None:
            self.validate('read_write', val)
        self._read_write = val
    
    _anon = None
    @property
    def anon(self):
        """
        All hosts with this user-id or username have root access
        to this directory.
        """
        return self._anon
    @anon.setter
    def anon(self, val):
        if val != None:
            self.validate('anon', val)
        self._anon = val
    
    _nosuid = None
    @property
    def nosuid(self):
        """
        If true, causes the server file system to silently ignore
        any attempt to enable the setuid or setgid mode bits.
        Default value is false.
        """
        return self._nosuid
    @nosuid.setter
    def nosuid(self, val):
        if val != None:
            self.validate('nosuid', val)
        self._nosuid = val
    
    _read_only = None
    @property
    def read_only(self):
        """
        An array of hostnames which only have read privileges
        for all the security flavors found in the sec-flavor
        list.
        """
        return self._read_only
    @read_only.setter
    def read_only(self, val):
        if val != None:
            self.validate('read_only', val)
        self._read_only = val
    
    @staticmethod
    def get_api_name():
          return "security-rule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'root',
            'sec-flavor',
            'read-write',
            'anon',
            'nosuid',
            'read-only',
        ]
    
    def describe_properties(self):
        return {
            'root': { 'class': ExportsHostnameInfo, 'is_list': True, 'required': 'optional' },
            'sec_flavor': { 'class': SecFlavorInfo, 'is_list': True, 'required': 'optional' },
            'read_write': { 'class': ExportsHostnameInfo, 'is_list': True, 'required': 'optional' },
            'anon': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nosuid': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'read_only': { 'class': ExportsHostnameInfo, 'is_list': True, 'required': 'optional' },
        }

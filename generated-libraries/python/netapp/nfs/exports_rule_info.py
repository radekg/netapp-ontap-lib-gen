from netapp.nfs.sec_flavor_info import SecFlavorInfo
from netapp.nfs.exports_hostname_info import ExportsHostnameInfo
from netapp.netapp_object import NetAppObject

class ExportsRuleInfo(NetAppObject):
    """
    Information necessary to create a new rule in the etc/exports
    file or for just adding a rule similar to the exportfs command.
    ORDER MATTERS for the hostnames in 'read-only' and
    'read-write' privileges. Please see documentation for exportfs
    command or etc/exports file for complete details.
    """
    
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
        privileges. Any hostname in read-only must not be in
        read-write also. By default, if no 'read-only' or
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
    
    _pathname = None
    @property
    def pathname(self):
        """
        In Data ONTAP 7-Mode, it must be directory name or file to
        export.
        In Data ONTAP Cluster-Mode, it must be the path of the
        volume or qtree to be exported such as
        &quot;vol/vol0&quot; or &quot;/vol/vol0/qtree0&quot;.
        """
        return self._pathname
    @pathname.setter
    def pathname(self, val):
        if val != None:
            self.validate('pathname', val)
        self._pathname = val
    
    _actual_pathname = None
    @property
    def actual_pathname(self):
        """
        In Data ONTAP 7-Mode, it must be pathname inside of
        the filer which is being exported. The default for
        this is value in 'pathname'.
        In Data ONTAP Cluster-Mode, this value must be an empty
        string.
        """
        return self._actual_pathname
    @actual_pathname.setter
    def actual_pathname(self, val):
        if val != None:
            self.validate('actual_pathname', val)
        self._actual_pathname = val
    
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
    
    _read_only = None
    @property
    def read_only(self):
        """
        An array of hostnames which only have read privileges.
        """
        return self._read_only
    @read_only.setter
    def read_only(self, val):
        if val != None:
            self.validate('read_only', val)
        self._read_only = val
    
    @staticmethod
    def get_api_name():
          return "exports-rule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'nosuid',
            'sec-flavor',
            'read-write',
            'anon',
            'pathname',
            'actual-pathname',
            'root',
            'read-only',
        ]
    
    def describe_properties(self):
        return {
            'nosuid': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'sec_flavor': { 'class': SecFlavorInfo, 'is_list': True, 'required': 'optional' },
            'read_write': { 'class': ExportsHostnameInfo, 'is_list': True, 'required': 'optional' },
            'anon': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pathname': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'actual_pathname': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'root': { 'class': ExportsHostnameInfo, 'is_list': True, 'required': 'optional' },
            'read_only': { 'class': ExportsHostnameInfo, 'is_list': True, 'required': 'optional' },
        }

from netapp.netapp_object import NetAppObject

class LicenseV2StatusInfo(NetAppObject):
    """
    Status information about a licensable package.
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
    
    _description = None
    @property
    def description(self):
        """
        Description of the licensed package.
        Attributes: non-creatable, non-modifiable
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    _expiration_time = None
    @property
    def expiration_time(self):
        """
        License expiration date.
        Attributes: non-creatable, non-modifiable
        """
        return self._expiration_time
    @expiration_time.setter
    def expiration_time(self, val):
        if val != None:
            self.validate('expiration_time', val)
        self._expiration_time = val
    
    _method = None
    @property
    def method(self):
        """
        Method in which a package is licensed in a cluster.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "none"      - None,
        <li> "license"   - License,
        <li> "site"      - Site,
        <li> "demo"      - Demo
        </ul>
        """
        return self._method
    @method.setter
    def method(self, val):
        if val != None:
            self.validate('method', val)
        self._method = val
    
    _package = None
    @property
    def package(self):
        """
        Name of the licensed package.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "base"                - Cluster Base License,
        <li> "nfs"                 - NFS License,
        <li> "cifs"                - CIFS License,
        <li> "iscsi"               - iSCSI License,
        <li> "fcp"                 - FCP License,
        <li> "cdmi"                - CDMI License,
        <li> "snaprestore"         - SnapRestore License,
        <li> "snapmirror"          - SnapMirror License,
        <li> "flexclone"           - FlexClone License,
        <li> "snapvault"           - SnapVault License,
        <li> "snaplock"            - SnapLock License,
        <li> "snapmanagersuite"    - SnapManagerSuite License,
        <li> "snapprotectapps"     - SnapProtectApp License,
        <li> "v_storageattach"     - Virtual Attached Storage License
        </ul>
        """
        return self._package
    @package.setter
    def package(self, val):
        if val != None:
            self.validate('package', val)
        self._package = val
    
    @staticmethod
    def get_api_name():
          return "license-v2-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'description',
            'expiration-time',
            'method',
            'package',
        ]
    
    def describe_properties(self):
        return {
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'expiration_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'method': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'package': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

from netapp.netapp_object import NetAppObject

class LicenseV2Cleanup(NetAppObject):
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
    
    _owner = None
    @property
    def owner(self):
        """
        Name of the controller associated with the license.
        Attributes: non-creatable, non-modifiable
        """
        return self._owner
    @owner.setter
    def owner(self, val):
        if val != None:
            self.validate('owner', val)
        self._owner = val
    
    _reason = None
    @property
    def reason(self):
        """
        The reason the license can be cleaned up.
        Attributes: non-creatable, non-modifiable
        """
        return self._reason
    @reason.setter
    def reason(self, val):
        if val != None:
            self.validate('reason', val)
        self._reason = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Serial number of the controller or cluster.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
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
          return "license-v2-cleanup"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'owner',
            'reason',
            'serial-number',
            'package',
        ]
    
    def describe_properties(self):
        return {
            'owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'package': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

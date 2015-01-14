from netapp.netapp_object import NetAppObject

class DiskOutageInfo(NetAppObject):
    """
    Information about a disk that is not in service.
    """
    
    _is_in_fdr = None
    @property
    def is_in_fdr(self):
        """
        True if disk has entry in the persistent Failed Disk
        Registry.  Omitted if excluded by 'desired-attributes'.
        """
        return self._is_in_fdr
    @is_in_fdr.setter
    def is_in_fdr(self, val):
        if val != None:
            self.validate('is_in_fdr', val)
        self._is_in_fdr = val
    
    _reason = None
    @property
    def reason(self):
        """
        Reason disk is not in service.
        Omitted if excluded by 'desired-attributes'.
        <p>
        Possible values:
        <ul>
        <li> "admin failed"    - Admin has persistently failed
        disk.
        <li> "admin removed"   - Admin requested spare disk
        to be removed from system.
        <li> "admin testing"   - Admin isolated disk for
        maintenance testing.
        <li> "bad label"       - Disk has bad RAID label.
        <li> "bypassed"        - Disk has been bypassed.
        <li> "failed"          - Disk is persistently failed.
        <li> "init failed"     - Disk failed initialization.
        <li> "label version"   - Disk has invalid RAID label
        version.
        <li> "labeled broken"  - Disk was persistently failed
        in a prior Data ONTAP
        release.
        <li> "labelmaint"      - Disk is isolated for online
        label maintenance.
        <li> "LUN resized"     - Array LUN was inappropriately
        resized.
        <li> "missing"         - Disk has gone missing.
        <li> "not responding"  - Disk is non-responsive.
        <li> "predict failure" - Disk failure is predicted.
        capacity than previously.
        <li> "rawsize shrank"  - Disk reporting smaller
        <li> "recovering"      - Disk is underoing recovery.
        <li> "sanitizing"      - Disk is in process of being
        sanitized.
        <li> "sanitized"       - Disk sanitization complete,
        but admin has not yet released
        disk back to the spare pool.
        in this release.
        <li> "SFO Disk"        - SFO disk, not supported on
        7-mode systems.
        <li> "SnapLock Disk"   - SnapLock disk, not supported.
        <li> "testing"         - System isolated disk for
        maintenance testing.
        <li> "unassigned"      - Disk ownership has not been
        assigned.
        <li> "unknown"         - Don't know reason disk is
        not in service.
        </ul>
        """
        return self._reason
    @reason.setter
    def reason(self, val):
        if val != None:
            self.validate('reason', val)
        self._reason = val
    
    @staticmethod
    def get_api_name():
          return "disk-outage-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-in-fdr',
            'reason',
        ]
    
    def describe_properties(self):
        return {
            'is_in_fdr': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'reason': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

from netapp.lock.op_lock import OpLock
from netapp.lock.share_lock import ShareLock
from netapp.lock.range_lock import RangeLock
from netapp.lock.pfs_lock import PfsLock
from netapp.lock.nlm_lock import NlmLock
from netapp.lock.fc_delegation_lock import FcDelegationLock
from netapp.lock.nfsv4_lock import Nfsv4Lock
from netapp.lock.cifs_lock import CifsLock
from netapp.netapp_object import NetAppObject

class LockStatusInfo(NetAppObject):
    """
    Information about a single lock.
    """
    
    _vif_id = None
    @property
    def vif_id(self):
        """
        Virtual interface id on which the lock request arrived.
        Refer to the description of "vif" in the input argument
        section.
        Range : [0..2^31-1]
        """
        return self._vif_id
    @vif_id.setter
    def vif_id(self, val):
        if val != None:
            self.validate('vif_id', val)
        self._vif_id = val
    
    _op_lock = None
    @property
    def op_lock(self):
        """
        Information about Opportunistic locks.
        """
        return self._op_lock
    @op_lock.setter
    def op_lock(self, val):
        if val != None:
            self.validate('op_lock', val)
        self._op_lock = val
    
    _share_lock = None
    @property
    def share_lock(self):
        """
        Information about share locks.
        """
        return self._share_lock
    @share_lock.setter
    def share_lock(self, val):
        if val != None:
            self.validate('share_lock', val)
        self._share_lock = val
    
    _lock_id = None
    @property
    def lock_id(self):
        """
        The 128-bit universally-unique identifier (UUID) of
        the lock.
        <p>
        UUIDs are formatted as 36-character strings.  These
        strings are composed of 32 hexadecimal characters
        broken up into five groupings separated by '-'s.  The
        first grouping has 8 hex characters, the second through
        fourth groupings have 4 hex characters each, and the
        fifth and final grouping has 12 hex characters.  Note
        that a leading '0x' is not used.
        """
        return self._lock_id
    @lock_id.setter
    def lock_id(self, val):
        if val != None:
            self.validate('lock_id', val)
        self._lock_id = val
    
    _file_name = None
    @property
    def file_name(self):
        """
        This is the file path on which the lock has been taken.
        The path is relative to the volume on which the file exists.
        The file-name format is "/volname/filepath". For example if
        the file is testdir/simple on volume root_vs0, then the
        returned path is /root_vs0/testdir/simple.
        """
        return self._file_name
    @file_name.setter
    def file_name(self, val):
        if val != None:
            self.validate('file_name', val)
        self._file_name = val
    
    _range_lock = None
    @property
    def range_lock(self):
        """
        Information about range lock.
        """
        return self._range_lock
    @range_lock.setter
    def range_lock(self, val):
        if val != None:
            self.validate('range_lock', val)
        self._range_lock = val
    
    _pfs_lock = None
    @property
    def pfs_lock(self):
        """
        Information about PFS locks
        """
        return self._pfs_lock
    @pfs_lock.setter
    def pfs_lock(self, val):
        if val != None:
            self.validate('pfs_lock', val)
        self._pfs_lock = val
    
    _client_id = None
    @property
    def client_id(self):
        """
        This is used to identify the client machine that owns the
        lock. "client-id" is a byte string that the n-blade generates
        for each lock request and is opaque to the d-blade. This
        value can be used as the "host" parameter for new
        invocations of d-lock-status-list-iter or d-lock-break.
        """
        return self._client_id
    @client_id.setter
    def client_id(self, val):
        if val != None:
            self.validate('client_id', val)
        self._client_id = val
    
    _blocking_lock_id = None
    @property
    def blocking_lock_id(self):
        """
        This is the 128-bit universally-unique identifier (UUID) of the lock
        on which the current lock is waiting.  Note that this field is
        applicable only if the lock is a "waiting" lock.
        """
        return self._blocking_lock_id
    @blocking_lock_id.setter
    def blocking_lock_id(self, val):
        if val != None:
            self.validate('blocking_lock_id', val)
        self._blocking_lock_id = val
    
    _nlm_lock = None
    @property
    def nlm_lock(self):
        """
        Information about NLM(Nfsv2/Nfsv3) lock.
        """
        return self._nlm_lock
    @nlm_lock.setter
    def nlm_lock(self, val):
        if val != None:
            self.validate('nlm_lock', val)
        self._nlm_lock = val
    
    _owner_id = None
    @property
    def owner_id(self):
        """
        This is used to identify the lock owner.
        owner-id is also a byte string. Similar to the "client-id"
        value, this is n-blade generated, opaque to d-blade.
        This value can be used as "owner" parameter for new
        invocations of d-lock-status-list-iter or d-lock-break.
        """
        return self._owner_id
    @owner_id.setter
    def owner_id(self, val):
        if val != None:
            self.validate('owner_id', val)
        self._owner_id = val
    
    _fc_delegation_lock = None
    @property
    def fc_delegation_lock(self):
        """
        Information about FlexCache delegation locks.
        """
        return self._fc_delegation_lock
    @fc_delegation_lock.setter
    def fc_delegation_lock(self, val):
        if val != None:
            self.validate('fc_delegation_lock', val)
        self._fc_delegation_lock = val
    
    _nfsv4_lock = None
    @property
    def nfsv4_lock(self):
        """
        Information about NFSv4 lock.
        """
        return self._nfsv4_lock
    @nfsv4_lock.setter
    def nfsv4_lock(self, val):
        if val != None:
            self.validate('nfsv4_lock', val)
        self._nfsv4_lock = val
    
    _lock_state = None
    @property
    def lock_state(self):
        """
        This field describes the current state of this lock.
        Possible values are:
        <ul>
        <li>"unknown",</li>
        <li>"granted",</li>
        <li>"waiting",</li>
        <li>"revoking",</li>
        <li>"revoked".</li>
        </ul>
        """
        return self._lock_state
    @lock_state.setter
    def lock_state(self, val):
        if val != None:
            self.validate('lock_state', val)
        self._lock_state = val
    
    _volume_dsid = None
    @property
    def volume_dsid(self):
        """
        The identity of the volume on which the lock is held.
        <p>
        The legal choice for a volume identifer is the Volume DSID.
        DSIDs are formatted as 16-character strings composed
        of 16 hex characters prefixed with '0x'.
        """
        return self._volume_dsid
    @volume_dsid.setter
    def volume_dsid(self, val):
        if val != None:
            self.validate('volume_dsid', val)
        self._volume_dsid = val
    
    _vserver_id = None
    @property
    def vserver_id(self):
        """
        Vserver to which the lock belongs. Refer to the description
        of "vserver" in the input argument section.
        Range : [0..2^31-1]
        """
        return self._vserver_id
    @vserver_id.setter
    def vserver_id(self, val):
        if val != None:
            self.validate('vserver_id', val)
        self._vserver_id = val
    
    _cifs_lock = None
    @property
    def cifs_lock(self):
        """
        Information about CIFS lock.
        """
        return self._cifs_lock
    @cifs_lock.setter
    def cifs_lock(self, val):
        if val != None:
            self.validate('cifs_lock', val)
        self._cifs_lock = val
    
    @staticmethod
    def get_api_name():
          return "lock-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vif-id',
            'op-lock',
            'share-lock',
            'lock-id',
            'file-name',
            'range-lock',
            'pfs-lock',
            'client-id',
            'blocking-lock-id',
            'nlm-lock',
            'owner-id',
            'fc-delegation-lock',
            'nfsv4-lock',
            'lock-state',
            'volume-dsid',
            'vserver-id',
            'cifs-lock',
        ]
    
    def describe_properties(self):
        return {
            'vif_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'op_lock': { 'class': OpLock, 'is_list': False, 'required': 'optional' },
            'share_lock': { 'class': ShareLock, 'is_list': False, 'required': 'optional' },
            'lock_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'file_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'range_lock': { 'class': RangeLock, 'is_list': False, 'required': 'optional' },
            'pfs_lock': { 'class': PfsLock, 'is_list': False, 'required': 'optional' },
            'client_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'blocking_lock_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nlm_lock': { 'class': NlmLock, 'is_list': False, 'required': 'optional' },
            'owner_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'fc_delegation_lock': { 'class': FcDelegationLock, 'is_list': False, 'required': 'optional' },
            'nfsv4_lock': { 'class': Nfsv4Lock, 'is_list': False, 'required': 'optional' },
            'lock_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume_dsid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vserver_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'cifs_lock': { 'class': CifsLock, 'is_list': False, 'required': 'optional' },
        }

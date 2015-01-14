from netapp.netapp_object import NetAppObject

class Nfsv4ClientStatsInfo(NetAppObject):
    """
    structure containing statistics for NFSv4 operations
    """
    
    _rename_ops = None
    @property
    def rename_ops(self):
        """
        total 'rename' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._rename_ops
    @rename_ops.setter
    def rename_ops(self, val):
        if val != None:
            self.validate('rename_ops', val)
        self._rename_ops = val
    
    _setattr_ops = None
    @property
    def setattr_ops(self):
        """
        total 'setattr' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._setattr_ops
    @setattr_ops.setter
    def setattr_ops(self, val):
        if val != None:
            self.validate('setattr_ops', val)
        self._setattr_ops = val
    
    _no_delegation_total = None
    @property
    def no_delegation_total(self):
        """
        total calls where a delegation could not be granted
        Range : [0..2^32-1].
        """
        return self._no_delegation_total
    @no_delegation_total.setter
    def no_delegation_total(self, val):
        if val != None:
            self.validate('no_delegation_total', val)
        self._no_delegation_total = val
    
    _lookup_ops = None
    @property
    def lookup_ops(self):
        """
        total 'lookup' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._lookup_ops
    @lookup_ops.setter
    def lookup_ops(self, val):
        if val != None:
            self.validate('lookup_ops', val)
        self._lookup_ops = val
    
    _lookupp_ops = None
    @property
    def lookupp_ops(self):
        """
        total 'lookupp' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._lookupp_ops
    @lookupp_ops.setter
    def lookupp_ops(self, val):
        if val != None:
            self.validate('lookupp_ops', val)
        self._lookupp_ops = val
    
    _readlink_ops = None
    @property
    def readlink_ops(self):
        """
        total 'readlink' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._readlink_ops
    @readlink_ops.setter
    def readlink_ops(self, val):
        if val != None:
            self.validate('readlink_ops', val)
        self._readlink_ops = val
    
    _open_downgrade_ops = None
    @property
    def open_downgrade_ops(self):
        """
        total 'open_downgrade' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._open_downgrade_ops
    @open_downgrade_ops.setter
    def open_downgrade_ops(self, val):
        if val != None:
            self.validate('open_downgrade_ops', val)
        self._open_downgrade_ops = val
    
    _compound_ops = None
    @property
    def compound_ops(self):
        """
        total 'compound' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._compound_ops
    @compound_ops.setter
    def compound_ops(self, val):
        if val != None:
            self.validate('compound_ops', val)
        self._compound_ops = val
    
    _access_ops = None
    @property
    def access_ops(self):
        """
        total 'access' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._access_ops
    @access_ops.setter
    def access_ops(self, val):
        if val != None:
            self.validate('access_ops', val)
        self._access_ops = val
    
    _putrootfh_ops = None
    @property
    def putrootfh_ops(self):
        """
        total 'putrootfh' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._putrootfh_ops
    @putrootfh_ops.setter
    def putrootfh_ops(self, val):
        if val != None:
            self.validate('putrootfh_ops', val)
        self._putrootfh_ops = val
    
    _lockt_ops = None
    @property
    def lockt_ops(self):
        """
        total 'lockt' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._lockt_ops
    @lockt_ops.setter
    def lockt_ops(self, val):
        if val != None:
            self.validate('lockt_ops', val)
        self._lockt_ops = val
    
    _badproc2_ops = None
    @property
    def badproc2_ops(self):
        """
        total 'badproc2' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._badproc2_ops
    @badproc2_ops.setter
    def badproc2_ops(self, val):
        if val != None:
            self.validate('badproc2_ops', val)
        self._badproc2_ops = val
    
    _open_ops = None
    @property
    def open_ops(self):
        """
        total 'open' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._open_ops
    @open_ops.setter
    def open_ops(self, val):
        if val != None:
            self.validate('open_ops', val)
        self._open_ops = val
    
    _verify_ops = None
    @property
    def verify_ops(self):
        """
        total 'verify' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._verify_ops
    @verify_ops.setter
    def verify_ops(self, val):
        if val != None:
            self.validate('verify_ops', val)
        self._verify_ops = val
    
    _restorefh_ops = None
    @property
    def restorefh_ops(self):
        """
        total 'restorefh' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._restorefh_ops
    @restorefh_ops.setter
    def restorefh_ops(self, val):
        if val != None:
            self.validate('restorefh_ops', val)
        self._restorefh_ops = val
    
    _write_delegation_total = None
    @property
    def write_delegation_total(self):
        """
        total calls where a write delegation was granted
        Range : [0..2^32-1].
        """
        return self._write_delegation_total
    @write_delegation_total.setter
    def write_delegation_total(self, val):
        if val != None:
            self.validate('write_delegation_total', val)
        self._write_delegation_total = val
    
    _delegpurge = None
    @property
    def delegpurge(self):
        """
        total 'delegpurge' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._delegpurge
    @delegpurge.setter
    def delegpurge(self, val):
        if val != None:
            self.validate('delegpurge', val)
        self._delegpurge = val
    
    _read_delegation_total = None
    @property
    def read_delegation_total(self):
        """
        total calls where a read delegation was granted
        Range : [0..2^32-1].
        """
        return self._read_delegation_total
    @read_delegation_total.setter
    def read_delegation_total(self, val):
        if val != None:
            self.validate('read_delegation_total', val)
        self._read_delegation_total = val
    
    _open_confirm_ops = None
    @property
    def open_confirm_ops(self):
        """
        total 'open_confirm' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._open_confirm_ops
    @open_confirm_ops.setter
    def open_confirm_ops(self, val):
        if val != None:
            self.validate('open_confirm_ops', val)
        self._open_confirm_ops = val
    
    _remove_ops = None
    @property
    def remove_ops(self):
        """
        total 'remove' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._remove_ops
    @remove_ops.setter
    def remove_ops(self, val):
        if val != None:
            self.validate('remove_ops', val)
        self._remove_ops = val
    
    _commit_ops = None
    @property
    def commit_ops(self):
        """
        total 'commit' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._commit_ops
    @commit_ops.setter
    def commit_ops(self, val):
        if val != None:
            self.validate('commit_ops', val)
        self._commit_ops = val
    
    _acls_set_total = None
    @property
    def acls_set_total(self):
        """
        number of ACLs set on files
        Range : [0..2^32-1].
        """
        return self._acls_set_total
    @acls_set_total.setter
    def acls_set_total(self, val):
        if val != None:
            self.validate('acls_set_total', val)
        self._acls_set_total = val
    
    _renew_ops = None
    @property
    def renew_ops(self):
        """
        total 'renew' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._renew_ops
    @renew_ops.setter
    def renew_ops(self, val):
        if val != None:
            self.validate('renew_ops', val)
        self._renew_ops = val
    
    _setclntid_ops = None
    @property
    def setclntid_ops(self):
        """
        total 'setclntid' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._setclntid_ops
    @setclntid_ops.setter
    def setclntid_ops(self, val):
        if val != None:
            self.validate('setclntid_ops', val)
        self._setclntid_ops = val
    
    _close_ops = None
    @property
    def close_ops(self):
        """
        total 'close' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._close_ops
    @close_ops.setter
    def close_ops(self, val):
        if val != None:
            self.validate('close_ops', val)
        self._close_ops = val
    
    _lock_ops = None
    @property
    def lock_ops(self):
        """
        total 'lock' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._lock_ops
    @lock_ops.setter
    def lock_ops(self, val):
        if val != None:
            self.validate('lock_ops', val)
        self._lock_ops = val
    
    _putfh_ops = None
    @property
    def putfh_ops(self):
        """
        total 'putfh' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._putfh_ops
    @putfh_ops.setter
    def putfh_ops(self, val):
        if val != None:
            self.validate('putfh_ops', val)
        self._putfh_ops = val
    
    _nverify_ops = None
    @property
    def nverify_ops(self):
        """
        total 'nverify' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._nverify_ops
    @nverify_ops.setter
    def nverify_ops(self, val):
        if val != None:
            self.validate('nverify_ops', val)
        self._nverify_ops = val
    
    _setclntid_cfm_ops = None
    @property
    def setclntid_cfm_ops(self):
        """
        total 'setclntid_cfm' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._setclntid_cfm_ops
    @setclntid_cfm_ops.setter
    def setclntid_cfm_ops(self, val):
        if val != None:
            self.validate('setclntid_cfm_ops', val)
        self._setclntid_cfm_ops = val
    
    _null_ops = None
    @property
    def null_ops(self):
        """
        total 'null' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._null_ops
    @null_ops.setter
    def null_ops(self, val):
        if val != None:
            self.validate('null_ops', val)
        self._null_ops = val
    
    _create_ops = None
    @property
    def create_ops(self):
        """
        total 'create' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._create_ops
    @create_ops.setter
    def create_ops(self, val):
        if val != None:
            self.validate('create_ops', val)
        self._create_ops = val
    
    _delegret_ops = None
    @property
    def delegret_ops(self):
        """
        total 'delegret' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._delegret_ops
    @delegret_ops.setter
    def delegret_ops(self, val):
        if val != None:
            self.validate('delegret_ops', val)
        self._delegret_ops = val
    
    _locku_ops = None
    @property
    def locku_ops(self):
        """
        total 'locku' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._locku_ops
    @locku_ops.setter
    def locku_ops(self, val):
        if val != None:
            self.validate('locku_ops', val)
        self._locku_ops = val
    
    _getattr_ops = None
    @property
    def getattr_ops(self):
        """
        total 'getattr' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._getattr_ops
    @getattr_ops.setter
    def getattr_ops(self, val):
        if val != None:
            self.validate('getattr_ops', val)
        self._getattr_ops = val
    
    _write_ops = None
    @property
    def write_ops(self):
        """
        total 'write' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._write_ops
    @write_ops.setter
    def write_ops(self, val):
        if val != None:
            self.validate('write_ops', val)
        self._write_ops = val
    
    _savefh_ops = None
    @property
    def savefh_ops(self):
        """
        total 'savefh' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._savefh_ops
    @savefh_ops.setter
    def savefh_ops(self, val):
        if val != None:
            self.validate('savefh_ops', val)
        self._savefh_ops = val
    
    _rlsowner_ops = None
    @property
    def rlsowner_ops(self):
        """
        total 'rlsowner' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._rlsowner_ops
    @rlsowner_ops.setter
    def rlsowner_ops(self, val):
        if val != None:
            self.validate('rlsowner_ops', val)
        self._rlsowner_ops = val
    
    _readdir_ops = None
    @property
    def readdir_ops(self):
        """
        total 'readdir' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._readdir_ops
    @readdir_ops.setter
    def readdir_ops(self, val):
        if val != None:
            self.validate('readdir_ops', val)
        self._readdir_ops = val
    
    _link_ops = None
    @property
    def link_ops(self):
        """
        total 'link' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._link_ops
    @link_ops.setter
    def link_ops(self, val):
        if val != None:
            self.validate('link_ops', val)
        self._link_ops = val
    
    _secinfo_ops = None
    @property
    def secinfo_ops(self):
        """
        total 'secinfo' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._secinfo_ops
    @secinfo_ops.setter
    def secinfo_ops(self, val):
        if val != None:
            self.validate('secinfo_ops', val)
        self._secinfo_ops = val
    
    _getfh_ops = None
    @property
    def getfh_ops(self):
        """
        total 'getfh' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._getfh_ops
    @getfh_ops.setter
    def getfh_ops(self, val):
        if val != None:
            self.validate('getfh_ops', val)
        self._getfh_ops = val
    
    _putpubfh_ops = None
    @property
    def putpubfh_ops(self):
        """
        total 'putpubfh' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._putpubfh_ops
    @putpubfh_ops.setter
    def putpubfh_ops(self, val):
        if val != None:
            self.validate('putpubfh_ops', val)
        self._putpubfh_ops = val
    
    _openattr_ops = None
    @property
    def openattr_ops(self):
        """
        total 'openattr' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._openattr_ops
    @openattr_ops.setter
    def openattr_ops(self, val):
        if val != None:
            self.validate('openattr_ops', val)
        self._openattr_ops = val
    
    _read_ops = None
    @property
    def read_ops(self):
        """
        total 'read' NFSv4 operations
        Range : [0..2^64-1].
        """
        return self._read_ops
    @read_ops.setter
    def read_ops(self, val):
        if val != None:
            self.validate('read_ops', val)
        self._read_ops = val
    
    @staticmethod
    def get_api_name():
          return "nfsv4-client-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'rename-ops',
            'setattr-ops',
            'no-delegation-total',
            'lookup-ops',
            'lookupp-ops',
            'readlink-ops',
            'open-downgrade-ops',
            'compound-ops',
            'access-ops',
            'putrootfh-ops',
            'lockt-ops',
            'badproc2-ops',
            'open-ops',
            'verify-ops',
            'restorefh-ops',
            'write-delegation-total',
            'delegpurge',
            'read-delegation-total',
            'open-confirm-ops',
            'remove-ops',
            'commit-ops',
            'acls-set-total',
            'renew-ops',
            'setclntid-ops',
            'close-ops',
            'lock-ops',
            'putfh-ops',
            'nverify-ops',
            'setclntid-cfm-ops',
            'null-ops',
            'create-ops',
            'delegret-ops',
            'locku-ops',
            'getattr-ops',
            'write-ops',
            'savefh-ops',
            'rlsowner-ops',
            'readdir-ops',
            'link-ops',
            'secinfo-ops',
            'getfh-ops',
            'putpubfh-ops',
            'openattr-ops',
            'read-ops',
        ]
    
    def describe_properties(self):
        return {
            'rename_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'setattr_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'no_delegation_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lookup_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lookupp_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'readlink_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'open_downgrade_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'compound_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'access_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'putrootfh_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lockt_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'badproc2_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'open_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'verify_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'restorefh_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'write_delegation_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'delegpurge': { 'class': int, 'is_list': False, 'required': 'optional' },
            'read_delegation_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'open_confirm_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'remove_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'commit_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'acls_set_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'renew_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'setclntid_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'close_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lock_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'putfh_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'nverify_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'setclntid_cfm_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'null_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'create_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'delegret_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'locku_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'getattr_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'write_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'savefh_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'rlsowner_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'readdir_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'link_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'secinfo_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'getfh_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'putpubfh_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'openattr_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'read_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

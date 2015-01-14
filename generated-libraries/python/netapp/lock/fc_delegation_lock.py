from netapp.netapp_object import NetAppObject

class FcDelegationLock(NetAppObject):
    """
    Information about FlexCache delegations
    """
    
    _mode = None
    @property
    def mode(self):
        """
        This field describes the delegation mode.
        Possible values are:
        <ul>
        <li>"read",</li>
        <li>"write".</li>
        </ul>
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    _fileid = None
    @property
    def fileid(self):
        """
        Inode for the delegation.
        Range : [0..2^64-1]
        """
        return self._fileid
    @fileid.setter
    def fileid(self, val):
        if val != None:
            self.validate('fileid', val)
        self._fileid = val
    
    @staticmethod
    def get_api_name():
          return "fc-delegation-lock"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'mode',
            'fileid',
        ]
    
    def describe_properties(self):
        return {
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fileid': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

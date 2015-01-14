from netapp.igroup.initiator_group_list_info import InitiatorGroupListInfo
from netapp.netapp_object import NetAppObject

class IscsiInitiatorListEntryInfo(NetAppObject):
    """
    Information about a single initiator.
    """
    
    _tpgroup_tag = None
    @property
    def tpgroup_tag(self):
        """
        Tag of target portal group associated with
        this session.
        """
        return self._tpgroup_tag
    @tpgroup_tag.setter
    def tpgroup_tag(self, val):
        if val != None:
            self.validate('tpgroup_tag', val)
        self._tpgroup_tag = val
    
    _initiator_aliasname = None
    @property
    def initiator_aliasname(self):
        """
        User-friendly name assigned to initiator.
        This field is only present if the initiator
        provided an alias during login.
        """
        return self._initiator_aliasname
    @initiator_aliasname.setter
    def initiator_aliasname(self, val):
        if val != None:
            self.validate('initiator_aliasname', val)
        self._initiator_aliasname = val
    
    _tpgroup_name = None
    @property
    def tpgroup_name(self):
        """
        The name of the target portal group associated
        with this session.
        """
        return self._tpgroup_name
    @tpgroup_name.setter
    def tpgroup_name(self, val):
        if val != None:
            self.validate('tpgroup_name', val)
        self._tpgroup_name = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of the vserver this initiator is connected
        to.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _initiator_nodename = None
    @property
    def initiator_nodename(self):
        """
        Name of initiator. The initiator name must
        conform to RFC 3720, for example:
        "iqn.1987-06.com.initvendor1:appsrv.sn.2346".
        """
        return self._initiator_nodename
    @initiator_nodename.setter
    def initiator_nodename(self, val):
        if val != None:
            self.validate('initiator_nodename', val)
        self._initiator_nodename = val
    
    _target_session_id = None
    @property
    def target_session_id(self):
        """
        iSCSI session identifier assigned by the target.
        """
        return self._target_session_id
    @target_session_id.setter
    def target_session_id(self, val):
        if val != None:
            self.validate('target_session_id', val)
        self._target_session_id = val
    
    _initiator_group_list = None
    @property
    def initiator_group_list(self):
        """
        List of initiator groups containing this
        iSCSI initiator.
        """
        return self._initiator_group_list
    @initiator_group_list.setter
    def initiator_group_list(self, val):
        if val != None:
            self.validate('initiator_group_list', val)
        self._initiator_group_list = val
    
    _isid = None
    @property
    def isid(self):
        """
        ISID for this session selected by initiator
        represented as 6 hexadecimal octets separated by
        colons, for example: "40:01:37:00:00:00".
        """
        return self._isid
    @isid.setter
    def isid(self, val):
        if val != None:
            self.validate('isid', val)
        self._isid = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-initiator-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'tpgroup-tag',
            'initiator-aliasname',
            'tpgroup-name',
            'vserver',
            'initiator-nodename',
            'target-session-id',
            'initiator-group-list',
            'isid',
        ]
    
    def describe_properties(self):
        return {
            'tpgroup_tag': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_aliasname': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tpgroup_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_nodename': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_session_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_group_list': { 'class': InitiatorGroupListInfo, 'is_list': True, 'required': 'optional' },
            'isid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

from netapp.vserver_peer_transition.vserver_peer_transition_info import VserverPeerTransitionInfo
from netapp.netapp_object import NetAppObject

class VserverPeerTransitionDestroyIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against vserver-peer-transition object.
    but were not deleted due to some error.
    deleted due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the deletion operation caused an error.
        """
        return self._error_code
    @error_code.setter
    def error_code(self, val):
        if val != None:
            self.validate('error_code', val)
        self._error_code = val
    
    _vserver_peer_transition_key = None
    @property
    def vserver_peer_transition_key(self):
        """
        The keys for the vserver-peer-transition object to which
        the deletion applies.
        """
        return self._vserver_peer_transition_key
    @vserver_peer_transition_key.setter
    def vserver_peer_transition_key(self, val):
        if val != None:
            self.validate('vserver_peer_transition_key', val)
        self._vserver_peer_transition_key = val
    
    _error_message = None
    @property
    def error_message(self):
        """
        Error description, if the operation caused an error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    @staticmethod
    def get_api_name():
          return "vserver-peer-transition-destroy-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'vserver-peer-transition-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver_peer_transition_key': { 'class': VserverPeerTransitionInfo, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

from netapp.iscsi.iscsi_portal_address_info import IscsiPortalAddressInfo
from netapp.netapp_object import NetAppObject

class IscsiConfigAdapterInfo(NetAppObject):
    """
    Configuration information about a single iscsi adapter.
    """
    
    _status = None
    @property
    def status(self):
        """
        A short status message explaining the state.  i.e. if
        the adapter is offline, the reason for it, or if its "error"
        what the error is. This will not be returned if the
        state of the adapter is "online".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _state = None
    @property
    def state(self):
        """
        State of the adapter, either "online", "offline",
        "local", "partner", "error".  "
        online" and "offline" is used when the adapter is used for the current host.
        "local" if the adapter is operating on behalf of the
        local host, and "partner" if the adapter is operating
        on behalf of the partner host.  "error" is used if some
        an internal error occurred when tring to load this adapter info.
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _name = None
    @property
    def name(self):
        """
        The name this adapter is given.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _portal_addresses = None
    @property
    def portal_addresses(self):
        """
        A list of portal group address + port that this adapter
        is listening on.
        """
        return self._portal_addresses
    @portal_addresses.setter
    def portal_addresses(self, val):
        if val != None:
            self.validate('portal_addresses', val)
        self._portal_addresses = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-config-adapter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'state',
            'name',
            'portal-addresses',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'portal_addresses': { 'class': IscsiPortalAddressInfo, 'is_list': True, 'required': 'required' },
        }

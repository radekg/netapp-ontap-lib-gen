from netapp.netapp_object import NetAppObject

class OwnerInfo(NetAppObject):
    """
    Information about the client host and the owner process
    on the client host whose locks have to be removed.
    """
    
    _client_host = None
    @property
    def client_host(self):
        """
        client host on which the locks have to be removed.
        """
        return self._client_host
    @client_host.setter
    def client_host(self, val):
        if val != None:
            self.validate('client_host', val)
        self._client_host = val
    
    _client_host_pid = None
    @property
    def client_host_pid(self):
        """
        process owner on the above client host whose locks
        have to be removed.
        """
        return self._client_host_pid
    @client_host_pid.setter
    def client_host_pid(self, val):
        if val != None:
            self.validate('client_host_pid', val)
        self._client_host_pid = val
    
    @staticmethod
    def get_api_name():
          return "owner-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'client-host',
            'client-host-pid',
        ]
    
    def describe_properties(self):
        return {
            'client_host': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'client_host_pid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

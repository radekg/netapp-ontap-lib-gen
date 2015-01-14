from netapp.iscsi.iscsi_connected_initiator_info import IscsiConnectedInitiatorInfo
from netapp.netapp_object import NetAppObject

class IscsiAdapterInitiatorsInfo(NetAppObject):
    """
    A list of initiators currently connected
    to the adapter.
    """
    
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
    
    _iscsi_connected_initiators = None
    @property
    def iscsi_connected_initiators(self):
        """
        Information about the connected initiators
        """
        return self._iscsi_connected_initiators
    @iscsi_connected_initiators.setter
    def iscsi_connected_initiators(self, val):
        if val != None:
            self.validate('iscsi_connected_initiators', val)
        self._iscsi_connected_initiators = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-adapter-initiators-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'iscsi-connected-initiators',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'iscsi_connected_initiators': { 'class': IscsiConnectedInitiatorInfo, 'is_list': True, 'required': 'required' },
        }

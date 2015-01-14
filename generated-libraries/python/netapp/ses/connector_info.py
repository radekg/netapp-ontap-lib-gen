from netapp.ses.sas_connector_info import SasConnectorInfo
from netapp.netapp_object import NetAppObject

class ConnectorInfo(NetAppObject):
    """
    Information on cables and/or connectors connected to the shelf
    """
    
    _sas_connector_list = None
    @property
    def sas_connector_list(self):
        """
        Information on SAS connectors & cables.
        """
        return self._sas_connector_list
    @sas_connector_list.setter
    def sas_connector_list(self, val):
        if val != None:
            self.validate('sas_connector_list', val)
        self._sas_connector_list = val
    
    @staticmethod
    def get_api_name():
          return "connector-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'sas-connector-list',
        ]
    
    def describe_properties(self):
        return {
            'sas_connector_list': { 'class': SasConnectorInfo, 'is_list': True, 'required': 'optional' },
        }

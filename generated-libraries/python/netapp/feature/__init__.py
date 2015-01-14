from netapp.connection import NaConnection
from managed_feature import ManagedFeature # 0 properties
from managed_feature_status_list import ManagedFeatureStatusList # 0 properties
from managed_feature_status_info import ManagedFeatureStatusInfo # 3 properties
from managed_feature_status import ManagedFeatureStatus # 0 properties

class FeatureConnection(NaConnection):
    
    def feature_status_list_info(self):
        """
        Returns status information for managed features.
        """
        return self.request( "feature-status-list-info", {
        }, {
            'managed-feature-status-list': [ ManagedFeatureStatusInfo, True ],
        } )

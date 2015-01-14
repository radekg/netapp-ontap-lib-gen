from netapp.connection import NaConnection
from flash_device_info import FlashDeviceInfo # 13 properties
from flash_threshold_profile import FlashThresholdProfile # 3 properties
from flash_thresholds_get_iter_key_td import FlashThresholdsGetIterKeyTd # 2 properties
from flash_device_get_iter_key_td import FlashDeviceGetIterKeyTd # 2 properties
from flash_threshold import FlashThreshold # 5 properties

class FlashConnection(NaConnection):
    
    def flash_device_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Flash Cache device info objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Flash Cache device info object.
                All Flash Cache device info objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "flash-device-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FlashDeviceInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FlashDeviceInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FlashDeviceInfo, True ],
        } )
    
    def flash_get_thresholds(self, node, profile=None):
        """
        Get threshold profiles available in Flash Management Module.
        
        :param node: The name of the system to which the flash thresholds apply.
        
        :param profile: Name of the threshold profile.
                If not provided, all available profiles will be printed.
        """
        return self.request( "flash-get-thresholds", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'profile': [ profile, 'profile', [ basestring, 'None' ], False ],
        }, {
            'flash-threshold-profile': [ FlashThresholdProfile, True ],
        } )
    
    def flash_thresholds_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Flash Cache threshold profiles objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Flash Cache threshold profiles object.
                All Flash Cache threshold profiles objects matching this query up
                to 'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "flash-thresholds-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FlashThresholdProfile, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FlashThresholdProfile, 'None' ], False ],
        }, {
            'attributes-list': [ FlashThresholdProfile, True ],
        } )
    
    def flash_device_list_info(self, node, slot_number=None):
        """
        This API is used to retrieve information about the flash
        devices in the controller registered with Flash Management
        Module (FMM).
        
        :param node: The name of the system where the flash device is installed.
        
        :param slot_number: PCI-e slot number of the flash device. If not provided,
                information of all the registered devices will be given.
        """
        return self.request( "flash-device-list-info", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'slot_number': [ slot_number, 'slot-number', [ int, 'None' ], False ],
        }, {
            'flash-device-info': [ FlashDeviceInfo, True ],
        } )

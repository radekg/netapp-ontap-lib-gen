from netapp.connection import NaConnection
from sp_fw_status import SpFwStatus # 0 properties
from sp_status import SpStatus # 0 properties
from sp_fw_update_type import SpFwUpdateType # 0 properties
from mac_address import MacAddress # 0 properties
from service_processor_network_info import ServiceProcessorNetworkInfo # 14 properties
from service_processor_image_update_progress_info import ServiceProcessorImageUpdateProgressInfo # 5 properties
from service_processor_image_info import ServiceProcessorImageInfo # 8 properties
from ip_address import IpAddress # 0 properties
from service_processor_info import ServiceProcessorInfo # 12 properties
from sp_link_status import SpLinkStatus # 0 properties
from service_processor_image import ServiceProcessorImage # 8 properties
from sp_type import SpType # 0 properties
from sp_dhcp_status import SpDhcpStatus # 0 properties
from sp_pass_fail import SpPassFail # 0 properties
from sp_ip_address_type import SpIpAddressType # 0 properties
from sp_fw_type import SpFwType # 0 properties

class ServiceProcessorConnection(NaConnection):
    
    def service_processor_reboot(self, node, firmware_image=None):
        """
        Reboot the Service Processor
        
        :param node: Node on which the device is located
        
        :param firmware_image: Image to boot upon reboot. Default is primary
        """
        return self.request( "service-processor-reboot", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'firmware_image': [ firmware_image, 'firmware-image', [ basestring, 'sp-fw-type' ], False ],
        }, {
        } )
    
    def service_processor_image_get(self, node, firmware_image, desired_attributes=None):
        """
        Get information about installed firmware images
        
        :param node: Node on which the device is located
        
        :param firmware_image: Is this image primary or backup firmware for the device
                Possible values:
                <ul>
                <li> "primary"   - Firmware which the device boots into by
                default,
                <li> "backup"    - Firmware which the device boots into if
                primary fails
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "service-processor-image-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'firmware_image': [ firmware_image, 'firmware-image', [ basestring, 'sp-fw-type' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ServiceProcessorImage, 'None' ], False ],
        }, {
            'attributes': [ ServiceProcessorImage, False ],
        } )
    
    def service_processor_image_modify(self, node, is_autoupdate_enabled=None):
        """
        Enable or disable automatic firmware update
        
        :param node: Node on which the device is located
        
        :param is_autoupdate_enabled: Is firmware autoupdate enabled on the device
        """
        return self.request( "service-processor-image-modify", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'is_autoupdate_enabled': [ is_autoupdate_enabled, 'is-autoupdate-enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def service_processor_image_update(self, node, update_type, install_baseline_image=None, clear_logs=None, package=None):
        """
        Install new firmware image
        
        :param node: Node on which the device is located
        
        :param update_type: Type of firmware update to be performed
        
        :param install_baseline_image: Install the version packaged with ONTAP if this parameter is set
                to true. Otherwise, -package must be used to specify the package
                to install
        
        :param clear_logs: Clear logs on the device after update. Default value is true
        
        :param package: Name of the package file containing the firmware to be installed.
                Not required when -baseline is true
        """
        return self.request( "service-processor-image-update", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'install_baseline_image': [ install_baseline_image, 'install-baseline-image', [ bool, 'None' ], False ],
            'clear_logs': [ clear_logs, 'clear-logs', [ bool, 'None' ], False ],
            'update_type': [ update_type, 'update-type', [ basestring, 'sp-fw-update-type' ], False ],
            'package': [ package, 'package', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def service_processor_network_get(self, node, address_type, desired_attributes=None):
        """
        Get the network configuration
        
        :param node: Node on which the device is located
        
        :param address_type: Network configuration that is being addressed i.e. IPv4 or IPv6
                Possible values:
                <ul>
                <li> "ipv4" - Internet Protocol version 4,
                <li> "ipv6" - Internet Protocol version 6
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "service-processor-network-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'address_type': [ address_type, 'address-type', [ basestring, 'sp-ip-address-type' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ServiceProcessorNetworkInfo, 'None' ], False ],
        }, {
            'attributes': [ ServiceProcessorNetworkInfo, False ],
        } )
    
    def service_processor_image_update_progress_get(self, node, desired_attributes=None):
        """
        Get firmware update progress
        
        :param node: Node on which the device is located
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "service-processor-image-update-progress-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ServiceProcessorImageUpdateProgressInfo, 'None' ], False ],
        }, {
            'attributes': [ ServiceProcessorImageUpdateProgressInfo, False ],
        } )
    
    def service_processor_get(self, node, desired_attributes=None):
        """
        Get basic information about the device
        
        :param node: Node on which the device is located
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "service-processor-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ServiceProcessorInfo, 'None' ], False ],
        }, {
            'attributes': [ ServiceProcessorInfo, False ],
        } )
    
    def service_processor_network_modify(self, node, address_type, prefix_length=None, is_enabled=None, netmask=None, ip_address=None, dhcp=None, gateway_ip_address=None):
        """
        Modify the network configuration
        
        :param node: Node on which the device is located
        
        :param address_type: Network configuration that is being addressed i.e. IPv4 or IPv6
                Possible values:
                <ul>
                <li> "ipv4" - Internet Protocol version 4,
                <li> "ipv6" - Internet Protocol version 6
                </ul>
        
        :param prefix_length: Prefix length of subnet mask
        
        :param is_enabled: Is this address configuration enabled
        
        :param netmask: Netmask for the device
        
        :param ip_address: IP address currently held by the device
        
        :param dhcp: DHCP status for the configuration
                Possible values:
                <ul>
                <li> "v4"   - DHCP for IPv4,
                <li> "none" - DHCP not enabled
                </ul>
        
        :param gateway_ip_address: IP address of the network gateway
        """
        return self.request( "service-processor-network-modify", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'prefix_length': [ prefix_length, 'prefix-length', [ int, 'None' ], False ],
            'is_enabled': [ is_enabled, 'is-enabled', [ bool, 'None' ], False ],
            'address_type': [ address_type, 'address-type', [ basestring, 'sp-ip-address-type' ], False ],
            'netmask': [ netmask, 'netmask', [ basestring, 'ip-address' ], False ],
            'ip_address': [ ip_address, 'ip-address', [ basestring, 'ip-address' ], False ],
            'dhcp': [ dhcp, 'dhcp', [ basestring, 'sp-dhcp-status' ], False ],
            'gateway_ip_address': [ gateway_ip_address, 'gateway-ip-address', [ basestring, 'ip-address' ], False ],
        }, {
        } )

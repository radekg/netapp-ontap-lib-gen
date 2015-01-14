from netapp.connection import NaConnection
from net_placement_cache_get_iter_key_td import NetPlacementCacheGetIterKeyTd # 5 properties
from lif_placement_info import LifPlacementInfo # 2 properties
from net_port_modify_iter_info import NetPortModifyIterInfo # 3 properties
from netmask_or_prefix import NetmaskOrPrefix # 0 properties
from config_status_info import ConfigStatusInfo # 2 properties
from net_routing_group_route_get_iter_key_td import NetRoutingGroupRouteGetIterKeyTd # 3 properties
from net_port_info import NetPortInfo # 25 properties
from address_info_socket_type import AddressInfoSocketType # 0 properties
from route_info import RouteInfo # 8 properties
from stream_protocol_service import StreamProtocolService # 0 properties
from receive_buffer import ReceiveBuffer # 5 properties
from dns_zone import DnsZone # 0 properties
from data_protocol import DataProtocol # 0 properties
from ipspace_config_info import IpspaceConfigInfo # 2 properties
from lif_bindable import LifBindable # 0 properties
from routing_group import RoutingGroup # 0 properties
from hosts_info import HostsInfo # 4 properties
from address_info_transport_protocol import AddressInfoTransportProtocol # 0 properties
from adapter_type import AdapterType # 0 properties
from switchless_cluster_info import SwitchlessClusterInfo # 1 properties
from failover_group import FailoverGroup # 0 properties
from net_dns_get_iter_key_td import NetDnsGetIterKeyTd # 1 properties
from routing_group_route_info import RoutingGroupRouteInfo # 6 properties
from net_failover_group_get_iter_key_td import NetFailoverGroupGetIterKeyTd # 3 properties
from host_info import HostInfo # 3 properties
from address_info_family import AddressInfoFamily # 0 properties
from net_dns_info import NetDnsInfo # 6 properties
from net_port_get_iter_key_td import NetPortGetIterKeyTd # 2 properties
from interface_config_info import InterfaceConfigInfo # 16 properties
from net_connections_receive_window_size_get_iter_key_td import NetConnectionsReceiveWindowSizeGetIterKeyTd # 3 properties
from net_interface_get_iter_key_td import NetInterfaceGetIterKeyTd # 2 properties
from net_failover_group_info import NetFailoverGroupInfo # 3 properties
from net_config_info import NetConfigInfo # 5 properties
from vlan_info import VlanInfo # 5 properties
from priority_entry_info import PriorityEntryInfo # 1 properties
from host_name import HostName # 0 properties
from device_capability import DeviceCapability # 0 properties
from ifgrp_info import IfgrpInfo # 6 properties
from ipv6_options_info import Ipv6OptionsInfo # 1 properties
from net_device_discovery_get_iter_key_td import NetDeviceDiscoveryGetIterKeyTd # 4 properties
from net_placement_cache import NetPlacementCache # 6 properties
from net_interface_modify_iter_key_td import NetInterfaceModifyIterKeyTd # 2 properties
from protocol_layer4 import ProtocolLayer4 # 0 properties
from link import Link # 0 properties
from net_interface_info import NetInterfaceInfo # 26 properties
from net_address_info import NetAddressInfo # 6 properties
from interface_dcb_priority_entry_info import InterfaceDcbPriorityEntryInfo # 4 properties
from ip_address_info import IpAddressInfo # 7 properties
from net_port_modify_iter_key_td import NetPortModifyIterKeyTd # 2 properties
from net_device_discovery_info import NetDeviceDiscoveryInfo # 9 properties
from network_type import NetworkType # 0 properties
from net_ifgrp_info import NetIfgrpInfo # 9 properties
from net_interface_modify_iter_info import NetInterfaceModifyIterInfo # 3 properties
from address_info_flag import AddressInfoFlag # 0 properties
from interface_dcb_entry_info import InterfaceDcbEntryInfo # 4 properties
from net_dcb_entry_info import NetDcbEntryInfo # 2 properties
from net_hosts_get_iter_key_td import NetHostsGetIterKeyTd # 2 properties
from net_vlan_get_iter_key_td import NetVlanGetIterKeyTd # 4 properties
from net_dcb_priority_entry_info import NetDcbPriorityEntryInfo # 2 properties
from ip_address_or_hostname import IpAddressOrHostname # 0 properties
from net_options import NetOptions # 2 properties

class NetConnection(NaConnection):
    
    def net_connections_receive_window_size_modify(self, protocol, network, service, receive_buffer=None, receive_auto_tune=None):
        """
        Modify receive buffer size properties
        
        :param protocol: The network layer 4 protocol type
                Possible values:
                <ul>
                <li> "udp"  - UDP,
                <li> "tcp"  - TCP,
                <li> "na"   - not_available
                </ul>
        
        :param network: The network topology classification
                Possible values:
                <ul>
                <li> "wan"       ,
                <li> "lan"       ,
                <li> "undefined"
                </ul>
        
        :param service: The stream protocol connection classification
                Possible values:
                <ul>
                <li> "mount"          - Mount stream protocol,
                <li> "nfs"            - NFS stream protocol,
                <li> "nfs_v2"         - NFS version 2 stream protocol,
                <li> "nfs_v3"         - NFS version 3 stream protocol,
                <li> "nlm_v4"         - Network lock manager stream protocol,
                <li> "sm"             - Session Manager stream protocol,
                <li> "ftp_ctrl"       - FTP control stream protocol,
                <li> "ftp_data"       - FTP data stream protocol,
                <li> "http_1_0"       - HTTP version 1 stream protocol,
                <li> "http_1_1"       - HTTP version 1.1 stream protocol,
                <li> "iscsi"          - ISCSI stream protocol,
                <li> "cifs_srv"       - CIFS server stream protocol,
                <li> "cifs_nam"       - CIFS name server stream protocol,
                <li> "loopback"       - loopback stream protocol,
                <li> "rf"             - RC stream protocol,
                <li> "rawscp"         - Raw secure copy stream protocol,
                <li> "discard"        - Descard stream protocol,
                <li> "port_map"       - Port map stream protocol,
                <li> "pass_thru"      - Passthru stream protocol,
                <li> "rclopcp"        - Rc connection stream protocol,
                <li> "nfs_v4"         - NFS version 4 stream protocol,
                <li> "fcache"         - Flex cache stream protocol,
                <li> "ctlopcp"        - Ct connection stream protocol,
                <li> "rquota"         - Rquota stream protocol,
                <li> "cifs_msrpc"     - CIFS MsRpc stream protocol,
                <li> "unknown"        - unknown protocol
                </ul>
        
        :param receive_buffer: If receive-auto-tune is false, receive buffer size in kilobytes
                (1024).  If receive-auto-tune flag is true, this value has no
                effect.  The default value is 2048 for the ctlopcp service using
                the WAN network type, and 256 in other cases.
        
        :param receive_auto_tune: If true, allow the system to automatically adjust the receive
                buffer size.  The default value is false for the ctlopcp service
                using the LAN network type, and true in all other cases.
        """
        return self.request( "net-connections-receive-window-size-modify", {
            'receive_buffer': [ receive_buffer, 'receive-buffer', [ int, 'None' ], False ],
            'receive_auto_tune': [ receive_auto_tune, 'receive-auto-tune', [ bool, 'None' ], False ],
            'protocol': [ protocol, 'protocol', [ basestring, 'protocol-layer4' ], False ],
            'network': [ network, 'network', [ basestring, 'network-type' ], False ],
            'service': [ service, 'service', [ basestring, 'stream-protocol-service' ], False ],
        }, {
        } )
    
    def net_routing_group_route_create(self, routing_group, vserver, gateway_address, destination_address, metric=None, return_record=None):
        """
        Create a new network routing group route.
        
        :param routing_group: Specifies the name of routing group.
                For example:
                <ul>
                <li> d192.168.1.0/24 ('d' stands for data LIF and 192.168.1.0/24
                is subnet),
                <li> c192.168.1.0/24 ('c' stands for cluster LIF and
                192.168.1.0/24 is subnet),
                <li> n192.168.1.0/24 ('n' stands for node management LIF and
                192.168.1.0/24 is subnet)
                <li> dfd20:13::0/64  ('d' stands for data LIF and
                fd20:13::0/64 is IPv6 subnet)
                </ul>
        
        :param vserver: Specifies the name of Vserver.
        
        :param gateway_address: Specifies the IP address of gateway.
                For example: '198.18.0.0', 'fd20:13::1'
        
        :param destination_address: Specifies the IP address and subnet mask of destination.
                For example: '198.18.10.0/24', 'fd20:13::0/64'
        
        :param metric: Specifies the metric (hop count) of the LIF.
                The default value is determined by the LIF role as follows:
                <ul>
                <li> If the LIF role is 'node_mgmt' or 'cluster_mgmt': 10,
                <li> If the LIF role is 'data' or 'undef': 20,
                <li> If the LIF role is 'cluster': 30,
                <li> If the LIF role is 'intercluster': 40
                </ul>
        
        :param return_record: If set to true, returns the network routing group route on
                successful creation.
                Default: false
        """
        return self.request( "net-routing-group-route-create", {
            'routing_group': [ routing_group, 'routing-group', [ basestring, 'None' ], False ],
            'metric': [ metric, 'metric', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'gateway_address': [ gateway_address, 'gateway-address', [ basestring, 'None' ], False ],
            'destination_address': [ destination_address, 'destination-address', [ basestring, 'None' ], False ],
        }, {
            'result': [ RoutingGroupRouteInfo, False ],
        } )
    
    def net_route_delete(self, route_info):
        """
        Delete a kernel route.  Does not
        modify persistent config.
        
        :param route_info: Route to delete.
        """
        return self.request( "net-route-delete", {
            'route_info': [ route_info, 'route-info', [ RouteInfo, 'None' ], False ],
        }, {
        } )
    
    def net_ifconfig_set(self, interface_config_info):
        """
        Configure network interface. Does not
        modify persistent config.
        
        :param interface_config_info: Interface configuration.
        """
        return self.request( "net-ifconfig-set", {
            'interface_config_info': [ interface_config_info, 'interface-config-info', [ InterfaceConfigInfo, 'None' ], False ],
        }, {
        } )
    
    def net_placement_cache_delete(self, node, vserver, netmask_length, port, address):
        """
        Delete LIF placement cached information.
        
        :param node: Specifies the name of the node.
        
        :param vserver: Vserver Name
        
        :param netmask_length: The number of bits in the subnet mask (i.e. 24 or 64).
        
        :param port: The port name on the node.
        
        :param address: The IP address that was searched.
        """
        return self.request( "net-placement-cache-delete", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'netmask_length': [ netmask_length, 'netmask-length', [ int, 'None' ], False ],
            'port': [ port, 'port', [ basestring, 'None' ], False ],
            'address': [ address, 'address', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def net_routing_group_route_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of network routing group route.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                network routing group route object.
                All network routing group route objects matching this query up to
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
        return self.request( "net-routing-group-route-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ RoutingGroupRouteInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ RoutingGroupRouteInfo, 'None' ], False ],
        }, {
            'attributes-list': [ RoutingGroupRouteInfo, True ],
        } )
    
    def net_port_ifgrp_create(self, node, ifgrp_name, mode, distribution_function, return_record=None):
        """
        Create a new network interface group.
        
        :param node: Specifies the name of node.
        
        :param ifgrp_name: Specifies the interface group name.
        
        :param mode: Specifies the link policy for the ifgrp.
                Possible values:
                <ul>
                <li> 'multimode      - All links are simultaneously active',
                <li> 'multimode_lacp - Link state is managed by the switch using
                link aggregation control protocol (LACP) (IEEE 802.3ad)',
                <li> 'singlemode     - Only one link is active at a time'
                </ul>
        
        :param distribution_function: Specifies the traffic distribution function for the ifgrp.
                Possible values:
                <ul>
                <li> "mac"            - Network traffic is distributed on the
                basis of MAC addresses,
                <li> "ip"             - Network traffic is distributed on the
                basis of IP addresses,
                <li> "sequential"     - Network traffic is distributed
                round-robin to each interface,
                <li> "port"           - Network traffic is distributed by
                transport layer address 4-tuple
                </ul>
        
        :param return_record: If set to true, returns the network interface group on successful
                creation.
                Default: false
        """
        return self.request( "net-port-ifgrp-create", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'ifgrp_name': [ ifgrp_name, 'ifgrp-name', [ basestring, 'lif-bindable' ], False ],
            'mode': [ mode, 'mode', [ basestring, 'None' ], False ],
            'distribution_function': [ distribution_function, 'distribution-function', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ NetIfgrpInfo, False ],
        } )
    
    def net_ifconfig_get(self, interface_name=None):
        """
        Output the current configuration for one interface.
        
        :param interface_name: This is the name of the interface to display.
                If not provided, all interfaces will be displayed.
        """
        return self.request( "net-ifconfig-get", {
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
            'interface-config-info': [ InterfaceConfigInfo, True ],
        } )
    
    def net_port_get(self, node, port, desired_attributes=None):
        """
        Get the attributes of a network port.
        
        :param node: Specifies the name of node.
        
        :param port: Specifies the name of port.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "net-port-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'port': [ port, 'port', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetPortInfo, 'None' ], False ],
        }, {
            'attributes': [ NetPortInfo, False ],
        } )
    
    def net_dns_modify(self, domains=None, dns_state=None, name_servers=None, attempts=None, timeout=None):
        """
        Modify the DNS configuration of the specified Vserver. Omitted
        (optional) fields will not be changed.
        
        :param domains: List of DNS domains such as 'sales.bar.com'. The first domain is
                the one that the Vserver belongs to.
        
        :param dns_state: Enable/Disable DNS. Possible values are 'enabled' or 'disabled'.
        
        :param name_servers: IPv4 addresses of name servers such as '123.123.123.123'.
        
        :param attempts: Max number of trials before giving up and returning error.
                Default is one.
        
        :param timeout: Number of seconds to wait for a response from a name server
                before trying a different name server. Default is two seconds.
        """
        return self.request( "net-dns-modify", {
            'domains': [ domains, 'domains', [ basestring, 'None' ], True ],
            'dns_state': [ dns_state, 'dns-state', [ basestring, 'enable' ], False ],
            'name_servers': [ name_servers, 'name-servers', [ basestring, 'ip-address' ], True ],
            'attempts': [ attempts, 'attempts', [ int, 'None' ], False ],
            'timeout': [ timeout, 'timeout', [ int, 'None' ], False ],
        }, {
        } )
    
    def net_options_modify(self, net_options):
        """
        Modify the attributes of net object.
        
        :param net_options: Network Options Typedef
        """
        return self.request( "net-options-modify", {
            'net_options': [ net_options, 'net-options', [ NetOptions, 'None' ], False ],
        }, {
        } )
    
    def net_device_discovery_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of network device discovery objects found
        by a discovery protocol such as CDP or LLDP.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                net-device-discovery object.
                All net-device-discovery objects matching this query up to
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
        return self.request( "net-device-discovery-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NetDeviceDiscoveryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetDeviceDiscoveryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NetDeviceDiscoveryInfo, True ],
        } )
    
    def net_failover_group_get(self, node, port, failover_group, desired_attributes=None):
        """
        Get the attributes of a failover group.
        
        :param node: The node on which the failover target (a network port or
                interface group) is located.
        
        :param port: The network port or interface group in the failover group.
        
        :param failover_group: A grouping of failover targets for logical interfaces on one or
                more nodes.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "net-failover-group-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetFailoverGroupInfo, 'None' ], False ],
            'port': [ port, 'port', [ basestring, 'None' ], False ],
            'failover_group': [ failover_group, 'failover-group', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ NetFailoverGroupInfo, False ],
        } )
    
    def net_ping(self, host_name_or_ip_address, retry_count=None):
        """
        Ping a host.  The API returns on the first successful
        ping of retry-count attempts.  EHOSTNOTFOUND is returned
        if the host cannot be resolved.  EONTAPI_EHOSTDOWN is
        returned if the host cannot be pinged.  The interval
        between retries is 1 second.  IPv6 is not supported at
        this time.
        EONTAPI_EHOSTDOWN
        INVALIDINPUTERROR
        ONTAPI_ENOMEM
        
        :param host_name_or_ip_address: The name or the IP address of the host to ping.  The format
                is an IPv4  host name or an IP address.
        
        :param retry_count: The number of pings to try before giving up.  Default is 3.
                Range: [1..5]
        """
        return self.request( "net-ping", {
            'host_name_or_ip_address': [ host_name_or_ip_address, 'host-name-or-ip-address', [ basestring, 'None' ], False ],
            'retry_count': [ retry_count, 'retry-count', [ int, 'None' ], False ],
        }, {
        } )
    
    def net_placement_discover(self, vserver, netmask_length, address, mac=None):
        """
        Find the ports direcly connected to the IP address
        
        :param vserver: Vserver Name
        
        :param netmask_length: Netmask Length
        
        :param address: IP Address
        
        :param mac: MAC Address
        """
        return self.request( "net-placement-discover", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'netmask_length': [ netmask_length, 'netmask-length', [ int, 'None' ], False ],
            'mac': [ mac, 'mac', [ basestring, 'None' ], False ],
            'address': [ address, 'address', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_failover_group_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of failover group objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the net
                object.
                All net objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "net-failover-group-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NetFailoverGroupInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetFailoverGroupInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NetFailoverGroupInfo, True ],
        } )
    
    def net_reverse_resolve(self, ip_address):
        """
        Resolves an IP address to one or more host names.
        Returns an error code of gethostbyaddr_r if failed.
        Does not support IPv6 at this time.
        
        :param ip_address: IP address of the host to be resolved in dotted notation
                (for example, 10.56.10.125).
        """
        return self.request( "net-reverse-resolve", {
            'ip_address': [ ip_address, 'ip-address', [ basestring, 'None' ], False ],
        }, {
            'alias-names': [ basestring, True ],
            'canonical-name': [ basestring, False ],
        } )
    
    def net_connections_receive_window_size_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over connections returning receive buffer size
        properties
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                net-connections-receive-window-size object.
                All net-connections-receive-window-size objects matching this
                query up to 'max-records' will be returned.
        
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
        return self.request( "net-connections-receive-window-size-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ReceiveBuffer, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ReceiveBuffer, 'None' ], False ],
        }, {
            'attributes-list': [ ReceiveBuffer, True ],
        } )
    
    def net_dns_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate through DNS configurations of the cluster
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the dns
                object.
                All dns objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "net-dns-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NetDnsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetDnsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NetDnsInfo, True ],
        } )
    
    def net_interface_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of network interface objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                given network interface object.
                All given network interface objects matching this query up to
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
        return self.request( "net-interface-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NetInterfaceInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetInterfaceInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NetInterfaceInfo, True ],
        } )
    
    def net_ping_info(self, host_name_or_ip_address, ping_count=None):
        """
        Ping a host.  The API pings the host count times, and
        returns the number of successful pings and times.
        EHOSTNOTFOUND is returned if the host cannot be resolved.
        EHOSTNOCONTACT is returned if the host cannot be pinged.
        The interval between ping attempts is 1 second.  IPv6 is
        not supported at this time.
        EONTAPI_EHOSTDOWN
        EINVALIDINPUTERROR
        EONTAPI_ENOMEM
        
        :param host_name_or_ip_address: The name or the IP address of the host to ping.  The format
                is an IPv4 host name or IP address.
        
        :param ping_count: The number of pings.  Default is 3.
                Range: [1..16]
        """
        return self.request( "net-ping-info", {
            'ping_count': [ ping_count, 'ping-count', [ int, 'None' ], False ],
            'host_name_or_ip_address': [ host_name_or_ip_address, 'host-name-or-ip-address', [ basestring, 'None' ], False ],
        }, {
            'packets-transmitted': [ int, False ],
            'round-trip-minimum-time': [ int, False ],
            'round-trip-maximum-time': [ int, False ],
            'packets-received': [ int, False ],
            'round-trip-mean-time': [ int, False ],
        } )
    
    def net_dns_get(self, desired_attributes=None):
        """
        Get the DNS configuration of the Vserver
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "net-dns-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetDnsInfo, 'None' ], False ],
        }, {
            'attributes': [ NetDnsInfo, False ],
        } )
    
    def net_interface_revert(self, vserver, interface_name):
        """
        Revert a logical interface back to its home port following a
        deliberate migration or failover.
        
        :param vserver: Specifies the Vserver that owns the logical interface that is to
                be reverted.
        
        :param interface_name: Specifies the logical interface that is to be reverted.
        """
        return self.request( "net-interface-revert", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_dcb_priority_list_info(self, priority=None, interface_name=None):
        """
        Returns the current Data Center Bridging (DCB) configuration
        for a specified network interface or all network interfaces
        indexed by the DCB priority.
        
        :param priority: The priority. Range: [0..7]
                If not specified, the priority associated DCB configuration
                for all DCB priorities will be displayed.
        
        :param interface_name: The interface name.
                If not specified, the priority associated DCB configuration
                for all DCB-capable network interfaces will be displayed.
        """
        return self.request( "net-dcb-priority-list-info", {
            'priority': [ priority, 'priority', [ int, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
            'net-dcb-priority-entries': [ NetDcbPriorityEntryInfo, True ],
        } )
    
    def net_vlan_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of VLAN objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                net-vlan object.
                All net-vlan objects matching this query up to 'max-records' will
                be returned.
        
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
        return self.request( "net-vlan-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VlanInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VlanInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VlanInfo, True ],
        } )
    
    def net_connections_receive_window_size_get(self, protocol, network, service, desired_attributes=None):
        """
        Get the receive buffer size properties of a service
        
        :param protocol: The network layer 4 protocol type
                Possible values:
                <ul>
                <li> "udp"  - UDP,
                <li> "tcp"  - TCP,
                <li> "na"   - not_available
                </ul>
        
        :param network: The network topology classification
                Possible values:
                <ul>
                <li> "wan"       ,
                <li> "lan"       ,
                <li> "undefined"
                </ul>
        
        :param service: The stream protocol connection classification
                Possible values:
                <ul>
                <li> "mount"          - Mount stream protocol,
                <li> "nfs"            - NFS stream protocol,
                <li> "nfs_v2"         - NFS version 2 stream protocol,
                <li> "nfs_v3"         - NFS version 3 stream protocol,
                <li> "nlm_v4"         - Network lock manager stream protocol,
                <li> "sm"             - Session Manager stream protocol,
                <li> "ftp_ctrl"       - FTP control stream protocol,
                <li> "ftp_data"       - FTP data stream protocol,
                <li> "http_1_0"       - HTTP version 1 stream protocol,
                <li> "http_1_1"       - HTTP version 1.1 stream protocol,
                <li> "iscsi"          - ISCSI stream protocol,
                <li> "cifs_srv"       - CIFS server stream protocol,
                <li> "cifs_nam"       - CIFS name server stream protocol,
                <li> "loopback"       - loopback stream protocol,
                <li> "rf"             - RC stream protocol,
                <li> "rawscp"         - Raw secure copy stream protocol,
                <li> "discard"        - Descard stream protocol,
                <li> "port_map"       - Port map stream protocol,
                <li> "pass_thru"      - Passthru stream protocol,
                <li> "rclopcp"        - Rc connection stream protocol,
                <li> "nfs_v4"         - NFS version 4 stream protocol,
                <li> "fcache"         - Flex cache stream protocol,
                <li> "ctlopcp"        - Ct connection stream protocol,
                <li> "rquota"         - Rquota stream protocol,
                <li> "cifs_msrpc"     - CIFS MsRpc stream protocol,
                <li> "unknown"        - unknown protocol
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "net-connections-receive-window-size-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ReceiveBuffer, 'None' ], False ],
            'protocol': [ protocol, 'protocol', [ basestring, 'protocol-layer4' ], False ],
            'network': [ network, 'network', [ basestring, 'network-type' ], False ],
            'service': [ service, 'service', [ basestring, 'stream-protocol-service' ], False ],
        }, {
            'attributes': [ ReceiveBuffer, False ],
        } )
    
    def net_hosts_create(self, hostname, host_ip_address, return_record=None, aliases=None):
        """
        Create a new IP to host names mapping
        
        :param hostname: Canonical hostname in a simple string or in FQDN
        
        :param host_ip_address: IPv4 address in dotted form as '123.123.123.123'.
        
        :param return_record: If set to true, returns the hosts on successful creation.
                Default: false
        
        :param aliases: The list of aliases such as 'host1.sales.foo.com'.
        """
        return self.request( "net-hosts-create", {
            'hostname': [ hostname, 'hostname', [ basestring, 'None' ], False ],
            'host_ip_address': [ host_ip_address, 'host-ip-address', [ basestring, 'ip-address' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'aliases': [ aliases, 'aliases', [ basestring, 'None' ], True ],
        }, {
            'result': [ HostsInfo, False ],
        } )
    
    def net_route_add(self, route_info):
        """
        Create a new kernel route.  Does not
        modify persistent config.
        
        :param route_info: Route to create.
        """
        return self.request( "net-route-add", {
            'route_info': [ route_info, 'route-info', [ RouteInfo, 'None' ], False ],
        }, {
        } )
    
    def net_interface_modify(self, interface_name, vserver, comment=None, use_failover_group=None, routing_group_name=None, failover_group=None, home_node=None, firewall_policy=None, dns_domain_name=None, listen_for_dns_query=None, is_auto_revert=None, netmask=None, administrative_status=None, failover_policy=None, address=None, netmask_length=None, home_port=None, is_ipv4_link_local=None):
        """
        Modify the attributes of network interface object.
        
        :param interface_name: Specifies the logical interface (LIF) name.
        
        :param vserver: Specifies the Vserver name.
        
        :param comment: Comment
        
        :param use_failover_group: Specifies whether failover rules are automatically created,
                manually created by the administrator, or disabled.
                For FCP and iSCSI LIFs, the default policy is 'disabled'; for
                NFS, CIFs and fcache LIFs, the default policy is
                'system_defined'.
                Possible values:
                <ul>
                <li> "system_defined" - Failover targets generated
                automatically by the system,
                <li> "disabled"       - Failover targets generated manually by
                the admin,
                <li> "enabled"        - Failover targets defined by
                failover-group
                </ul>
        
        :param routing_group_name: Specifies the routing group, which enables multiple logical
                interfaces to share a set of routing table entries.
                For example:
                d192.168.1.0/24 ('d' stands for data LIF and 192.168.1.0/24 is
                subnet)
                c192.168.1.0/24 ('c' stands for cluster LIF and 192.168.1.0/24 is
                subnet)
                n192.168.1.0/24 ('n' stands for node management LIF and
                192.168.1.0/24 is subnet)
                dfd20:13::0/50  ('d' stands for data LIF and fd20:13::0/50 is
                IPv6 subnet)
        
        :param failover_group: Specifies the failover group name.
        
        :param home_node: Specifies the LIF's home node.
        
        :param firewall_policy: Specifies the firewall policy for the LIF.
                Default firewall-policy is set as per the following table:
                <ul>
                <li> 'LIF Role    Protocols   Default policy',
                <li> '-------     ---------   --------------',
                <li> 'data         none             mgmt',
                <li> 'data         any              data',
                <li> 'node_mgmt    any              mgmt',
                <li> 'cluster_mgmt any              mgmt',
                <li> 'cluster      any              cluster',
                <li> 'intercluster any              intercluster'
                </ul>
        
        :param dns_domain_name: Specifies the unique, fully qualified domain name of the DNS zone
                of this LIF.
        
        :param listen_for_dns_query: If True, this IP address will listen for DNS queries for the
                dns-zone specified.
        
        :param is_auto_revert: If true, data LIF will revert to its home node under certain
                circumstances such as startup, and load balancing migration
                capability is disabled automatically.
                Default: false
        
        :param netmask: Specifies the LIF's netmask.
                This element is valid for all data protocols except FCP.
        
        :param administrative_status: Specifies the administrative status of the LIF.
                The administrative status can differ from the operational status;
                for instance, if you specify the status as up but a network
                problem prevents the interface from functioning, the operational
                status remains as down.
                Possible values:
                <ul>
                <li> 'up',
                <li> 'down',
                <li> 'unknown'
                </ul>
        
        :param failover_policy: Specifies the failover policy for the LIF.
                For FCP and iSCSI LIFs, the only failover policy is 'disabled';
                for NFS, CIFs and fcache LIFs, the default policy is
                'nextavail'.
                Possible values:
                <ul>
                <li> "nextavail" - Next failover target selected based on next
                port in failover targets list, preferring local ports first,
                <li> "priority"  - Next failover target selected based on first
                available port in failover targets list,
                <li> "disabled"  - Failover disabled
                </ul>
        
        :param address: Specifies the LIF's IP address.
                This element is valid for all data protocols except FCP.
        
        :param netmask_length: Specifies number of bits in the netmask.
        
        :param home_port: Specifies the LIF's home port.
        
        :param is_ipv4_link_local: If true, automatically configure an interface with an IPv4
                address.
                User can configure an interface by explicitly specifying
                &lt;address&gt; and &lt;netmask&gt (or &lt;netmask-length&gt;);
                or by enabling is-ipv4-link-local to true.
        """
        return self.request( "net-interface-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'use_failover_group': [ use_failover_group, 'use-failover-group', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
            'routing_group_name': [ routing_group_name, 'routing-group-name', [ basestring, 'routing-group' ], False ],
            'failover_group': [ failover_group, 'failover-group', [ basestring, 'failover-group' ], False ],
            'home_node': [ home_node, 'home-node', [ basestring, 'None' ], False ],
            'firewall_policy': [ firewall_policy, 'firewall-policy', [ basestring, 'None' ], False ],
            'dns_domain_name': [ dns_domain_name, 'dns-domain-name', [ basestring, 'dns-zone' ], False ],
            'listen_for_dns_query': [ listen_for_dns_query, 'listen-for-dns-query', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'is_auto_revert': [ is_auto_revert, 'is-auto-revert', [ bool, 'None' ], False ],
            'netmask': [ netmask, 'netmask', [ basestring, 'ip-address' ], False ],
            'administrative_status': [ administrative_status, 'administrative-status', [ basestring, 'None' ], False ],
            'failover_policy': [ failover_policy, 'failover-policy', [ basestring, 'None' ], False ],
            'address': [ address, 'address', [ basestring, 'ip-address' ], False ],
            'netmask_length': [ netmask_length, 'netmask-length', [ int, 'None' ], False ],
            'home_port': [ home_port, 'home-port', [ basestring, 'None' ], False ],
            'is_ipv4_link_local': [ is_ipv4_link_local, 'is-ipv4-link-local', [ bool, 'None' ], False ],
        }, {
        } )
    
    def net_port_ifgrp_destroy(self, node, ifgrp_name):
        """
        Destroy an existing network interface group.
        
        :param node: Specifies the name of node.
        
        :param ifgrp_name: Specifies the interface group name.
        """
        return self.request( "net-port-ifgrp-destroy", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'ifgrp_name': [ ifgrp_name, 'ifgrp-name', [ basestring, 'lif-bindable' ], False ],
        }, {
        } )
    
    def net_get_address_info(self, host_info):
        """
        Resolves a host name to one or more IPv4 or IPv6 addresses.
        Returns appropriate errorcode if the host name cannot be
        resolved.
        
        :param host_info: Contains name of the host to be resolved, hints will be
                provided in order to return the appropriate type of addresses,
                service name for which the address will be used.
        """
        return self.request( "net-get-address-info", {
            'host_info': [ host_info, 'host-info', [ HostInfo, 'None' ], False ],
        }, {
            'host-result': [ NetAddressInfo, True ],
        } )
    
    def net_ipspace_create(self, ipspace_config_info):
        """
        Create a new ipspace.  Modifies persistent config.
        
        :param ipspace_config_info: Ipspace to create.
        """
        return self.request( "net-ipspace-create", {
            'ipspace_config_info': [ ipspace_config_info, 'ipspace-config-info', [ IpspaceConfigInfo, 'None' ], False ],
        }, {
        } )
    
    def net_port_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of network port or a group of network port
        objects.
        
        :param query: If modifying a specific given network port, this input element
                must specify all keys.
                If modifying given network port objects based on query, this
                input element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching given
                network port even when the modification of a previous matching
                given network port fails, and do so until the total number of
                objects failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of given network
                port objects (just keys) that were successfully updated.
                If set to false, the list of given network port objects modified
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple given network port
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                given network port even when modification of a previous given
                network port fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of given network
                port objects (just keys) that were not modified due to some
                error.
                If set to false, the list of given network port objects not
                modified will not be returned.
                Default: true
        """
        return self.request( "net-port-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ NetPortInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ NetPortInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ NetPortModifyIterInfo, True ],
            'failure-list': [ NetPortModifyIterInfo, True ],
        } )
    
    def net_interface_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of network interface or a group of network
        interface objects.
        
        :param query: If modifying a specific given network interface, this input
                element must specify all keys.
                If modifying given network interface objects based on query, this
                input element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching given
                network interface even when the modification of a previous
                matching given network interface fails, and do so until the total
                number of objects failed to be modified reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of given network
                interface objects (just keys) that were successfully updated.
                If set to false, the list of given network interface objects
                modified will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple given network
                interface objects match a given query.
                If set to true, the API will continue modifying the next matching
                given network interface even when modification of a previous
                given network interface fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of given network
                interface objects (just keys) that were not modified due to some
                error.
                If set to false, the list of given network interface objects not
                modified will not be returned.
                Default: true
        """
        return self.request( "net-interface-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ NetInterfaceInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ NetInterfaceInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ NetInterfaceModifyIterInfo, True ],
            'failure-list': [ NetInterfaceModifyIterInfo, True ],
        } )
    
    def net_config_get_persistent(self):
        """
        Reads filer's /etc/rc and outputs contents.
        ECHECKRESULTS
        """
        return self.request( "net-config-get-persistent", {
        }, {
            'net-config-info': [ NetConfigInfo, False ],
        } )
    
    def net_cluster_ping(self, destination_address, node=None, interface_owner=None, retry_count=None, interface=None, use_source_port=None, wait=None):
        """
        Ping an IP address to verify whether the interface is alive
        
        :param destination_address: Specifies IPv4 address of the destination.
        
        :param node: Specifies the node from which ping request is to be sent.
                Element &lt;node&gt; is mutually exclusive with
                &lt;interface-owner&gt; and &lt;interface&gt;.
                If neither &lt;node&gt; nor &lt;interface-owner&gt; and
                &lt;interface&gt; is specified, then the ping request will
                originate from the node receiving the API request.
        
        :param interface_owner: Specifies the name of logical interface (LIF) owner. It may be a
                node or Vserver name.
                Element &lt;interface-owner&gt; and &lt;interface&gt; are
                mutually exclusive with element &lt;node&gt;.
        
        :param retry_count: Specifies the number of ECHO_REQUEST retries for the given
                destination address.
                Ping stops upon first successful reply from the destination.
                Default: 20
        
        :param interface: Specifies the LIF from which the ping request is to be sent.
                This element must be specified with &lt;interface-owner&gt;.
        
        :param use_source_port: Specifies whether to send out ping via the port which is hosting
                the lif.  Only applicable when lif parameter when specified.
                Default: false
        
        :param wait: Specifies inter packet time interval (secs) for sending
                ECHO_REQUEST.
                Default: 1
        """
        return self.request( "net-cluster-ping", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'interface_owner': [ interface_owner, 'interface-owner', [ basestring, 'None' ], False ],
            'retry_count': [ retry_count, 'retry-count', [ int, 'None' ], False ],
            'destination_address': [ destination_address, 'destination-address', [ basestring, 'None' ], False ],
            'interface': [ interface, 'interface', [ basestring, 'None' ], False ],
            'use_source_port': [ use_source_port, 'use-source-port', [ bool, 'None' ], False ],
            'wait': [ wait, 'wait', [ int, 'None' ], False ],
        }, {
        } )
    
    def net_hosts_get(self, host_ip_address, desired_attributes=None):
        """
        Given an IP address, return the corresponding IP to host names
        mapping of the running Vserver context
        
        :param host_ip_address: IPv4 address in dotted form as '123.123.123.123'.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "net-hosts-get", {
            'host_ip_address': [ host_ip_address, 'host-ip-address', [ basestring, 'ip-address' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ HostsInfo, 'None' ], False ],
        }, {
            'attributes': [ HostsInfo, False ],
        } )
    
    def net_options_get(self):
        """
        Get the attributes of the net.
        """
        return self.request( "net-options-get", {
        }, {
            'net-options': [ NetOptions, False ],
        } )
    
    def net_port_ifgrp_remove_port(self, node, ifgrp_name, port):
        """
        Remove port from a network interface group.
        
        :param node: Specifies the name of node.
        
        :param ifgrp_name: Specifies the interface group name.
        
        :param port: Specifies the name of port.
        """
        return self.request( "net-port-ifgrp-remove-port", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'ifgrp_name': [ ifgrp_name, 'ifgrp-name', [ basestring, 'lif-bindable' ], False ],
            'port': [ port, 'port', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_port_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of network port objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                given network port object.
                All given network port objects matching this query up to
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
        return self.request( "net-port-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NetPortInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetPortInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NetPortInfo, True ],
        } )
    
    def net_dcb_list_info(self, interface_name=None, priority_group_id=None):
        """
        Returns the current Data Center Bridging (DCB) configuration for
        a specified network interface or all network interfaces indexed by
        the priority group id.
        
        :param interface_name: The network interface name.
                If not specified, the priority group associated DCB configuration
                for all DCB-capable network interfaces will be displayed.
        
        :param priority_group_id: The Priority Group ID. Range: [0..15]
                If not specified, the DCB configuration for all assigned priority groups
                will be displayed.
        """
        return self.request( "net-dcb-list-info", {
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
            'priority_group_id': [ priority_group_id, 'priority-group-id', [ int, 'None' ], False ],
        }, {
            'net-dcb-entries': [ NetDcbEntryInfo, True ],
        } )
    
    def net_port_modify(self, node, port, administrative_speed=None, administrative_duplex=None, is_administrative_auto_negotiate=None, mtu=None, autorevert_delay=None, role=None, administrative_flowcontrol=None, is_administrative_up=None):
        """
        Modify the given attributes of network port and the rest remain
        unchanged.
        
        :param node: Specifies the name of node.
        
        :param port: Specifies the name of port.
        
        :param administrative_speed: Specifies the user preferred speed setting of the port.
                Possible values:
                <ul>
                <li> "undef"     - No defined speed,
                <li> "auto"      - Auto-negotiate speed for link,
                <li> "10"        - 10 megabits per second,
                <li> "100"       - 100 megabits per second,
                <li> "1000"      - 1 gigabit per second,
                <li> "10000"     - 10 gigabits per second
                </ul>
        
        :param administrative_duplex: Specifies the user preferred duplex setting of the port.
                Possible values:
                <ul>
                <li> "undef"     - No defined duplex,
                <li> "auto"      - Auto-negotiate duplex setting for link,
                <li> "half"      - Half-duplex link usage,
                <li> "full"      - Full-duplex link usage
                </ul>
        
        :param is_administrative_auto_negotiate: Enables or disables Ethernet auto-negotiation of speed, duplex
                and flow control.
        
        :param mtu: Specifies the maximum transmission unit (MTU) of the port.
        
        :param autorevert_delay: For a port with role 'cluster', specifies the delay in seconds
                before autoreverting a LIF to this port.
        
        :param role: Specifies the role associated with the port.
                Possible values:
                <ul>
                <li> 'undef          - No defined role',
                <li> 'cluster        - Used for communication using the private
                cluster network',
                <li> 'data           - Used for communicating with file service
                clients',
                <li> 'node_mgmt      - Used by administrators to configure the
                node',
                <li> 'intercluster   - Used for communication with a different
                cluster'
                </ul>
        
        :param administrative_flowcontrol: Specifies the user preferred flow control setting of the port.
        
        :param is_administrative_up: If true, it changes the state of the port to 'up'.
        """
        return self.request( "net-port-modify", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'administrative_speed': [ administrative_speed, 'administrative-speed', [ basestring, 'None' ], False ],
            'administrative_duplex': [ administrative_duplex, 'administrative-duplex', [ basestring, 'None' ], False ],
            'is_administrative_auto_negotiate': [ is_administrative_auto_negotiate, 'is-administrative-auto-negotiate', [ bool, 'None' ], False ],
            'mtu': [ mtu, 'mtu', [ int, 'None' ], False ],
            'autorevert_delay': [ autorevert_delay, 'autorevert-delay', [ int, 'None' ], False ],
            'role': [ role, 'role', [ basestring, 'None' ], False ],
            'administrative_flowcontrol': [ administrative_flowcontrol, 'administrative-flowcontrol', [ basestring, 'None' ], False ],
            'is_administrative_up': [ is_administrative_up, 'is-administrative-up', [ bool, 'None' ], False ],
            'port': [ port, 'port', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_interface_create(self, interface_name, vserver, role, home_node, home_port, comment=None, use_failover_group=None, data_protocols=None, failover_group=None, address=None, firewall_policy=None, dns_domain_name=None, listen_for_dns_query=None, return_record=None, is_auto_revert=None, netmask=None, failover_policy=None, netmask_length=None, administrative_status=None, routing_group_name=None, is_ipv4_link_local=None):
        """
        Create a new logical interface.
        
        :param interface_name: Specifies the logical interface (LIF) name.
        
        :param vserver: Specifies the Vserver name.
        
        :param role: Specifies the role of the LIF.
                Default: data
                Possible values:
                <ul>
                <li> "undef"          - No defined role,
                <li> "cluster"        - Used for communication using the
                private cluster network,
                <li> "data"           - Used for communicating with file
                service clients,
                <li> "node_mgmt"      - Used by administrators to configure the
                node,
                <li> "intercluster"   - Used for communication with a different
                cluster,
                <li> "cluster_mgmt"   - Used by administrators to configure the
                cluster
                </ul>
        
        :param home_node: Specifies the LIF's home node.
        
        :param home_port: Specifies the LIF's home port.
        
        :param comment: Comment
        
        :param use_failover_group: Specifies whether failover rules are automatically created,
                manually created by the administrator, or disabled.
                For FCP and iSCSI LIFs, the default policy is 'disabled'; for
                NFS, CIFs and fcache LIFs, the default policy is
                'system_defined'.
                Possible values:
                <ul>
                <li> "system_defined" - Failover targets generated
                automatically by the system,
                <li> "disabled"       - Failover targets generated manually by
                the admin,
                <li> "enabled"        - Failover targets defined by
                failover-group
                </ul>
        
        :param data_protocols: Specifies the list of data protocols configured on the LIF.
                By default, the values in this element are nfs, cifs and fcache.
                Other supported protocols are iscsi and fcp.
                A LIF can be configured to not support any data protocols by
                specifying 'none'.
                Protocol values of none, iscsi or fcp can't be combined with any
                other data protocol(s).
                Possible values:
                <ul>
                <li> "nfs"       - Used for NFS connections,
                <li> "cifs"      - Used for CIFS connections,
                <li> "iscsi"     - Used for iSCSI connections,
                <li> "fcp"       - Used for Fibre Channel connections,
                <li> "fcache"    - Used for FlexCache connections,
                <li> "none"      - Used for management. Does not serve any file
                protocols.
                </ul>
        
        :param failover_group: Specifies the failover group name.
        
        :param address: Specifies the LIF's IP address.
                This element is valid for all data protocols except FCP.
        
        :param firewall_policy: Specifies the firewall policy for the LIF.
                Default firewall-policy is set as per the following table:
                <ul>
                <li> 'LIF Role    Protocols   Default policy',
                <li> '-------     ---------   --------------',
                <li> 'data         none             mgmt',
                <li> 'data         any              data',
                <li> 'node_mgmt    any              mgmt',
                <li> 'cluster_mgmt any              mgmt',
                <li> 'cluster      any              cluster',
                <li> 'intercluster any              intercluster'
                </ul>
        
        :param dns_domain_name: Specifies the unique, fully qualified domain name of the DNS zone
                of this LIF.
        
        :param listen_for_dns_query: If True, this IP address will listen for DNS queries for the
                dns-zone specified.
        
        :param return_record: If set to true, returns the given network interface on successful
                creation.
                Default: false
        
        :param is_auto_revert: If true, data LIF will revert to its home node under certain
                circumstances such as startup, and load balancing migration
                capability is disabled automatically.
                Default: false
        
        :param netmask: Specifies the LIF's netmask.
                This element is valid for all data protocols except FCP.
        
        :param failover_policy: Specifies the failover policy for the LIF.
                For FCP and iSCSI LIFs, the only failover policy is 'disabled';
                for NFS, CIFs and fcache LIFs, the default policy is
                'nextavail'.
                Possible values:
                <ul>
                <li> "nextavail" - Next failover target selected based on next
                port in failover targets list, preferring local ports first,
                <li> "priority"  - Next failover target selected based on first
                available port in failover targets list,
                <li> "disabled"  - Failover disabled
                </ul>
        
        :param netmask_length: Specifies number of bits in the netmask.
        
        :param administrative_status: Specifies the administrative status of the LIF.
                The administrative status can differ from the operational status;
                for instance, if you specify the status as up but a network
                problem prevents the interface from functioning, the operational
                status remains as down.
                Possible values:
                <ul>
                <li> 'up',
                <li> 'down',
                <li> 'unknown'
                </ul>
        
        :param routing_group_name: Specifies the routing group, which enables multiple logical
                interfaces to share a set of routing table entries.
                For example:
                d192.168.1.0/24 ('d' stands for data LIF and 192.168.1.0/24 is
                subnet)
                c192.168.1.0/24 ('c' stands for cluster LIF and 192.168.1.0/24 is
                subnet)
                n192.168.1.0/24 ('n' stands for node management LIF and
                192.168.1.0/24 is subnet)
                dfd20:13::0/50  ('d' stands for data LIF and fd20:13::0/50 is
                IPv6 subnet)
        
        :param is_ipv4_link_local: If true, automatically configure an interface with an IPv4
                address.
                User can configure an interface by explicitly specifying
                &lt;address&gt; and &lt;netmask&gt (or &lt;netmask-length&gt;);
                or by enabling is-ipv4-link-local to true.
        """
        return self.request( "net-interface-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'use_failover_group': [ use_failover_group, 'use-failover-group', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
            'data_protocols': [ data_protocols, 'data-protocols', [ basestring, 'data-protocol' ], True ],
            'failover_group': [ failover_group, 'failover-group', [ basestring, 'failover-group' ], False ],
            'address': [ address, 'address', [ basestring, 'ip-address' ], False ],
            'firewall_policy': [ firewall_policy, 'firewall-policy', [ basestring, 'None' ], False ],
            'dns_domain_name': [ dns_domain_name, 'dns-domain-name', [ basestring, 'dns-zone' ], False ],
            'listen_for_dns_query': [ listen_for_dns_query, 'listen-for-dns-query', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'is_auto_revert': [ is_auto_revert, 'is-auto-revert', [ bool, 'None' ], False ],
            'netmask': [ netmask, 'netmask', [ basestring, 'ip-address' ], False ],
            'role': [ role, 'role', [ basestring, 'None' ], False ],
            'failover_policy': [ failover_policy, 'failover-policy', [ basestring, 'None' ], False ],
            'home_node': [ home_node, 'home-node', [ basestring, 'None' ], False ],
            'netmask_length': [ netmask_length, 'netmask-length', [ int, 'None' ], False ],
            'administrative_status': [ administrative_status, 'administrative-status', [ basestring, 'None' ], False ],
            'home_port': [ home_port, 'home-port', [ basestring, 'None' ], False ],
            'routing_group_name': [ routing_group_name, 'routing-group-name', [ basestring, 'routing-group' ], False ],
            'is_ipv4_link_local': [ is_ipv4_link_local, 'is-ipv4-link-local', [ bool, 'None' ], False ],
        }, {
            'result': [ NetInterfaceInfo, False ],
        } )
    
    def net_dns_create(self, dns_state, domains, attempts=None, return_record=None, name_servers=None, timeout=None):
        """
        Creates DNS configuration for a Vserver
        
        :param dns_state: Enable/Disable DNS. Possible values are 'enabled' or 'disabled'.
        
        :param domains: List of DNS domains such as 'sales.bar.com'. The first domain is
                the one that the Vserver belongs to.
        
        :param attempts: Max number of trials before giving up and returning error.
                Default is one.
        
        :param return_record: If set to true, returns the dns on successful creation.
                Default: false
        
        :param name_servers: IPv4 addresses of name servers such as '123.123.123.123'.
        
        :param timeout: Number of seconds to wait for a response from a name server
                before trying a different name server. Default is two seconds.
        """
        return self.request( "net-dns-create", {
            'dns_state': [ dns_state, 'dns-state', [ basestring, 'enable' ], False ],
            'attempts': [ attempts, 'attempts', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'name_servers': [ name_servers, 'name-servers', [ basestring, 'ip-address' ], True ],
            'timeout': [ timeout, 'timeout', [ int, 'None' ], False ],
            'domains': [ domains, 'domains', [ basestring, 'None' ], True ],
        }, {
            'result': [ NetDnsInfo, False ],
        } )
    
    def net_ipspace_assign(self, ipspace_config_info):
        """
        Assign a list of interfaces to an ipspace.
        Modifies persistent config.
        
        :param ipspace_config_info: Ipspace to create.
        """
        return self.request( "net-ipspace-assign", {
            'ipspace_config_info': [ ipspace_config_info, 'ipspace-config-info', [ IpspaceConfigInfo, 'None' ], False ],
        }, {
        } )
    
    def net_config_get_active(self):
        """
        Output the current network config
        Output includes vlans, ifgrps and static routes with information from
        vlan, ifgrp, route & ifconfig commands
        EINVALIDINPUTERROR
        EAPINOTIMPLEMENTED
        ENOPARTNERIFC
        """
        return self.request( "net-config-get-active", {
        }, {
            'net-config-info': [ NetConfigInfo, False ],
        } )
    
    def net_vlan_create(self, vlan_info):
        """
        Create a new vlan interface.
        In Data ONTAP 7-Mode, changes made by this API are not
        persisted across system reboots.
        In Data ONTAP Cluster-Mode, changes made by this API are
        persisted across system reboots.
        
        :param vlan_info: Vlan to create.
        """
        return self.request( "net-vlan-create", {
            'vlan_info': [ vlan_info, 'vlan-info', [ VlanInfo, 'None' ], False ],
        }, {
        } )
    
    def net_hosts_destroy(self, host_ip_address):
        """
        Delete an existing hosts object.
        
        :param host_ip_address: IPv4 address in dotted form as '123.123.123.123'.
        """
        return self.request( "net-hosts-destroy", {
            'host_ip_address': [ host_ip_address, 'host-ip-address', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def net_placement_cache_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the LIF placement cached information.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                network interface placement object.
                All network interface placement objects matching this query up to
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
        return self.request( "net-placement-cache-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NetPlacementCache, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetPlacementCache, 'None' ], False ],
        }, {
            'attributes-list': [ NetPlacementCache, True ],
        } )
    
    def net_port_ifgrp_get(self, node, ifgrp_name, desired_attributes=None):
        """
        Get the attributes of a network interface group (ifgrp).
        
        :param node: Specifies the name of node.
        
        :param ifgrp_name: Specifies the interface group name.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "net-port-ifgrp-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'ifgrp_name': [ ifgrp_name, 'ifgrp-name', [ basestring, 'lif-bindable' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetIfgrpInfo, 'None' ], False ],
        }, {
            'attributes': [ NetIfgrpInfo, False ],
        } )
    
    def net_resolve(self, host_name):
        """
        Resolves a host name to one or more IP addresses.
        Returns an error code of gethostbyname_r if failed.
        Does not support IPv6 at this time.
        
        :param host_name: Name of the host to be resolved.
        """
        return self.request( "net-resolve", {
            'host_name': [ host_name, 'host-name', [ basestring, 'None' ], False ],
        }, {
            'ip-addresses': [ basestring, True ],
        } )
    
    def net_san_lif_placement_get(self, nodelist, protocol, lifs_per_node, adapter_type):
        """
        Get the attributes of the SAN LIF Placement.
        
        :param nodelist: Nodes list
        
        :param protocol: Protocol
        
        :param lifs_per_node: LIFs per node
        
        :param adapter_type: Adapter type
        """
        return self.request( "net-san-lif-placement-get", {
            'nodelist': [ nodelist, 'nodelist', [ basestring, 'node-name' ], True ],
            'protocol': [ protocol, 'protocol', [ basestring, 'data-protocol' ], False ],
            'lifs_per_node': [ lifs_per_node, 'lifs-per-node', [ int, 'None' ], False ],
            'adapter_type': [ adapter_type, 'adapter-type', [ basestring, 'adapter-type' ], False ],
        }, {
            'lif-placement': [ LifPlacementInfo, True ],
        } )
    
    def net_interface_delete(self, vserver, interface_name):
        """
        Destroy an existing network interface object.
        
        :param vserver: Specifies the Vserver name.
        
        :param interface_name: Specifies the logical interface (LIF) name.
        """
        return self.request( "net-interface-delete", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_hosts_modify(self, host_ip_address, hostname=None, aliases=None):
        """
        Given an IP address, modify the corresponding IP to host name
        mapping. Omitted (optional) fields will not be changed.
        
        :param host_ip_address: IPv4 address in dotted form as '123.123.123.123'.
        
        :param hostname: Canonical hostname in a simple string or in FQDN
        
        :param aliases: The list of aliases such as 'host1.sales.foo.com'.
        """
        return self.request( "net-hosts-modify", {
            'hostname': [ hostname, 'hostname', [ basestring, 'None' ], False ],
            'host_ip_address': [ host_ip_address, 'host-ip-address', [ basestring, 'ip-address' ], False ],
            'aliases': [ aliases, 'aliases', [ basestring, 'None' ], True ],
        }, {
        } )
    
    def net_interface_get(self, interface_name, desired_attributes=None):
        """
        Get the attributes of a network interface.
        
        :param interface_name: Specifies the logical interface (LIF) name.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "net-interface-get", {
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NetInterfaceInfo, 'None' ], False ],
        }, {
            'attributes': [ NetInterfaceInfo, False ],
        } )
    
    def net_enable_readonly(self, vserver, interface_name):
        """
        auto generated : Enable a logical interface in read-only mode
        
        :param vserver: Specifies the Vserver name.
        
        :param interface_name: Specifies the logical interface (LIF) name.
        """
        return self.request( "net-enable-readonly", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_hosts_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate all IP to host name mappings (over all Vserver) of the
        cluster
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                hosts object.
                All hosts objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "net-hosts-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ HostsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ HostsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ HostsInfo, True ],
        } )
    
    def net_config_set_persistent(self, net_config_info):
        """
        Writes filer's persistent network config.
        EIPV6
        EMODE
        EFILENOTFOUND
        EFILEIO
        
        :param net_config_info: Persistent network configuration (/etc/rc).
        """
        return self.request( "net-config-set-persistent", {
            'net_config_info': [ net_config_info, 'net-config-info', [ NetConfigInfo, 'None' ], False ],
        }, {
        } )
    
    def net_vlan_get(self, node, interface_name, desired_attributes=None):
        """
        Get the attributes of a VLAN.
        
        :param node: Node name of vlan interface.
        
        :param interface_name: Name of vlan interface. The name must be of the format
                &lt;parent-inteface&gt;-&lt;vlanid&gt;
        
        :param desired_attributes: Specify the attributes that should be returned. If not present,
                all attributes for which information is available will be
                returned. If present, only the desired attributes for which
                information is available will be returned.
        """
        return self.request( "net-vlan-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VlanInfo, 'None' ], False ],
        }, {
            'attributes': [ VlanInfo, False ],
        } )
    
    def net_vlan_delete(self, vlan_info):
        """
        Delete a vlan interface.
        In Data ONTAP 7-Mode, changes made by this API are not
        persisted across system reboots.
        In Data ONTAP Cluster-Mode, changes made by this API are
        persisted across system reboots.
        
        :param vlan_info: Vlan to delete.
        """
        return self.request( "net-vlan-delete", {
            'vlan_info': [ vlan_info, 'vlan-info', [ VlanInfo, 'None' ], False ],
        }, {
        } )
    
    def net_interface_migrate(self, lif, vserver, destination_node, destination_port=None, force=None, source_node=None):
        """
        Migrate a Logical Interface between nodes and ports
        
        :param lif: Specifies the logical interface that is to be migrated.
                example: lif1
        
        :param vserver: Specifies the Vserver that owns the logical interface that is to
                be migrated.
                example:  vs0
        
        :param destination_node: Specifies the node to which the logical interface is to be
                migrated.
        
        :param destination_port: Specifies the port or interface group to which the logical
                interface is to be migrated. If not specified, this field will be
                set to the port name of the port on which the LIF currently
                resides.
                example: node2
        
        :param force: Force the migration operation. If not specified, this field will
                be set to false. If set to true, migrating a LIF whos 'sticky'
                field is set to true, or whose current node is sick will be
                allowed. Otherwise they will not be permitted.
        
        :param source_node: Specifies the node from which the logical interface is to be
                migrated. If not specifed, this field will be set to the node on
                which the LIF currently resides.
                example: node1
        """
        return self.request( "net-interface-migrate", {
            'destination_port': [ destination_port, 'destination-port', [ basestring, 'None' ], False ],
            'lif': [ lif, 'lif', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'source_node': [ source_node, 'source-node', [ basestring, 'node-name' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'destination_node': [ destination_node, 'destination-node', [ basestring, 'node-name' ], False ],
        }, {
        } )
    
    def net_port_ifgrp_add_port(self, node, ifgrp_name, port):
        """
        Add port to a network interface group.
        
        :param node: Specifies the name of node.
        
        :param ifgrp_name: Specifies the interface group name.
        
        :param port: Specifies the name of port.
        """
        return self.request( "net-port-ifgrp-add-port", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'ifgrp_name': [ ifgrp_name, 'ifgrp-name', [ basestring, 'lif-bindable' ], False ],
            'port': [ port, 'port', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_ipspace_destroy(self, ipspace_name):
        """
        Destroy an ipspace.  Modifies persistent config.
        
        :param ipspace_name: IPSpace name.
        """
        return self.request( "net-ipspace-destroy", {
            'ipspace_name': [ ipspace_name, 'ipspace-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_routing_group_route_destroy(self, vserver, destination_address, routing_group):
        """
        Destroy an existing network routing group route.
        
        :param vserver: Specifies the name of Vserver.
        
        :param destination_address: Specifies the IP address and subnet mask of destination.
                For example: '198.18.10.0/24', 'fd20:13::0/64'
        
        :param routing_group: Specifies the name of routing group.
                For example:
                <ul>
                <li> d192.168.1.0/24 ('d' stands for data LIF and 192.168.1.0/24
                is subnet),
                <li> c192.168.1.0/24 ('c' stands for cluster LIF and
                192.168.1.0/24 is subnet),
                <li> n192.168.1.0/24 ('n' stands for node management LIF and
                192.168.1.0/24 is subnet)
                <li> dfd20:13::0/64  ('d' stands for data LIF and
                fd20:13::0/64 is IPv6 subnet)
                </ul>
        """
        return self.request( "net-routing-group-route-destroy", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'destination_address': [ destination_address, 'destination-address', [ basestring, 'None' ], False ],
            'routing_group': [ routing_group, 'routing-group', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def net_routing_group_route_get(self, destination_address, routing_group, desired_attributes=None):
        """
        Get the attributes of a network routing group route.
        
        :param destination_address: Specifies the IP address and subnet mask of destination.
                For example: '198.18.10.0/24', 'fd20:13::0/64'
        
        :param routing_group: Specifies the name of routing group.
                For example:
                <ul>
                <li> d192.168.1.0/24 ('d' stands for data LIF and 192.168.1.0/24
                is subnet),
                <li> c192.168.1.0/24 ('c' stands for cluster LIF and
                192.168.1.0/24 is subnet),
                <li> n192.168.1.0/24 ('n' stands for node management LIF and
                192.168.1.0/24 is subnet)
                <li> dfd20:13::0/64  ('d' stands for data LIF and
                fd20:13::0/64 is IPv6 subnet)
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "net-routing-group-route-get", {
            'destination_address': [ destination_address, 'destination-address', [ basestring, 'None' ], False ],
            'routing_group': [ routing_group, 'routing-group', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ RoutingGroupRouteInfo, 'None' ], False ],
        }, {
            'attributes': [ RoutingGroupRouteInfo, False ],
        } )
    
    def net_dns_destroy(self):
        """
        Remove the DNS configuration of the specified Vserver
        """
        return self.request( "net-dns-destroy", {
        }, {
        } )
    
    def net_ipspace_list(self):
        """
        List ipspaces.
        """
        return self.request( "net-ipspace-list", {
        }, {
            'ipspace-list': [ IpspaceConfigInfo, True ],
        } )
    
    def net_disable_readonly(self, vserver, interface_name):
        """
        auto generated : Disable a logical interface in read-only mode
        
        :param vserver: Specifies the Vserver name.
        
        :param interface_name: Specifies the logical interface (LIF) name.
        """
        return self.request( "net-disable-readonly", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )

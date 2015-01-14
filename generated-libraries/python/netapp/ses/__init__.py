from netapp.connection import NaConnection
from shelf_environ_channel_info import ShelfEnvironChannelInfo # 7 properties
from ariodata_specific_info import AriodataSpecificInfo # 1 properties
from shelf_bay_list_info import ShelfBayListInfo # 9 properties
from storage_shelf_enclosure_info import StorageShelfEnclosureInfo # 65 properties
from phy_expander_info import PhyExpanderInfo # 19 properties
from shelf_bay_info import ShelfBayInfo # 2 properties
from shelf_environ_channel_address_map import ShelfEnvironChannelAddressMap # 2 properties
from esh_info import EshInfo # 2 properties
from shelf_bay_port_info import ShelfBayPortInfo # 5 properties
from port_hub_info import PortHubInfo # 11 properties
from module_info import ModuleInfo # 3 properties
from xyratex_specific_info import XyratexSpecificInfo # 2 properties
from shelf_environ_shelf_info import ShelfEnvironShelfInfo # 29 properties
from current_sensor_info import CurrentSensorInfo # 5 properties
from channel_info import ChannelInfo # 1 properties
from connector_info import ConnectorInfo # 1 properties
from enclosure_info import EnclosureInfo # 2 properties
from dongle_info import DongleInfo # 3 properties
from processor_complex_info import ProcessorComplexInfo # 3 properties
from es_electronics_info import EsElectronicsInfo # 9 properties
from eurologic_specific_info import EurologicSpecificInfo # 7 properties
from voltage_sensor_info import VoltageSensorInfo # 5 properties
from ses_generic_info import SesGenericInfo # 12 properties
from alternate_control_path_info import AlternateControlPathInfo # 17 properties
from bay_info import BayInfo # 2 properties
from temp_sensor_info import TempSensorInfo # 10 properties
from sas_specific_info import SasSpecificInfo # 1 properties
from shelf_info import ShelfInfo # 15 properties
from cooling_element_info import CoolingElementInfo # 4 properties
from power_supply_info import PowerSupplyInfo # 10 properties
from sas_connector_info import SasConnectorInfo # 14 properties
from shelf_id_info import ShelfIdInfo # 1 properties

class SesConnection(NaConnection):
    
    def storage_shelf_update_fw(self, shelf_id=None, channel_name=None):
        """
        Start shelf firmware download process to update firmware on disk
        shelves. This operation is asynchronous, and therefore
        returns no errors that might occur during the download
        process. This operation will only update firmware on
        shelves that do not have the latest firmware revision.
        The firmware revision on the shelves can be monitored via
        the storage-shelf-get-shelf-info API. NOT IMPLEMENTED YET.
        Internal error.
        Wrong input combination of channel and/or shelf was given.
        This will cause the command to fail immediately. No action
        will be taken.
        
        :param shelf_id: If present, will only update firmware on the given
                shelf on specified channel.
                If not present, and a channel-name is specified, then
                all shelves on the channel will be updated.
                Example: To update firmware on 2a.shelf1, channel
                should be 2a and shelf should be 1.
        
        :param channel_name: If present, will only update firmware on all shelves (or a single
                shlef depending on shelf-id) on the given channel.
                If not present, then all shelves on all channels are
                updated.
                Example: To update firmware on 2a.shelf1, channel
                should be 2a and shelf should be 1.
        """
        return self.request( "storage-shelf-update-fw", {
            'shelf_id': [ shelf_id, 'shelf-id', [ basestring, 'None' ], False ],
            'channel_name': [ channel_name, 'channel-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_shelf_get_channel_list(self):
        """
        Get the list of SES channels present on this system.
        """
        return self.request( "storage-shelf-get-channel-list", {
        }, {
            'channel-list': [ ChannelInfo, True ],
        } )
    
    def storage_shelf_set_led_state(self, action, shelf_id, channel_name, shelf_bay=None, identify=None, duration=None, lun=None):
        """
        Set or clear the LED for a disk, shelf of disks
        or loop of shelves.
        LEDs to affect can be specified as:
        {channel-name},
        {channel-name, shelf-id},
        {channel-name, shelf-id, shelf-bay},
        {channel-name, shelf-id, shelf-bay},
        {channel-name, shelf-id, shelf-bay, lun}.
        
        :param action: This specifies the action to apply.  Possible values
                are: on, and off.  on: Turn the LED(s) on
                indefinitely.  off: Turn the LED(s) off.
        
        :param shelf_id: If present, the shelf-id indicates which shelf has the
                drive or drives where the LEDs to affect reside.
                Range : [0..2^24-1]
        
        :param channel_name: The channel to which the shelf or drive LED to be
                affected is connected.
                A channel-name is the adapter number or switch
                name and the port number (together, called the
                channel).  Examples are 8a and switch:5.
        
        :param shelf_bay: If present, the shelf-bay indicates the specific drive
                where the LED affected resides.  If shelf-id is
                supplied but shelf-bay is not, then the LEDs for all
                drives in the shelf will be affected.
                Range : [0..255]
        
        :param identify: This parameter allows the caller to specify the
                identify LED.  The default is for the command to
                affect the fault LED.  Not all disks have identify
                LEDs.  In that case, the identify option is ignored
                and the fault LED is affected.
        
        :param duration: This parameter allows the caller to specify the
                duration (in seconds) that the action will be
                applied.  Note that the action 'on' is indefinite,
                while 'test' uses duration.  'blink' also uses
                duration.
        
        :param lun: Some targets have a logical unit number.  In that case,
                the lun will be required to uniquely specify the
                LED to affect.
                Range : [0..255]
        """
        return self.request( "storage-shelf-set-led-state", {
            'shelf_bay': [ shelf_bay, 'shelf-bay', [ int, 'None' ], False ],
            'action': [ action, 'action', [ basestring, 'None' ], False ],
            'identify': [ identify, 'identify', [ bool, 'None' ], False ],
            'duration': [ duration, 'duration', [ int, 'None' ], False ],
            'shelf_id': [ shelf_id, 'shelf-id', [ int, 'None' ], False ],
            'lun': [ lun, 'lun', [ int, 'None' ], False ],
            'channel_name': [ channel_name, 'channel-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_shelf_enclosure_list_info(self):
        """
        Obtains data about Enclosures.
        """
        return self.request( "storage-shelf-enclosure-list-info", {
        }, {
            'enclosure-list': [ StorageShelfEnclosureInfo, True ],
        } )
    
    def storage_shelf_get_shelf_info(self, node_name, shelf_id, channel_name):
        """
        This returns information about an identified shelf.
        The information is the number of bays present (bay-count),
        and which shelf bays have drives (bay-list).
        Shelf bays are numbered from 0 to bay-count minus 1.
        Shelf bay 0 is always on the right when looking at
        the front of the shelf.  Incidentally, the bay-list may
        be empty indicating the absence of any drives.  However,
        there are some shelf designs which require a disk drive
        in bay 0 or 1 for any SES functionality to operate (e.g.,
        DS14 and DS14-Mk2-FC).  In these cases,
        shelves without drives in bay 0 or 1 will not be listed.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. This is the storage system name
                name the command will be executed on.
        
        :param shelf_id: The shelf id specifies the shelf for which a list of
                disk bays is desired.
                Range : [0..2^24-1]
        
        :param channel_name: The adapter number or switch name and theport number
                (together, called the channel).
                Examples are 8a and switch:5
        """
        return self.request( "storage-shelf-get-shelf-info", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'shelf_id': [ shelf_id, 'shelf-id', [ int, 'None' ], False ],
            'channel_name': [ channel_name, 'channel-name', [ basestring, 'None' ], False ],
        }, {
            'firmware-rev-A': [ basestring, False ],
            'firmware-rev-B': [ basestring, False ],
            'shelf-type': [ basestring, False ],
            'node-name': [ basestring, False ],
            'bay-count': [ int, False ],
            'bay-list': [ BayInfo, True ],
            'firmware-revision': [ basestring, False ],
        } )
    
    def storage_shelf_get_shelf_list(self, channel_name):
        """
        Get the list of SES shelves present on a channel.  Use
        storage-shelf-get-channel-list to determine all the channels
        to which shelves are connected.  Note that some
        shelves may be connected to multiple channels.
        
        :param channel_name: The adapter number or switch name and the port number
                (together, called the channel).  Examples are 8a and
                switch:5.
        """
        return self.request( "storage-shelf-get-shelf-list", {
            'channel_name': [ channel_name, 'channel-name', [ basestring, 'None' ], False ],
        }, {
            'shelf-list': [ ShelfIdInfo, True ],
        } )
    
    def storage_shelf_environment_list_info(self, node_name, shelf_id=None, channel_name=None):
        """
        Returns the environmental information for a selected
        number of shelves, or optionally all shelves connected to
        the storage controller.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. This is the storage system name
                the command will be executed on.
        
        :param shelf_id: Get environment information for the specified shelf-id on the
                specified channel-name. This parameter requires channel-name
                parameter as well. If shelf-id is specified without channel-name
                then the error code EINVALIDINPUTERROR will be returned.
                If shelf-id is not specified and a channel-name is specified,
                then data for all shelves on the channel-name is returned.
                If an invalid shelf-id is specified, then error code
                ESHELFNOTFOUND will be returned.
        
        :param channel_name: Get environment information for shelves on this channel. shelf-id
                parameter can be specified to request data on a single shelf. If a
                channel-name is not specified, then data on all shelves on all
                channels will be returned. If an invalid channel-name is
                specified, then error code ECHANNELNOTFOUND will be returned.
        """
        return self.request( "storage-shelf-environment-list-info", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'shelf_id': [ shelf_id, 'shelf-id', [ int, 'None' ], False ],
            'channel_name': [ channel_name, 'channel-name', [ basestring, 'None' ], False ],
        }, {
            'shelf-environ-channel-list': [ ShelfEnvironChannelInfo, True ],
        } )
    
    def storage_shelf_list_info(self, node_name, shelf_id=None, channel_name=None):
        """
        This interface returns information about one or more shelves.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. This is the storage system name
                the command will be executed on.
        
        :param shelf_id: shelf-id is the shelf number for which shelf data is
                requested. This input requires that channel-name input
                also be specified. If a channel-name and shelf-id are
                both specified then information for the specified shelf
                will be presented (a single shelf). If channel-name is
                specified, but shelf-id is missing, then information for
                all shelves on the channel will be presented.
                If channel-name is not specified then shelf-id is not
                supported. In such case information for all shelves on all
                channels will be presented.
        
        :param channel_name: The adapter number or switch name and the port number
                (together, called the channel). If missing, then information
                for all shelves on all channels will be presented.
                If missing, then shelf-id input is not allowed.
                Examples are 8a and switch:5
        """
        return self.request( "storage-shelf-list-info", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'shelf_id': [ shelf_id, 'shelf-id', [ int, 'None' ], False ],
            'channel_name': [ channel_name, 'channel-name', [ basestring, 'None' ], False ],
        }, {
            'shelf-list': [ ShelfInfo, True ],
        } )
    
    def storage_shelf_bay_list_info(self, node_name=None, shelf_id=None, channel_name=None):
        """
        Returns information about storage shelf bays and ports
        for a selected number of shelves, or optionally all
        shelves connected to the storage controller.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. If node-name is not specified
                when the request is sent to Admin VserverLIF, then all
                matching shelves in the cluster will be returned.
                This is the storage system name the command will
                be executed on.
        
        :param shelf_id: shelf-id is the shelf number for which shelf data is
                requested. This input requires that channel-name input
                also be specified. If a channel-name and shelf-id are
                both specified then information for the specified shelf
                will be presented (a single shelf). If channel-name is
                specified, but shelf-id is missing, then information for
                all shelves on the channel will be presented.
                If channel-name is not specified then shelf-id is not
                supported and an error will be returned.
        
        :param channel_name: The adapter number or switch name and the port number
                (together, called the channel). If missing, then information
                for all shelves on all channels will be presented.
                If missing, then shelf-id input is not allowed.
                Examples: 8a, switch:5
        """
        return self.request( "storage-shelf-bay-list-info", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'shelf_id': [ shelf_id, 'shelf-id', [ int, 'None' ], False ],
            'channel_name': [ channel_name, 'channel-name', [ basestring, 'None' ], False ],
        }, {
            'shelf-bay-list': [ ShelfBayListInfo, True ],
        } )
    
    def storage_shelf_get_disk_info_by_name(self, disk_name):
        """
        Obtains a channel-name, shelf-id, shelf-bay and,
        optionally, a lun for the supplied disk-name.
        
        :param disk_name: The name of the disk for which disk information
                is to be obtained.  If disk-name is not
                supplied, the command will return EAPIMISSINGARGUMENT.
                If the disk is not found, the command will return
                EDISKNOTFOUND.
                An example disk-name is '8a.32'.
                The output of this command is channel-name, shelf-id,
                and shelf-bay with an optional lun value.  Some disks
                can be dual attached.  Dual attached disks have
                two paths.  This command picks an arbitrary path for
                the named disk.  Either path should work fine.
                There is no API for getting the secondary
                path.
        """
        return self.request( "storage-shelf-get-disk-info-by-name", {
            'disk_name': [ disk_name, 'disk-name', [ basestring, 'None' ], False ],
        }, {
            'shelf-id': [ int, False ],
            'lun': [ int, False ],
            'shelf-bay': [ int, False ],
            'channel-name': [ basestring, False ],
        } )

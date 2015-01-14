from netapp.disk.storage_ssd_info import StorageSsdInfo
from netapp.disk.v_series_detail_info import VSeriesDetailInfo
from netapp.netapp_object import NetAppObject

class DiskDetailInfo(NetAppObject):
    """
    Disk status information.
    """
    
    _raid_group = None
    @property
    def raid_group(self):
        """
        Raid group disk belongs.  Not returned if
        disk doesn't belong to any raid group.
        """
        return self._raid_group
    @raid_group.setter
    def raid_group(self, val):
        if val != None:
            self.validate('raid_group', val)
        self._raid_group = val
    
    _copy_destination = None
    @property
    def copy_destination(self):
        """
        The name of the disk selected as the destination to
        copy this disk when it must be replaced (is-prefailed
        or is-replacing is true).
        This element is not returned if the destination is
        not selected.  The destination might not be present
        even when is-prefailed or is-replacing is true, if
        there is no appropriate spare, or other
        disk copy is in progress, or the destination was not
        yet selected, including immediately after
        disk-replace-start.
        """
        return self._copy_destination
    @copy_destination.setter
    def copy_destination(self, val):
        if val != None:
            self.validate('copy_destination', val)
        self._copy_destination = val
    
    _grown_defect_list_count = None
    @property
    def grown_defect_list_count(self):
        """
        Number of entries in the drive's grown defect list.
        Range: [0..2^64-1]
        """
        return self._grown_defect_list_count
    @grown_defect_list_count.setter
    def grown_defect_list_count(self, val):
        if val != None:
            self.validate('grown_defect_list_count', val)
        self._grown_defect_list_count = val
    
    _used_space = None
    @property
    def used_space(self):
        """
        Used space in bytes.  Range : [0..2^64-1].
        """
        return self._used_space
    @used_space.setter
    def used_space(self, val):
        if val != None:
            self.validate('used_space', val)
        self._used_space = val
    
    _is_zeroed = None
    @property
    def is_zeroed(self):
        """
        True if the disk is a spare and has already been
        zeroed, false otherwise.  If disk is not a spare
        or if it is currently being zeroed, this element
        will not be included with the output.
        """
        return self._is_zeroed
    @is_zeroed.setter
    def is_zeroed(self, val):
        if val != None:
            self.validate('is_zeroed', val)
        self._is_zeroed = val
    
    _bytes_per_sector = None
    @property
    def bytes_per_sector(self):
        """
        Bytes per sector.  Range : [0..2^31-1].
        """
        return self._bytes_per_sector
    @bytes_per_sector.setter
    def bytes_per_sector(self, val):
        if val != None:
            self.validate('bytes_per_sector', val)
        self._bytes_per_sector = val
    
    _blocks_read = None
    @property
    def blocks_read(self):
        """
        Number of blocks read since the controller was powered
        on last.
        Range: [0..2^64-1]
        """
        return self._blocks_read
    @blocks_read.setter
    def blocks_read(self, val):
        if val != None:
            self.validate('blocks_read', val)
        self._blocks_read = val
    
    _aggregate = None
    @property
    def aggregate(self):
        """
        Aggregate that the disk resides on. Returned for
        disks contained on a flexible volume. Not returned
        for traditional volumes.
        """
        return self._aggregate
    @aggregate.setter
    def aggregate(self, val):
        if val != None:
            self.validate('aggregate', val)
        self._aggregate = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Disk serial number.  Maximum length of 129
        characters.
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _firmware_revision = None
    @property
    def firmware_revision(self):
        """
        Firmware revision of disk.  The format of the
        firmware revision  will vary depending on the
        type of disk and its vendor.
        """
        return self._firmware_revision
    @firmware_revision.setter
    def firmware_revision(self, val):
        if val != None:
            self.validate('firmware_revision', val)
        self._firmware_revision = val
    
    _raid_type = None
    @property
    def raid_type(self):
        """
        Raid type.  Possible values are :
        pending, parity, dparity, data, and unowned.
        """
        return self._raid_type
    @raid_type.setter
    def raid_type(self, val):
        if val != None:
            self.validate('raid_type', val)
        self._raid_type = val
    
    _id = None
    @property
    def id(self):
        """
        internal Id of disk.  Range : [-2^31..2^31-1].
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    _used_blocks = None
    @property
    def used_blocks(self):
        """
        Number of 512-byte blocks used.  Range : [0..2^64-1].
        """
        return self._used_blocks
    @used_blocks.setter
    def used_blocks(self, val):
        if val != None:
            self.validate('used_blocks', val)
        self._used_blocks = val
    
    _ssd_info = None
    @property
    def ssd_info(self):
        """
        Info block for solid-state storage devices.
        """
        return self._ssd_info
    @ssd_info.setter
    def ssd_info(self, val):
        if val != None:
            self.validate('ssd_info', val)
        self._ssd_info = val
    
    _rpm = None
    @property
    def rpm(self):
        """
        Rotational speed in revolutions per minute.
        Possible values are: 5400, 7200, 10000, and 15000.
        This element is not returned when the value is not
        known, or when it does not apply.
        """
        return self._rpm
    @rpm.setter
    def rpm(self, val):
        if val != None:
            self.validate('rpm', val)
        self._rpm = val
    
    _port = None
    @property
    def port(self):
        """
        Port of disk, e.g. A.
        """
        return self._port
    @port.setter
    def port(self, val):
        if val != None:
            self.validate('port', val)
        self._port = val
    
    _is_dynamically_qualified = None
    @property
    def is_dynamically_qualified(self):
        """
        True if the drive was dynamically qualified.
        """
        return self._is_dynamically_qualified
    @is_dynamically_qualified.setter
    def is_dynamically_qualified(self, val):
        if val != None:
            self.validate('is_dynamically_qualified', val)
        self._is_dynamically_qualified = val
    
    _secondary_name = None
    @property
    def secondary_name(self):
        """
        Secondary name.
        """
        return self._secondary_name
    @secondary_name.setter
    def secondary_name(self, val):
        if val != None:
            self.validate('secondary_name', val)
        self._secondary_name = val
    
    _scrub_last_done = None
    @property
    def scrub_last_done(self):
        """
        Number of seconds since the last time scrub was completed.
        Range: [0-2^64-1]
        """
        return self._scrub_last_done
    @scrub_last_done.setter
    def scrub_last_done(self, val):
        if val != None:
            self.validate('scrub_last_done', val)
        self._scrub_last_done = val
    
    _secondary_host_adapter = None
    @property
    def secondary_host_adapter(self):
        """
        Secondary Host adapter.
        """
        return self._secondary_host_adapter
    @secondary_host_adapter.setter
    def secondary_host_adapter(self, val):
        if val != None:
            self.validate('secondary_host_adapter', val)
        self._secondary_host_adapter = val
    
    _node = None
    @property
    def node(self):
        """
        Controller supplying this disk record.
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _disk_type = None
    @property
    def disk_type(self):
        """
        Type of disk: ATA, BSAS, EATA, FCAL, FSAS, LUN, MSATA,
        SAS, SATA, SCSI, SSD, XATA, XSAS, or unknown.
        """
        return self._disk_type
    @disk_type.setter
    def disk_type(self, val):
        if val != None:
            self.validate('disk_type', val)
        self._disk_type = val
    
    _broken_details = None
    @property
    def broken_details(self):
        """
        Reason for the disk failure, if raid-state is
        'broken'.  Possible values are 	'unknown',
        'failed', 'admin failed', 'labeled broken',
        'init failed', 'admin removed', 'not responding',
        'pulled', 'bad label', 'bypassed', 'SFO Disk'
        and 'not failed'.  If raid-state is not 'broken',
        broken-details will be omitted in the ouput.
        """
        return self._broken_details
    @broken_details.setter
    def broken_details(self, val):
        if val != None:
            self.validate('broken_details', val)
        self._broken_details = val
    
    _disk_model = None
    @property
    def disk_model(self):
        """
        Disk model.
        """
        return self._disk_model
    @disk_model.setter
    def disk_model(self, val):
        if val != None:
            self.validate('disk_model', val)
        self._disk_model = val
    
    _shm_time_interval = None
    @property
    def shm_time_interval(self):
        """
        Number of seconds we have been counting errors from
        SHM (Storage Health Monitor). Range: [0..2^64-1]
        """
        return self._shm_time_interval
    @shm_time_interval.setter
    def shm_time_interval(self, val):
        if val != None:
            self.validate('shm_time_interval', val)
        self._shm_time_interval = val
    
    _checksum_compatibility = None
    @property
    def checksum_compatibility(self):
        """
        An indication of the checksum types that this
        disk is capable of supporting.  Each possible
        return value represents one or more checksum
        types.
        <p>
        Starting in Data ONTAP 8.1, "zoned/block"
        is no longer supported.
        <p>
        Possible values are:
        <ul>
        <li> "advanced_zoned"           - Supports advanced_zoned
        checksum.
        <li> "block"                    - Supports block checksum.
        <li> "none"                     - No checksum support.
        <li> "zoned/advanced_zoned" - Supports zoned and
        advanced_zoned checksum.
        <li> "zoned/block"              - Supports zoned and
        block checksum.
        </ul>
        """
        return self._checksum_compatibility
    @checksum_compatibility.setter
    def checksum_compatibility(self, val):
        if val != None:
            self.validate('checksum_compatibility', val)
        self._checksum_compatibility = val
    
    _shelf = None
    @property
    def shelf(self):
        """
        Disk shelf. If disk shelf can't be determined, value
        will be "?".
        """
        return self._shelf
    @shelf.setter
    def shelf(self, val):
        if val != None:
            self.validate('shelf', val)
        self._shelf = val
    
    _poweron_hours = None
    @property
    def poweron_hours(self):
        """
        Number of hours the drive has been powered on.
        Range: [0..2^64-1]
        """
        return self._poweron_hours
    @poweron_hours.setter
    def poweron_hours(self, val):
        if val != None:
            self.validate('poweron_hours', val)
        self._poweron_hours = val
    
    _zeroing_percent = None
    @property
    def zeroing_percent(self):
        """
        Zeroing percentage done, if disk is being zeroed.
        Element is not returned if disk is not being zeroed.
        Range : [0..100].
        """
        return self._zeroing_percent
    @zeroing_percent.setter
    def zeroing_percent(self, val):
        if val != None:
            self.validate('zeroing_percent', val)
        self._zeroing_percent = val
    
    _plex = None
    @property
    def plex(self):
        """
        Plex the disk belongs.  Not returned if
        disk doesn't belong to any plex.  Example :
        plex0.
        """
        return self._plex
    @plex.setter
    def plex(self, val):
        if val != None:
            self.validate('plex', val)
        self._plex = val
    
    _volume = None
    @property
    def volume(self):
        """
        Volume the disks is used in.  Not returned if
        disk isn't used in any volume or if the disk
        belongs to a partner or if the disk is in an
        aggregate.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _raid_state = None
    @property
    def raid_state(self):
        """
        Raid state.  Possible values are :
        partner, broken, zeroing, spare, copy,
        pending, reconstructing, present and
        unknown.
        """
        return self._raid_state
    @raid_state.setter
    def raid_state(self, val):
        if val != None:
            self.validate('raid_state', val)
        self._raid_state = val
    
    _physical_space = None
    @property
    def physical_space(self):
        """
        Physical disk size in bytes.  Range :
        [0..2^64-1].
        """
        return self._physical_space
    @physical_space.setter
    def physical_space(self, val):
        if val != None:
            self.validate('physical_space', val)
        self._physical_space = val
    
    _vendor_id = None
    @property
    def vendor_id(self):
        """
        Vendor of this disk.
        """
        return self._vendor_id
    @vendor_id.setter
    def vendor_id(self, val):
        if val != None:
            self.validate('vendor_id', val)
        self._vendor_id = val
    
    _copy_percent = None
    @property
    def copy_percent(self):
        """
        Percent of disk copy done, if disk is involved in
        Rapid RAID Recovery, either as the source
        (is-prefailed or is-replacing is true) or as the
        destination (raid-state is 'copy') of disk copy.
        This element is not returned if the destination is
        not selected yet.
        Range : [0..100].
        """
        return self._copy_percent
    @copy_percent.setter
    def copy_percent(self, val):
        if val != None:
            self.validate('copy_percent', val)
        self._copy_percent = val
    
    _host_adapter = None
    @property
    def host_adapter(self):
        """
        Host adapter.
        """
        return self._host_adapter
    @host_adapter.setter
    def host_adapter(self, val):
        if val != None:
            self.validate('host_adapter', val)
        self._host_adapter = val
    
    _blocks_written = None
    @property
    def blocks_written(self):
        """
        Number of blocks written since the controller was
        powered on last.
        Range: [0..2^64-1]
        """
        return self._blocks_written
    @blocks_written.setter
    def blocks_written(self, val):
        if val != None:
            self.validate('blocks_written', val)
        self._blocks_written = val
    
    _v_series_detail_info = None
    @property
    def v_series_detail_info(self):
        """
        Lists LUN status from RAID array LUNs
        """
        return self._v_series_detail_info
    @v_series_detail_info.setter
    def v_series_detail_info(self, val):
        if val != None:
            self.validate('v_series_detail_info', val)
        self._v_series_detail_info = val
    
    _pool = None
    @property
    def pool(self):
        """
        Pool the disk is in.  Example : pool0.
        """
        return self._pool
    @pool.setter
    def pool(self, val):
        if val != None:
            self.validate('pool', val)
        self._pool = val
    
    _scrub_count = None
    @property
    def scrub_count(self):
        """
        Number of times the drive was scrubbed since the
        controller was powered on last. Range: [0..2^64-1]
        """
        return self._scrub_count
    @scrub_count.setter
    def scrub_count(self, val):
        if val != None:
            self.validate('scrub_count', val)
        self._scrub_count = val
    
    _is_replacing = None
    @property
    def is_replacing(self):
        """
        True if the disk is marked to be replaced with
        another disk and undergoing disk copy (as the source)
        or waiting for such disk copy to be started, false
        otherwise.
        """
        return self._is_replacing
    @is_replacing.setter
    def is_replacing(self, val):
        if val != None:
            self.validate('is_replacing', val)
        self._is_replacing = val
    
    _is_prefailed = None
    @property
    def is_prefailed(self):
        """
        True if the disk is prefailed and undergoing disk
        copy (as the source) or waiting for such disk copy
        to be started, false otherwise.
        """
        return self._is_prefailed
    @is_prefailed.setter
    def is_prefailed(self, val):
        if val != None:
            self.validate('is_prefailed', val)
        self._is_prefailed = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the disk, e.g. v1.1
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _reconstruction_percent = None
    @property
    def reconstruction_percent(self):
        """
        Percent of reconstruction done, if the disk is
        undergoing reconstruction (raid-state is
        'reconstructing').  This element is not returned if
        the disk is not being reconstructed.
        Range : [0..100].
        """
        return self._reconstruction_percent
    @reconstruction_percent.setter
    def reconstruction_percent(self, val):
        if val != None:
            self.validate('reconstruction_percent', val)
        self._reconstruction_percent = val
    
    _raw_disk_sectors = None
    @property
    def raw_disk_sectors(self):
        """
        Number of sectors on disk (as reported by the read
        capacity command).
        Range: [0..2^64-1].
        """
        return self._raw_disk_sectors
    @raw_disk_sectors.setter
    def raw_disk_sectors(self, val):
        if val != None:
            self.validate('raw_disk_sectors', val)
        self._raw_disk_sectors = val
    
    _bay = None
    @property
    def bay(self):
        """
        Disk bay. If disk bay can't be determined, value will
        be "?".
        """
        return self._bay
    @bay.setter
    def bay(self, val):
        if val != None:
            self.validate('bay', val)
        self._bay = val
    
    _is_offline = None
    @property
    def is_offline(self):
        """
        True if the disk is offline. If the disk is not
        offline, this element will not be included with
        the output.
        """
        return self._is_offline
    @is_offline.setter
    def is_offline(self, val):
        if val != None:
            self.validate('is_offline', val)
        self._is_offline = val
    
    _physical_blocks = None
    @property
    def physical_blocks(self):
        """
        Number of 512-byte blocks on disk.  Range :
        [0..2^64-1].
        """
        return self._physical_blocks
    @physical_blocks.setter
    def physical_blocks(self, val):
        if val != None:
            self.validate('physical_blocks', val)
        self._physical_blocks = val
    
    _secondary_port = None
    @property
    def secondary_port(self):
        """
        Secondary port.
        """
        return self._secondary_port
    @secondary_port.setter
    def secondary_port(self, val):
        if val != None:
            self.validate('secondary_port', val)
        self._secondary_port = val
    
    _port_name = None
    @property
    def port_name(self):
        """
        The port name of the disk object, e.g. FC:A.
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _effective_disk_type = None
    @property
    def effective_disk_type(self):
        """
        Disks with same effective-disk-type are compatible,
        and they can be used in the same aggregate, even though
        their physical disk type, as reported by disk-type
        may be different.  Possible values are the same as
        for disk-type: ATA, BSAS, EATA, FCAL, FSAS, LUN, MSATA,
        SAS, SATA, SCSI, SSD, XATA, XSAS, or unknown.
        """
        return self._effective_disk_type
    @effective_disk_type.setter
    def effective_disk_type(self, val):
        if val != None:
            self.validate('effective_disk_type', val)
        self._effective_disk_type = val
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        Disk unique identifier. Maximum length of 90
        characters.
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    @staticmethod
    def get_api_name():
          return "disk-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'raid-group',
            'copy-destination',
            'grown-defect-list-count',
            'used-space',
            'is-zeroed',
            'bytes-per-sector',
            'blocks-read',
            'aggregate',
            'serial-number',
            'firmware-revision',
            'raid-type',
            'id',
            'used-blocks',
            'ssd-info',
            'rpm',
            'port',
            'is-dynamically-qualified',
            'secondary-name',
            'scrub-last-done',
            'secondary-host-adapter',
            'node',
            'disk-type',
            'broken-details',
            'disk-model',
            'shm-time-interval',
            'checksum-compatibility',
            'shelf',
            'poweron-hours',
            'zeroing-percent',
            'plex',
            'volume',
            'raid-state',
            'physical-space',
            'vendor-id',
            'copy-percent',
            'host-adapter',
            'blocks-written',
            'v-series-detail-info',
            'pool',
            'scrub-count',
            'is-replacing',
            'is-prefailed',
            'name',
            'reconstruction-percent',
            'raw-disk-sectors',
            'bay',
            'is-offline',
            'physical-blocks',
            'secondary-port',
            'port-name',
            'effective-disk-type',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'raid_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'copy_destination': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'grown_defect_list_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'used_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_zeroed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'bytes_per_sector': { 'class': int, 'is_list': False, 'required': 'required' },
            'blocks_read': { 'class': int, 'is_list': False, 'required': 'required' },
            'aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'firmware_revision': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'raid_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'id': { 'class': int, 'is_list': False, 'required': 'required' },
            'used_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
            'ssd_info': { 'class': StorageSsdInfo, 'is_list': False, 'required': 'optional' },
            'rpm': { 'class': int, 'is_list': False, 'required': 'optional' },
            'port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_dynamically_qualified': { 'class': bool, 'is_list': False, 'required': 'required' },
            'secondary_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'scrub_last_done': { 'class': int, 'is_list': False, 'required': 'required' },
            'secondary_host_adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'broken_details': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_model': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'shm_time_interval': { 'class': int, 'is_list': False, 'required': 'required' },
            'checksum_compatibility': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'shelf': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'poweron_hours': { 'class': int, 'is_list': False, 'required': 'optional' },
            'zeroing_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'plex': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'raid_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'physical_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'vendor_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'copy_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'host_adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'blocks_written': { 'class': int, 'is_list': False, 'required': 'required' },
            'v_series_detail_info': { 'class': VSeriesDetailInfo, 'is_list': False, 'required': 'optional' },
            'pool': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'scrub_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_replacing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_prefailed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'reconstruction_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'raw_disk_sectors': { 'class': int, 'is_list': False, 'required': 'required' },
            'bay': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_offline': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'physical_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
            'secondary_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'effective_disk_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }

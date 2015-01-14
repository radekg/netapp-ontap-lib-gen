from netapp.snapmirror.snapmirror_error import SnapmirrorError
from netapp.netapp_object import NetAppObject

class SnapmirrorSyncScheduleInfo(NetAppObject):
    """
    Contains the synchronous SnapMirror schedule per
    destination.  If the schedule contains an error, only
    destination-location and snapmirror-error will be present.
    """
    
    _is_compressed = None
    @property
    def is_compressed(self):
        """
        If true SnapMirror will compress/decompress the data
        that is transferred between the source and destination
        storage system. If false, transferred data will not be
        compressed. The default is false.
        """
        return self._is_compressed
    @is_compressed.setter
    def is_compressed(self, val):
        if val != None:
            self.validate('is_compressed', val)
        self._is_compressed = val
    
    _ops_throttle = None
    @property
    def ops_throttle(self):
        """
        The number of outstanding operations allowed
        before blocking on the source.  The format is
        a number followed by the one of the following
        units: "ops", "s", or "ms".
        If the specified value is less than 10s, the mirror
        is configured to run in a fully synchronous mode.
        If the specified value is greater than or equal to
        10s, the mirror is configured to run in semi-synchronous
        mode.
        """
        return self._ops_throttle
    @ops_throttle.setter
    def ops_throttle(self, val):
        if val != None:
            self.validate('ops_throttle', val)
        self._ops_throttle = val
    
    _snapmirror_error = None
    @property
    def snapmirror_error(self):
        """
        Present if there is an error for a snapmirror
        schedule.
        """
        return self._snapmirror_error
    @snapmirror_error.setter
    def snapmirror_error(self, val):
        if val != None:
            self.validate('snapmirror_error', val)
        self._snapmirror_error = val
    
    _sync_mode = None
    @property
    def sync_mode(self):
        """
        This specifies whether the mirror is configured
        in sync or in semi-sync mode. Possible values are:
        "full_sync" and "semi_sync".
        "full_sync" means that the mirror is configured
        to run in a fully synchronous mode. "semi_sync"
        means that the mirror is configured to run in
        a semi synchronous mode.
        """
        return self._sync_mode
    @sync_mode.setter
    def sync_mode(self, val):
        if val != None:
            self.validate('sync_mode', val)
        self._sync_mode = val
    
    _visibility_frequency = None
    @property
    def visibility_frequency(self):
        """
        Controls how often the source snapspot will be visible
        on the destination mirror.
        """
        return self._visibility_frequency
    @visibility_frequency.setter
    def visibility_frequency(self, val):
        if val != None:
            self.validate('visibility_frequency', val)
        self._visibility_frequency = val
    
    _tcp_window_size = None
    @property
    def tcp_window_size(self):
        """
        TCP window size in bytes. If not present, then the TCP
        window size is set to an internally determined default value.
        """
        return self._tcp_window_size
    @tcp_window_size.setter
    def tcp_window_size(self, val):
        if val != None:
            self.validate('tcp_window_size', val)
        self._tcp_window_size = val
    
    _destination_location = None
    @property
    def destination_location(self):
        """
        The destination location of the schedule.  The
        destination location is of the volume form:
        &lt;filer&gt;:&lt;volume&gt; or the qtree form:
        &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        """
        return self._destination_location
    @destination_location.setter
    def destination_location(self, val):
        if val != None:
            self.validate('destination_location', val)
        self._destination_location = val
    
    _source_location = None
    @property
    def source_location(self):
        """
        The source location of the schedule.  The source
        location is of the volume form:
        &lt;filer&gt;:&lt;volume&gt; or the qtree form:
        &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        If there is an error, source-location will not
        be present and snapmirror-error will be present.
        """
        return self._source_location
    @source_location.setter
    def source_location(self, val):
        if val != None:
            self.validate('source_location', val)
        self._source_location = val
    
    _max_transfer_rate = None
    @property
    def max_transfer_rate(self):
        """
        Maximum transfer rate in kilobytes per second.  If not
        present, then the transfer rate is as fast as the filer
        can transfer.
        """
        return self._max_transfer_rate
    @max_transfer_rate.setter
    def max_transfer_rate(self, val):
        if val != None:
            self.validate('max_transfer_rate', val)
        self._max_transfer_rate = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-sync-schedule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-compressed',
            'ops-throttle',
            'snapmirror-error',
            'sync-mode',
            'visibility-frequency',
            'tcp-window-size',
            'destination-location',
            'source-location',
            'max-transfer-rate',
        ]
    
    def describe_properties(self):
        return {
            'is_compressed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ops_throttle': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snapmirror_error': { 'class': SnapmirrorError, 'is_list': False, 'required': 'optional' },
            'sync_mode': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'visibility_frequency': { 'class': int, 'is_list': False, 'required': 'optional' },
            'tcp_window_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_location': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'source_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_transfer_rate': { 'class': int, 'is_list': False, 'required': 'optional' },
        }

from netapp.snapmirror.snapmirror_error import SnapmirrorError
from netapp.netapp_object import NetAppObject

class SnapmirrorScheduleInfo(NetAppObject):
    """
    Contains the SnapMirror schedule per destination.  If the
    schedule contains an error, only destination-location and
    snapmirror-error will be present.
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
    
    _max_transfer_rate = None
    @property
    def max_transfer_rate(self):
        """
        Maximum transfer rate in kilobytes per second.  If not
        present, then the transfer rate is as fast as the
        filer can transfer.
        """
        return self._max_transfer_rate
    @max_transfer_rate.setter
    def max_transfer_rate(self, val):
        if val != None:
            self.validate('max_transfer_rate', val)
        self._max_transfer_rate = val
    
    _hours = None
    @property
    def hours(self):
        """
        Hours in the day for which the schedule is set.
        The form is crontab-like, with possible values of:
        <ul>
        <li> -       := match nothing;
        <li> 1       := match hour 1;
        <li> 1,3     := match hour 1 and 3;
        <li> 2-5     := match hour 2,3,4,5;
        <li> 1-24/3  := match hour 1,4,7,10,13,16,19,22;
        <li> *       := matches all possible legal values;
        </ul>
        If there is an error, hours will not be present
        and snapmirror-error will be present.
        """
        return self._hours
    @hours.setter
    def hours(self, val):
        if val != None:
            self.validate('hours', val)
        self._hours = val
    
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
    
    _days_of_month = None
    @property
    def days_of_month(self):
        """
        Days in the month for which the schedule is set.
        The form is crontab-like, with possible values of:
        <ul>
        <li> -       := match nothing;
        <li> 1       := match day 1;
        <li> 1,3     := match day 1 and 3;
        <li> 2-5     := match day 2,3,4,5;
        <li> 1-30/7  := match day 1,8,15,22,29;
        <li> *       := matches all possible legal values;
        </ul>
        If there is an error, days-of-month will not be present
        and snapmirror-error will be present.
        """
        return self._days_of_month
    @days_of_month.setter
    def days_of_month(self, val):
        if val != None:
            self.validate('days_of_month', val)
        self._days_of_month = val
    
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
    
    _minutes = None
    @property
    def minutes(self):
        """
        Minutes in the hour for which the schedule is set.
        The form is crontab-like, with possible values of:
        <ul>
        <li> -       := match nothing;
        <li> 1       := match minute 1;
        <li> 1,3     := match minute 1 and 3;
        <li> 2-5     := match minute 2,3,4,5;
        <li> 1-12/3  := match minute 1,4,7,10;
        <li> 0-55/5  := match minute 0,5,10,15,20,25,30,35,40,
        45,50,55;
        <li> *       := matches all possible legal values;
        </ul>
        If there is an error, minutes will not be present
        and snapmirror-error will be present.
        """
        return self._minutes
    @minutes.setter
    def minutes(self, val):
        if val != None:
            self.validate('minutes', val)
        self._minutes = val
    
    _days_of_week = None
    @property
    def days_of_week(self):
        """
        Days in the week for which the schedule is set.
        0 represents Sunday, and 6 represents Saturday.
        The form is crontab-like, with possible values of:
        <ul>
        <li> -       := match nothing.
        <li> 1       := match day 1 (Mon);
        <li> 1,3     := match day 1 and 3 (Mon and Wed);
        <li> 2-5     := match day 2,3,4,5 (Tue,Wed,Thu,Fri);
        <li> *       := matches all possible legal values;
        </ul>
        If there is an error, days-of-week will not be present
        and snapmirror-error will be present.
        """
        return self._days_of_week
    @days_of_week.setter
    def days_of_week(self, val):
        if val != None:
            self.validate('days_of_week', val)
        self._days_of_week = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-schedule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-compressed',
            'snapmirror-error',
            'max-transfer-rate',
            'hours',
            'tcp-window-size',
            'destination-location',
            'days-of-month',
            'source-location',
            'minutes',
            'days-of-week',
        ]
    
    def describe_properties(self):
        return {
            'is_compressed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'snapmirror_error': { 'class': SnapmirrorError, 'is_list': False, 'required': 'optional' },
            'max_transfer_rate': { 'class': int, 'is_list': False, 'required': 'optional' },
            'hours': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tcp_window_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_location': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'days_of_month': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'minutes': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'days_of_week': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

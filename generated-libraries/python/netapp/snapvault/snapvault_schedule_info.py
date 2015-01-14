from netapp.netapp_object import NetAppObject

class SnapvaultScheduleInfo(NetAppObject):
    """
    Representation of the scheduling information.
    """
    
    _hours_of_day = None
    @property
    def hours_of_day(self):
        """
        Hours of the day for which this schedule has been
        set. This is a comma separated list of the hours
        during the day where hours are specified as
        integers from 0 to 23. Hour ranges are also
        allowed. Step values are allowed in conjunction
        with ranges.
        Here are the possible formats:
        <ul>
        <li> 4      := matches 4 am.
        <li> 0,13   := matches midnight and 1pm.
        <li> 0-23   := matches all hours
        <li> 0-8/2  := matches 'every 2 hours' starting
        from midnight until 8am.
        </ul>
        Default value is 0, i.e. midnight.
        """
        return self._hours_of_day
    @hours_of_day.setter
    def hours_of_day(self, val):
        if val != None:
            self.validate('hours_of_day', val)
        self._hours_of_day = val
    
    _days_of_week = None
    @property
    def days_of_week(self):
        """
        Days of the week for which this schedule has been
        set. This is a comma separated list of days, where
        a day is specified by the first three letters of
        the day. Day ranges are also allowed.
        Here are the possible formats:
        <ul>
        <li> -       := matches no day of the week
        <li> mon     := matches Monday
        <li> tue,thu := matches Tuesday and Thursday
        <li> mon-fri := matches mon,tue,wed,thu,fri
        </ul>
        Default value is mon-sun, i.e. every day.
        """
        return self._days_of_week
    @days_of_week.setter
    def days_of_week(self, val):
        if val != None:
            self.validate('days_of_week', val)
        self._days_of_week = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-schedule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'hours-of-day',
            'days-of-week',
        ]
    
    def describe_properties(self):
        return {
            'hours_of_day': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'days_of_week': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }

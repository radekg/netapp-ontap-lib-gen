from netapp.connection import NaConnection
from o_timezone import OTimezone # 0 properties

class ClockConnection(NaConnection):
    
    def clock_set_timezone(self, timezone):
        """
        Set current timezone to the specified timezone.
        
        :param timezone: Name of the timezone value which has to be set as current
                timezone value.  A timezone can have one of the two formats:
                <ol>
                <li>"Using a location string specified in Arthur David
                Olsen's public domain time zone database.  For example,
                "Americas/New_York" represents most of the Eastern
                Time Zone.";
                <li>"A traditional time zone abbreviation incorporating
                default	rules for daylight savings time.  For example,
                "EST5EDT" for the US Eastern Time Zone.";
                </ol>
        """
        return self.request( "clock-set-timezone", {
            'timezone': [ timezone, 'timezone', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def clock_get_timezone(self):
        """
        Gets current timezone and timezone file version.
        """
        return self.request( "clock-get-timezone", {
        }, {
            'timezone': [ basestring, False ],
            'timezone-version': [ basestring, False ],
            'timezone-UTC': [ basestring, False ],
        } )
    
    def clock_get_clock(self, is_compliance_clock=None):
        """
        gets current date and time from filer.
        
        :param is_compliance_clock: If true, then local-time and utc-time are values for the
                compliance clock, otherwise they are values for the local clock.
                Default is false.
                Note: This field is deprecated in Data ONTAP 8.1 and later.
                If true, the operation will fail with error EOPNOTSUPPORTED.
                Clients should use the API snaplock-get-system-compliance-clock or
                snaplock-get-volume-compliance-clock as applicable to get the
                compliance clock time.
        """
        return self.request( "clock-get-clock", {
            'is_compliance_clock': [ is_compliance_clock, 'is-compliance-clock', [ bool, 'None' ], False ],
        }, {
            'utc-time': [ int, False ],
            'local-time': [ int, False ],
        } )
    
    def clock_set_clock(self, is_utc_clock, time):
        """
        Set current date and time  to the specified date and time.
        
        :param is_utc_clock: If this is true, then clock is given in UTC (universal time)
                instead of local time.
        
        :param time: Actual value of the date and time which has to be set as the
                current date and time on filer.  Value will be seconds since
                Midnight, 1/1/1970.  Depending on the time zone and
                clock settings, this might be negative by up to 12 hours.
        """
        return self.request( "clock-set-clock", {
            'is_utc_clock': [ is_utc_clock, 'is-utc-clock', [ bool, 'None' ], False ],
            'time': [ time, 'time', [ int, 'None' ], False ],
        }, {
        } )

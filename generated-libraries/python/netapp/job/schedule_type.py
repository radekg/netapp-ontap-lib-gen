class ScheduleType(basestring):
    """
    Jobs may be scheduled according to one of three major styles:
    'cron' is for jobs that should be run at a specific time or
    well-defined calendar date; 'interval' is for jobs that should be
    run on a regular period; 'builtin' is for jobs that should be run
    according to internal rules.  Of these 'cron' and 'interval' may
    be customized.
    Possible values:
    <ul>
    <li> "cron"     ,
    <li> "interval" ,
    <li> "builtin"  ,
    <li> "unknown"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "schedule-type"
    

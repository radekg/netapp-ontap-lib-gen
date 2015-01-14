class JobLogLevel(basestring):
    """
    All jobs optionally produce logging and/or tracing output as they
    execute.  This output is organized by module in the system and
    its verbosity is controlled by a logging level.  Levels are
    organized in order of increased verbosity with emergency levels
    being the most important but least verbose and debug levels being
    the least important and most verbose.
    Possible values:
    <ul>
    <li> "emerg"    ,
    <li> "alert"    ,
    <li> "crit"     ,
    <li> "err"      ,
    <li> "warning"  ,
    <li> "notice"   ,
    <li> "info"     ,
    <li> "debug"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "job-log-level"
    

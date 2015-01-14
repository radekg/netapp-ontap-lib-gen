class Vsadminstate(basestring):
    """
    running|stopped|starting|stopping
    Possible values:
    <ul>
    <li> "running"       ,
    <li> "stopped"       ,
    <li> "starting"      ,
    <li> "stopping"      ,
    <li> "initializing"  ,
    <li> "deleting"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vsadminstate"
    

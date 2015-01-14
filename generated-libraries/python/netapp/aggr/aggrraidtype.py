class Aggrraidtype(basestring):
    """
    raid_dp|raid4
    Possible values:
    <ul>
    <li> "raid_dp"            ,
    <li> "raid4"              ,
    <li> "raid0"              ,
    <li> "mixed_raid_type"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "aggrraidtype"
    

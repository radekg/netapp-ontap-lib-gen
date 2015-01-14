class NvramBatteryStatusEnum(basestring):
    """
    ok|partially discharged|fully discharged|not present|near
    eol|eol|unknown|over charged|fully charged
    Possible values:
    <ul>
    <li> "battery_ok"                   ,
    <li> "battery_partially_discharged" ,
    <li> "battery_fully_discharged"     ,
    <li> "battery_not_present"          ,
    <li> "battery_near_end_of_life"     ,
    <li> "battery_at_end_of_life"       ,
    <li> "battery_unknown"              ,
    <li> "battery_over_charged"         ,
    <li> "battery_fully_charged"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "nvram-battery-status-enum"
    

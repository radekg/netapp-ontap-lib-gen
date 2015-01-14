class SisQosPolicy(basestring):
    """
    Efficiency QoS policy
    Possible values:
    <ul>
    <li> "background"    ,
    <li> "best_effort"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-qos-policy"
    

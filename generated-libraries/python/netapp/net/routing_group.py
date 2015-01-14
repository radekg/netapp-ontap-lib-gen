class RoutingGroup(basestring):
    """
    Specifies the name of routing group.
    For example:
    <ul>
    <li> d192.168.1.0/24 ('d' stands for data LIF and 192.168.1.0/24
    is subnet),
    <li> c192.168.1.0/24 ('c' stands for cluster LIF and
    192.168.1.0/24 is subnet),
    <li> n192.168.1.0/24 ('n' stands for node management LIF and
    192.168.1.0/24 is subnet)
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "routing-group"
    

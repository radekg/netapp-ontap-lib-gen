class HmScope(basestring):
    """
    Node or Cluster context of Health Monitor
    Possible values:
    <ul>
    <li> "node_context"       ,
    <li> "cluster_context"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "hm-scope"
    

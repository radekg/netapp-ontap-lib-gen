class Nfschownmode(basestring):
    """
    restricted|unrestricted|use-export-policy
    Possible values:
    <ul>
    <li> "restricted"         ,
    <li> "unrestricted"       ,
    <li> "use_export_policy"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "nfschownmode"
    

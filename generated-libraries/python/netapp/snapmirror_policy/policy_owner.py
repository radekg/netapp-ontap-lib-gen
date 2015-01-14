class PolicyOwner(basestring):
    """
    cluster-admin|vserver-admin
    Possible values:
    <ul>
    <li> "cluster_admin" ,
    <li> "vserver_admin"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "policy-owner"
    

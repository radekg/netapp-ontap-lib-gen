class AdvancedAccessRights(basestring):
    """
    Advanced access right
    Possible values:
    <ul>
    <li> "read_data"     ,
    <li> "write_data"    ,
    <li> "append_data"   ,
    <li> "read_ea"       ,
    <li> "write_ea"      ,
    <li> "execute_file"  ,
    <li> "delete_child"  ,
    <li> "read_attr"     ,
    <li> "write_attr"    ,
    <li> "delete"        ,
    <li> "read_perm"     ,
    <li> "write_perm"    ,
    <li> "write_owner"   ,
    <li> "full_control"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "advanced-access-rights"
    

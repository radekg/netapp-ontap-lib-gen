class FpolicyOperation(basestring):
    """
    File Operation
    Possible values:
    <ul>
    <li> "close"         - File close operation,
    <li> "create"        - File create operation,
    <li> "create_dir"    - File create directory operation,
    <li> "delete"        - File delete operation,
    <li> "delete_dir"    - Directory delete operation,
    <li> "getattr"       - Get attribute operation,
    <li> "link"          - Link operation,
    <li> "lookup"        - Lookup operation,
    <li> "open"          - File open operation,
    <li> "read"          - File read operation,
    <li> "write"         - File write operation,
    <li> "rename"        - File rename operation,
    <li> "rename_dir"    - Directory rename operation,
    <li> "setattr"       - Set attribute operation,
    <li> "symlink"       - Symbolic link operation
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fpolicy-operation"
    

class Arrayerrortype(basestring):
    """
    ARRAY_INCONSISTENT_ADDRESSING_METHOD|ARRAY_DEVTYPE_ERROR
    Possible values:
    <ul>
    <li> "array_inconsistent_addressing_method"   - Array is using
    inconsistent LUN addressing schemes.,
    <li> "array_devtype_error"                    - Array has
    encountered a device class error.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "arrayerrortype"
    

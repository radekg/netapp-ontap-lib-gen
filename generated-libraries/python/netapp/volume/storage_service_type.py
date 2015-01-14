class StorageServiceType(basestring):
    """
    legacy|normal
    Possible values:
    <ul>
    <li> "legacy"   - No Support for Storage Services,
    <li> "normal"   - Support For Storage Services
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "storage-service-type"
    

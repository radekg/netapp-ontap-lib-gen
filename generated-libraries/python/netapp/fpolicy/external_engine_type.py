class ExternalEngineType(basestring):
    """
    External Engine Type
    Possible values:
    <ul>
    <li> "synchronous"   - Synchronous External Engine,
    <li> "asynchronous"  - Asynchronous External Engine
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "external-engine-type"
    

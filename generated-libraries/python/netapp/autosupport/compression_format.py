class CompressionFormat(basestring):
    """
    7z|tgz
    Possible values:
    <ul>
    <li> "7z"  - 7-Zip Archive,
    <li> "tgz" - Zipped Tarball
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "compression-format"
    

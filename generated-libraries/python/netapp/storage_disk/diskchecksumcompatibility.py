class Diskchecksumcompatibility(basestring):
    """
    advanced_zoned | block | none | zoned/advanced_zoned
    Possible values:
    <ul>
    <li> "advanced_zoned"          - Supports advanced zoned
    checksum,
    <li> "block"                   - Supports block checksum,
    <li> "none"                    - No checksum support,
    <li> "zoned_advanced_zoned"    - Supports zoned and advanced
    zoned checksums
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "diskchecksumcompatibility"
    

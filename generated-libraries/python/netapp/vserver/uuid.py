class Uuid(basestring):
    """
    The 128-bit universally-unique identifier (UUID).
    <p>
    UUIDs are formatted as 36-character strings. These strings are
    composed of 32 hexadecimal characters broken up into five
    groupings separated by '-'s.The first grouping has 8 hex
    characters, the second through fourth groupings have four hex
    characters each, and the fifth and final grouping has 12 hex
    characters. Note that a leading '0x' is not used.
    """
    
    @staticmethod
    def get_api_name():
          return "uuid"
    

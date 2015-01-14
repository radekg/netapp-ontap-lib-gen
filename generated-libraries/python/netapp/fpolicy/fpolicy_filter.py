class FpolicyFilter(basestring):
    """
    Filter
    Possible values:
    <ul>
    <li> "monitor_ads"                  - Monitor alternate data
    stream,
    <li> "close_with_modification"      - Filter close with
    modification,
    <li> "close_without_modification"   - Filter close without
    modification,
    <li> "first_read"                   - Filter first read,
    <li> "first_write"                  - Filter first write,
    <li> "offline_bit"                  - Filter offline bit set,
    <li> "open_with_delete_intent"      - Filter open with delete
    intent,
    <li> "open_with_write_intent"       - Filter open with write
    intent,
    <li> "write_with_size_change"       - Filter write with size
    change
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fpolicy-filter"
    

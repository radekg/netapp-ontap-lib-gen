class StripingType(basestring):
    """
    Striping information of aggregate.
    Allowed values are:
    <ul>
    <li>"striped": Member of stripe.
    <li>"not_striped": Not member of stripe.
    <li>"unknown": Not known.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "striping-type"
    

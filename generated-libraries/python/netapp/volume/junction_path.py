class JunctionPath(basestring):
    """
    The Junction Path.
    <p>
    The fully-qualified pathname in the owning Vserver's namespace at
    which a volume is mounted.  Note that this pathname may itself
    contain junctions, one for each volume (other than the namespace
    root volume) that provides storage along the pathname's length.
    As with all fully-qualified pathnames , this string must begin
    with '/'.  In addition, it must not end with '/'. An Infinite
    Volume has the additional restriction of allowing only one
    element.
    <p>
    An example of a valid FlexVol junction path is:
    '/user/my_volume'.
    An example of a valid Infinite Volume junction path is:
    '/repository'.
    <p>
    Only one volume can be mounted at any given junction path.
    """
    
    @staticmethod
    def get_api_name():
          return "junction-path"
    

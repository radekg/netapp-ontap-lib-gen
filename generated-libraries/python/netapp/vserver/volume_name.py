class VolumeName(basestring):
    """
    The name of the volume.
    <p>
    Volume names can contain letters, numbers, and the underscore
    character (_).  The first character must be a letter or an
    underscore. When creating a Cluster-Mode volume, the user can
    specify at most 203 characters. If the prefix '/vol/' appears in
    the volume name, it is striped out and the characters that follow
    the prefix constitute the actual volume name.
    <p>
    Volume names are scoped by their owning Vserver in a cluster,
    with each Vserver's volume namespace being totally independent.
    Thus, any Vserver 'S' in a cluster cannot have two volumes with
    the same name 'V'.  However, two different Vservers in the same
    cluster can each have a volume named 'V'.
    <p>
    For example, any given Vserver in a cluster can only have at most
    one volume named 'vol0'. However, two different Vservers S1 and
    S2 in the cluster may each have a volume named 'vol0'.
    """
    
    @staticmethod
    def get_api_name():
          return "volume-name"
    

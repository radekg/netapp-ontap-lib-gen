class PortsetPortName(basestring):
    """
    String representing a member of a portset.
    In Data ONTAP 7-Mode, the port name is of the
    format "filer:slotletter" or "slotletter".
    In Data ONTAP Cluster-Mode, the port name is the name of
    an FCP data lif or iSCSI target portal group.
    """
    
    @staticmethod
    def get_api_name():
          return "portset-port-name"
    

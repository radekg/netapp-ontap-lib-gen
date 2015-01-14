class FilterData(basestring):
    """
    A string, representing filter data, in the format of key=value
    pairs. Multiple pairs can be specified via comma (",") or pipe ("|")
    separation. The applied filter is a combination of ANDing and ORing the
    key-value pairs.<p>
    A comma indicates ANDing, a pipe indicates ORing, and the order
    of precedence is AND and then OR. For example,
    "<tt>instance_name=volA,vserver_name=vs1|vserver_name=vs2</tt>"
    equates to "<tt>(instance_name=volA &amp;&amp; vserver_name=vs1) |
    (vserver_name=vs2)</tt>". This would return instances on
    Vserver <tt>vs1</tt> with name <tt>volA</tt> and all instances
    on Vserver <tt>vs2</tt>.
    """
    
    @staticmethod
    def get_api_name():
          return "filter-data"
    

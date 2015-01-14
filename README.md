# NetApp ONTAP Python library generator

This is a more human friendly NetApp ONTAP Filer API library. The main difference is: *no need to play with XML nodes, yay!*

# Generator

To run the generator:

    chmod +x bin/generator
    ./bin/generator <options>

Options documented in the generator file.

# Generated libraries

This repo comes with the code generated for Python. Generators can be added by specifying `<language>.py` file and placing it in the `bin/lib` folder.

For every language a counterpart of `generated-libraries/python/netapp_object.py` and `generated-libraries/python/connection.py` have to be created.

# Generating the code

To generate the code for selected language ZEDI Explorer is required.

# Usage

Clone, deploy to your code, have a look at the example:

    from netapp.connection import NaErrorResponse, NaPagedResponse
    from netapp.net import NetConnection
    from netapp.net.net_port_info import NetPortInfo
    
    conn = NetConnection("192.168.135.100", "admin", "admin")
    print "LISTING ALL PORTS:"
    print "-----------------------------------------------"
    query = None
    # To apply a query filter:
    # query = NetPortInfo(node="radontap-02")
    response = conn.net_port_get_iter( max_records=3, desired_attributes="node,port".split(","), query=query )
    
    if isinstance(response, NaPagedResponse):
        for npi in response.output:
            print "{}: {}".format( npi.port, npi )
        while response.has_more():
            next = response.next()
            if isinstance(next.result, NaErrorResponse):
                print "There was an error: {} : {}".format( next.result.error_code, next.result.reason )
            else:
                for npi in next.output:
                    print "{}: {}".format( npi.port, npi )
    elif isinstance(response, NaErrorResponse):
        print "There was an error: {} : {}".format( response.error_code, response.reason )
    else:
        # if max_records is not given or is set to None
        for npi in response:
            print "{}: {}".format( npi.port, npi )
    
    print "GET A SINGLE PORT:"
    print "-----------------------------------------------"
    port_info = conn.net_port_get( node="radontap-02", port="e0c", desired_attributes="node,port".split(",") )
    print port_info

More Python examples in generated-libraries/python.

# Code not maintained

This code is not under active development but maybe someone will have some use for it.

# Author

Rad Gruchalski <radek@gruchalski.com>

# License

MIT, except of the files in `netapp/core_netapp`.
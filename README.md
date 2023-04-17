# P4_experiment_Fabric
Example P4 experiment on Fabric Testbed

# P4Lang Tutorials of FABRIC, Basic FABRIC Slice Configuration

1. 
```import json
import traceback
from fabrictestbed_extensions.fablib.fablib import fablib 
```

2.  

``` from ipaddress import ip_address, IPv4Address, IPv6Address, IPv4Network, IPv6Network

# Slice 
slice_name = 'Nagm_P4Test'

#[site1,site2,site3] = fablib.get_random_sites(count=3)
site1 = 'NCSA'
site2 = 'WASH'
site3 = 'TACC'
print(f"Sites: {site1},{site2},{site3}")


# Switches
s1_name = "s1"
s2_name = "s2"
s3_name = "s3"

switch_cores = 4
switch_ram = 16
switch_disk = 200

# Hosts
h1_name = "h1"
h2_name = "h2"
h3_name = "h3"

h1_subnet=IPv4Network('10.0.1.0/24')
h1_addr=IPv4Address('10.0.1.1')

h2_subnet=IPv4Network('10.0.2.0/24')
h2_addr=IPv4Address('10.0.2.2')

h3_subnet=IPv4Network('10.0.3.0/24')
h3_addr=IPv4Address('10.0.3.3')

host_cores = 8
host_ram = 16
host_disk = 500

net_h1_name = 'net_h1'
net_h2_name = 'net_h2'
net_h3_name = 'net_h3'

net_s1_s2_name = 'net_s1_s2'
net_s2_s3_name = 'net_s2_s3'
net_s1_s3_name = 'net_s1_s3'

# All node properties
image = 'default_ubuntu_20'
```

3. 
```
try:
    #Create Slice
    slice = fablib.new_slice(name=slice_name)
    
    # Add switch node s1
    s1 = slice.add_node(name=s1_name, site=site1,  image=image, 
                        cores=switch_cores, ram=switch_ram, disk=switch_disk)
    s1.set_capacities(cores=switch_cores, ram=switch_ram, disk=switch_disk)
    s1_iface_local = s1.add_component(model='NIC_Basic', name="s1_local_nic").get_interfaces()[0]
    s1_iface_to_s2 = s1.add_component(model='NIC_Basic', name="s1_switch_nic1").get_interfaces()[0]
    s1_iface_to_s3 = s1.add_component(model='NIC_Basic', name="s1_switch_nic2").get_interfaces()[0]

    # Add switch node s2
    s2 = slice.add_node(name=s2_name, site=site2,  image=image, 
                        cores=switch_cores, ram=switch_ram, disk=switch_disk)
    s2_iface_local = s2.add_component(model='NIC_Basic', name="s2_local_nic").get_interfaces()[0]
    s2_iface_to_s1 = s2.add_component(model='NIC_Basic', name="s2_switch_nic1").get_interfaces()[0]
    s2_iface_to_s3 = s2.add_component(model='NIC_Basic', name="s2_switch_nic2").get_interfaces()[0]
    
    # Add switch node s3
    s3 = slice.add_node(name=s3_name, site=site3,  image=image, 
                        cores=switch_cores, ram=switch_ram, disk=switch_disk)
    s3_iface_local = s3.add_component(model='NIC_Basic', name="s3_local_nic").get_interfaces()[0]
    s3_iface_to_s1 = s3.add_component(model='NIC_Basic', name="s3_switch_nic1").get_interfaces()[0]
    s3_iface_to_s2 = s3.add_component(model='NIC_Basic', name="s3_switch_nic2").get_interfaces()[0]    
    
    # Add host node h1
    h1 = slice.add_node(name=h1_name, site=site1, image=image,
                        cores=host_cores, ram=host_ram, disk=host_disk)
    h1_iface = h1.add_component(model='NIC_Basic', name="h1_nic").get_interfaces()[0]
    
    # Add host node h2
    h2 = slice.add_node(name=h2_name, site=site2, image=image,
                        cores=host_cores, ram=host_ram, disk=host_disk)
    h2_iface = h2.add_component(model='NIC_Basic', name="h2_nic").get_interfaces()[0]
    
    # Add host node h3
    h3 = slice.add_node(name=h3_name, site=site3, image=image,
                        cores=host_cores, ram=host_ram, disk=host_disk)
    h3_iface = h3.add_component(model='NIC_Basic', name="h3_nic").get_interfaces()[0]
    
    #Add swtich networks
    switch_net1 = slice.add_l2network(name=net_s1_s2_name, interfaces=[s1_iface_to_s2, s2_iface_to_s1])
    swtich_net2 = slice.add_l2network(name=net_s2_s3_name, interfaces=[s2_iface_to_s3, s3_iface_to_s2])
    swtich_net3 = slice.add_l2network(name=net_s1_s3_name, interfaces=[s3_iface_to_s1, s1_iface_to_s3])

    #Add host networks 
    host_net1 = slice.add_l2network(name=net_h1_name, interfaces=[s1_iface_local, h1_iface])
    host_net2 = slice.add_l2network(name=net_h2_name, interfaces=[s2_iface_local, h2_iface])
    host_net3 = slice.add_l2network(name=net_h3_name, interfaces=[s3_iface_local, h3_iface])
    
    #Submit Slice Request
    slice.submit() 
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
```

4. 

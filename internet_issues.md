
# Internet issues 

If you are encountering internet issues like : 

```ping google.com```


Change the structure of ``` vim /etc/resolv.conf ``` as shown below : 


For IPV6 IPs /etc/resolv.conf should look like : 

```
options edns0 trust-ad
search openstacklocal
nameserver 2a00:1098:2c::1
nameserver 2a01:4f8:c2c:123f::1
nameserver 2a00:1098:2b::1
```

For IPV4 IPs /etc/resolv.conf should look like : 

```
options edns0 trust-ad
search openstacklocal
nameserver 8.8.8.8 
nameserver 8.8.4.4 
nameserver 1.1.1.1
```


# check the running p4 program 

```
ps -aux | grep simple_switch
```

The results : 

```
root       12960  0.0  0.0   2608   592 ?        Ss+  17:08   0:00 sh -c simple_switch --interface 1@ --interface 2@ --interface 3@ /root/tutorials/exercises/basic_tunnel/basic_tunnel.json
root       12966  0.0  0.0 249864 13016 ?        Sl+  17:08   0:00 simple_switch --interface 1@ --interface 2@ --interface 3@ /root/tutorials/exercises/basic_tunnel/basic_tunnel.json
ubuntu     13821  0.0  0.0   8164   720 pts/0    S+   17:24   0:00 grep --color=auto simple_switch
```

# Login in into the docker : 

```
sudo docker exec -it fabric_p4 bash
```

Create your p4 file. 

Then compile it : 

```
p4c --p4runtime-files basic.txt --target bmv2 --arch v1model arp_pl.p4
```

Then run it : 

```
simple_switch --log-console --interface 1@ens7 --interface 2@ens8 --interface 3@ens9 arp_pl.json
```

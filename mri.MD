# MRI experiment commands. 

To search for dockers : 
```
sudo docker ps 
```
The results : 
```
CONTAINER ID   IMAGE                                                 COMMAND   CREATED          STATUS          PORTS     NAMES
954e3b3fcf64   registry.ipv6.docker.com/pruth/fabric-images:0.0.2j   "bash"    25 minutes ago   Up 25 minutes             fabric_p4
```

To start bash inside docker : 
```
sudo docker exec -it 954e3b3fcf64 bash
```

To switch to control plane of bmv2 switch : 

```
./tools/behavioral-model/tools/runtime_CLI.py
```
The result : 
```
Obtaining JSON from switch...
Done
Control utility for runtime P4 table manipulation
RuntimeCmd: 
```

Send packets from host1 to host2 : 

```
sudo python3 tutorials/exercises/mri/send_modified.py 10.0.2.2 "message100" 2
```

# Solution : 

I killed the existing simple_switch process: 

```
root@fc770b13bdc1:~/tutorials/exercises/pl_basic# ps aux | grep simple_switch 
root        1200  0.0  0.0   3304   664 pts/5    S+   18:40   0:00 grep --color=auto simple_switch
```

Then compiled the program again : 

```
root@fc770b13bdc1:~/tutorials/exercises/pl_basic# p4c --p4runtime-files basic.txt --target bmv2 --arch v1model arp_pl.p4
```

Then reloaded the simple_switch again : 

```
root@fc770b13bdc1:~/tutorials/exercises/pl_basic# sudo simple_switch --log-console --interface 1@ens7 --interface 2@ens8 --interface 3@ens9 /root/tutorials/exercises/pl_basic/arp_pl.json 
```


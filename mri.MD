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

Send packets from host1 to host2 : 

```
sudo python3 tutorials/exercises/mri/send_modified.py 10.10.2.2 "message100" 2
```

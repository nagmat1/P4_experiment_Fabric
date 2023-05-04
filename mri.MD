# MRI experiment commands. 

To search for dockers : 
```
sudo docker ps 
```

To start bash inside docker : 
```
sudo docker exec -it 8c39cc0eb450 bash
```

To switch to control plane of bmv2 switch : 

```
./tools/behavioral-model/tools/runtime_CLI.py
```

Send packets from host1 to host2 : 

```
sudo python3 tutorials/exercises/mri/send_modified.py 10.10.2.2 "message100" 2
```

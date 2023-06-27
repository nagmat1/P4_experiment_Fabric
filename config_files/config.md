After setting up the tables : 

on host1 : 

```
sudo ip route add 10.0.3.3 via 10.0.1.1 dev ens7
```

on host3 : 

```
sudo ip route add 10.0.1.1 via 10.0.3.3 dev ens7
```

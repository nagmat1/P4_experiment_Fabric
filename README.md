To connect to fabric_testbed slice : 

```
 ssh -F ssh_config -i Nagmat2_Silver ubuntu@2001:1948:417:7:f816:3eff:fe4f:13bc
```

Configure the ssh stuff according to this video : https://www.youtube.com/watch?v=ieTr9Mj6uuc

How to configure p4 switches : https://github.com/fabric-testbed/jupyter-examples/blob/master/fabric_examples/complex_recipes/P4_bmv2/p4lang_tutorials.ipynb

Bring the interfaces up : 
```
sudo ip link set dev ens7 up
```

How to install tshark on ubuntu : 
```
sudo apt install -y tshark
```

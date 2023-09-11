
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

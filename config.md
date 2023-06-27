# S1 : 

```
table_add ingress.routing_table ipv4_forward 10.0.3.0/24 => 10.0.1.2 3
table_add ingress.routing_table ipv4_forward 10.0.1.0/24 => 10.0.1.3 1
table_add egress.switching_table set_dmac 10.0.1.2 => 0e:60:fb:cb:da:46
table_add egress.switching_table set_dmac 10.0.1.3 => 16:71:10:b0:88:76
table_add egress.mac_rewriting_table set_smac 3 => 12:b9:0f:87:ff:f5
table_add egress.mac_rewriting_table set_smac 1 => 12:79:54:77:fd:5a


```


# S3 

```
table_add ingress.routing_table ipv4_forward 10.0.3.0/24 => 10.0.3.3 1
table_add ingress.routing_table ipv4_forward 10.0.1.0/24 => 10.0.3.2 3
table_add egress.switching_table set_dmac 10.0.3.2 => 12:b9:0f:87:ff:f5
table_add egress.switching_table set_dmac 10.0.3.3 => 0e:b5:27:2c:30:b5
table_add egress.mac_rewriting_table set_smac 3 => 0e:60:fb:cb:da:46
table_add egress.mac_rewriting_table set_smac 1 => 0a:24:fa:0c:83:46

```

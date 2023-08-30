Experiment 2 : We connected 2 host with Basic NICs over network service(direct connection) as shown below : 

<img width="1390" alt="Screenshot 2023-08-30 at 2 42 21 PM" src="https://github.com/nagmat1/P4_experiment_Fabric/assets/51871069/4664654d-37ea-413a-b2c3-93c5ba005a19">

After tuning the parameters, Maximum I am getting is **20Gbit/s**. I thought that network service was the problem but I guess Basic NICs is the problem. 

<img width="1343" alt="Screenshot 2023-08-30 at 2 46 26 PM" src="https://github.com/nagmat1/P4_experiment_Fabric/assets/51871069/a531b94a-6214-4105-a0fd-e18fdb6ea492">

Will try to experiment with Dedicated NICs. 

# What may be the Bottleneck? 

Tuning network performance to 100Gbps and beyond depends on a large number of parameters. The notebooks Paul pointed out show some of them. Things like

– number of available cores and RAM

– affinity between vCPUs, physical CPUs and network cards (Affinity between vCPUs weren't the issue)

– the type of network card (to get close to 100Gbps you need dedicated not shared NICs)

– MTU size

– Number of threads used by the data transfer app

– etc etc etc

Network service type will not affect the performance. The type of network card used will.

Try looking at the iPerf3 examples in the JupyterHub.

The basic version should get at least 30 Gbps.  (https://github.com/fabric-testbed/jupyter-examples/blob/main/fabric_examples/complex_recipes/iPerf3/iperf3.ipynb)

If you want to get closer to 100Gbps you will need to look at the NUMA tuning examples (https://github.com/fabric-testbed/jupyter-examples/blob/main/fabric_examples/complex_recipes/iPerf3/iperf3_optimized.ipynb)

Note that a few sites are still connected with slower bandwidth links but they are all capped at least 10 Gbps. 10 Gbps should be attainable with minimal tuning required.

I set up a connection between INDI and WASH. 

After “sudo usermod -G docker rocky” and tuning the parameters for both hosts, I am getting30Gbits/s. The setup is shown below : 

<img width="1411" alt="Screenshot 2023-08-30 at 1 47 36 PM" src="https://github.com/nagmat1/P4_experiment_Fabric/assets/51871069/c55acab2-c7ab-4aa3-979b-790323a37572">


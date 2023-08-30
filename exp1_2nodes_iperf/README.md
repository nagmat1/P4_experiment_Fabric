Try looking the iPerf3 examples in the JupyterHub.

The basic version should get at least 30 Gbps.  (https://github.com/fabric-testbed/jupyter-examples/blob/main/fabric_examples/complex_recipes/iPerf3/iperf3.ipynb)

If you want to get closer to 100Gbps you will need to look at the NUMA tuning examples (https://github.com/fabric-testbed/jupyter-examples/blob/main/fabric_examples/complex_recipes/iPerf3/iperf3_optimized.ipynb)

Note that a few sites are still connected with slower bandwidth links but they are all capped at least 10 Gbps. 10 Gbps should be attainable with minimal tuning required.


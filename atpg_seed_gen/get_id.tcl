read_netlist gscl45nm.v -library
read_netlist <design.v>
set_build -nodelete_unused_gates -merge noglobal_tie_propagate
run_build_model <top_module_name>
add_clocks 0 <clk_name>
drc 
test 
report_primitives <targetnet_name> >> tmax_data_nets.log
exit
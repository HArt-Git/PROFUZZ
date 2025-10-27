read_netlist gscl45nm.v -library
read_netlist <design.v>
set_build -nodelete_unused_gates -merge noglobal_tie_propagate
run_build_model <top_module_name>
add_clocks 0 <clk_name>
set_scan_ability on -all
drc 
test 
set pindata seq_sim_data
# Net with IDx for Value 1
run_justification -full_sequential -set { IDx 1 } -verbose -store
# Net with IDy for Value 0
run_justification -full_sequential -set { IDy 1 } -verbose -store
report_patterns -internal -all
exit
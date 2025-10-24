import subprocess

import time
from base_coverage import base_cov

def cadence():
  
  
  
 subprocess.run("xrun syn_flat_i2c.v tb_dut.vhd -top tb_dut -v gscl45nm.v -nospecify -timescale 1ns/10ps -coverage T -covfile common.ccf -v93 -covdut i2c_master_top -covoverwrite",shell= True)
 subprocess.run("imc -exec imc.tcl",shell=True)
 init_cov=base_cov()
 return init_cov
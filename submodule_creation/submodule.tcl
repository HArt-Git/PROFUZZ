set inst {}
foreach i [get_object_name [get_db insts]] {   


     puts $i
     lappend inst $i

}    
  
set fileId [open "submodules.txt" w]

# Write the list to the file
puts $fileId $inst

# Close the file after writing
close $fileId

exec python3 sub.py

source sub.tcl
source main_target.tcl
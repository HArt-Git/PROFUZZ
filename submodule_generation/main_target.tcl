set target {}

foreach i [get_db [get_db hports -if {.direction == in} ] .net.name ] {

  lappend target $i
  
}

set len [llength $target]
puts "Length of the list: $len"
set fileId [open "main_target2.txt" w]

# Write the list to the file
puts $fileId $target

# Close the file after writing
close $fileId

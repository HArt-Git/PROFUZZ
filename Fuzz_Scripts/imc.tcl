load test
config analysis.enable_partial_toggle -set true
load -refinement targetsites.vRefine


csv_export -out coverage.csv -overwrite
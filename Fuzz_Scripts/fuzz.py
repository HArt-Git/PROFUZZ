import subprocess

import time

from atpg_flip import bit_flip_sequence
from atpg_mutate import deploy_mutation
from atpg_placeholder import seed_holder
from atpg_simulation import cadence

bit_flip_sequence("in_sedd.txt", "flipped_atpg_pat.txt")
subprocess.run("rm -r atpg_mutated_seeds.txt", shell=True)
deploy_mutation("flipped_atpg_pat.txt")
seed_holder("atpg_mutated_seeds.txt", "mutate_seeds_placeholder.txt")
initcov=cadence()
print("main inicov",initcov)


from fuzz_mutate import fuzz_mutation




import subprocess

def atpgfuzz(file_a, file_b, init_cov):
    current_file = file_a  # Start with the original file
    
    while True:  # Keep iterating until coverage exceeds 90%
        with open(current_file, 'r') as fa:
            for line in fa:
                with open(file_b, 'w') as fb:  # Open in 'w' mode to overwrite previous content
                    fb.write(line.strip() + '\n')
                    
                subprocess.run("rm -r fuzz_mutated_seeds.txt", shell=True)
                fuzz_mutation(file_b) #output is fuzz_mutated_seeds.txt
                seed_holder("fuzz_mutated_seeds.txt", "mutate_seeds_placeholder.txt")
                
                mu_cov = cadence()#EDA reads mutate_seeds_placeholder
                print("************************************** Mutation cov:", mu_cov)
                print("************************************** Previous:", init_cov)
                with open("coverage_log.txt", "a") as file:
                  file.write(f"************************************** Mutation cov: {mu_cov}\n")
                  file.write(f"************************************** Previous: {init_cov}\n")

                if mu_cov > 90 : 
                    print(f"Coverage reached {mu_cov}%, stopping script.")
                    with open("interesting.txt", 'a') as file:
                      file.write(f"{line.strip()} - Coverage: {mu_cov}%\n")
                    exit()
                elif init_cov > 90:
                   print(f"Coverage reached {init_cov}%, stopping script (atpg mutation itself).")
                   with open("interesting.txt", 'a') as file:
                       file.write(f"{line.strip()} - Coverage: {mu_cov}%\n")
                   exit()
                      
                
                elif mu_cov > init_cov * 1.025:  # If coverage increases by 5%
                    init_cov = mu_cov 
                    with open("interesting.txt", 'a') as file:
                        file.write(f"{line.strip()} - Coverage: {mu_cov}%\n")

                    # Swap the input file for the next iteration
                    current_file = "mutate_seeds_placeholder.txt" #if current_file == "atpg_mutated_seeds.txt" else "atpg_mutated_seeds.txt"
                    break;

                
               

        # Ensure iteration continues with the updated file
        if current_file == "mutate_seeds_placeholder.txt":
            current_file = "mutate_seeds_placeholder.txt"  # Keep iterating with the fuzzed seeds
        else:
            current_file = "atpg_mutated_seeds.txt"  # Otherwise, restart from ATPG seeds


if initcov > 90:
    print("atpg mutation itself yields high coverage !",initcov)
    
else:
    atpgfuzz('atpg_mutated_seeds.txt', 'fuzz_mutate_placeholder.txt', initcov)
  





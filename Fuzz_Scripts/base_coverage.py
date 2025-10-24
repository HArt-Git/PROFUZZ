import pandas as pd

def base_cov():
    """
    Reads the 'coverage.csv' file, extracts coverage information, calculates the percentage, 
    and appends it to 'base_coverage.txt'.
    """
    file_path = 'coverage.csv'  # Hardcoded file path
    insts = x  # no of target signals should be modified 

    # Read the CSV file
    df = pd.read_csv(file_path)

    try:
        # Extract coverage value
        coverage = df.loc[df['Name'] == 'Instances', 'Overall Covered'].values[0]

        # Calculate coverage percentage
        coverage = round((coverage / insts) * 100, 2)
        print(coverage)

        # Append to file
        with open('base_coverage.txt', 'w') as file:
            file.write(str(coverage) + '\n')
        return coverage 
        print(f"Coverage recorded: {coverage}%")

    except IndexError:
        print("Error: 'Instances' not found in the CSV file.")

# Example usage


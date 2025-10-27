def merge_vectors(v1, v2):
    """
    Merge two vectors. 'X' in either vector is replaced by the non-'X' value from the other vector.
    """

    # Merge vectors
    result_vector = []
    for char1, char2 in zip(v1, v2):
        if char1 == 'X':
            result_vector.append(char2)
        else:
            result_vector.append(char1)
    
    merged_vector = ''.join(result_vector)

    return merged_vector

def merge_lists(list1,net_names):
    """
    Merge list of patterns by checking all pairs and merging them if no conflict arises.
    """
    merged_results = []

    res_patt = list1[0] if list1[0].count('X') > list1[1].count('X') else list1[1]

    positive_val = [] #to store nets with value 1
    negative_val = [] #to store nets with value 0

    if list1[0].count('X') > list1[1].count('X'):
        positive_val.append(net_names[0])
    else:
        negative_val.append(net_names[0])

    conflict_nets = []

    for i in range(2,len(list1)-1,2):
        flag1 = 0
        flag2 = 0
        if can_merge(res_patt, list1[i]):
            merged_vector_1 = merge_vectors(res_patt, list1[i]) 
            flag1 = 1

        if can_merge(res_patt, list1[i+1]):
            merged_vector_2 = merge_vectors(res_patt, list1[i+1])
            flag2 = 1

        if flag1 == 1 and flag2 == 1:
            res_patt = merged_vector_1 if merged_vector_1.count('X') > merged_vector_2.count('X') else merged_vector_2
            if merged_vector_1.count('X') > merged_vector_2.count('X'):
                positive_val.append(net_names[int(i/2)])
            else:
                negative_val.append(net_names[int(i/2)])
        elif flag1 == 1 and flag2 == 0:
            res_patt = merged_vector_1
            positive_val.append(net_names[int(i/2)])
        elif flag1 == 0 and flag2 == 1:
            res_patt = merged_vector_2
            negative_val.append(net_names[int(i/2)])
        elif flag1 == 0 and flag2 == 0:
            conflict_nets.append(net_names[int(i/2)])
            print("Conflict..For Net id : ",net_names[int(i/2)])
    
    #return final merged pattern, nets with respective values (0/1) and list of conflict nets
    return res_patt,positive_val,negative_val,conflict_nets

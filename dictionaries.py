

def Merge_Dictionaries(a,b):
   
    merge_dict = dict_1.copy() #copy the first dictionary

    merge_dict.update(dict_2) # update the merge_dict with copying the dict_2
    
    return merge_dict
    
    
dict_1={"a": 1, "b": 2, "c": 3}
dict_2={ "b": 10, "d": 4}

result = Merge_Dictionaries(dict_1,dict_2)
print(result)

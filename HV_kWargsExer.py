# reverse given name in list with first level in capital
def rev_name(name_list,rev_str=False):
    if rev_str: 
        return [name[::-1].capitalize() for name in name_list]
    return [name.capitalize() for name in name_list]
print(rev_name(['sri','kavi'],rev_str=False))
def create_dict(some_data):
    template = dict()
    if isinstance(some_data, dict):
        return some_data
    elif isinstance(some_data, int) or isinstance(some_data, float) or isinstance(some_data, str):
        template[some_data] = some_data
        return template
    else:
        return None


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        elem_append = create_dict(i_element)
        if elem_append is not None:
            new_list.append(elem_append)
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)

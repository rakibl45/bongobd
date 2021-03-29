def print_depth(data, start=0):
    initial_value = 0
    for key, value in data.items():
        print(key, start+1)
        if isinstance(value, dict):
           print_depth(value, start=start+1)


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}

print_depth(a)

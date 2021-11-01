
def nested_object(input_object, find_key):
    internal_value = input_object
    for k in find_key:
        internal_value = internal_value.get(k, None)
        if internal_value is None:
            return None
    return internal_value

print(nested_object({"a":{"b":{"c":"d"}}},["a","b","c"]))  ---- Output d
print(nested_object({"x":{"y":{"z":"a"}}},["x","y","z"]))  ---- Output a

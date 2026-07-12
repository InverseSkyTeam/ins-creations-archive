d = {
    'bilibili':111,
    'alpha':'666',
    'config':'xxx',
    'zebra':'banma',
    'what':'az',
    'az':0b1101110110100101,
}
def sort_data(data,sortmode='UP'):
    new_data = {}
    ld = len(data)
    while len(new_data) != ld:
        md = min(data)
        new_data[md] = data[md]
        del data[md]
    return new_data

d = sort_data(d)
print(d)
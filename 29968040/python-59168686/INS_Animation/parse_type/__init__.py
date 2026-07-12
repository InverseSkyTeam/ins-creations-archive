def parse_time(time):
    if isinstance(time, (int, float)):
        return float(time)
    elif isinstance(time, str):
        if time.endswith('s'):
            return float(time[:-1])
        elif time.endswith('ms'):
            return float(time[:-2]) / 1000

def meminfo() -> dict:
    dic = dict()
    with open('/proc/meminfo') as f:
        for line in f:
            label, value, *_ = line.split()
            dic[label.rstrip(':')] = int(value)
    return dic

def get_used_memory_level(with_swap=False) -> float:
    mi = meminfo()

    if with_swap:
        return (mi['MemTotal']-mi['MemAvailable']+mi['SwapTotal']-mi['SwapFree'])/(mi['MemTotal'] + mi['SwapTotal'])
    else:
        return (mi['MemTotal']-mi['MemAvailable'])/mi['MemTotal']
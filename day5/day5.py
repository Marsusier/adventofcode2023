from functools import reduce

seeds, *mappings = open('data.txt').read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))


def lookup(inputs, mapping):
    outputs = []

    for start, length in inputs:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                dst, src, len = map(int, m.split())
                if src <= start < src+len:
                    len -= max(start-src, len-length)
                    outputs.append((start-src+dst, len))
                    start += len
                    length -= len
                    break
            else:
                outputs.append((start, length))
                break

    return outputs


print(*[min(reduce(lookup, mappings, s))[0] for s in [
    zip(seeds, [1] * len(seeds)),
    zip(seeds[0::2], seeds[1::2])]])

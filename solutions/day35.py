def segregate_rgb(rgb):
    r, g = 0, 0
    b = len(rgb) - 1

    while g <= b:
        if rgb[g] == 'R':
            rgb[g], rgb[r] = rgb[r], rgb[g]
            r += 1
            g += 1
        elif rgb[g] == 'B':
            rgb[g], rgb[b] = rgb[b], rgb[g]
            b -= 1
        else:
            g += 1

    return rgb


rgb1 = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
rgb2 = ['B', 'R', 'B', 'R', 'G', 'G']
print(segregate_rgb(rgb1))
print(segregate_rgb(rgb2))

import colorgram

colorgram_colors = colorgram.extract('image.jpg', 30)
rgb_colors = []

for color in colorgram_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    t = (r,g,b)
    rgb_colors.append(t)

print(rgb_colors)
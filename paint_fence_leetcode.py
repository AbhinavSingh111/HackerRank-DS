# paint n fence with given k color such that not more than two consecutive fences get the same color

from types import new_class


def fence_paint(fences, colors):
    MOD = (10**9)+7
    if fences<2:
        return colors
    last_two_color_same = colors*1
    last_two_color_different = colors*(colors-1)
    total = (last_two_color_same+last_two_color_different)%MOD
    for i in range(2,fences):
        last_two_color_same = last_two_color_different*1
        last_two_color_different = total*(colors-1)
        total=(last_two_color_same+last_two_color_different)%MOD
        
    return total%MOD






fences = 1
colors= 17
print(fence_paint(fences, colors))

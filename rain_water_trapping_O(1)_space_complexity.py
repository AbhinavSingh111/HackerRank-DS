# this approach has O(n) time complexity and O(1) space complexity
buildings = [3,1,2,4,0,1,3,2]
l,r=0,len(buildings)-1
left_largest = 0
right_largest = 0
water_trapped = 0

while(l<=r):
    if buildings[l]<=buildings[r]:
        if buildings[l]>=left_largest:
            left_largest=buildings[l]
            l+=1
        else:
            water_trapped+=left_largest-buildings[l]
            l+=1
    elif buildings[r]<=buildings[l]:
        if buildings[r]>=right_largest:
            right_largest=buildings[r]
            r-=1
        else:
            water_trapped+=right_largest-buildings[r]
            r-=1
print(water_trapped)


# Another way is to explicitly calculate left_largrst and right_largest with each iteration

while(l<=r):
    left_largest=max(left_largest,buildings[l])
    right_largest=max(right_largest,buildings[r])
    
    if left_largest<right_largest:
        water_trapped+=left_largest-buildings[l]
        l+=1
    else:
        water_trapped+=right_largest-buildings[r]
        r-=1
print(water_trapped)

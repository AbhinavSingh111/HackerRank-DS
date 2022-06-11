def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start<end:
        while start<len(elements) and elements[start]<=pivot:
            start+=1
        while elements[end]>pivot:
            end-=1
        if start<end:
            elements[start],elements[end]=elements[end],elements[start]
    elements[pivot_index],elements[end]=elements[end],elements[pivot_index]
    return end

def quick_sort(elements,start,end):
    if start<end:
        j=partition(elements,start,end)
        quick_sort(elements,start,j-1)
        quick_sort(elements,j+1,end)
    print(elements)


if __name__=="__main__":
    elements=[60,40,20,70,90,10,30,80,50]
    print(quick_sort(elements,0,len(elements)-1))




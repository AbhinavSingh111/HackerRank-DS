def bubble_sort(elements):
    for i in range(len(elements)):
        for j in range(len(elements)-i-1):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]
    print(elements)

if __name__=="__main__":
    elements = [3,85,2,6,1,9,33]
    bubble_sort(elements)

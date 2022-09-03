# given are the n number of studenks and k number of books with their page numbers
# allocate these books among students such that the maximum number of pages they \
# get to read is minimum
# constraints : books can be allocated continously
# each student should get atleast one book
# books attlocated to one student should be read completely by him

# it is not necessary that the array of page numbers of books is sorted

# take the max number of pages as start point and the sum of total pages of all books as end point
# apply binary search on it , if the mid is not valid , move to right
# if is valid , move to left to get a smaller value

# the function that will check the validity will run a linear loop on array and 
# will start summation of pages , if the sum exceeds the mid , increase the count of students 
# if at any point the number of students exceeds the given number of students , return false , else return true.


def is_valid(pages , students , mid ):
    sum=0
    stu = 1
    for i in pages:
        sum+=i
        if sum>mid:
            stu+=1
            sum = i
            if stu > students:
                return False
    return True

def min_pages(pages , students):
    if students>len(pages):
        return -1
    start = max(pages)
    end  = sum(pages)
    while start<=end:
        mid = start + (end-start)//2

        if is_valid(pages , students , mid ):
            res = mid
            end = mid-1
        else:
            start = mid+1
    return res

pages = [10,20,30,40]
students = 5
print(min_pages(pages,students))

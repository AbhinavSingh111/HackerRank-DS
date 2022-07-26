def count_substring(string, sub_string):
    count=0
    string=string.lower()
    sub_string=sub_string.lower()
    for i in range(len(string)):
        l=string[i:3+i]
        if l==sub_string:
            count+=1
            
    return count

    # count = 0

    # while sub_string in string:
    #     i = string.find(sub_string)
    #     string = string[:i] + string[i + 1:]
    #     count += 1

    # return count
# string="ABCDCDC"
# sub_string="CDC"

string="ThIsisCoNfUsInG"
sub_string="is"
print(count_substring(string,sub_string))

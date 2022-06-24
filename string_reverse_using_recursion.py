def string_reversing(string):
    if string=="":
        return ""
    else:
        return string_reversing(string[1:])+ string[0]

if __name__=="__main__":
    string = "Abhinav wants to move ahead of Shreya"
    print(string)
    reversed_string = string_reversing(string)
    print(reversed_string)

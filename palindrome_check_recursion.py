def palindrome_checker(string):
    if len(string)==0 or len(string)==1:
        return True
    elif string[0]==string[len(string)-1]:
        return palindrome_checker(string[1:len(string)-1])
    else:
        return False

if __name__=="__main__":
    string = "POP"
    print(string)
    if palindrome_checker(string):
        print("True")
    else:
        print("False")

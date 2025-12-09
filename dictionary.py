outcome_dict={}
username_list=[]

#this function is used, to check if pass, defer and fail marks are valid or not
def score_check(score):
    if score%20!=0:
        print("Out of range")
        check_loop = "continue"
    elif score>=0 and score<=120:
        check_loop = "break"
    elif score<0 or score>120:
        print("Enter a number between 0-120")
        check_loop = "continue"
    return check_loop
    

status=0
state=0
while status!=1:    #loop continues until user inputs 'q'
    while state!=1:
        while True: #checks if the username is valid
            print("-"*26)
            try:
                username=input("Enter your user ID: ")
                username=username.lower()
                original=1
                valid=0
                for count in range (len(username_list)):
                    if username==username_list[count]:  #username duplication                       
                        original=0
                    else:
                        original=1
                #username validation
                num1=int(username[1:9])
                num2=int(username[1:9])
                if num1>=0000000 and num2<=9999999:
                    valid=1
                else:
                    valid=0
                        
                if len(username)==8 and username[0]=='w' and original==1 and valid==1:
                    break
                else:
                    print("Username should start with a 'w'\nUsername should be unique\nUsername should have 7 numbers after the 'w'")
            except ValueError:
                print("Invalid")
        while True: #used to check if pass credits is valid
            try:
                passm=int(input("Enter your PASS credits: "))
                loop_breaker = score_check(passm)   #uses the user-defined function
                if loop_breaker == "continue":
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")
        while True: #used to check if defer credits is valid
            try:
                defer=int(input("Enter your DEFER credits: "))
                loop_breaker = score_check(defer)   #uses the user-defined function
                if loop_breaker == "continue":
                    continue
                else:
                    break
            except ValueError:  
                print("Integer required")
        
        while True: #used to check if fail credits is valid
            try:
                fail=int(input("Enter your FAIL credits: "))
                loop_breaker = score_check(fail)    #uses the user-defined function
                if loop_breaker == "continue":
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")
        

        total=passm+defer+fail
    
        if total==120: #checks if total credit is valid or not
            username_list.append(username)
            state=1
        else:
            print("Total incorrect")
    
    #checks for the students's outcome
    
    if passm==120:  #checks for the progress outcome
        outcome="Progress- {}, {}, {}".format(passm, defer, fail)
        print("Progress")

    elif passm==100:
        outcome="Progress (module trailer)- {}, {}, {}".format(passm, defer, fail)
        print("Progress (module trailer)")
    elif fail>=80:
        outcome="Exclude- {}, {}, {}".format(passm, defer, fail)
        print("Exclude")
    else:
        outcome="Module Retriever- {}, {}, {}".format(passm, defer, fail)
        print("Do not progress - module retriever")
    outcome_dict[username]=outcome
    print("Would you like to enter another set of data?")
#checks if another set of data needs to be added, if no the while loop stops
    while True:
#checks whether the loop should continue or stop
        try:
            result=input("Enter 'y' for yes or 'q' to quit and view results: ")
            result=result.lower()
            if result=="y" or result=="q":
                break
            if result!="y" or result!="q":
                print("Invalid input")
                continue
        except ValueError:
            print("Invalid input")
    if result=="y":
        status=0
        state=0
    else:
        status=1
        state=1

score_summary= ("\n".join(f"{key} : {value}" for key, value in outcome_dict.items()))
print(score_summary)


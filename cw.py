#the counts are used for the histrogram 
countP=0
countT=0
countR=0
countE=0
#adds '*' in each outcome everytime to display on the histrogram
progress=" "
trailer=" "
retriever=" "
excluded=" "
#to store all the scores and outcomes. used for part 2
passlist=[]
deferlist=[]
faillist=[]
outcomelist=[]

#this function is used, to check if pass, defer and fail marks are valid or not
def score_check(score):
    if score%20!=0:
        print("Out of range")
        check_loop = "continue"
    elif score>=0 and score<=120:
        check_loop = "break"
    elif score<0 or score>120:
        
        print("Out of range")
        check_loop = "continue"
    return check_loop
    

status=0
state=0
score_sheet=open("score_sheet.txt", "w")    #makes a new file or clears an existing file

while status!=1:    #loop continues until user inputs 'q'
    score_sheet=open("score_sheet.txt", "a") 
    while state!=1:
        while True: #used to check if pass credits is valid
            print("-"*26)
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
            state=1
        else:
            print("Total incorrect")
            
    passlist.append(passm)  #adds the valid pass credit to pass list
    deferlist.append(defer) #adds the valid defer credit to defer list
    faillist.append(fail) #adds the valid fail credit to fail list
    
    

    #checks for the students's outcome
    
    if passm==120:  #checks for the progress outcome
        countP=countP+1     #if the student has progressed, it increments by 1 to count the number of students
        progress=progress+"*"   #used for the histrogram by concatenating
        outcome="Progress"
        print("Progress")
    elif passm==100:
        countT=countT+1   #if the student has progressed, it increments by 1 to count the number of students  
        trailer=trailer+"*"     #used for the histrogram by concatenating
        outcome="Progress (module trailer)"
        print("Progress (module trailer)")
    elif fail>=80:
        countE=countE+1     #if the student has progressed, it increments by 1 to count the number of students
        excluded=excluded+"*"   #used for the histrogram by concatenating
        outcome="Exclude"
        print("Exclude")
    else:
        countR=countR+1     #if the student has progressed, it increments by 1 to count the number of students
        retriever=retriever+"*"     #used for the histrogram by concatenating
        outcome="Module Retriever"
        print("Do not progress - module retriever")
    outcomelist.append(outcome)     #adds the valid outcome credit to outcome list
    score_sheet.write(f"{outcome}  - {passm}, {defer}, {fail}\n")
    print("\nWould you like to enter another set of data?")
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

#prints the histrogram 
print("\nHistrogram")
print(f"Progress {countP}  :  {progress}")
print(f"Trailer {countT}   :  {trailer}")
print(f"Retriever {countR} :  {retriever}")
print(f"Excluded {countE}  :  {excluded}")

count=0
number=len(outcomelist)     #counts the number of elements so that the loop will repeat the set amount of times to print all the sets of data
print("\nPart 3")
for count in range(0,number):   #prints all the sets of data 
    print(f"{outcomelist[count]} - {passlist[count]}, {deferlist[count]}, {faillist[count]}")
    
score_sheet.close() #closes the file

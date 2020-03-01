'''
This program firstly grabs all the students' data from website, and form a pythonlist,
and then use such a awesome algorithem to transform the python list into a binary
search tree. And then it uses binary search tree to do the following 5 functionalities.

1)add new student to the database
2)find the average of the score of all students
3)count the number of students who got less than 50%
4)find a particular student
5)update final score of a particular student

Author: Min Jie
StudentID:20048927
'''

import urllib.request

'''
This function is used for reading the database from website, and store it as a python
list, and return this python list
'''
def read_html():
    students_list = []
    response = urllib.request.urlopen("http://www.cs.queensu.ca/home/cords2/marks.txt")
    html = response.readline()  #reads one line
   
    #store each line into the students_list
    while len(html) > 0:
        #split the str by ", and store one student's grade as a list
        data = html[0:-1].decode('utf-8').split(',')
        #add each student's grade list to students_list
        students_list.append(data)
        html = response.readline()  #reads one line
    #change the type of score from str to float
    for i in range(len(students_list)):
        for j in range(len(students_list[i])):
            students_list[i][j] = float(students_list[i][j])

    return students_list

'''
This function is used for adding student's data into the binary search tree.
In other words. change the students' data type from python list into binary
search tree.
'''
def add_new_node(tree,students):
    #base case when tree is empty
    if tree == None:
        tree = {}
        tree['data'] = students
        tree['right'] = None
        tree['left'] = None
        return tree
    #build the BST by students ID
    #add the new student to the right of the tree if his/her students ID is larger
    elif students[0] > tree['data'][0]:
        tree['right'] = add_new_node(tree['right'],students)
        return tree
    #add the new student to the right of the tree if his/her students ID is smaller
    elif students[0] < tree['data'][0]:
        tree['left'] = add_new_node(tree['left'],students)
        return tree
    
    return tree #when students number are same. Though it is impossible.

'''
This function is used for finding the sum of one assignment or exam.
It is a part function to find average of one assignment or exam.
'''
def find_sum(tree,user_choice):
    #base case
    if tree == None:
        return 0
    #current student's score
    score_sum = tree['data'][user_choice]
    #add students score from left by recursive function
    score_sum = score_sum + find_sum(tree['left'],user_choice)
    #add studengs score from right by recursive function
    score_sum = score_sum + find_sum(tree['right'],user_choice)
    #return the sum of the score
    return score_sum

'''
This function is used for finding the total number of students
It is a part function to find average of one assignment or exam
'''
def count_total(tree,count):
    #base case
    if tree == None:
        #return current number of students
        return count
    #call the left subtree
    count = count_total(tree['left'],count)
    #call the right subtree
    count = count_total(tree['right'],count)
    #If a student is in current tree, add 1 to count
    if tree != None:
        count += 1
    #return current count to the last function
    return count

'''
This function is used for finding the total number of students who fail(<50%)
'''
def countF(tree,count):
    #base case 
    if tree == None:
        #return current students who get fail
        return count #reach the base case, dont change the number
    #call the left subtree
    count = countF(tree['left'],count)
    #call the right subtree
    count = countF(tree['right'],count)
    #when current tree data is less than 50%, count was added 1
    if tree['data'][7] < (65*0.5):
        count += 1
    #return current count to the last function
    return count

'''
This function is used for find a particular student, and then print his
or her all grades.
'''
def find_students(tree,studentID):
    #When the student ID can not be found
    if tree == None:
        print('Student does not exist')
        return None
    #When find the stidents, print his or her all data
    if tree['data'][0] == studentID:
        print('student mark: \nassign 1:', tree['data'][1],
              '\nassign 2:', tree['data'][2],
              '\nassign 3:', tree['data'][3],
              '\nassign 4:', tree['data'][4],
              '\nassign 5:', tree['data'][5],
              '\nmidterm:',tree['data'][6],
              '\nfinal exam:', tree['data'][7])
    #When student ID that we are looking for is smaller than student ID of current tree
    #Go to the left subtree
    elif tree['data'][0] > studentID:
        find_students(tree['left'],studentID)
    #When student ID that we are looking for is greater than student ID of current tree
    #Go to the right subtree
    elif tree['data'][0] < studentID:
        find_students(tree['right'],studentID)

'''
This function is used for updating final exam of a particular student
'''
def update_final(tree,studentID):
    #When the student ID can not be found
    if tree == None:
        print('Student does not exist')
        return None
    #When we find the student, and prompt user to input the updated final mark
    if tree['data'][0] ==studentID:
        tree['data'][7] = float(input('Please enter the updated final mark:'))
        return tree
    #When student ID that we are looking for is smaller than student ID of current tree
    #Go to the left subtree
    elif tree['data'][0] > studentID:
        return update_final(tree['left'],studentID)
        #return tree
    #When student ID that we are looking for is greater than student ID of current tree
    #Go to the left subtree
    elif tree['data'][0] < studentID:
        return update_final(tree['right'],studentID)
        #return tree
'''
The menu function is used for asking user what functionality he/she would like to use
And then run the correspongding function(algorithm)
'''
def menu():

    try:
        #a python list that contains all students' data
        alist = read_html()
        #Creat an empty tree
        tree = None
        #add each student's data into the binary search tree
        for i in alist:
            tree = add_new_node(tree, i)
        
        restart = 'y'
        while restart == 'y':
            print('Please enter 1-5 to choose a functionlity\n')
            #Ask user to choose a functionality
            user_choice = int(input("1)add a new student's data\n"
                                    "2)find the average of any one of the marks\n"
                                    "3)count the number of students who got less than 50%\n"
                                    "4)look up the marks for a particular student\n"
                                    "5)update the final exam mark for a student\n"))
        
            if user_choice == 1:
                #create an empty list
                data_list = []
                #ask for student's number and score, andthen add it to the list
                data_list.append(float(input("Please enter the new student's number\n")))
                data_list.append(float(input("Please enter the new student's assign 1 mark\n")))
                data_list.append(float(input("Please enter the new student's assign 2 mark\n")))
                data_list.append(float(input("Please enter the new student's assign 3 mark\n")))
                data_list.append(float(input("Please enter the new student's assign 4 mark\n")))
                data_list.append(float(input("Please enter the new student's assign 5 mark\n")))
                data_list.append(float(input("Please enter the new student's midterm exam mark\n")))
                data_list.append(float(input("Please enter the new student's final exam mark\n")))
                tree = add_new_node(tree,data_list)
                print('Add successfully')
                
            elif user_choice == 2:
                #ask user to choose one assginment or exam
                score = int(input('Please enter 1 for assign 1\n'
                                  'Please enter 2 for assign 2\n'
                                  'Please enter 3 for assign 3\n'
                                  'Please enter 4 for assign 4\n'
                                  'Please enter 5 for assign 5\n'
                                  'Please enter 6 for midterm\n'
                                  'Please enter 7 for final\n'))
                #count the total students
                num = count_total(tree,0)
                #count the sum of all student's score
                score_sum = find_sum(tree,score)
                #print the average
                print('The average is', score_sum/num)
                
                
            elif user_choice == 3:
                #print the number of students who got less than 50%
                print('The number of students who got less than 50% is',countF(tree,0))
                
            elif user_choice == 4:
                #Ask user to input a studentID that he/she is looking for
                studentID = int(input("Please enter the student's number you are looking for"))
                find_students(tree,studentID)
                
            elif user_choice == 5:
                #Ask user to input a studentID that he/she is looking for
                studentID = int(input("Please enter the student's number you would like to update"))
                #update the grade
                update_final(tree,studentID)
                print('Update successfully')
            #Ask if user would like to continue using the program.
            restart = input('\nEnter y to continue, other key to quit the program\n')
    except:
        print('Error!')
menu()

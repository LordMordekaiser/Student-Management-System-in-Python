#student class
class Student:
    
    def __init__(self,name,lname,age,sex,major):
        self.name=name
        self.lname=lname
        self.age=age
        self.sex=sex
        self.major=major
    #"def's" defines the functions
    def get_name(self):
        return self.name

    def get_last(self):
        return self.lname
    
    def get_age(self):
        return self.age
    
    def get_sex(self):
        return self.sex
    
    def get_major(self):
        return self.major
    
     
    def set_name(self,name):
        
        self.name=name
    
    def set_lastname(self,lname):
        
        self.lname=lname
    
    def set_age(self,age):
        
        self.age=age
        
    def set_Sex(self,sex):
            
            self.sex=sex
    
    def set_major(self,major):
        
        self.major=major
    

    
    
    def add(name,lname,age,sex,major):
        
        
        ob=Student(name,lname,age,sex,major)
        ls.append(ob)
    
    #it defines search funciton
    def search(name,surname):
        
        for i in ls:
            if i.get_name()==name and i.get_last()==surname:
                print("Name:",i.name)
                print("Surname:",i.lname)
                print("Age:",i.age)
                print("Sex:",i.sex)
                print("Major:",i.major)
                print("\n")
                
         
        x=ls.index(i)
        
        return ls[x-1]
    
    #function for show all of the students
    def showall():
        
        for i in ls:
            print("Name:",i.name)
            print("Surname:",i.lname)
            print("Age:",i.age)
            print("Sex:",i.sex)
            print("Major:",i.major)
            print("\n")
    

    #function for modifying student
    def modify(name,surname):
        
        #here we search student from his/her name and surname
        l=Student.search(name,surname)
        
        loop=True
        
        while(loop):
            
            #first it prints all changeable data when you press the number it asks a data to replace if you click "6" it breaks the loop
            print("1.Name\n2.Surname\n3.Age\n4.Sex\n5.Major\n6.Exit")
            ch=int(input("Enter your choice:\n"))
            
            #for example if you click 1 it asks for new name for selected student
            if ch==1:
                
                Name=input("Enter new name")
                
                l.set_name(Name)
                
                
            elif ch==2:
                
                Surname=input("Enter new surname")
                
                l.set_lastname(Surname)
            
            elif ch==3:
            
                Age=str(input("Enter new age"))                
                
                l.set_age(Age)
            
            elif ch==4:
                
                Sex=input("Enter new sex")
                
                l.set_Sex(Sex)
            
            elif ch==5:
                
                Major=input("Enter new major")
                
                l.set_major(Major)
                
            elif ch==6:
                
                loop=False
        
        #in the end it prints everything after you change a data
        print("Name:",l.name)
        print("Surname:",l.lname)
        print("Age:",l.age)
        print("Sex:",l.sex)
        print("Major:",l.major)
        print("\n")
        print("Terminating.......")
    

    #function to search student by age interval 2 numbers
    def search_by_Age(age1,age2):
         
        for i in ls:
            
            if int(i.age)>=age1 and int(i.age)<=age2:
               print("Name:",i.name)
               print("Surname:",i.lname)
               print("Age:",i.age)
               print("Sex:",i.sex)
               print("Major:",i.major)
               print("\n") 
         

#function to delete student array
    def delete(name,surname):
    
        l=Student.search(name,surname)
        i=ls.index(l)
        del ls[i]
    
#it opens student.txt file and writes student array
    def writetofile():
        
        with open('student.txt','a') as f:
            
            for i in ls:
                f.write(i.name + ' ' + i.lname + ' ' + i.age + ' ' + i.sex +  ' ' + i.major)
                f.write('\n')
     
#from student.txt file it reads the data of student arrays
    def readfromfile():
        
        with open('student.txt','r') as f:
            
            data=f.read()
            print(data)
    
ls=[]
ob=Student('','','','','')

lop=True

#it is the main menu of the code
while(lop):
    #here code shows the main options
    print("MENU\n1.Add New Student\n2.Search Student\n3.Show All Students\n4.Modify Student\n5.Show by Age\n6.Delete Student\n7.Write to file\n8.Read from File\n9.Exit")
    choice=int(input("Please enter your choice:\n"))
    
    #if enter 1 to console it will let you add new student by calling properties of student calls sudent.add function
    if choice==1:
        
        Name=input("Please enter name:")
        Surname=input("Please enter surname:")
        Age=str(input("Please enter age:"))
        Sex=input("Please enter sex:")
        Major=input("Please enter major:")
        Student.add(Name,Surname,Age,Sex,Major)
    
    #if enter 2 it calls student.search function and asks 2 variables
    elif choice==2:
        
        Name=input("Please enter the name for search:")
        Surname=input("Enter surname:")
        Student.search(Name, Surname)
    
    #calls showall function and lists all the students with their data
    elif choice==3:
        
        Student.showall()
    
    #asks name and surname of student then calls student.modify function
    elif choice==4:
        
        Name=input("Please enter the name for modify:")
        Surname=input("Enter the surname:")
        Student.modify(Name,Surname)
    
    #calls search by age functions
    elif choice==5:
    
        Age1=int(input("Please enter the lower limit for search:"))
        Age2=int(input("Enter the upper limit"))
        
        Student.search_by_Age(Age1, Age2)
    
    #calls delete student function
    elif choice==6:
        
        Name=input("Please enter the name for delete:")
        Surname=input("Enter the surname:")
        Student.delete(Name, Surname)

    #calls writetofile function and prints everything to student.txt file in the same folder location of code file
    elif choice==7:
        
        Student.writetofile()
    
    #calls readfromfile function and reads from file "student.txt" in the same folder location of code file 
    elif choice==8:
        
        Student.readfromfile()
    
    #closes the main menu
    elif choice == 9:
        print("Exiting from menu")
        break
    
    #if type anything else then numbers 1 to 9 automatically closes the menu
    else:
        print("Exitig...")
        lop=False






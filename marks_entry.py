class person:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
class student(person):
    def __init__(self,name,email,phone,roll,year,depart):
        super().__init__(name,email,phone)
        self.roll=roll
        self.year=year
        self.depart=depart
        
class subject:
    def __init__(self,sub_name,faculty,code,mid1,mid2,mid3,final):
        self.sub_name=sub_name
        self.faculty=faculty
        self.code=code
        self.mid1=mid1
        self.mid2=mid2
        self.mid3=mid3
        self.final=final
        self.total=mid1+mid2+mid3+final
        self.grade,self.grade_point=self.calculate_grade()
        
    def calculate_grade(self):
        if(self.total>=90):
            return " A+",10
        if(self.total>=80):
            return " A",9
        if(self.total>=70):
            return " B",8
        if(self.total>=60):
            return " C",7
        if(self.total>=50):
            return " D",6
        if(self.total>=40):
            return "FAIL",0
    def display(self):
        print(f" SUBJECT : {self.sub_name} \t\t CODE  : {self.code} \t\t FACULTY : { self.faculty}\n")
        print(f" Marks : Mid1-{self.mid1}\tMid2-{self.mid2} \t Mid3-{self.mid3} \t SEM-{self.final}\n ")
        print(f" Total - {self.total}   |   Grade - {self.grade}   |   Grade Points - {self.grade_point}\n")
print("------------------------------------------------------------------------------------------------")
class reportcard(student,subject):
    def __init__(self,student,subjects):
        self.student=student
        self.subjects=subjects
    def calculate_cgpa(self):
        self.total_points=sum(sub.grade_point for sub in self.subjects)
        return round((self.total_points)/len(self.subjects),2)
    def display_report(self):
        print("---------------------------------------------------------------------------------------------")
        print(f"Student:{self.student.name}\t\tEmail-id{self.student.email} \t\t Phone-no{self.student.phone}\n")          
        print(f"Roll-no:{self.student.roll} \t\t\t Year:{self.student.year}\t\t\t Deapartment{self.student.depart}\n")
        print("-------------------------------------------------------------------------------------------")
        for sub in self.subjects:
            print("------------------------------------------------------------------------------------------------")
            sub.display()
        print("------------------------------------------------------------------------------------------------")
        print(f"CGPA: {self.calculate_cgpa()}")
        print("------------------------------------------------------------------------------------------------")
student1=student("Aswani","Yashu@gmail.com",6302169832,50,2025,"AIML")
sub1=subject("CS001","RAJESH","MATHS",18,20,16,35)
sub2=subject("CS002","UDAY KUMAR","AIML",19,16,20,38)
report=reportcard(student1,[sub1,sub2])
report.display_report()

      
        
    
        
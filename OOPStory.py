class Person:
    moods=("Happy","Lazy","Tired")
    
    def __init__(self,name,money,mood,healthrate):
        self.name=name
        self.money=money
        self.mood=mood
        self._healthrate=healthrate
        
    def sleep(self,hours):
        if isinstance(hours,int)==False:
           print("not a numebr")
           return False
        elif hours==7:
            self.mood=Person.moods[0]
            return True
        elif hours>7:
            self.mood=Person.moods[1]
            return True     
        elif hours<7:
             self.mood=Person.moods[2]
             return True                
        else:
           print("Not Valid")
           return False  
                 
    def eat(self,meals):
        if isinstance(meals,int)==False:
           print("not a numebr")
           return False
        elif meals==3:
            self._healthrate="75%"
            return True
        elif meals==2:
            self._healthrate="75%"
            return True     
        elif meals==1:
             self._healthrate="50%"
             return True                
        else:
           print("Not Valid Number needs to be 1 or 2 or 3 meals")
           return False
    def buy(self,items):
        if isinstance(items,int)==False:
           print("not a numebr")
           return False
        else:
            TotalItems=items*10
            if TotalItems > self.money:
                print("Total Cost exceeds the mony")
                return False
            else:
                self.money=self.money-TotalItems
                return True
    @property
    def healthrate(self):
       return self._healthrate
    @healthrate.setter
    def healthrate(self, healthrate):
         if isinstance(healthrate,int):
           print("not a number") 
         if healthrate >= 0 and healthrate<=100:
             self._healthrate=healthrate
                 
                    
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
class Employee(Person):
     def __init__(self,id,car,email,salary,distanceToWork,name,money,mood,healthrate):
         super(Employee, self).__init__(name,money,mood,healthrate)
         self.id=id
         self.car=car
         self.__email=email
         self.__salary=salary
         self.distanceToWork=distanceToWork
     def work(self,hours):
        if isinstance(hours,int)==False:
           print("not a numebr")
           return False
        elif hours==8:
            self.mood=Person.moods[0]
            return True
        elif hours>8:
            self.mood=Person.moods[2]
            return True     
        elif hours<7:
             self.mood=Person.moods[1]
             return True                
        else:
           print("Not Valid")
           return False  
     def drive(self):
        pass 
     def refuel(self):
        pass
     def send_mail(self,to,subject,message,reciever_name):
        try: 
            with  open("email.txt","w") as emailfile:
                emailfile.write(f"From:{self.__email}")
                emailfile.write(f"To: {to}")
                emailfile.write(f"Subject: {subject}")
                emailfile.write(f"Hi,{reciever_name}")
                emailfile.write(message)
                emailfile.write("Thanks")
                emailfile.close()
                return True 
        except Exception as e:
            print("something wrong happened")
            return False
        
        
     @property
     def salary(self):
       return self. __salary
     @salary.setter
     def salary(self, salary):
         if isinstance(salary,int):
           print("not a number") 
         if salary >= 1000:
           self. __salary = salary
         if salary < 1000:
            self. __salary = 1000
                        
            
     @property
     def email(self):
       return self. __email
     @email.setter
     def email(self, email):
         if (re.fullmatch(regex,email)):
               self. __email = email
         else:
             print("email is not right")
             
            
            
            
                           
class Office:
    def __init__(self,name,employess):
        self.name=name
        self.employees=employess
    
    def get_all_employees(self):
        pass
    def get_employee(self):
        pass
    def hire(self):
        pass
    def fire(Self):
        pass
    def calculate_latness(self):
        pass
    def deduct(self):
        pass
    def reward(self):
        pass
        
class Car:
    def __init__(self,fuelrate,velocity):
        self.fuelrate=fuelrate
        self.velocity=velocity    
    def run(self):
        pass
    def stop(self):
        pass                                  

emp=Employee(5,Car(20,50),'m@g.com',500,200,'mina',6000,'happy',20)   

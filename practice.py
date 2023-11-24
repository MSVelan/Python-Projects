# Unknown number of positional arguments
'''
def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
    # print(type(args))
    # return sum(args)
print(add(1,2,3))
print(add(2,4))
print(add(6,1,1,4))
'''

# Unknown number of keyword arguments
'''
def calculate(n,**kwargs):
    n+=kwargs['add']
    n*=kwargs['multiply']
    # type(kwargs) is dict
    # for k,v in kwargs.items():
    #     print(k," ",v)
    return n

print(calculate(2,add=3,multiply=5,divide=6))
'''
'''
class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model') # if model is not there in argument then no error None gets stored

my_car = Car(make = "India", model = "Toyota")
print(my_car.make)

'''
#Error handling in python
'''
fruits = ['Apple','Pear','Orange']

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(-5)

'''
'''
import requests
apiKey = "Xp2GhMHPlUoV6WycD4yrV4dOjTHMLYcC"

server = "https://api.tequilla.kiwi.com"
endPoint = "/locations/query"
city = "London"
parameters = {
    "apikey": apiKey,
    "term": city,
    "location_types": "airport", 
    "limit": 10
}
response = requests.get(url=f"{server}/{endPoint}", params=parameters)
print(response.text)
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Endpoint = "https://www.linkedin.com/jobs/search/?currentJobId=3538511592&f_E=1%2C2&f_T=2732%2C9%2C25169%2C54%2C24%2C11845&f_WT=2&keywords=python%20developer&refresh=true&sortBy=R"

email = "muthiahsivavelan2026@gmail.com"
password = "testing12@MSV"

driver = webdriver.Chrome()

driver.get(Endpoint)

signinBtn = driver.find_element(By.CSS_SELECTOR,".nav__cta-container .nav__button-secondary")
signinBtn.click()

emailBtn = driver.find_element(By.ID,"username")
emailBtn.send_keys(email)

passwordBtn = driver.find_element(By.ID,"password")
passwordBtn.send_keys(password)

driver.implicitly_wait(4.0)

formSubmit = driver.find_element(By.CSS_SELECTOR,".login__form_action_container button")
formSubmit.click()
try:
    minimiseBtn = driver.find_element(By.ID,"ember113")
    minimiseBtn.click()
except:
    print("Error occurred")

driver.implicitly_wait(5.0)
a = driver.find_element(By.CSS_SELECTOR,".jobs-unified-top-card__company-name a")
# driver.get(a.get_attribute("href"))
a.click()

driver.implicitly_wait(4.0)

followBtn = driver.find_element(By.CSS_SELECTOR,".org-company-follow-button")
if(followBtn.text!="Following"):
    followBtn.click()

time.sleep(3000.0)
driver.quit()

'''

#Use of decorators:
'''
import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
      intime = time.time()
      function()
      endtime = time.time()
      print("Run time for", function.__name__ ,":",endtime-intime)
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
      
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
fast_function()
slow_function()
'''

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if(args[0].logged_in==True):
            function(args[0])
        else:
            print("Login first!")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print("New blog post from", user.name,".Do check it out!!")

me = User("Muthiah")
me.logged_in=True
create_blog_post(me)
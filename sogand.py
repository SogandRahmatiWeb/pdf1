print("hello world")
#نمایش مستقیم متن با پرینت 

x=5
y = "hello world"
#متغیر ها در پایتون 

x= str(3)
y=int(3)
z = float(3)
print(x)
print(y)
print(z)
3
3
3.0
 #نوع متغیر ها

x=5
y="john"
print(type(x))
print(type(y))
  #نوع متغیر را دریافت کنید 
     
x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)
     #در یک خط میتوانید به چند متغیر مقدار بدهید


x = y = z ="orange"
print(x)
print(y)
print(z)
#یک مقدار برای چندین متغیر 


fruits = ["apple", "banana", "cherry"]
x , y,z= fruits
#میتوانیم مقادیر را در متغیر ها استخراج کنیم 


x="python"
print(x)
#پرینت اغلب برای خروجی دادن متغیر ها استفاده میشود 


x= "python"
y="is"
z="easy"
print(x, y, z)
#چندین متغیر را که با کاما از هم جداشده اند نمایش میدهد



#همچنین میتوان از + هم برای نمایش متغیر استفاده کرد 
x= "python"
y="is"
z="easy"
print(x + y + z)


#برای اعداد این کاراکتر+ به عنوان عملگر ریاضی عمل میکند 
x=10
y=50
print(x + y)

#ایجاد یک متغیر خارج از تابع و استفاده از ان داخل تابع که به ان متغیر سراسری میگویند 
x = "easy"
def myfunc():
    print(" python is " + x)
    myfunc()

    #ایجاد یک متغیر درون یک تابع و استفاده از ان در داخل تابع
    x= "awesome"

    def myfunc():
        x = "easy"
        print("python is " + x )
myfunc()
print("python is " + x )
#خروجی
#python is easy 
#python is awesome


#برای تغییر مقدار یک متغییر سراسری درون یک تابع ب استفاده از کلمه کلیدی global به متغیر اشاره کنید
x = "easy"
def myfunc():
    global x
x= "fantastic"

myfunc()
print ("python is" + x)




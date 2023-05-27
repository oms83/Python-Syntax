                        # What PYTHON

# Programming language that can do anything 
# Free and open sourse
# interpreted يتم معالجة الكود مباشرة من الرام بعكس باقي اللغات 
# interactive مكان كتابة الكود تظهر النتيجة


                        # Why PYTHON 1

# Easy to install سهلة التثبيت
# Clean and Easy سهلة التعلم
# Error Handling سهولة إيجاد الخطأ
# Debugging is Easy(Debugger created with python) سهولةالتعامل مع الأخطاء
# Gross Platform تتعامل مع أنظمة التشغيل كلها 
# Expressive لغة معبّرة
# OOP تدعم


                        # Why PYTHON 2

# integrated يمكن دمجها مع لغة ثانية في نفس التطبيق
# Support Module and Packages
# Lage Set of Libs and Plugins
# Memory Management (Garbage Collection) إذا تم نسيان أي بيانات في الذاكر البايثون تتعامل معه 
#  Multi Purpose متعددة الاستخدام
# Growing fast 
# You can switch careers with the basic knowladge من أساسيات اللغة التي نعرفها ممكن أن ننطلق بهذا المعرفة عن اللغة لأي مجال


                        # What's Python Used For

# Web Development (Django, Flask)
# Games(PyGame)
# Desktop Apps(PyGUI, Tkinter)
# Hacking 
# Machine Learning & Data Science
# AI & Robots in Mars
# Automation أتمتة
# Web Scrapping(Harvest) (مثل بيانات أسعار الذهب أو البيتكوين)ممكن ان نحصل علي بيانتا من موقع ثاني ونعرضها بموقعنا 
# Android Game


                        # Apps Created with Python

# Disqus
# Instagram
# Spotify
# Dropbox
# Uber
# Reddit


                        # Companies Using Python

# Google
# Facebook
# Netflix



# if True:
#     print("I love python"); print("\t Python Language")
#     print("my name Omer")
#     if True:
#         print("My old is 22")
#         if True:
#             print("I'm from Syria")

# ----------------------------------
# Information About File
# License
# Who Created The File
# When The file Created
# Why The File Created
# Write Before The Programming line
# Write Beside The Programming line
# Prevent Code From Run
# ctrl+/ for make comment
# ----------------------------------

# This is Comment
# print("omer memes") # this is inline comment

# """
# This is 
# Not
# Multiple
# Line 
# Comments
# لم تخصص بإسم string هذا عبارة عن 
# """

# ----------------------------------
# type()  
# All Data in Python is Object
# ----------------------------------

# print(type(10))     # <class 'int'>
# print(type(-50))    # <class 'int'>

# print(type(75.4))   # <class 'float'>
# print(type(-5.3))   # <class 'float'>

# print(type('a'))    # <class 'str'>
# print(type(' '))    # <class 'str'>
# print(type('\n'))   # <class 'str'>
# print(type('\0'))   # <class 'str'>
# print(type('\t'))   # <class 'str'>
# print(type('\a'))   # <class 'str'>
# print(type("omer")) # <class 'str'>
# print(type("\n"))   # <class 'str'>

# print(type(["omer", "ali"]))   # <class 'list'>
# print(type([ 1, 3, 5, 7 ]))   # <class 'list'>

# print( type( (1, 3, 5, 7) ) )   # <class 'tuple'>
# print( type( ("omer", "ali") ) )   # <class 'tuple'> مترابطة بيانية
# print( type( ('x', 'a') ) )   # <class 'tuple'>

# print( type( { "One":1, "Two":2, "Tree":3 } ) )   # <class 'dict'> (Dictionary) (قاموس , معجم)

# print(type(2==2))   # <class 'bool'>  Boolean
# print(type(2==5))   # <class 'bool'>  Boolean

# -----------------------------------------------------------------
# Syntax => [Variable Name] [Assigment Operator] [Value]
# 
# Name Convention and Rules
# --->> Variables <<---
# [1] Can Strat With (a-z A-Z) or Underscore ( _ )
# [2] You Cannot Start With Num or Special Characters (0-9 $^#@...)
# [3] Can Include (0-9) Or Underscore
# [4] Cannpt Include Special Characters
# [5] Name is Not Like name [Case sensitive]
# -----------------------------------------------------------------

# name = "omer MEMES" # Single Word => Normal
# myName = "omer MEMES" # Two Word => camelCase
# my_name = "omer MEMES" # Two Word => snake_case
# print(name)
# print(myName)
# print(my_name)

# -----------------------------------------------------------------
# --->> Variables <<---
# source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language
# Compilation : Translate Code Before Run Time
# Run-Time : Period App Take To Executing Command
# interpreted : Code Translated On The Fly During Execution
# -----------------------------------------------------------------


# x=10          # لغة ديناميكية    
# x="omer"
# print(x) # omer


# Reserved Words كلمات اللغة المحجوزة
# help("keywords")
# # False               class               from                or   
# # None                continue            global              pass 
# # True                def                 if                  raise
# # and                 del                 import              return
# # as                  elif                in                  try
# # assert              else                is                  while
# # async               except              lambda              with
# # await               finally             nonlocal            yield
# # break               for                 not


# a, b, c = 3, 4, 5
# print(a)
# print(b)
# print(c)

# -----------------------------------------------------------------
# Escape Sequences Character 
# \b => back space إلغاء آخرف لكل استخدام
# \ => New Line, Escape New Line + \
# \ => Scape Back Slash
# \ => Single Quote --> \'test\'
# \ => Double Quote --> "test\" 
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab يعمل تاب مكانه
# \xhh => Character Hex Value
# -----------------------------------------------------------------

# Back Space
# print("Hello\bWorld")   # HellWorld

# # Escape New Line + Back Slash
# print("My \
#     name is: \
#         omer")

# Escape Back Slash
# print("I Love Python \\")     # I Love Python \

# Escape Single Quote
# print("I Love Single Quote \'test\' ")     # I Love Back Slash 'test' 

# Escape Double Quote
# print("I Love Double Quote \"test\" ")     # I Love Back Slash "test" 

# # Line Feed 
# print("Hello World\nSecond Line")

# # Carriage Return
# print("aaab33fdef\r1234")   #1234ef

# # Horizantal Tab
# print("Omer\tMEMES")    # Omer    MEMES

# # Character Hex Value
# print("\x4F\75")   # O=


# -------------------
# -- Concatenation --
# -------------------

# msg = "I Love"
# lang = "Python"
# print(msg + " " + lang) # I Love Python
# print(msg + ' ' + lang) # I Love Python
# full = msg+" "+lang
# print(full) # I Love Python

# a = "First \
#      Second \
#      Thrid"

# b = "A \
#      B \
#      C"
# print(a+' '+b)  #First      Second      Thrid A      B      C

# # print("Hello"+2) #Error


# ------------
# -- String --
# ------------

# myStringOne = "my name is omer memes"
# myStringTwo = 'my name is omer memes'
# print(myStringOne)
# print(myStringTwo)
 

# # # Dynamic Language
# myStringOne = "my name is 'omer memes' " # single quote بدل استخدام 
# myStringTwo = 'my name is "omer memes" ' # double quote بدل استخدام 
# print(myStringOne)
# print(myStringTwo)


# myStringThree = \
# '''One
# Two
# Three'''
# myStringFour = \
# """1
# 2
# 3"""
# ## feed line (\n) فإننا نتحول مباشرة لسطر جديد بدون استخدام string عند استخدام هذا النوع من الـ   

# print(myStringThree)
# print(myStringFour)

# myStringfive = \
# '''One '1'
# Two "2" \\\ 
# Three '3'
# '''
# ## \\\_ ثلاث سلاشات وبعدها مسافة يُكتب لنا داخل النص سلاشين


# myStringSix =\
# """1 "One"
# 2 'Two' \\\
# 3 "Three"
# """
# ## ثلاث سلاشات وليس بعدهم مسافة يُكتب لنا في النص فقط سلاش واحد
# print(myStringfive)
# print(myStringSix)

# -----------------------------------------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contion Elements
# [3] Evert Element has Its Own Index
# [4] Python Use Zero Based Inedexing (index strat from zero)
# [5] Use Square Brackets To Access Element
# [6] Slicing : Enable Accessing Parts of Strings, Tuples Or Lists
# -----------------------------------------------------------------

# # Indexing (Access Single Item)
# myName = "my name is Omer MEMES"
# print(myName[1])    #الوصول للنص من اليسار عند استخدام الأعداد صفر وما فوق
# print(myName[-3])   # عند استخدام الساب نصل للنص من اليمين

# # Slicing (Access Multiple Sequence Item)
# # [Strat:End] End Not Included
# # [Strat:End:Steps]

# print(myName[8:10])

# print(myName[:10])  # if start is not here will strat from zero
# print(myName[11:])  # if end not here will go to the end

# print(myName[0::1])  # Full Data
# print(myName[::1])  # Full Data
# print(myName[0::])  # Full Data
# print(myName[::])  # Full Data

# print(myName[0::2])  # حرف يُطبع وحرف لا # omer memes >> o e  e e s
# print(myName[::3])   # يطبع حرف ويوفّت حرفين




# ---------------------
# -- Strings Methods --
# ---------------------

## len() قياس طول النص
# a = "I Love Python"
# b = "      I Love Python      "
# print(len(a))   #13
# print(len(b))   #25

# # strip()   تحذف المسافات عن اليمين واليسار
# # rstrip()  تحذف المسافات عن اليمين
# # lstrip()  تحذف المسافات عن اليسار
# print(b.strip())    # I Love Python|
# print(b.rstrip())   # |      I Love Python
# print(b.lstrip())   # I Love Python      |


# a = "#####I Love Python#####"
# print(a.strip("#")) 
# print(a.rstrip("#"))  
# print(a.lstrip("#"))   

# a = "##%##%#I Love Python##%##%#"
# print(a.strip("#%")) 
# print(a.rstrip("#%"))  
# print(a.lstrip("#%"))  

# # title() أول حرف من كل كلمة كبير والأحرف التي تأتي بعدر الأقارم تصبح كبيرة
# myName = "my name is omer memes, my old is 22 years."
# print(myName.title())   # My Name Is Omer Memes, My Old Is 22 Years.

# # capitalize() تحول أول حرف من كل كلمة لحرف كبير ولكن الاحرف التي تأتي بعد الأقام تبقى على حالها
# print(myName.capitalize())  # My name is omer memes, my old is 22 years.

# # zfill تعبئى الفراغات بالمطلوب
# a, b, c, d = "1", "11", "111", "1111"
# print(a.zfill(3))   # 001
# print(b.zfill(3))   # 011
# print(c.zfill(3))   # 111
# print(d.zfill(3))   # 1111


# # upper() & lower()
# n = "omer"
# n = "OMER"
# print(n.upper())
# print(n.lower())

# # split() & rsplit() تحويل كلمات النص إلى ليستا
# str_ = "Hello i am omer i am from syria"
# print(str_.split()) # ['Hello', 'i', 'am', 'omer', 'i', 'am', 'from', 'syria']


# str_ = "Hello-i-am-omer-i-am-from-syria"
# print(str_.split()) # ['Hello-i-am-omer-i-am-from-syria']


# str_ = "Hello-i-am-omer-i-am-from-syria"
# print(str_.split("-")) # ['Hello', 'i', 'am', 'omer', 'i', 'am', 'from', 'syria']


# str_ = "Hello-i-am-omer-i-am-from-syria"
# print(str_.split("-", 2)) # ['Hello', 'i', 'am-omer-i-am-from-syria']


# str_ = "Hello-i-am-omer-i-am-from-syria"
# print(str_.rsplit("-", 3))  # ['Hello-i-am-omer-i', 'am', 'from', 'syria']


# # center() إضافة رموز إلى طرفي الكلمة # بحاجة إلى معامل إجباري

# e = "Omer"
# print(e.center(9))      # spac      #    Omer  
# print(e.center(9, "#")) # Hashes    # ###Omer##
# print(e.center(9, "@")) # Hashes    # @@@Omer@@

# # count() يبين عدد مرات تكرار الكلمة أو الحرف في النص
# f = "I love python and php because php is easy"
# print(f.count("php"))   # 2
# print(f.count("a"))   # 3
# print(f.count("a", 0, 29))   # ابحث عن المطلوب من الدليل صفر حتى الدليل 29


# # swapcase() جعل الأحرف الكبيرة صغيرة والصغيرة كبيرة
# g = "omer MEMES"
# h = "ALI memes"
# print(g.swapcase()) # OMER memes
# print(h.swapcase()) # ali MEMES


# # startswith() # هل الكلمة  تبدأ بالحرف المطلوب
# i = "I Love Python"
# print(i.startswith("I"))    # true
# print(i.startswith("i"))    # False
# print(i.startswith("P",7, 12))    # True



# # endswith  """End Not Included """ 
# # # هل الكلمة  تنتهي بالحرف المطلوب
# j = "I Love Python"
# print(j.endswith("n"))    # True
# print(j.endswith("n",7, 13))    # True
# print(j.endswith("N",7, 12))    # false
# print(j.endswith("e",2, 6))    # True

# # index(substring, start, end)
# a = "my name omar"
# print(a.index("a")) # 4
# print(a.index("a", 5)) # 10   ابحث عالحرف من عند الدليل 5
# print(a.index("a", 5)) # 10   ابحث عالحرف من عند الدليل 5
# print(a.index("a", 10, 11)) # 10   ابحث عالحرف من عند الدليل 10
# # print(a.index("a", 0,4)) # Error


# # find(substring, start, end)
# # فهو يعطي خطأ index فقط في حالة عدم وجود الحرف المطلوب يُظهر النتيجة كسالب واحد على عكس الـ index يعمل عمل الـ


# print(a.find("a", 10, 11)) # 10   ابحث عالحرف من عند الدليل 10
# print(a.find("a", 0,4)) # -1



# # rjust(width, fill char)  ljust(width, fill char)  إضافة رموز لطرفي الكلمة
# c="omer"
# print(c.rjust(10))      # |      omer
# print(c.rjust(10,"#"))  # ######omer

# print(c.ljust(10))      # omer      |
# print(c.ljust(10,"#"))  # omer######


# # splitlines() تحويل السطور إلى ليست
# e = """First Line
# Second Line
# Thrid Line"""

# print(e)
# print(e.splitlines())   # ['First Line', 'Second Line', 'Thrid Line']


# # expandtabs() اضافة فراغات على حسب الطلب
# g = "Hello\tMy\tName\tOmer"
# print(g.expandtabs(20)) # مكان التاب الواحد يضع 20 تاب

# # istitel()   هل هذا عنوان ؟
# n = "I Love Python 3D"
# m = "I Love Python 3d"
# print(n.istitle())  # True
# print(m.istitle())  # False

# # isspace() هل هذه مسافة؟
# k = " "
# l = ""
# print(k.isspace())  # True
# print(l.isspace())  # False

# # islower()
# one = "i love python"
# two = "I Love Python"
# print(one.islower())    # True
# print(two.islower())    # False

# # isidentifier()  هل النص يصلح أن يكون اسم متغير؟
# three = "my_name"
# four = "myName"
# five = "_myName"
# six = "myName10"
# seven = "100my--name"
# eight = "my-name"
# print(three.isidentifier()) # True
# print(four.isidentifier())  # True
# print(five.isidentifier())  # True
# print(six.isidentifier())   # True
# print(seven.isidentifier()) # False
# print(eight.isidentifier()) # False


# # isalpha() هل النص عبارة عن أحرف فقط؟
# nine = "iLovePython"
# ten = "i love python"
# eleven = "i love python 11"
# print(nine.isalpha())   # True
# print(ten.isalpha())    # False  تحتوي على سبيس
# print(eleven.isalpha()) # False  تحتوي على سبيس وأرقام

# # isalpha() هل النص عبارة عن أحرف فقط؟
# nine = "iLovePython"
# ten = "i love python 12"
# eleven = "ilovepython 11"
# print(nine.isalnum())   # True
# print(ten.isalnum())    # False  تحتوي على سبيس
# print(eleven.isalnum()) # True  

# # replace(old value, new value, count) تبديل كلمات النص على حسب الطلب
# a = "one two three one two one three one"
# print(a.replace("one", "1", 1)) # 1 two three one two one three one
# print(a.replace("one", "1", 2)) # 1 two three 1 two one three one
# print(a.replace("one", "1"))    # 1 two three 1 two 1 three 1


# # join(iterable) دمج وإضافة رموز لعناصر الليست
# myListe = ["Ali", "Omer", "MEMES"]
# print(" ".join(myListe))    # Ali Omer MEMES
# print(' '.join(myListe))    # Ali Omer MEMES
# print("-".join(myListe))    # Ali-Omer-MEMES
# print("_".join(myListe))    # Ali_Omer_MEMES


# ---------------------
# -- Strings Methods --
# ---------------------
# 1  # len() قياس طول النص
# 2  # strip()   تحذف المسافات عن اليمين واليسار
# 3  # rstrip()  تحذف المسافات عن اليمين
# 4  # lstrip()  تحذف المسافات عن اليسار
# 5  # title() أول حرف من كل كلمة كبير والأحرف التي تأتي بعدر الأقارم تصبح كبيرة
# 6  # capitalize() تحول أول حرف من كل كلمة لحرف كبير ولكن الاحرف التي تأتي بعد الأقام تبقى على حالها
# 7  # upper() & lower()
# 8  # split() & rsplit() تحويل كلمات النص إلى ليستا
# 9  # center() إضافة رموز إلى طرفي الكلمة # بحاجة إلى معامل إجباري
# 10 # count() يبين عدد مرات تكرار الكلمة أو الحرف في النص
# 11 # swapcase() جعل الأحرف الكبيرة صغيرة والصغيرة كبيرة
# 12 # startswith() # هل الكلمة  تبدأ بالحرف المطلوب
# 13 # endswith  """End Not Included """ 
# 14 # # هل الكلمة  تنتهي بالحرف المطلوب
# 15 # index(substring, start, end)
# 16 # find(substring, start, end)
# 17 # فهو يعطي خطأ index فقط في حالة عدم وجود الحرف المطلوب يُظهر النتيجة كسالب واحد على عكس الـ index يعمل عمل الـ
# 18 # rjust(width, fill char)  ljust(width, fill char)  إذافة رموز لطرفي الكلمة
# 19 # expandtabs() اضافة فراغات على حسب الطلب
# 20 # istitel()   هل هذا عنوان ؟
# 21 # isspace() هل هذه مسافة؟
# 22 # islower()
# 23 # isidentifier()  هل النص يصلح أن يكون اسم متغير؟
# 24 # isalpha() هل النص عبارة عن أحرف فقط؟
# 25 # replace(old value, new value, count) تبديل كلمات النص على حسب الطلب
# 26 # join(iterable) دمج وإضافة رموز لعناصر الليست
# ---------------------



# ------------------------
# -- Strings Formatting --
# ------------------------

# name = "omer"
# age = 22
# rank = 10
# print("My Name is: " + name)    # My name is: omer
# # print("My Name is: " + name + " and My Age is: " + age) # Type Error

# print("My name is: %s" % "omer")    # My name is: omer
# print("My name is: %s" % name)      # My name is: omer
# print("My name is: %s and my age is: %d" % (name, age)) # My name is: omer and my age is: 22
# print("My name is: %s and my age is: %d and my rank is: %.2f" % (name, age, rank)) # My name is: omer and my age is: 22 and my rank is: 10.00

# n = "Omer"
# l = "Python"
# y = 10
# print("Iam %s Iam %s Developer With %d Exp" % (n,l,y)) # Iam Omer Iam Python Developer With 10 Exp

# # Control Floating Point Number التحكم بالنقاط العدد العشري
# myNumber = 10
# print("My Number: %d" % myNumber)   # 10
# print("My Number: %f" % myNumber)   # 10.000000
# print("My Number: %.3f" % myNumber) # 10.000
 

# # Split Strings || Slice Strings || Truncate Strings
# myLongString = "Hello Pepoles of Afak Team Education I Love Your All"
# print("Message is [%.5s]" % myLongString)
# print("Message is [%s]" % myLongString) # Will be show All string



n = "Omer"
l = "Python"
y = 10
print("Iam {:s} Iam {:s} Developer With {:f} Exp".format(n,l,y)) # Iam Omer Iam Python Developer With 10 Exp

# # Control Foating Point Number التحكم بالنقاط العدد العشري
# myNumber = 10
# print("My Number: {:d}".format(myNumber))   # 10
# print("My Number: {:f}".format(myNumber))   # 10.000000
# print("My Number: {:.3f}".format(myNumber)) # 10.000


# # Split Strings || Slice Strings || Truncate Strings
# myLongString = "Hello Pepoles of Afak Team Education I Love Your All"
# print("Message is {:.5s}".format(myLongString))
# print("Message is {:s}".format(myLongString)) # Will be show All string

# # Format Money
# myMoney = 53424242
# print("My Money in Bank is :: {}".format(myMoney))  # 53424242
# print("My Money in Bank is :: {:d}".format(myMoney))  # 53424242
# print("My Money in Bank is :: {:_}".format(myMoney))  # 53_424_242
# print("My Money in Bank is :: {:_d}".format(myMoney))  # 53_424_242
# print("My Money in Bank is :: {:,d}".format(myMoney))  # 53,424,242


# #ReArrange Items
# a, b, c = "One", "Two", "Three"
# print("Hello {} {} {}".format(a, b, c)) # Hello One Two Three
# print("Hello {1} {2} {0}".format(a, b, c)) # Hello Two Three One

# x, y, z = 10, 20, 30
# print(" {} {} {} ".format(x,y,z))
# print(" {1} {0} {2} ".format(x,y,z))
# print(" {1:.5f} {2:.3f} {0:.2f} ".format(x,y,z))    
# print(" {2:d} {1:d} {0:f} ".format(x,y,z))  # 30 20 10.000000

# # Format in Version 3.6+
# myName = "omer"
# myAge = 22
# print("My name is: {myName} and my age is : {myAge}")   # My name is: {myName} and my age is : {myAge}
# print(f"My name is: {myName} and my age is : {myAge}")  # My name is: omer and my age is : 22




# # ------------------------
# # ------- Numbers --------
# # ------------------------

# #Integer
# print(type(1))
# print(type(-1312))

# #Float
# print(type(13.54))
# print(type(-112.4))

# #Complex
# print(type(5-21j))
# print(type(4+7j))
# print(type(4+0j))
# print(type(1j))
# myComplexNumber = 2+3j
# print("Real Part is : {}".format(myComplexNumber.real))
# print("Imaginary Part is : {}".format(myComplexNumber.imag))

# # [1] You Can Convert From int To float Or Complex
# # [2] You Can Convert From float To int Or Complex
# # [3] You Cannot Convert Complex To Any Type

# print(100)
# print(float(100))
# print(complex(100))

# print(12.4)
# print(int(12.9))
# print(complex(12.9))




# # --------------------------
# # -- Arithmetic Operators --
# # --------------------------
# # [+] Addition
# # [-] Subtraction
# # [*] Multiplication   
# # [/] Division 
# # [%] Modulus
# # [**] Exponent أس
# # [//] Floor Division
# # --------------------------
# print(3+4)
# print(3-4)
# print(3*4)
# print(36/5)
# print(int(36/4))
# print(26%4)
# print(2**4)
# print(23//4) # هنا العملية بعكس عملية باقي الفسمة هنا النتيجة تكون ناتج القسمة بدون باقي


# # --------------------------
# # ---------- List ----------
# # --------------------------
# [1] List Items Are Enclosed in Square Brakets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] Liste is Not Unique
# [5] List Can Have Different Data Types
#-----------------------------

# myAwesomeList = [ "one", "Two", 2, 4, True ]
# print(myAwesomeList)
# print(myAwesomeList[1]) # 2Item
# print(myAwesomeList[-1]) # last item

# print(myAwesomeList[1:4]) # Slice # End Donnot Included # ['Two', 2, 4]
# print(myAwesomeList[:4]) # ['one', 'Two', 2, 4] 
# print(myAwesomeList[0:]) # ['one', 'Two', 2, 4, True]
# print(type(myAwesomeList)) # <class 'list'>

# print(myAwesomeList[::2]) # ['one', 2, True]

# myAwesomeList[1] = 2    # second item equal thrid item 
# print(myAwesomeList) # ['one', 2, 2, 4, True]
# myAwesomeList[-1] = False
# print(myAwesomeList) # ['one', 2, 2, 4, False]

# myAwesomeList[0:2] = "omer", "memes"
# print(myAwesomeList) # ['omer', 'memes', 2, 4, False]

# myAwesomeList[0:3] = ["A", "B", "C"]
# print(myAwesomeList) # ['A', 'B', 'C', 4, False]

# myAwesomeList[0:3] = ["B"]
# print(myAwesomeList) # ['B', 4, False]

# # ----------------------------------
# # ---------- List Methods ----------
# # ----------------------------------

# # append() # Add Item الليستة الجديدة تضاف كعنصر واحد 


# myFriends = [ "omer", "ali", "Yusuf" ]
# myOldFriends = [ "Muhammed", "Mustafa", "Ahmed" ]
# myFriends.append("Musa")
# print(myFriends)  # ['omer', 'ali', 'Yusuf', 'Musa']

# myFriends.append(myOldFriends)
# print(myFriends)   # ['omer', 'ali', 'Yusuf', 'Musa', ['Muhammed', 'Mustafa', 'Ahmed']]
# print(myFriends[4]) # ['Muhammed', 'Mustafa', 'Ahmed']
# print(myFriends[4][2]) # Ahmed

# #extend() (تدمج) عناصر الليستة الجديدة تضاف لعناصر الليستة الأساسية 
# a = [ 1, 2, 3, 4 ]
# b = [ "one", "two", "three", "four" ]
# a.extend(b)
# print(a)  # [1, 2, 3, 4, 'one', 'two', 'three', 'four']

# c = [ "a", "b", "c", "d" ]
# e = [ "x", "y", "z", "w" ]
# a.extend(e)
# a.extend(c)
# print(a) # [1, 2, 3, 4, 'one', 'two', 'three', 'four', 'x', 'y', 'z', 'w', 'a', 'b', 'c', 'd']

# # remove() delete
# a.remove("a")
# a.remove("c")
# a.remove("x")
# a.remove("z")
# a.remove(1)
# print(a) # [2, 3, 4, 'one', 'two', 'three', 'four', 'y', 'w', 'b', 'd']

# # sort() عند استخدام هذه الدالة يجب أن تكون عناصر الليت من نوع واحد
# numbers = [ 1, 2, 5, 64, -2, -32, 4 ]
# numbers.sort()
# print(numbers) # [-32, -2, 1, 2, 4, 5, 64]

# numbers.sort(reverse=False) # [-32, -2, 1, 2, 4, 5, 64]
# print(numbers)

# numbers.sort(reverse=True) # [64, 5, 4, 2, 1, -2, -32]
# print(numbers)

# # revese()  الدالة لا تشترط بأن تكون عناصر الليست من نوع واحد
# z = [ 1, 2, 3, 4, 5, 6 ]
# z.reverse()
# print(z)  # [6, 5, 4, 3, 2, 1]

# strA = [ "a", "b", "c", "e"]
# strA.reverse()
# print(strA) # ['e', 'c', 'b', 'a']
# print(strA.reverse()) # None


# # clear()
# a = [ 1, 2, 3, 4 ]
# a.clear()
# print(a)  # []

# # copy() بعد نسخ الليست في ليست ثانية أي تعديل يطرؤ على الليست الاٍاسية لا يغير من الليست المنسوخ إليها
# b = [ 1, 2, 3, 4, 5, 6 ]
# c = b.copy()
# print(b) # [ 1, 2, 3, 4, 5, 6 ]
# print(c) # [ 1, 2, 3, 4, 5, 6 ]


# b.append(7)
# print(b) # [1, 2, 3, 4, 5, 6, 7]
# print(c) # [ 1, 2, 3, 4, 5, 6 ]


# # count  # Counter
# t = [ 1, 2, 3, 2, 3, 4, 2, 1, 3 ]
# print(t.count(1))
# g = t.count(2)
# print(g)

# # index   # access to item index
# n = [ "omer", "ali", "mustafa", "yusuf" ]
# h = n.index("omer")
# print(h)
# print(n.index("ali"))

# # insert     # add item  # have two argument # this function same append function
# j = [ 5, 6, 4, 6, 7 ]
# print(j)         # [ 5, 6, 4, 6, 7 ]
# j.insert(4, 6)   # [ 5, 6, 4, 6, 6, 7 ]
# print(j) 

# # pop()  # This function gets the index of the items
# names = [ "omer", "ali", "yusuf", "osama", "osman" ]
# print(names.pop("ali"))  error

# # ----------------------------------
# # ---------- List Methods ----------
# # ----------------------------------v
# 1 #  append() # Add Item الليستة الجديدة تضاف كعنصر واحد 
# 2 #  extend() (تدمج) عناصر الليستة الجديدة تضاف لعناصر الليستة الأساسية 
# 3 #  remove() delete
# 4 #  sort() عند استخدام هذه الدالة يجب أن تكون عناصر الليت من نوع واحد
# 5 #  revese()  الدالة لا تشترط بأن تكون عناصر الليست من نوع واحد
# 6 #  clear()
# 7 #  copy() بعد نسخ الليست في ليست ثانية أي تعديل يطرؤ على الليست الاٍاسية لا يغير من الليست المنسوخ إليها
# 8 #  count  # Counter
# 9 #  index   # access to item index
# 10 # insert     # add item  # have two argument # this function same append function
# 11 # pop()  # This function gets the index of the items
# # ----------------------------------


# -----------------------------
# ----------- Tuple -----------
# -----------------------------
# [1] Tuple Item Are Enclosed in Parantheses 
# [2] You Can Remove Parantheses If You Want
# [3] Tuple Are Order, To Use Index To Access Item
# [4] Tuple Are Immutable => You Can Add Or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] operators used in strings and lists available in tuples
# -----------------------------


# myAwesomeTupleOne = ("Omer", "Ali")
# myAwesomeTupleTwo =  "Omer", "Ali"
# print(type(myAwesomeTupleOne))  # <class 'tuple'>
# print(type(myAwesomeTupleTwo))  # <class 'tuple'>

# # Tuple Indexing
# myAwesomeTupleThree = ("ali", "omer", "Yusud")
# print(myAwesomeTupleThree[1])  # omer


# # Tuple Assign Value
# myAwesomeTupleFour = ( 1, 2, 3, 4, 5 )
# # myAwesomeTupleFour[2] = "Three" # غير قابلة للتغيير
# #### print(myAwesomeTupleFour) # tuple' object does not support item assignment


# # Tuple Item
# myAwesomeTupleFive = ( "omer", "ali", 32, 52, 1.3, True )
# print(myAwesomeTupleFive) # ('omer', 'ali', 32, 52, 1.3, True)
# print(myAwesomeTupleFive[-1]) # True
# print(myAwesomeTupleFive[1])  # ali


# #Tuple With One Element
# t1 = "omer"     # string
# t2 = ("ali")    # string
# t3 = ("musa",)    # tuple
# t4 = "Osama",   # tuple

# print(t1)
# print(t2)
# print(t3)
# print(t4)

# print(type(t1))
# print(type(t2))
# print(type(t3))
# print(type(t4))

# print(len(t1))  # 4
# print(len(t2))  # 3
# print(len(t3))  # 1
# print(len(t3))  # 1

# a = ( 1, 3, 5, 6 )
# b = ( 4, 6 )
# c = a + b  # (1, 3, 5, 6, 4, 6)
# h = b + a  # (4, 6, 1, 3, 5, 6)
# k = a + a  # (1, 3, 5, 6, 1, 3, 5, 6)
# l = 2*a    # (1, 3, 5, 6, 1, 3, 5, 6)
# x = a + b + ( "a", "b", "c" )
# print(c) # (1, 3, 5, 6, 4, 6)
# print(h) # (4, 6, 1, 3, 5, 6)
# print(k) # (1, 3, 5, 6, 1, 3, 5, 6)
# print(l) # (1, 3, 5, 6, 1, 3, 5, 6)
# print(x) # (1, 3, 5, 6, 4, 6, 'a', 'b', 'c')


# # Tuple, List, String Reoeat (*)

# myString = "omer "
# myList = [1,2]
# myTuple = ("A","B")

# print(myString*3)   # omer omer omer
# print(myList*3)     # [1, 2, 1, 2, 1, 2]
# print(myTuple*3)    # ('A', 'B', 'A', 'B', 'A', 'B')

# # Method -> count()
# a = ( 3, 5, 5, 6, 3, 2, 4, 5, 6, 7, 5 )
# print(a.count(5))  # 4

# # Method -> index()
# a = ( 3, 5, 5, 6, 3, 2, 4, 5, 6, 7, 5 )
# # print("The position of index is : " + a.index(7)) # Error
# print("The position of index is : {}".format(a.index(7))) # The position of index is : 9
# print(f"The position of index is : {a.index(7)}") # The position of index is : 9


# # Tuple Destruct 
# a = ( "A", "B", "C" )
# x, y, z = "A", "B", "C"
# print(x)    # A
# print(y)    # B
# print(z)    # C


# a = ( "A", "B", "C" )
# x, y, z = a
# print(x) # A
# print(y) # B
# print(z) # C




# -----------------------------
# ----------- Set -------------
# -----------------------------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Not Order And Not Indexed
# [3] Set indexing and Slicing Cannot Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------


# #  Set Items Not Order And Not Indexed غير مرتبة فهذا يعني بأننا لن نستطيع الوصول للعنصر محدد مباشرة
# mySetOne = { "omer", "ali", "yusuf", 100 }
# print(mySetOne) # {'yusuf', 'ali', 'omer', 100} في كل مرة يختلف الترتيب
# # print(mySetOne[1]) # Error
# # Sliceing Connot Be Done print(mySetOne[0:5])
# # Set Has Only Immutable Data Types
# # mySetTwo = { "omer", 2, 103.5, [4, 3, 5] } #Error
# # print(mySetTwo)

# mySetThree = { "omer", 2, 103.5, ("omer", 4) } # {'omer', 2, ('omer', 4), 103.5}
# print(mySetThree)

# # Set Items Is Unique تطبع بدون تكرار
# mySetFour = { 3, 2, "omer", "ali", 3, "yusuf", 2, "omer" }
# print(mySetFour) # {2, 3, 'yusuf', 'omer', 'ali'} 


# # -------------------------------------
# # ----------- Set Methods -------------
# # -------------------------------------

# # clear()
# a = {1, 3, 5}
# a.clear()
# print(a) # set()

# # union اتحاد
# b = {"one", "two", "three"}
# c = {"1", "2", "3"}
# print(c|b) # {'three', '3', '1', '2', 'two', 'one'}
# d = { "ali", 4, "A", 6.7 }
# print(c.union(d), b) # {'1', 'ali', '3', 4, '2', 6.7, 'A'} {'two', 'three', 'one'}
# print(c.union(d, b)) # {'2', 4, 6.7, 'two', 'ali', 'one', 'A', '1', '3', 'three'}


# # add()     # Add() function it takes only one argument
# e = { 2, 3, 4, 2, 5, 6 }
# e.add(7)
# print(e) # {2, 3, 4, 5, 6, 7}
# e.add(2) 
# print(e) # {2, 3, 4, 5, 6, 7}


# # copy()
# f = { 3, 5, 6, 7, 8 }
# g = f.copy()
# print(f) # {3, 5, 6, 7, 8}
# print(g) # {3, 5, 6, 7, 8}
# f.add(1)
# print(f) # {1, 3, 5, 6, 7, 8}
# print(g) # {3, 5, 6, 7, 8}

# # remove()
# h = { "omer", "ali", "yusuf" }
# h.remove("omer")
# print(h) # {'ali', 'yusuf'}
# # # print(h.remove("ali")) # None

# # h.remove("mustafa") # ERROR



# # discard() # لا تعطي خطأ بحال كان العنصر غير موجود وتم طلب حذف على عكس الريموف
# i = { "omer", "ali", "yusuf" }
# i.discard("Mustaf") # لا تعطي خطأ بحال كان العنصر غير موجود وتم طلب حذف

# # pop()  # this function is removes a random element from a set
# j = { 1, 2, 3, 4, 5, 6, 7, 8 }
# j.pop()
# print(j) # {2, 3, 4, 5, 6, 7, 8}
# print(j.pop()) # 2

# # update()
# k = { 1, 2, 3, 4 }
# l = { 1, 2, "A", "B", 5, 2 }
# k.update(l)
# print(k) # {1, 2, 3, 4, 'B', 5, 'A'}

# k.update(["a", "b", "c" ])
# print(k) # {1, 2, 3, 4, 5, 'b', 'c', 'B', 'a', 'A'}


# # difference()
# m = { "a", "b", "c", 3, 2, 1 }
# n = { 1, 3, "a", "B", "c" }
# m.difference(n)
# print(m) # { "a", "b", "c", 3, 2, 1 }
# print(m.difference(n)) # {'b', 2} difference_update() هذا هو الفرق بين هذه الدالة ودالة 
# print(m-n)  # {'b', 2}


# # difference_update()
# o = { "a", "b", "c", 3, 2, 1 }
# p = { 1, 3, "a", "B", "c" }
# o.difference_update(p)
# print(o) # {'b', 2}

# # intersection() sets الأولى والعناصر المشتركة بين كلا الـ set عناصر الـ
# s = { "a", "b", "c", 3, 2, 1 }
# t = { 1, 3, "a", "B", "c" }
# s.intersection_update(t)
# print(s)    # {'c', 1, 3, 'a'}

# # symmetric_difference() فرق الاثنين
# v = { "a", "b", "c", 3, 2, 1 }
# w = { 1, 3, "a", "B", "c" }
# print(v.symmetric_difference(w)) # {2, 'B', 'b'}

# # symmetric_difference_update() فرق الاثنين
# x = { "a", "b", "c", 3, 2, 1 }
# z = { 1, 3, "a", "B", "c" }
# print(x.symmetric_difference(z))    # {'b', 'B', 2}


# # issuperset()
# a = { 1, 2, 3, 4 }
# b = { 1, 3, 2 }
# c = { 1, 2, 3, 4, 5 }
# print(a.issuperset(b)) # true
# print(a.issuperset(c)) # flase


# # issubset() ------> issuperset()  عكس
# a = { 1, 2, 3, 4 }
# b = { 1, 3, 2 }
# c = { 1, 2, 3, 4, 5 }
# print(a.issubset(b)) # false
# print(a.issubset(c)) # true


# # isdisjoint() ------> مختلفين 
# a = { 1, 2, 3, 4 }
# b = { 1, 3, 2 }
# c = { 6, 7, 8, 9, 5 }
# print(a.isdisjoint(b)) # false
# print(a.isdisjoint(c)) # true

# # -------------------------------------
# # ----------- Set Methods -------------
# # -------------------------------------
# 1 #   clear()
# 2 #   union اتحاد
# 3 #   add()     # Add() function it takes only one argument
# 4 #   copy()
# 5 #   remove()
# 6 #   discard() # لا تعطي خطأ بحال كان العنصر غير موجود وتم طلب حذف على عكس الريموف
# 7 #   pop()  # this function is removes a random element from a set
# 8 #   update()
# 9 #   difference()
# 10 #  difference_update()
# 11 #  intersection() sets الأولى والعناصر المشتركة بين كلا الـ set عناصر الـ
# 12 #  symmetric_difference() فرق الاثنين
# 13 #  symmetric_difference_update() فرق الاثنين
# 14 #  issuperset()
# 15 #  issubset() ------> issuperset()  عكس
# 16 #  isdisjoint() ------> مختلفين 
# # -------------------------------------


# # ------------------------------------
# # ----------- Dictionary -------------
# # ------------------------------------
# [1] Dict items are enclosed in curly braces
# [2] Dict items are contains key : value
# [3] Dict key need to be immutable -> (number, string, tuple) List not allowed
# [4] Dict value can have any data types
# [5] Dict key need to be unique
# [6] Dict is not ordered you access its element with key
# # ------------------------------------

# # user = {
#     "Name Surname" : "Omer MEMES",
#     "age" : 22,
#     "country" : "Syria",
#     "skills" : ["C", "C++", "C#", "Python" ],
#     "rating" : 9.5,
# }
# print(user)
# print(user.values())    # dict_values(['Omer MEMES', 22, 'Syria', ['C', 'C++', 'C#', 'Python'], 9.5])
# print(user.keys())      # dict_keys(['Name Surname', 'age', 'country', 'skills', 'rating'])
# print(user["country"])  # syria
# print(user['rating'])   # 9.5
# print(user.get("age"))  # 22


# # Two_Dimensional_Dictionary

# languages = {
#     "One" : {
#         "name" : "C",
#         "progress" : "60%"
#     },
#     "Two" : {
#         "name" : "C++",
#         "progress" : "70%"
#     },
#     "Three" : {
#         "name" : "C#",
#         "progress" : "30%"
#     },
#     "Four" : {
#         "name" : "python",
#         "progress" : "20%"
#     },
# }
# print(languages)
# print(languages['One'])
# print(languages.get("Three"))
# print(languages['One']['progress']) # %60

# print(len(languages)) # 4
# print(len(languages["Two"])) # 2

# print("-"*50)

# languageOne = {
#     "name" : "C",
#     "progress" : "70%"
# }
# languageTwo = {
#     "name" : "C++",
#     "progress" : "70%"
# }
# languageThree = {
#     "name" : "python",
#     "progress" : "20%"
# }
# LANGUAGE = {
#     "ONE" : languageOne,
#     "TWO" : languageTwo,
#     "THREE" : languageThree,
# }
# print(LANGUAGE)


# # --------------------------------------------
# # ----------- Dictionary Methods -------------
# # --------------------------------------------

# # # clear()
# from turtle import update


# languages = {
#     "One" : {
#         "name" : "C",
#         "progress" : "60%"
#     },
#     "Two" : {
#         "name" : "C++",
#         "progress" : "70%"
#     },
#     "Three" : {
#         "name" : "C#",
#         "progress" : "30%"
#     },
#     "Four" : {
#         "name" : "python",
#         "progress" : "20%"
#     },
# }
# print(languages)
# languages.clear()
# print(languages)    # {}

# # # update()
# person = {
#     "one" : {
#         "name" : "omer",
#         "surname" : "memes"
#     },
#     "two" : {
#         "name" : "ali",
#         "surname" : "memes"
#     },
# }
# person["one"]["age"] = 22
# person["two"]["age"] = 14
# print(person) 

# omer = {
#     "age" : 22,
#     "country" : "syria",
# }
# print(omer) # {'age': 22, 'country': 'syria'}
# omer.update({"city" : "idlib"})
# print(omer) # {'age': 22, 'country': 'syria', 'city': 'idlib'}

# # # copy()
# omer = {
#     "age" : 22,
#     "country" : "syria",
# }
# memes = omer.copy()
# print(omer)    # {'age': 22, 'country': 'syria'}
# omer.update({"city" : "hatay"})
# print(omer)     # {'age': 22, 'country': 'syria', 'city': 'hatay'}
# print(memes)    # {'age': 22, 'country': 'syria'}

# print(omer.keys())
# print(omer.values())

# # setdefault() تستخدم للإضافة أيضا اذا كان المفتاح المضاف موجود فترجع قيمته وإن كان غير مضاف تضيف العنصر المراد إضافته
# omer = {
#     "age" : 22,
#     "country" : "syria",
# }
# print(omer)
# print(omer.setdefault("name" , "omer"))
# print(omer.setdefault("age" , 21)) # سترجع قيمة العمر لأنه موجود ولن تضيف هذا العنصر
# print(omer)

# # # popitem() يرجع آخر عنصر تمت إضافته
# omer = {
#     "age" : 22,
#     "country" : "syria"
# }
# omer["neme"] = "omer"
# omer["skills"] = "c++"
# omer.update({"rating":10})  # ('rating', 10)
# print(omer.popitem())

# # # items() يحتفظ بكل الحدود حتى ولو قمنا بالتعديل على القاموس
# omer = {
#     "age" : 22,
#     "country" : "syria"
# }
# allItems = omer.items()
# omer["name"] = "omer"
# # omer["name"] = "memes" عند تكرار إضافة العنصر نفسه سيضيف الأخير فقط
# omer["rating"] = 10
# print(allItems) # dict_items([('age', 22), ('country', 'syria'), ('name', 'omer'), ('rating', 10)])

# # # fromkeys() # dict.fromkeys()
# names = {"omer", "ali", "osman", "yusuf"}   # we can used this
# names = ("omer", "ali", "osman", "yusuf")   # we can used this
# names = ["omer", "ali", "osman", "yusuf"]   # we can used this
# memesFamily = 'memes'
# print(dict.fromkeys(names, memesFamily)) # {'omer': 'memes', 'ali': 'memes', 'osman': 'memes', 'yusuf': 'memes'}


# # --------------------------------------------
# # ----------- Dictionary Methods -------------
# # --------------------------------------------
# 1 # clear()
# 2 # update() # person["one"]["age"] = 22
# 3 # copy()
# 4 setdefault() تستخدم للإضافة أيضا اذا كان المفتاح المضاف موجود فترجع قيمته وإن كان غير مضاف تضيف العنصر المراد إضافته
# 5 # popitem() يرجع آخر عنصر تمت إضافته
# 6 # items() يحتفظ بكل الحدود حتى ولو قمنا بالتعديل على القاموس
# 7 # fromkeys() # dict.fromkeys()
# # --------------------------------------------



# # ---------------------------------
# # ----------- Boolean -------------
# # ---------------------------------
# [1] I programming You Nee to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are the Two Constant Objects False + True
# # ---------------------------------
# name = ""
# space = " "
# print(name.isspace)     # false
# print(space.isspace())  # true

# print(7>3) # true 
# print(56>78) # false 




# print("-"*50)

# # True Values
# print(bool("omer"))# true
# print(bool(100)) # true
# print(bool(10.5)) # true
# print(bool(["omer", "ali"])) # true
# print(bool((1, 3, 6, "a"))) # true
# print(bool({"omer", "memes", 3})) # true
# print(bool(True)) # true

# print("-"*50)

# # False Values
# print(bool("")) # false
# print(bool('')) # false
# print(bool(0)) # false
# print(bool(0.0)) # false
# print(bool([])) # false
# print(bool(())) # false
# print(bool({})) # false
# print(bool(None)) # false
# print(bool(False)) # false


# # # -------------------------------------------
# # # ----------- Boolean Operators -------------
# # # -------------------------------------------
# # [1] and
# # [2] or
# # [3] not
# # # -------------------------------------------

# name = "omer"
# age = 22
# country = "syria"

# print(age==22 and country == "syria" and name == "omer" )   # true

# print(age==22 and country == "turkey" and name == "omer" )  # flase

# print(age==22 and country == "turkey" or name == "omer" )  # true

# print(age==22 or country == "turkey" and name == "omer" )  # true

# print(age>20 or country == "turkey" and name == "omer" )  # true

# print(age>20 and country == "turkey" and name == "omer" )  # false


# x = 20
# y = 55
# z = 40
# print(x>19 or y<50 and z==40) # True
# print(x>19 and y<50 and z==40) # False
# print(x>19 and y<50 and z==40) # False
# print(not x>20) # True


# # # ----------------------------------------------
# # # ----------- Assignment Operators -------------
# # # ----------------------------------------------
# # # =
# # # +=
# # # -=
# # # *=
# # # /=
# # # **=
# # # %=
# # # //=
# # # ----------------------------------------------

# print(21+5)  # 26
# print(21-5)  # 16
# print(21*5)  # 105
# print(21/5)  # 4.2
# print(21//5) # 4
# print(21%5)  # 1
# print(2**5)  # 32
# x=5
# z=x
# print(z)     # 5


# # # ----------------------------------------------
# # # ----------- Comparison Operators -------------
# # # ----------------------------------------------
# # # [1] [==] Equal
# # # [2] [!=] Not Equal
# # # [3] [>]  Greater Than
# # # [4] [<]  Less Than
# # # [5] [>=] Greater or Equal
# # # [6] [<=] Less or Equal
# # # ----------------------------------------------

# print(10==10)   # True
# print(10!=10)   # False
# print(10!=13)   # True
# print(10>13)    # False 
# print(15>13)    # True
# print(15<13)    # False
# print(11<13)    # True 
# print(11>=11)    # True 
# print(11>=12)    # False 
# print(11<=12)    # True 
# print(11<=10)    # False 




# # # -----------------------------------------
# # # ----------- Type Conversion -------------
# # # -----------------------------------------

# # str()
# a = 10
# print(type(a))      # <class 'int'>
# print(type(str(a))) # <class 'str'>


# # # tuple() 
# a = "omer"
# b = { 1, 2, "a", "b" }
# c = [ "A", "B", 4, 3 ]
# d = ( "o", "m", 2, True)
# e = { "A":1, "B":2 }
# print(tuple(a)) # ('o', 'm', 'e', 'r')
# print(tuple(b)) # ('a', 2, 'b', 1)
# print(tuple(c)) # ('A', 'B', 4, 3)
# print(tuple(e)) # ('A', 'B')
# # print(tuple(500)) # ERROR

# # # set()
# print(set(a))   # {'m', 'e', 'o', 'r'} 
# print(set(c))   # {3, 'B', 4, 'A'}
# print(set(d))   # {'m', 2, 'o', True}
# print(set(e))   # {'B', 'A'}
# # print(set(500))  # ERROR


# # # list()
# print(list(a))   # ['m', 'e', 'o', 'r']
# print(list(b))   # ['a', 1, 2, 'b']
# print(list(d))   # ['m', 2, 'o', True]
# print(list(e))   # ['B', 'A']
# # print(set(500))  # ERROR

# # # dict()    set() و string غير فعال في هذه الخطائص للـ
# a = ( (3, 1), ("B", 2), ("C", 3) )    
# b = [ [3, 1], ["B", 2], ["C", 3] ]    
# # c = { {3, 1}, {"B", 2}, {"C", 3} }    
# print(dict(a))  # {3: 1, 'B': 2, 'C': 3}
# print(dict(b))  # {3: 1, 'B': 2, 'C': 3}
# # print(dict(c))  # ERROR


# # # ------------------------------------
# # # ----------- User Input -------------
# # # ------------------------------------

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# age = input("Enter your age: ")
# skills = input("Enter your skills: ")
# print(name)
# print(surname)
# print(skills)
# print(age)

# print(f"Hello {name} {surname} your skills is {skills} and your age {age} ") # Hello    omer     memes your skills is C++ and your age 22
# print("Hello {} {} your skills is {} and your age {} ".format(name, surname, skills, age)) # Hello    omer     memes your skills is C++ and your age 22
# # # We used the strip() function because if the user enters a space before its value, this function deletes the added spaces
# print(f"Hello {name.strip()} {surname.strip()} your skills is {skills.strip()} and your age {age.strip()} ")  #Hello omer memes your skills is C++ and your age 22

# name = name.strip().capitalize()
# surname = surname.strip().capitalize()
# age = age.strip().capitalize()
# skills = skills.strip().capitalize()

# # # values entered like this
# # OMER MEMES 22 PYTHON 
# print(f"Hello {name} {surname} your skills is {skills} and your age {age} ") # Hello Omer Memes your skills is C++ and your age 22 


# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# # # # values entered like this
# # # omer memes
# print(f"Hello {name.strip().capitalize()} {surname.capitalize().strip()}") # Hello Omer Memes



# # # -----------------------------------------------
# # # ----------- Practical Slice Email -------------
# # # -----------------------------------------------

# # email = "oms_memes@gmail.com"
# # print(email[:9]) # للسهولة نستخدم الطريقة الثانية
# # print(email[:email.index('@')])

# from operator import index


# name = input("What's your name: ").strip().capitalize()
# email = input("Wath's your email: ").strip()

# userName = email[:email.index("@")]
# webSite = email[email.index("@")+1:]
# print(f"Hello {name} your email is {email} ") # Hello omer your email is oms83@gmail.com 
# print(f"Your username is {userName} \nyour website is {webSite}") #Your username is oms83 and your website is gmail.com


# # # ---------------------------------------------------------
# # # ----------- Practical Your Age Full Details -------------
# # # ---------------------------------------------------------


# # age = int(input("what\'s your age : ").strip())
# # print(type(age))    # <class 'int'>

# # age = input("what\'s your age : ").strip()
# # print(type(int(age)))   # <class 'int'>

# age = int(input("What\'s your age: ").strip())
# months = age*12
# weeks = months*4
# days = age*365
# hours = days*24
# minutes = hours*60
# seconds = minutes*60
# print("Your Live For: ")
# print(f"{months} Months.")
# print(f"{weeks} Weeks.")
# print(f"{days} Days.")
# print(f"{hours:,} Hours.")
# print(f"{minutes:,} Minutes.")
# print(f"{seconds:,} Seconds.")


# # # ----------------------------------------
# # # -----------  Control Flow  -------------
# # # ----------- if, elif, else -------------
# # # ----------- Make Decisions -------------
# # # ----------------------------------------

# uName = "Omer"
# cName = "C++"
# cPrice = 100
# cDiscount = 30
# print(f"Hello {uName} The Course \"{cName}\" Price is: {cPrice-cDiscount}") # Hello Omer The Course "C++" Price is: 70

# uName = input("Enter your name: ").strip().capitalize()
# uCountry = int(input("For Syria(1) \nFor Turkey(2) \nFor Egypt(3) \nFor kuwait(4) \nFor Qatar(5) \nFor somali(6) \nChoose your country:: "))
# cName = "C++"
# cPrice = 100
# country = {
#     1: "Syria",
#     2: "Turkey",
#     3: "Egypt",
#     4: "kuwait",
#     5: "Qatar",
#     7: "Somali",
# }
# if uCountry==1:
#     print(f"Hello {uName} In The \"{cName}\"")
#     print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-60}")
# elif uCountry==2:
#     print(f"Hello {uName} In The \"{cName}\"")
#     print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-40}")
# elif uCountry==3:
#     print(f"Hello {uName} In The \"{cName}\"")
#     print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-60}")
# elif uCountry==4:
#     print(f"Hello {uName} In The \"{cName}\"")
#     print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-10}")
# elif uCountry==5:
#     print(f"Hello {uName} In The \"{cName}\"")
#     print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-10}")
# elif uCountry==6:
#     print(f"Hello {uName} In The \"{cName}\"")
#     print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-80}")
# else:
#     print(f"{uName.capitalize()} since your country is not found, you cannot access the course")


# # # -------------------------------------
# # # -----------  Nested If  -------------
# # # -------------------------------------

# uName = input("Enter your name: ").strip().capitalize()
# uCountry = int(input("For Syria(1) \nFor Turkey(2) \nFor Egypt(3) \nFor kuwait(4) \nFor Qatar(5) \nFor somali(6) \nChoose your country:: "))
# is_student = int(input("Are your student (1, yes) (0, no): ").strip())
# cName = "C++"
# cPrice = 100
# country = {
#     1: "Syria",
#     2: "Turkey",
#     3: "Egypt",
#     4: "kuwait",
#     5: "Qatar",
#     6: "Somali",
# }

# if uCountry==1:
#     if is_student == 1:  
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-50}")
#     elif is_student == 0:
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-700}")

# elif uCountry==2:
#     if is_student == 1:  
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[2]}, The Course Price is: {cPrice-60}")
#     elif is_student == 0:
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[2]}, The Course Price is: {cPrice-70}")

# elif uCountry==3:
#     if is_student == 1:  
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[3]}, The Course Price is: {cPrice-60}")
#     elif is_student == 0:
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[3]}, The Course Price is: {cPrice-50}")

# elif uCountry==4:
#     if is_student == 1:  
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[4]}, The Course Price is: {cPrice-10}")
#     elif is_student == 0:
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[4]}, The Course Price is: {cPrice}")

# elif uCountry==5:
#     if is_student == 1:
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[5]}, The Course Price is: {cPrice-10}")
#     elif is_student == 0:
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[5]}, The Course Price is: {cPrice}")

# elif uCountry==6:
#     if is_student == 1: 
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[6]}, The Course Price is: {cPrice-70}")
#     elif is_student == 0:
#         print(f"Hello {uName} In The \"{cName}\"")
#         print(f"Because You Are From {country[6]}, The Course Price is: {cPrice-50}")
# else:
#     print(f"{uName.capitalize()} since your country is not found, you cannot access the course")



# # # --------------------------------------------------------
# # # -----------  Ternary Conditional Operator  -------------
# # # --------------------------------------------------------
# omerName = input("Omer enter your name :) ").strip().capitalize()
# aliName = input("Ali enter your name :) ").strip().capitalize()
# omerAge = int(input("Omer, enter your age: ").strip())
# aliAge = int(input("Ali, enter your age: ").strip())
# print(f"{omerAge} greater than {aliName}" if omerAge>aliAge else f"{aliName} greater than {omerName}")


# # # ---------------------------------------------------------------
# # # -----------  Calculate Age Advanced and Training  -------------
# # # ---------------------------------------------------------------

# # Write Note
# print("#"*70)
# print(" You Can Write First Letter Or Full Name of The Time Unit.. ".center(70,"#"))
# print("#"*70)

# # Collect Age Data
# age = input("Please write your age: ").strip()
# # Collect Time Unit Data
# unit = input("Please Choose Time Unite: Months, Weeks, Days: ").strip().lower()
# # Get Time Units
# months = int(age)*12
# weeks = int(months)*4
# days = int(age)*365

# if unit == 'months' or unit == 'm':
#         print("You Choosed The Unit Months.")
#         print(f"You Lived {months:,} Months.")

# elif unit == 'weeks' or unit == 'w':
#         print("You Choosed The Unit Weeks.")
#         print(f"You Lived {weeks:,} Weeks.")

# elif unit == 'days' or unit == 'd':
#         print("You Choosed The Unit Days.")
#         print(f"You Lived {days:,} Days.")



# # # ------------------------------------------------
# # # -----------  Membership Operators  -------------
# # # ------------------------------------------------
# # # in
# # # not in
# # # ------------------------------------------------

# name = "omer"
# print("m" in name) # True
# print('r' in name) # True
# print('q' in name) # False

# friends = ["omer", "ali", "yusuf"]
# print("omer" in friends) # True
# print("omer" not in friends) # False
# print("musa" not in friends) # True

# print("#"*70)

# countryOne = ["Syria", "Turkey", "Jordan", "Egypt"]
# countryOneDiscount = 50

# countryTwo = ["Kuwait", "Bahrain", "Qatar", "Ksa"]
# countryTwoDiscount = 30

# myCountry = input("Enter your country: ").capitalize().strip()

# if myCountry in countryTwo:
#     print(f"Hello you have a discount equal to ${countryTwoDiscount}")
# elif myCountry in countryOne:
#     print(f"Hello you have a discount equal to ${countryOneDiscount}")
# else:
#     print("You have not discount")

 

# # # --------------------------------------------------------
# # # -----------  Practical Membership Control  -------------
# # # --------------------------------------------------------
# from operator import index


# admins = [ "omer", "ali", "yusuf", "osama", "osman", "musa" ]
# name = input("Enter your name: ").strip().lower()

# if name in admins:

#     print(f"Hello {name} Welcome Back")
#     option = input("Delete Or Update Your Name ? ").strip().capitalize()
    
#     if option == "Update" or option == "update":
#         print(f"You Choosed {option}")
#         theNewName = input("Your New Name : ").strip().capitalize()
#         admins[admins.index(name)] = theNewName
#         print(admins)

#     elif option == "Delete" or option == "delete":
#         print(f"You Choosed {option}")
#         admins.remove(name)
#         print("Name Deleted")
#         print(admins)
#     else:
#         print("Worng Option Choosed")

# else:
#     status = input("Not Admin, Add You (yes or no) ? ").strip().lower()
#     if status == "yes" or status == "Yes" or status == "y":
#         admins.append(name)
#         print(admins)
#     else:
#         print("You Are Not Added..")




# # # --------------------------
# # # ---------- List ----------
# # # --------------------------
# # [1] List Items Are Enclosed in Square Brakets
# # [2] List Are Ordered, To Use Index To Access Item
# # [3] List Are Mutable => Add, Delete, Edit
# # [4] Liste is Not Unique
# # [5] List Can Have Different Data Types
# #-----------------------------


# # -----------------------------
# # ----------- Tuple -----------
# # -----------------------------
# # [1] Tuple Item Are Enclosed in Parantheses 
# # [2] You Can Remove Parantheses If You Want
# # [3] Tuple Are Order, To Use Index To Access Item
# # [4] Tuple Are Immutable => You Can Add Or Delete
# # [5] Tuple Items Is Not Unique
# # [6] Tuple Can Have Different Data Types
# # [7] 
# # -----------------------------


# # -----------------------------
# # ----------- Set -------------
# # -----------------------------
# # [1] Set Items Are Enclosed in Curly Braces
# # [2] Set Items Not Order And Not Indexed
# # [3] Set indexing and Slicing Cannot Be Done
# # [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# # [5] Set Items Is Unique
# # -----------------------------

# # # ------------------------------------
# # # ----------- Dictionary -------------
# # # ------------------------------------
# # [1] Dict items are enclosed in curly braces
# # [2] Dict items are contains key : value
# # [3] Dict key need to be immutable -> (number, string, tuple) List not allowed
# # [4] Dict value can have any data types
# # [5] Dict key need to be unique
# # [6] Dict is not ordered you access its element with key
# # # ------------------------------------

 
# # # -----------------------
# # # ----- While Loop  -----
# # # -----------------------

# myList = [ 1, 2, 3, 4, 5, 6, 7 ]
# mySet = { 1, 2, 3, 4, 5, 6, 7 }
# myTuple = ( 1, 2, 3, 4, 5, 6, 7 )

# i=0
# print("*"*70)
# while i<len(myList):
#     print(myList[i])
#     i+=1
# print("*"*70)

# i=0
# print("*"*70)
# while i<len(myTuple):
#     print(myTuple[i])
#     i+=1
# print("*"*70)

# # i=0 -------------- >> Error Not Indexed
# # print("*"*70)
# # while i<len(mySet):
# #     print(mySet[i])
# #     i+=1
# # print("*"*70)
# my_list = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ]
# i=0
# while i<len(my_list):
#     print(f"#{str(i+1).zfill(2)} {my_list[i]}")
#     i+=1

# myFavouritWebs = []
# maximumWebs = 5
# while maximumWebs>0:
#     web = input("WebSite Name Without https:// ")
#     myFavouritWebs.append(f"https://{web.strip().lower()}")
#     maximumWebs-=1
#     print(f"WebSite Added, {maximumWebs} Places Left" )
#     print(myFavouritWebs)
# else:
#     print("Bookmark is Full, You Cannot Add More")

# if len(myFavouritWebs) > 0:
#     myFavouritWebs.sort()
#     index=0
#     print("Printing The List Of WebSite in Your Bookmark")
#     while index < len(myFavouritWebs):
#         print(myFavouritWebs[index])
#         index+=1


# # # ----------------------------------
# # # ----- Loop => While Training -----
# # # ----- Simple Password Guess  -----
# # # ----------------------------------

# tries = 4
# mainPassword = "oms321"
# inputPassword = input("Write Your Password: ")+
# while inputPassword != mainPassword:
#     tries-=1
#     print(f"Wrong Password, {'Last' if tries==0 else tries} Chance Left")
#     inputPassword = input("Write Your Password: ")

#     if tries == 0:
#         print("All Tries is Finished.")
#         break
# else: 
# # else فإننا في حال أدخلنا كلمة المرور بشكل صحيح فسيدحل إلى الـ else عند استخدام الـ
# # "All Tries is Finished." ولو أدخلنا كل الحالات بشكل خاطئ فآخر شيء سيتم طباعته هو
#     print("Corrent Password")

# # "Corrent Password" و "All Tries is Finished." وأدخلنا كل المحاولات يشكل خاطئ فسيطبع آخر شيء else ولكن لو أننا لم نستخدم الـ
# # "Corrent Password" ولو أننا أدخل كلمة المرور بشكل صحيح فسيطبع فقط


# ------------------
# ---- for loop ----
# ------------------
# for item int iterable_object:
# do something with item
# ------------------
# item is a vairable you create an call when ever you want
# item refer to the current position and will run ad visit all items to the end
# iterable_object => sequence [list, tuple, dict, set, string if characters, etc ...]
# ------------------


# myNumber = [ 1, 3, 4, 5, 6, 8 ]
# for i in myNumber:
#     if i%2 == 0:
#         print("Even")
#     else: 
#         print("Odd")
# else:
#     print("Loop is finished")

# myName = "omer"
# for letter in myName:
#     print(letter)


# myName = "omer"
# for letter in myName:
#     print(f"[{letter.upper()}]")

# myRange = range(1, 21)
# for number in myRange:
#     print(number)

# # Range
# mySkills = {
#     "C" : "70%",
#     "C++" : "80%",
#     "C#" : "50%",
#     "Python" : "60%",
#     "HTML" : "40%",
# }

# for skill in mySkills:
#     print(skill)


# for skill in mySkills:
#     print(f"My progress in lang {skill} is: {mySkills[skill]}")


# for skill in mySkills:
#     print(f"My progress in lang {skill} is: {mySkills.get(skill)}")


# # Nested loop

# peoples = [ "omer", "musa", "ali", "yusuf" ]
# skills = [ "C++", "C", "C#", "Python" ]

# for name in peoples:
    
#     print(f"{name} skills is: ")

#     for skill in skills:
#         print(skill)



# peoples = {
#     "Omer" : {
#         "C"      : "80%",
#         "C++"    : "90%",
#         "C#"     : "50%",
#         "Python" : "60%",
#         "HTML"   : "40%",
#     },
#     "Ali" : {
#         "C"      : "60%",
#         "C++"    : "80%",
#         "C#"     : "40%",
#         "Python" : "50%",
#         "HTML"   : "40%",
#     },
#     "Yusuf" : {
#         "C"      : "70%",
#         "C++"    : "80%",
#         "C#"     : "50%",
#         "Python" : "60%",
#         "HTML"   : "40%",
#     },
# }

# # print(peoples["Omer"]["C"])
# # print(peoples.get("Omer"))
# for name in peoples:
#     print(f"Skills and progress for {name} is: {peoples[name]} ")


# for name in peoples:
#     print(f"Skills and progress for {name} is: ")
#     for skill in  peoples[name]:
#         print(f"{skill} => {peoples[name][skill]}")

# myNumber = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# for number in myNumber:
#     if number == 4:
#         continue
#     print(number)

# for number in myNumber:
#     if number == 4:
#         break
#     print(number)

# for number in myNumber:
#     for number in myNumber:
#         if number%2==0:
#             continue
#         print(number)

# pass تتفادى الأخطاء
# for number in myNumber:
#     pass
# print(myNumber)

# ----------------------------------------
# ------- Advanced Dictionary Loop -------
# ----------------------------------------

# mySkills = {
#     "C" : "70%",
#     "C++" : "80%",
#     "C#" : "50%",
#     "Python" : "60%",
#     "HTML" : "40%",
# }

# print(mySkills.items())

# for skill in mySkills:
#     print(f"{skill} => {mySkills[skill]}")

# for skill, progress in mySkills.items():
#     print(f"{skill} => {progress}")


# peoples = {
#     "Omer" : {
#         "C"      : "80%",
#         "C++"    : "90%",
#         "C#"     : "50%",
#         "Python" : "60%",
#         "HTML"   : "40%",
#     },
#     "Ali" : {
#         "C"      : "60%",
#         "C++"    : "80%",
#         "C#"     : "40%",
#         "Python" : "50%",
#         "HTML"   : "40%",
#     },
#     "Yusuf" : {
#         "C"      : "70%",
#         "C++"    : "80%",
#         "C#"     : "50%",
#         "Python" : "60%",
#         "HTML"   : "40%",
#     },
# }
# for name, skill in peoples.items():
#     print(f"Skills and progress for {name} is:")
#     for lang, prog in skill.items():
#         print(f"language {lang} progress {prog} ")



# -----------------------------------
# ------- Function And Return -------
# -----------------------------------   
# [1] a function is a reusable block of code do a task
# [2] a function run when you call it
# [3] a function accept elemnet to deal with called [parameters]
# [4] a function can do the task without returning date
# [5] a function can return data after job is finished
# [6] a function create to prevent DRY
# [7] a function accept elemnts when you call it called [arguments]
# [8] There's a Built_in functions and user defined functions
# [9] a function is for all team and all apps
# -----------------------------------   

# def name():
#     print("Your name is omer ")
# name()

# summation=0
# def sum():
#     number1 = int(input("Enter your number: "))
#     number2 = int(input("Enter your number: "))
#     summation = number1 + number2
#     print(f"Summation is : {summation}")
# sum()

# summation=0
# number1 = int(input("Enter your number: "))
# number2 = int(input("Enter your number: "))
# def sum(number1, number2):
#     summation = number1 + number2
#     return summation
# print(f"Summation is: {sum(number1, number2)}")
    
# a, b, c = "omer", "ali", "yusuf"
# def names(a,b,c):
#     print(f"Hello {a}")
#     print(f"Hello {b}")
#     print(f"Hello {c}")
# names(a,b,c)


# def names(name):
#     print(f"Hello {name}")

# names("omer")
# names("ali")

# def sum(n1, n2):
#     print(n1+n2)
# sum(8,8)


# def sum(n1, n2):
#     if type(n1) != int or type(n2) != int:
#         print("only integers allowed")
#     else:
#         print(n1+n2)

# sum(8,"omer")

# def full_name(first, middle, last):
#     print(first+" "+middle+" "+last)
#     print(f"Hello {first.strip().capitalize()} {middle.capitalize():.1s} {last.strip().capitalize()} ")
# full_name("omer", "ahmed", "memes")

# # # parameter المتغير
# # # Argument قمية المتغير

# ----------------------------------------------------------
# ------- Function Packing, Unpacking Argument *Args -------
# ----------------------------------------------------------

# myList = [ 1, 3, 4, 5 ]
# print(*myList)
# print(myList)

# def say_hello(n1, n2, n3, n4):
#     peoples = [ n1, n2, n3, n4 ]
#     for name in peoples:
#         print(f"Hello {name}")
# say_hello("omer", "ali", "musa", "yusuf")



# # def say_hello(n1, n2, n3, n4):
# #     peoples = [ n1, n2, n3, n4 ]
# #     for name in peoples:
# #         print(f"Hello {name}")
# # say_hello("omer", "ali", "musa", "yusuf", "mustafa") # will give error
# # عدد الأرغومنت لا يساوي عدد المتغيرات


# def say_hello(*peoples):
#     for name in peoples:
#         print(f"Hello {name}")
# say_hello("omer", "ali", "musa", "yusuf", "mustafa", "muhammed", "taha", "osama") # يمكننا إضافة عدد غير معين من الأرغومنت

# def show_dateils(*skills):
#     print(f"Hello Omer your skills is: ")
#     for skill in skills:
#         print(skill)
# show_dateils("C", "C++", "C#", "Python")


# # --------------------------------------------
# # ------- Function Default Parameters  -------
# # --------------------------------------------


# def say_hello(name="Unknown", age="Unknown", country="Unknown"):
#     print(f"Hello {name} your age is {age} your country {country} ")
# say_hello("omer", 22, "syria")
# say_hello("ali", 21, "Turkey")
# say_hello("yusuf", 33)
# say_hello("musa")
# say_hello()

# # --------------------------------------------------------------
# # ------- Function Packind, Unpacking Argument **KWArgs  -------
# # --------------------------------------------------------------

# mySkills = {
#     "C" : "70%",
#     "C++" : "80%",
#     "C++" : "80%",
#     "Python" : "60%",
#     "HTML" : "40%",
# }

# def skills(**skill):
#     print(type(skill))
#     for lang, prog in skill.items():
#         print(f"Language {lang} Progress {prog}")

# skills(C = "70%", CPulsPlus = "80%", CCharp = "50%", Python = "60%" )
# print(*mySkills)
# skills(**mySkills)

# # print(**mySkills) # will give ERROR

# for skill, prog in mySkills.items():
#     print(skill + " => " + prog )



# # --------------------------------------------------------------
# # ------- Function Packind, Unpacking Argument Trainings  -------
# # --------------------------------------------------------------
# myTuple = ( "html", "python", "c++")
# def show_skills(name, *skills, **skillsWithProgres):
#     print(f"Hello {name} \nSkills Without Progress is: ")
#     for skill in skills:
#         print(skill)
#     print("Skills With Progress is: ")
#     for skill_key, skill_value in skillsWithProgres.items():
#         print(f"-> {skill_key} => {skill_value}")

# show_skills("omer", *myTuple, C = "80%", Cplusplus="90%", python="60%")





# myList = {
#     "C" : "70%",
#     "C++" : "80%",
#     "C++" : "80%",
#     "Python" : "60%",
#     "HTML" : "40%",
# }
# myTuple = ( "HTML5", "CSS", "C#")
# def show_skills(name, *skills, **skillsWithProgres):
#     print(f"Hello {name} \nSkills Without Progress is: ")
#     for skill in skills:
#         print(skill)
#     print("Skills With Progress is: ")
#     for skill_key, skill_value in skillsWithProgres.items():
#         print(f"-> {skill_key} => {skill_value}")

# show_skills("omer", "HTML5", "CSS", "C#", C = "80%", Cplusplus="90%", python="60%")
# show_skills("Omer", *myTuple, **myList)




# # -------------------------------
# # ------- Function Scpoe  -------
# # -------------------------------
# x=1
# def one():
#     print(f"x: {x}")

# def two():
#     x=3
#     print(f"x: {x}")
# def three():
#     print(f"x: {x}")


# print(f"x: {x}") #1
# one() #1
# two() #3
# print(f"x: {x}") #1
# three() #1

# print("="*20)

# x=1
# def one():
#     print(f"x: {x}")

# def two():
#     global x
#     x=3
#     print(f"x: {x}")
# def three():
#     x=4
#     print(f"x: {x}")


# print(f"x: {x}") #1
# one() #1
# two() #3
# print(f"x: {x}") #3
# three() #4



# # -----------------------------------
# # ------- Function Recursion  -------
# # -----------------------------------
# # --------------------------------------------------------------------------------
# # ------- To Understand Recursion, You Need to First Understand Recursion  -------
# # --------------------------------------------------------------------------------

# def cleanWord(word):
#     if len(word) == 1: 
#         return word
#     if word[0]==word[1]:
#         return cleanWord(word[1:])
#     return word[0] + cleanWord(word[1:])
# print(cleanWord("ooooommmmmmmeeeeeeerrr"))


# # --------------------------------
# # ------- Function Lambda  -------
# # ------ Anonymous Function  -----
# # --------------------------------
# # [1] It has not name
# # [2] You can call inline without defining it
# # [3] You can use it in return data from another function
# # [4] Lambda used for simple functions and def handle the large tasks
# # [5] Lambda is one single expression not block of code
# # [6] Lambda type is function
# # --------------------------------

# def say_hello(name): return f"Hello {name}"
# hello = lambda name : f"Hello {name}"

# print(say_hello("Omer"))
# print(hello("Ali"))

# print(say_hello.__name__)
# print(hello.__name__) 


# def say_hello(name, age): return f"Hello {name} your age is: {age}"
# hello = lambda name, age : f"Hello {name} your age is: {age}"

# print(say_hello("Omer", 22))
# print(hello("Ali", 21))

# print(type(hello))
# print(type(say_hello))





# # -----------------------------
# # ------- File Handling -------
# # -----------------------------
# # [1] "a" Append Open File For Appending Values, Create File If Not Exists
# # [2] "r" Read [Default Value] Open File For Read and Give Error If File is Not Exists
# # [3] "w" Write Open File For Writing, Create File If Not Exists
# # [4] "x" Create Create File, Give Error If File Exists
# # -----------------------------

# file = open("Pomer.txt")  # Will Give Error Because The file not found
# file = open("Pomer.txt")    # Will Give True, We are created the file
# file = open("Pomer.txt") # غيرنا موقع الملف فلذلك سوف نحصل على خطأ

# import os
# # # Main Current Working Directory 
# # print(os.getcwd())
# # # Directory For The Opened File
# # print(os.path.dirname(os.path.abspath(__file__)))
# # # print(os.path.abspath(__file__)) # موقع صفحة الحالية

# # # Change Current Working Directory
# # os.chdir(os.path.dirname(os.path.abspath(__file__)))


# file = open(r"C:\Users\ALFURAT LAPTOP\OneDrive\Desktop\PROGRAMING\NewPythonFile.txt")


# # ------------------------------------------
# # ------- File Handling => Read File -------
# # ------------------------------------------

# file = open("Pomer.txt", "r")
# print(file) # File Date Object # <_io.TextIOWrapper name='Pomer.txt' mode='r' encoding='cp1256'>

# print(file.name)     # Pomer.txt
# print(file.mode)     # r
# print(file.encoding) # cp1256

# print(file.read())
# print(file.read(5)) # read only first five characeters

# print(file.readline()) # read only line
# print(file.readline(10)) # read only first 10 charecters of line

# print(file.readlines())        # Returns text as list
# print(type(file.readlines()))  # <class 'list'>

# for line in file:
#     print(line)
#     if line.startswith("04"):
#         break

# file.close()



# # ---------------------------------------------------------
# # ------- File Handling => Write and Append In File -------
# # ---------------------------------------------------------

# # file = open("WritePomer.txt", "w") # بمجرد تشغيل الكود سيتم إنشاء الملف
# # file.write("Hello, my name is: Omer MEMES\n")
# # file.write("I live in Turkey")

# file = open("file.txt", "w")

# # file.write("Omer\n"*333)

# myList = ["omer\n", "ali\n", "musa\n"]
# # file.write(myList) ERROR
# file.writelines(myList)

# file = open("file2.txt", "a")
# file.write("what's happening in Vegas stays in Vegas")
# file.write("\n\n\nomer\n\n\n")
# file.write("ali")

# file = open("fileP.txt", "a")
# file.write("Hello Python")
# file.truncate(5) # Hello

# print(file.tell()) # يرجع موقع مؤشر الكتابة مع العلم بأن السطر الجديد يعتبر 2 كريكتر


# file = open("pythonFile.txt", "r")
# file.seek(11) # نقل مؤشر الكتابة للإندكس 11
# print(file.read())

# # Remove Files
# import os
# os.remove("file2.txt")
# os.remove("file.txt")



# # ----------------------------------
# # ------- Built In Functions -------
# # ----------------------------------
# # all()
# # any()
# # bin()
# # id()
# # ----------------------------------

# x = [ 1, 2, 3, [] ]
# if all(x):  
#     print("All element is True")
# else:
#     print("Theres at least on element is flase")


# x = [ 1, 2, 3, 6 ]
# if all(x):  
#     print("All element is True")
# else:
#     print("Theres at least one element is flase")



# x = [ 0, {}, [], (), 5 ]
# if any(x):  
#     print("There's at least one element is true")
# else:
#     print("There's no any true elements")



# x = [ 0, {}, [], (), False ]
# if any(x):  
#     print("There's at least one element is true")
# else:
#     print("There's no any true elements")



# print(bin(100))

# a=1
# b=2
# print(id(a))
# print(id(b))


# # ----------------------------------
# # ------- Built In Functions -------
# # ----------------------------------
# # sum()
# # round()
# # range()
# # print()
# # ----------------------------------

# # sum(iterable, start)
# a = [ 3, 54, 6, 7 ]
# print(sum(a))
# print(sum(a, 50)) # 70 +50

# # round(number, numOfDigit)
# print(round(123.43)) # 123
# print(round(123.68)) # 124

# print(round(123.68,1)) # 123.7
# print(round(143.55,1)) # 143.6
# print(round(143.55343,2)) # 143.55
# print(round(143.55599,2)) # 143.56

# # range(start, end, step) # step default is 1
# print(list(range(0))) # [] 
# print(list(range(0,11)))     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(0, 20, 2))) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# # print()
# print("omer", "ali", "memes")
# print("omer ali memes")
# print("omer", "ahmed", "memes", sep="-") # omer-ahmed-memes

# print("omer", "memes", end="\n", sep="_")
# print(end= "new line") # استخدامها يأتي في نهاية النص أو في سطر لحالها
# print( " ali", "memes",)

# print("First Line", end=" ")
# print("Second Line")
# print("Thrid Line")



# # ----------------------------------
# # ------- Built In Functions -------
# # ----------------------------------
# # abs()
# # pow()
# # min()
# # max()
# # slice()
# # ----------------------------------

# # abs(base, exp, mod)
# print(100)
# print(abs(-100)) # 100

# # pow()
# print(pow(3,4)) # 81

# print(pow(2,2,3)) #2*2%3=1

# # min(item, item, item)
# print(min(43, 65, 76, 32)) # 32
# print(min("a", "b", "omer")) # a

# myList = [ 54, 33, 23, 51, 76, 12 ]
# print(min(myList)) # 12


# # max(item, item, item)
# print(max(43, 65, 76, 32)) # 32
# print(max("a", "b", "omer")) # a

# myList = [ 54, 33, 23, 51, 76, 12 ]
# print(max(myList)) # 12

# # slice()
# a = [ "A", "B", "c", "F", "r", 1 , 43 ]
# print(a[4:])  # ['r', 1, 43]
# print(a[slice(2,5)]) # ['c', 'F', 'r']


# # -----------------------------------------
# # ------- Built In Functions => Map -------
# # -----------------------------------------
# # [1] Map Take A Function + Iterator
# # [2] Map Called Map Because It Map The Function On Every Element
# # [3] The Function Can Be Pre-Defined Function or Lambda function
# # ----------------------------------


# # Use Map with Predefined function

# def formatText(text):
#     return f"- {text} -".capitalize()

# myTexts = [ "omer", "ali", "yusuf" ]

# myFromatData = map(formatText, myTexts)
# print(myFromatData)

# for name in myFromatData:
#     print(name)

# for name in map(formatText, myTexts):
#     print(name)

# for name in list(map(formatText, myTexts)):
#     print(name)

# # Use Lambda with Predefined function

# myTexts = [ "omer", "ali", "yusuf" ]

# for name in map(lambda text :f"- {text} -".capitalize(), myTexts):
#     print(name)



# # --------------------------------------------
# # ------- Built In Functions => Filter -------
# # --------------------------------------------
# # [1] Filter Take A Function + Iterator
# # [2] Filter Run A Function On Every Element
# # [3] The Function Can Be Pre_Defined Function or Lambda Function
# # [4] Filter Out All Element For Which The Function Return True
# # [5] The Function Need To Return Boolean Value
# # --------------------------------------------


# # Example 1

# from functools import reduce


# def checkNumber(num):
#         return num>10 #  Function Return True

# Numbers = [ 2, 23, 5, 54, 65, 7, 64, 11, 3 ]    

# myResult = filter(checkNumber, Numbers)

# print(myResult) # <filter object at 0x00000154C8D5BD00>

# for number in myResult:
#     print(number)


# # Example 2

# def checkname(name):
#     return name.startswith("O")

# names = ["Omer", "Ali", "Yusuf", "Osman"]
# myResult = filter(checkname, names)
# for name in myResult:
#     print(name)

# # Example 2

# names = ["Omer", "Ali", "Yusuf", "Osman"]
# myResult = filter(lambda name : name.startswith("O"), names)

# for name in myResult:
#     print(name)


# # --------------------------------------------
# # ------- Built In Functions => Reduce -------
# # --------------------------------------------
# # [1] Reduce Take A Function + Iterator
# # [2] Reduce Run A Function On First And Second Element And Give Result
# # [3] Then Run Function On Result And Third Element
# # [4] Then Run Function On Result And Fourth Element And So On
# # [5] Till One Element is Left and This is The Result of The Reduce
# # --------------------------------------------


# def sumAll(num1, num2):
#     return num1+num2


# number = [ 3,4,5,6,7,8,5 ]
# Result = reduce(sumAll, number) # ((((1+2)+3)+4)+5)

# print(Result)

# number = [ 3,4,5,6,7,8,5 ]
# Result = reduce(lambda num1, num2: num1+num2, number) # ((((1+2)+3)+4)+5)

# print(Result)



# # ----------------------------------
# # ------- Built In Functions -------
# # ----------------------------------
# # enumerate()
# # help()
# # reversed()
# # ----------------------------------

# # enumerate()
# skills = [ "c", "c++", "c#", "python" ]

# for skill in skills:
#     print(skill)

# mySkillsWithCounter = enumerate(skills, 20)
# for skill in mySkillsWithCounter:
#     print(skill)

# for c,s in mySkillsWithCounter:
#     print(f" {c} - {s} ")

# # help() => print(help(print)) تشرح خواص دالة

# # reversed()
# name = "omer"
# print(reversed(name))

# for letter in reversed(name):
#     print(letter)


# # ---------------------------------------------
# # ------- Built In Functions => Modules -------
# # ---------------------------------------------
# # [1] Module is A File Contain A Set of Functions
# # [2] You Can Import Module in Your App To Help You
# # [3] You Can Import Multiple Modules
# # [4] You Can Create Your Own Modules
# # [5] Modules Saves Your Tim
# # ---------------------------------------------

#######################################################################################################################################
print("-"*60)
x = 6
y = type(x)
print(type(x)) # <class 'int'>
print(type(y)) # <class 'type'>
print("-"*60)

print("-"*60)
print("1234fazla\r1234") # 1234fazla
print("omerr\b memes")  # omer memes
print("-"*60)

print("-"*60)
fullName = "omer \
            ahmed \
            memes"

name = "omer"
surname = "memes"
print(name + " " + surname)  # omer memes
print("-"*60)
#######################################################################################################################################
# ***** string *****
# سلاسل الفهرسة والتقطيع
# [1] جميع البيانات في بيثون هي كائن
# [2] عناصر الحالة الكائن
# [3] كل عنصر له فهرس خاص به
# [4] بيثون استخدام "صفر" الفهرسة القائمة (مؤشر تبدأ من الصفر)
# [5] استخدم الأقواس المربعة للوصول إلى العنصر
# [6] التقطيع: تمكين الوصول إلى أجزاء من السلاسل أو المجموعات أو القوائم

# Indexing (Access Single Item)
print("-"*60)
full_name = "omer ahmed memes"
print(full_name[2]) # e
print(full_name[0]) # o
print(full_name.index("o")) # 0 هذه الدالة تعيد لنا موقع الحرف
print(full_name[-1]) # s آخر عنصر من العبارة
print("-"*60)

# # Slicing (Access Multiple Sequence Item)
# التقطيع (الوصول إلى عنصر تسلسل متعدد)
print("-"*60)
full_name = "omer ahmed memes"
print(full_name[5:]) # ahmed memes
print(full_name[:4]) # omer
print(full_name[::]) # omer ahmed memes
print(full_name[0::1])  # Full Data 
print(full_name[::1])  # Full Data
print(full_name[0::])  # Full Data  
print(full_name[::])  # Full Data
print("-"*60)
# print(full_name[::3])   # يطبع حرف ويوفّت حرفين

# ---------------------
# -- Strings Methods --
# ---------------------
# 1  # len() قياس طول النص
print("-"*60)
name = "omer"; print(len(name)); print(len("omer memes"))
print("-"*60)

# 2  # strip()   تحذف المسافات عن اليمين واليسار (عزل) 
# 3  # rstrip()  تحذف المسافات عن اليمين
# 4  # lstrip()  تحذف المسافات عن اليسار
print("-"*60)
name = "      omer      "; print(name.strip())
name = "33$%$##**omer**33%##"; print(name.strip("*$#%3")) # omer
name = "      omer      "; print(name.rstrip()) # right strip
name = "      omer      "; print(name.lstrip()) # left strip
print("-"*60)
# 5  # title() أول حرف من كل كلمة كبير والأحرف التي تأتي بعدر الأقارم تصبح كبيرة
print("-"*60)
name = 'omer memes'; print(name.title()) # Omer Memes
name = 'omer memes'.title(); print(name) # Omer Memes
print("-"*60)
# 6  # capitalize() تحول أول حرف من كل كلمة لحرف كبير ولكن الاحرف التي تأتي بعد الأقام تبقى على حالها
print("-"*60)
name = "omer memes".capitalize(); print(name) #Omer memes
name = "omer memes"; print(name.capitalize()) # Omer memes
print("-"*60)
# 7  # upper() & lower()
print("-"*60)
name = "omer memes".upper(); print(name) #OMER MEMES
name = "omer memes"; print(name.upper()) #OMER MEMES
name = "OMER MEMES".lower(); print(name) #omer memes
name = "OMER MEMES".lower(); print(name.lower()) #omer memes
print("-"*60)
# 8  # split() (تقسيم) & rsplit() تحويل كلمات النص إلى ليستا
print("-"*60)
name = "omer memes".split(); print(name) #['omer', 'memes']
name = "omer memes"; print(name.split()) #['omer', 'memes']
name = "ali omer ahmed memes"; print(name.rsplit("-")) #['ali omer ahmed memes']
name = "ali omer ahmed memes"; print(name.rsplit(" ")) #['ali', 'omer', 'ahmed', 'memes'
name = "ali omer ahmed memes"; print(name.rsplit()) #['ali', 'omer', 'ahmed', 'memes'
print("-"*60)
# 9  # center() إضافة رموز إلى طرفي الكلمة # بحاجة إلى معامل إجباري
print("-"*60)
name = "omer".center(10,"*"); print(name) # ***omer***
name = "omer"; print(name.center(10))     #    omer
print("-"*60)
# 10 # count() يبين عدد مرات تكرار الكلمة أو الحرف في النص
print("-"*60)
name = "omer memes"; print(name.count("m")) # 3
name = "omer memes".count("m"); print(name) # 3
name = "omer memes".count("memes"); print(name) # 1
print("-"*60)
# 11 # swapcase() جعل الأحرف الكبيرة صغيرة والصغيرة كبيرة
print("-"*60)
name = "omer MEMES".swapcase(); print(name) # OMER memes
name = "omer MEMES"; print(name.swapcase()) # OMER memes
print("-"*60)
# 12 # startswith() # هل الكلمة  تبدأ بالحرف المطلوب
# 13 # endswith  """End Not Included """ 
# 14 # # هل الكلمة  تنتهي بالحرف المطلوب
print("-"*60)
name = "omer MEMES".startswith("o"); print(name) # True
name = "omer MEMES"; print(name.startswith("o")) # True
name = "omer MEMES"; print(name.startswith("M",5,9)) # True
name = "omer MEMES"; print(name.endswith("S")) # True
name = "omer MEMES"; print(name.endswith("S",5,10)) # True
name = "omer MEMES"; print(name.endswith("S",5,9)) # False
print("-"*60)

# 15 # index(substring, start, end)
print("-"*60)
name = "ali omer ahmed memes"
name = "ali omer ahmed memes"
print(name.index("a")) # 0
print(name.index("a", 5)) #    ابحث عالحرف من عند الدليل 5
print(name.index("m", 5)) #    ابحث عالحرف من عند الدليل 5
print(name.index("a", 0)) # 0
# print(name.index("b")) # error
print("-"*60)
# 16 # find(substring, start, end)
# 17 # فهو يعطي خطأ index فقط في حالة عدم وجود الحرف المطلوب يُظهر النتيجة كسالب واحد على عكس الـ index يعمل عمل الـ
print("-"*60)
name = "ali omer ahmed memes"
name = "ali omer ahmed memes"
print(name.find("a")) # 0
print(name.find("a", 5)) #    ابحث عالحرف من عند الدليل 5
print(name.find("m", 5)) #    ابحث عالحرف من عند الدليل 5
print(name.find("b")) # -1
print("-"*60)
# 18 # rjust(width, fill char)  ljust(width, fill char)  إذافة رموز لطرفي الكلمة
print("-"*60)
name = "ali memes".rjust(15,"*"); print(name) # ******ali memes
name = "ali memes"; print(name.ljust(15,"#")) # ali memes######
name = "ali memes"; print(name.ljust(15,"#").rstrip("#")) # ali memes
name = "ali memes"; print(name.rjust(15,"#").rstrip("#")) # ######ali memes
name = "ali memes"; print(name.rjust(15,"#").strip("#")) # ali memes
print("-"*60)
# 19 # expandtabs() اضافة فراغات على حسب الطلب
print("-"*60)
name = "omer\tmemes".expandtabs(50); print(name) # omer                                              memes
name = "omer\tmemes"; print(name.expandtabs(50)) # omer                                              memes
print("-"*60)
# 20 # istitel()   هل هذا عنوان ؟
print("-"*60)
name = "Omer MEMES".istitle(); print(name) # False
name = "Omer memes"; print(name.istitle()) # False
name = "omer Memes"; print(name.istitle()) # False
name = "Omer Memes"; print(name.istitle()) # True
name = "omer memes"; print(name.istitle()) # False
print("-"*60)
# 21 # isspace() هل هذه مسافة؟
print("-"*60)
# isspace() هل هذه مسافة؟
k = " "
l = ""
print(k.isspace())  # True
print(l.isspace())  # False
print("-"*60)
# 22 # islower()
print("-"*60)
name = "omer memes".islower(); print(name) # True
name = "Omer MEMES".islower(); print(name) # False
print("-"*60)
# 23 # isidentifier()  هل النص يصلح أن يكون اسم متغير؟
print("-"*60)
name = "_omer"; print(name.isidentifier()) # True
name = "_omer_"; print(name.isidentifier()) # True
name = "omer3"; print(name.isidentifier()) # True
name = "omer_memes"; print(name.isidentifier()) # True
name = "omer-memes"; print(name.isidentifier()) # False
name = "-omer"; print(name.isidentifier()) # False
name = "*omer"; print(name.isidentifier()) # False
name = "3omer"; print(name.isidentifier()) # False
print("-"*60)
# 24 # isalpha() هل النص عبارة عن أحرف فقط؟
print("-"*60)
name = "omer MEMES"; print(name.isalpha()) # False
name = "omerMEMES"; print(name.isalpha()) # True
print("-"*60)
# 25 # replace(old value, new value, count) تبديل كلمات النص على حسب الطلب
print("-"*60)
a = "one two three one two one three one"
print(a.replace("one", "1", 1)) # 1 two three one two one three one
print(a.replace("one", "1", 2)) # 1 two three 1 two one three one
print(a.replace("one", "1"))    # 1 two three 1 two 1 three 1
print("-"*60)
# 26 # join(iterable المتوقع || المطلوب) دمج وإضافة رموز لعناصر الليست
print("-"*60)
name = ["omer", "ahmed", "memes"]; print("-".join(name))
print("-"*60)
# 27 # zfill تعبئى الفراغات بالمطلوب
print("-"*60)
one, two, three, four, five, six, seven, eight, nine, ten =  "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" 
print(one.zfill(2)) #01
print(two.zfill(2)) #02
print(three.zfill(2)) #03
print(four.zfill(2)) #04
print(five.zfill(2)) #05
print(six.zfill(2)) #06
print("-"*60)
# ---------------------

# ------------------------
# -- Strings Formatting --
# ------------------------
print("-"*60)
name="omer"; age=22; print("my name is:", name , "and my age is:", age) # my name is: omer and my age is: 22
name="omer"; age=22; print("my name is:" + " " +  name + " " + "and my age is:" , age) # my name is: omer and my age is: 22
name="omer"; age=22; print("my name is: %s and my age is: %s " % (name, age)) # my name is: omer and my age is: 22
name="omer"; age=22; print("my name is: %s and my age is: %d " % (name, age)) # my name is: omer and my age is: 22
name="omer"; age=22; print("my name is: {} and my age is: {} ".format(name, age)) # my name is: omer and my age is: 22
name="omer"; age=22; print("my name is: %s and my age is: %.2f " % (name, age)) # my name is: omer and my age is: 22.00
name="omer"; age=22; print(f"my name is: {name} and my age is: {age} ") # my name is: omer and my age is: 22
print("-"*60)

# # Split Strings || Slice Strings || Truncate Strings
# # انقسام || التقطيع || اقتطاع
print("-"*60)
name="ali omer ahmed omer memes"; print("my child name is: [%.3s]"%name) # my child full name is: [ali]
name="ali omer ahmed omer memes"; print("my child full name is: [%s]"%name) # my child full name is: [ali]
name="omer memes"; age=22; print("my name is: {:.4s} and my age is: {:.2f} ".format(name, age)) # my name is: omer and my age is: 22.00
name="omer memes"; age=22; print("my name is: {:s} and my age is: {:d} ".format(name, age)) # my name is: omer memes and my age is: 22
print("-"*60)
# # Format Money
print("-"*60)
money = 15757999; print("my money in the bank is: {}".format(money)) # 15757999
money = 15757999; print("my money in the bank is: %d"%money)  # 15757999
money = 15757999; print("my money in the bank is: %.5f"%money) # 15757999.00000
money = 15757999; print(f"my money in the bank is: {money}")  # 15757999
money = 15757999; print("my money in the bank is: {:,d}".format(money)) # 15,757,999
money = 15757999; print("my money in the bank is: {:-d}".format(money)) # 15757999
money = 15757999; print("my money in the bank is: {:_d}".format(money)) # 15_757_99
name, surname, age, country, salary = "omer", "memes", 22, "syria", 7000
print("-"*60)
print("my name is: {}, surname is: {}, my age is: {:d}, i am from {} i am student in turkey and my salary is: {:.3f}".format(name, surname, age, country, salary))
# my name is: omer, surname is: memes, my age is: 22, i am from syria i am student in turkey and my salary is: 7000.000
name = "omer"; surname="memes"; age=22;  country="syria"; salary=7000
print("my name is: {}, surname is: {}, my age is: {}, i am from {} i am student in turkey and my salary is: {}".format(name, surname, age, country, salary))
# my name is: omer, surname is: memes, my age is: 22, i am from syria i am student in turkey and my salary is: 7000
print("-"*60)
# #ReArrange Items
print("-"*60)
x, y, z = 10, 20, 30
print(" {} {} {} ".format(x,y,z))
print(" {1} {0} {2} ".format(x,y,z))
print(" {1:.5f} {2:.3f} {0:.2f} ".format(x,y,z))    
print(" {2:d} {1:d} {0:f} ".format(x,y,z))  # 30 20 10.000000
x, y, z = "omer", 22, "memes"
print("my name is: {1} my surname is: {2} my age is: {0}".format(age, name, surname)) # my name is: omer my surname is: memes my age is: 22
print("-"*60)

# # ------------------------
# # ------- Numbers --------
# # ------------------------
print("-"*60)
print(type(10));print(type(-10));print(type(0j));print(type(5+0j));print(type(0.5))
# # [1] يمكنك التحويل من int to float أو complex
# # [2] يمكنك التحويل من تعويم إلى int أو معقد
# # [3] لا يمكنك تحويل المركب إلى أي نوع
print(100) # 100 
print(float(100)) # 100.0
print(complex(100)) # (100+0j)

print(12.4) # 12.4
print(int(12.9)) # 12
print(complex(12.9)) # (12.9+0j)
print("-"*60)


# # --------------------------
# # -- Arithmetic Operators --
# # --------------------------
# # [+] Addition
# # [-] Subtraction
# # [*] Multiplication   
# # [/] Division 
# # [%] Modulus
# # [**] Exponent أس
# # [//] Floor Division
# # --------------------------

# # ---------------------------
# # ---------- قائمة ----------
# # ---------------------------
# [1] عناصر القائمة محاطة بأقواس مربعة
# [2] تم ترتيب القائمة ، لاستخدام الفهرس للوصول إلى العنصر
# [3] القائمة قابلة للتغيير => إضافة ، حذف ، تحرير
# [4] ليست ليست فريدة من نوعها
# [5] يمكن أن تحتوي القائمة على أنواع بيانات مختلفة
# -----------------------------

print("-"*60)
lst = [ "omer", 22, 'oms', True, 8.3 ]
print(lst[0])
print(lst[-1])
print(lst[::])  # ['omer', 22, 'oms', True, 8.3]
print(lst[0::]) # ['omer', 22, 'oms', True, 8.3]
print(lst[::1]) # ['omer', 22, 'oms', True, 8.3]
print(lst[0:])  # ['omer', 22, 'oms', True, 8.3]

# # ----------------------------------
# # ---------- List Methods ----------
# # ----------------------------------
# # append() # Add Item الليستة الجديدة تضاف كعنصر واحد 
# append() = inster() || index() || extend()
# #extend() (تدمج) عناصر الليستة الجديدة تضاف لعناصر الليستة الأساسية 
# # insert     # add item  # have two argument # this function same append function
lst.append("memes"); print(lst) # ['omer', 22, 'oms', True, 8.3, 'memes']
lst.append(["ali", "memes"]); print(lst) # ['omer', 22, 'oms', True, 8.3, 'memes', ['ali', 'memes']]
print(lst.index(['ali', 'memes'])) #6
print(lst[6][0]) #ali
lst.insert(1, "my age: "); print(lst) # ['omer', 'my age: ', 22, 'oms', True, 8.3, 'memes', ['ali', 'memes']]
names = [ "omer", "ali", "osman" ]
surnames = [ "memes", "memes", "memes" ]
names.extend(surnames); print(names) # ['omer', 'ali', 'osman', 'memes', 'memes', 'memes']
print("-"*60)
print("-"*60)
# # remove() delete
lst = [ "omer", 22, 'oms', True, 8.3 ]
# lst.remove(); print(lst) # ERROR
lst.remove(22)
print(lst) # ['omer', 'oms', True, 8.3]
lst.remove("oms"); print(lst)
print(lst.remove("omer")) # None
# lst.remove(22); #ERROR
print("-"*60)
# # sort() عند استخدام هذه الدالة يجب أن تكون عناصر الليست من نوع واحد
print("-"*60)
lst = [ 4,5,76,34,32,15,43,27,89,10 ]; lst.sort(); print(lst) # [4, 5, 10, 15, 27, 32, 34, 43, 76, 89]
lst = [ 4,5,76,34,32,15,43,27,89,10 ].sort(); print(lst) # None
lst = [ 4,5,76,34,32,15,43,27,89,10 ]; lst.sort(reverse=False); print(lst) # [4, 5, 10, 15, 27, 32, 34, 43, 76, 89]
lst = [ 4,5,76,34,32,15,43,27,89,10 ]; lst.sort(reverse=True); print(lst) # [89, 76, 43, 34, 32, 27, 15, 10, 5, 4]
lst = [ 4,5,76,34,32,15,43,27,89,10 ]; print(lst.sort(reverse=True)) # None
lst = [ "a", "b", "C", "K", "r", "6" ]; lst.sort(); print(lst) # ['6', 'C', 'K', 'a', 'b', 'r']
print("-"*60)
# # revese()  الدالة لا تشترط بأن تكون عناصر الليست من نوع واحد
print("-"*60)
lst = [ "a", "b", "C", "K", "r", "6" ]; lst.reverse(); print(lst) # ['6', 'r', 'K', 'C', 'b', 'a'
lst = [ 4,5,76,34,32,15,43,27,89,10 ]; lst.reverse(); print(lst) # [10, 89, 27, 43, 15, 32, 34, 76, 5, 4]
lst = [ 4,5,76,34,32,15,43,27,89,10 ].reverse(); print(lst) # None 
print("-"*60)
# # clear()
print("-"*60)
lst = [ 4,5,76,34,32,15,43,27,89,10 ]; lst.clear(); print(lst) # []
print("-"*60)
# # count  # Counter
print("-"*60)
lst = [ 1, 2, 3, 2, 3, 4, 2, 1, 3 ].count(1); print(lst) #2
lst = [ 1, 2, 3, 2, 3, 4, 2, 1, 3 ]; print(lst.count(1)) #2
lst = [ 1, 2, 3, 2, 3, 4, 2, 1, 3 ]; r=lst.count(1); print(r) #2
print("-"*60)
# # pop()  # This function gets the index of the items
print("-"*60)
names = [ "omer", "ali", "osman" ]; names.pop(); print(names) # ['omer', 'ali']
print("-"*60)

# -----------------------------
# ----------- مترابطة بيانية -----------
# -----------------------------
# [1] تم تضمين عنصر Tuple في أقواس
# [2] يمكنك إزالة الأقواس إذا أردت
# [3] ترتيب المجموعات ، لاستخدام الفهرس للوصول إلى العنصر
# [4] Tuple غير قابل للتغيير => يمكنك الإضافة أو الحذف
# [5] عناصر Tuple ليست فريدة من نوعها
# [6] يمكن أن يحتوي Tuple على أنواع بيانات مختلفة
# [7] عوامل التشغيل المستخدمة في السلاسل والقوائم المتاحة في مجموعات
# -----------------------------
print("-"*60)
names = ("\"omer\"", "ali", "osama")
print(type(names)) #<class 'tuple'>
print(names[0]) # "omer"
print(names[1]) # ali
print(names[0::]); print(names[::]);print(names[0::1]);print(names[0::1]) #full data
print(names[-1]) # osama
print("-"*60)


print("-"*60)
names = "omer", "ali", "osama"; print(type(names)) # <class 'tuple'>
names = "omer",; print(type(names)) # <class 'tuple'>
names = ("omer",); print(type(names)) # <class 'tuple'>
names = ("omer"); print(type(names)) # <class 'str'>
names = "omer"; print(type(names)) # <class 'str'>
print("-"*60)


print("-"*60)
names = "omer", "ali", "osama"; print(len(names)) #3 tuple
names = "omer",; print(len(names)) #1 tuple
names = "omer"; print(len(names)) #4 string
print("-"*60)
print("-"*60)
names = "omer", "ali", "osama";
surnames = "memes", "memes", "memes";
fullName = names+surnames; print(fullName) # ('omer', 'ali', 'osama', 'memes', 'memes', 'memes')
num1 =  (3,45,6,7,8,9)
num2 =  (3,5,5,3,1,32)
result = num1+num2; print(result) #(3, 45, 6, 7, 8, 9, 3, 5, 5, 3, 1, 32)
result = num1+num2+("a","b"); print(result) #(3, 45, 6, 7, 8, 9, 3, 5, 5, 3, 1, 32, 'a', 'b')
result = 2*num2; print(result) #(3, 5, 5, 3, 1, 32, 3, 5, 5, 3, 1, 32)
print("-"*60)
# # Method -> count()
# # Method -> index()
print("-"*60)
num2 =  (3,5,5,3,1,32).count(3); print(num2) #2
num2 =  (3,5,5,3,1,32); print(num2.count(3)) #2
num2 =  (3,5,5,3,1,32); print(num2.index(1)) #4
num2 =  (3,5,5,3,1,32).index(1); print(num2) #4
print("-"*60)
# # Tuple Destruct 
print("-"*60)
names = ("omer", "ali", "osama")
n1, n2, n3 = names; print(n1,n2,n3)  # omer ali osama
print("-"*60)
# -----------------------------
# ----------- تعيين -------------
# -----------------------------
# [1] عناصر المجموعة محاطة بأقواس معقوفة
# [2] عيّن العناصر غير مرتبة وليست مفهرسة
# [3] لا يمكن إجراء الفهرسة والتقطيع
# [4] تحتوي المجموعة على أنواع بيانات ثابتة فقط (أرقام ، سلاسل ، مجموعات) وقائمة الإملاء ليست كذلك
# [5] مجموعة العناصر فريدة من نوعها
# -----------------------------
# # -------------------------------------
# # ----------- Set Methods -------------
# # -------------------------------------
# 1 #   clear() 
print("-"*60)
numbers = { 4, 5, 6, 1, 3, 7, 9, 76, 43, 2, 6, 5, 8, 12, 1, 2, 3 }
numbers.clear(); print(numbers) #set()
# 2 #   union اتحاد
numbers = { 4, 5, 6, 1, 3, 7, 9, 76, 43, 2, 6, 5, 8, 12, 1, 2, 3 };numbers1 = { 0000000000, 54, 00000000000 }
print(numbers.union(numbers1)) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 43, 76, 12, 54}
b = {"one", "two", "three"}
c = {"1", "2", "3"}
print(c|b) # {'three', '3', '1', '2', 'two', 'one'}
print("-"*60)
# 3 #   add()     # Add() function it takes only one argument
print("-"*60)
numbers = { 4, 5, 6, 1, 3, 7, 9, 76, 43, 2, 6, 5, 8, 12, 1, 2, 3 };numbers.add(7777777); print(numbers) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 43, 76, 12, 7777777}
print("-"*60)
# 4 #   copy()
print("-"*60)
f = { 3, 5, 6, 7, 8 }
g = f.copy()
print(f) # {3, 5, 6, 7, 8}
print(g) # {3, 5, 6, 7, 8}
f.add(1)
print(f) # {1, 3, 5, 6, 7, 8}
print(g) # {3, 5, 6, 7, 8}
print("-"*60)
# 5 #   remove()
# 6 #   discard() # لا تعطي خطأ بحال كان العنصر غير موجود وتم طلب حذف على عكس الريموف
# 7 #   pop()  # this function is removes a random element from a set
print("-"*60)
h = { "omer", "ali", "yusuf" }; h.remove("omer");print(h) # {'ali', 'yusuf'}
print("-"*60)
# 8 #   update() دمج
print("-"*60)
k = { 1, 2, 3, 4 }
l = { 1, 2, "A", "B", 5, 2 }
k.update(l)
print(k) # {1, 2, 3, 4, 'B', 5, 'A'}
print("-"*60)
# 9 #   difference()
# 10 #  difference_update()
# 11 #  intersection() sets الأولى والعناصر المشتركة بين كلا الـ set عناصر الـ
# 12 #  symmetric_difference() دمج فرق الإثنين
print("-"*60)
x = { "a", "b", "c", 3, 2, 1 }
z = { 1, 3, "a", "B", "c" }
print(x.symmetric_difference(z))    # {'b', 'B', 2}
print("-"*60)
# 13 #  symmetric_difference_update() فرق الاثنين
# 14 #  issuperset()
print("-"*60)
a = { 1, 2, 3, 4 }
b = { 1, 3, 2 }
c = { 1, 2, 3, 4, 5 }
print(a.issuperset(b)) # true  (big-small)
print(a.issuperset(c)) # flase
print("-"*60)
# 15 #  issubset() ------> issuperset()  الاحتواء
print("-"*60)
a = { 1, 2, 3, 4, }
b = { 1, 3, 2 }
c = { 1, 2, 3, 4, 5 }
print(a.issubset(b)) # false (small-big)
print(a.issubset(c)) # true
print("-"*60)
# 16 #  isdisjoint() ------> مختلفين 
print("-"*60)
a = { 1, 2, 3, 4 }
b = { 1, 3, 2 }
c = { 6, 7, 8, 9, 5 }
print(a.isdisjoint(b)) # false
print(a.isdisjoint(c)) # true
print("-"*60)
# # -------------------------------------

# # ------------------------------------
# # ----------- قاموس -------------
# # ------------------------------------
# [1] عناصر القاموس محاطة بأقواس معقوفة
# [2] تحتوي عناصر القاموس على المفتاح: القيمة
# [3] يجب أن يكون مفتاح القاموس غير قابل للتغيير -> (رقم ، سلسلة ، مجموعة) قائمة غير مسموح بها
# [4] يمكن أن تحتوي قيمة القاموس على أي أنواع بيانات
# [5] يجب أن يكون مفتاح القاموس فريدًا
# [6] القاموس لم يأمر بالوصول إلى عنصره بالمفتاح
# # ------------------------------------
print("-"*60)
languages = {
    "One" : { "name" : "C", "progress" : "60%" },
    "Two" : { "name" : "C++", "progress" : "70%" },
    "Three" : { "name" : "C#", "progress" : "30%" },
    "Four" : { "name" : "python", "progress" : "20%" },
            }
print(languages) #{'One': {'name': 'C', 'progress': '60%'}, 'Two': {'name': 'C++', 'progress': '70%'}, 'Three': {'name': 'C#', 'progress': '30%'}, 'Four': {'name': 'python', 'progress': '20%'}}
print(languages["Four"]) # {'name': 'python', 'progress': '20%'}
print(languages["Four"]["name"]) # python
print(len(languages)) #4
print("-"*60)
# # update()
languages["Four"]["name"] = "HTML" ; print(languages) # {'One': {'name': 'C', 'progress': '60%'}, 'Two': {'name': 'C++', 'progress': '70%'}, 'Three': {'name': 'C#', 'progress': '30%'}, 'Four': {'name': 'HTML', 'progress': '20%'}}
languages.clear(); print(languages) # {}

print("-"*60)
omer = { "age" : 22, "country" : "syria", }; omer.update({"city":"idlip"})
print(omer) # {'age': 22, 'country': 'syria', 'city': 'idlip'}
name = omer.copy(); print(name) # {'age': 22, 'country': 'syria', 'city': 'idlip'}
omer.update({"surname":"memes"}); print(omer) # {'age': 22, 'country': 'syria', 'city': 'idlip', 'surname': 'memes'}
print(name) # {'age': 22, 'country': 'syria', 'city': 'idlip'}
print("-"*60)

print("-"*60)
print(omer.keys()) # dict_keys(['age', 'country', 'city'])
print(omer.values()) # dict_values([22, 'syria', 'idlip'])
print("-"*60)
print("-"*60)
# # fromkeys() # dict.fromkeys()
names = {"omer", "ali", "osman", "yusuf"}   # we can used this
names = ("omer", "ali", "osman", "yusuf")   # we can used this
names = ["omer", "ali", "osman", "yusuf"]   # we can used this
memesFamily = 'memes'
print(dict.fromkeys(names, memesFamily)) # {'omer': 'memes', 'ali': 'memes', 'osman': 'memes', 'yusuf': 'memes'}
print("-"*60)
print("-"*60)
# # items() يحتفظ بكل الحدود حتى ولو قمنا بالتعديل على القاموس
omer = { "age" : 22, "country" : "syria" }
allItems = omer.items()
omer["name"] = "omer"
# omer["name"] = "memes" عند تكرار إضافة العنصر نفسه سيضيف الأخير فقط
omer["rating"] = 10
print("-"*60)
# # --------------------------------------------
# # ----------- Dictionary Methods -------------
# # --------------------------------------------
# 1 # clear()
# 2 # update() # person["one"]["age"] = 22
# 3 # copy()
# 4 setdefault() تستخدم للإضافة أيضا اذا كان المفتاح المضاف موجود فترجع قيمته وإن كان غير مضاف تضيف العنصر المراد إضافته
# 5 # popitem() يرجع آخر عنصر تمت إضافته
# 6 # items() يحتفظ بكل الحدود حتى ولو قمنا بالتعديل على القاموس
# 7 # fromkeys() # dict.fromkeys()
# # --------------------------------------------

# # ---------------------------------
# # ----------- Boolean -------------
# # ---------------------------------
print("-"*60)
# True Values
print(bool("omer"))# true
print(bool(100)) # true
print(bool(10.5)) # true
print(bool(["omer", "ali"])) # true
print(bool((1, 3, 6, "a"))) # true
print(bool({"omer", "memes", 3})) # true
print(bool(True)) # true
print("-"*60)
print("-"*60)
# False Values
print(bool("")) # false
print(bool('')) # false
print(bool(0)) # false
print(bool(0.0)) # false
print(bool([])) # false
print(bool(())) # false
print(bool({})) # false
print(bool(None)) # false
print(bool(False)) # false
print("-"*60)
print("-"*60)
name = "omer"
age = 22
country = "syria"
print(age==22 and country == "syria" and name == "omer" )   # true
print(age==22 and country == "turkey" and name == "omer" )  # flase
print(age==22 and country == "turkey" or name == "omer" )  # true
print(age==22 or country == "turkey" and name == "omer" )  # true
print(age>20 or country == "turkey" and name == "omer" )  # true
print(age>20 and country == "turkey" and name == "omer" )  # false
print("-"*60)
# # # -----------------------------------------
# # # ----------- تحويل النوع ----------------
# # # -----------------------------------------
# str()
print("-"*60)
a = 10
print(type(a))      # <class 'int'>
print(type(str(a))) # <class 'str'>
print("-"*60)


# # tuple() 
print("-"*60)
a = "omer";  b = { 1, 2, "a", "b" };  c = [ "A", "B", 4, 3 ];  d = ( "o", "m", 2, True);  e = { "A":1, "B":2 }
print(tuple(a)) # ('o', 'm', 'e', 'r')
print(tuple(b)) # ('a', 2, 'b', 1)
print(tuple(c)) # ('A', 'B', 4, 3)
print(tuple(d)) # ( "o", "m", 2, True)
print(tuple(e)) # ('A', 'B')
print("-"*60)
# print(tuple(500)) # ERROR

# # set()
print("-"*60)
print(set(a))   # {'m', 'e', 'o', 'r'} 
print(set(b))   # {'b', 1, 2, 'a'}
print(set(c))   # {3, 'B', 4, 'A'}
print(set(d))   # {'m', 2, 'o', True}
print(set(e))   # {'B', 'A'}
# print(set(500))  # ERROR
print("-"*60)


# # list()
print("-"*60)
print(list(a))   # ['m', 'e', 'o', 'r']
print(list(b))   # ['a', 1, 2, 'b']
print(list(d))   # ['m', 2, 'o', True]
print(list(e))   # ['B', 'A']
# print(set(500))  # ERROR
print("-"*60)

# # dict()    set() و string غير فعال في هذه الخطائص للـ
print("-"*60)
a = ( (3, 1), ("B", 2), ("C", 3) )    
b = [ [3, 1], ["B", 2], ["C", 3] ]    
# c = { {3, 1}, {"B", 2}, {"C", 3} }    
print(dict(a))  # {3: 1, 'B': 2, 'C': 3}
print(dict(b))  # {3: 1, 'B': 2, 'C': 3}
# print(dict(c))  # ERROR
print("-"*60)
# # ------------------------------------------------
# # -----------  Membership Operators  -------------
# # ------------------------------------------------
# # in
# # not in
# # ------------------------------------------------
print("-"*60)
name = "omer"
print("m" in name) # True
print('q' in name) # False
print("-"*60)
friends = ["omer", "ali", "yusuf"]
print("omer" in friends) # True
print("omer" not in friends) # False
print("musa" not in friends) # True
print("-"*60)
friends = ("omer", "ali", "yusuf")
print("omer" in friends) # True
print("omer" not in friends) # False
print("musa" not in friends) # True
print("-"*60)
print("-"*60)
friends = {"omer", "ali", "yusuf"}
print("omer" in friends) # True
print("omer" not in friends) # False
print("musa" not in friends) # True
print("-"*60)


# # -----------------------------------------------
# # ----------- Practical Slice Email -------------
# # -----------------------------------------------

# email = "oms_memes@gmail.com"
# print(email[:9]) # للسهولة نستخدم الطريقة الثانية
# print(email[:email.index('@')])



name = input("What's your name: ").strip().capitalize()
email = input("Wath's your email: ").strip()

userName = email[:email.index("@")]
webSite = email[email.index("@")+1:]
print(f"Hello {name} your email is {email} ") # Hello omer your email is oms83@gmail.com 
print(f"Your username is {userName} \nyour website is {webSite}") #Your username is oms83 and your website is gmail.com


# # ---------------------------------------------------------
# # ----------- Practical Your Age Full Details -------------
# # ---------------------------------------------------------


# age = int(input("what\'s your age : ").strip())
# print(type(age))    # <class 'int'>

# age = input("what\'s your age : ").strip()
# print(type(int(age)))   # <class 'int'>

age = int(input("What\'s your age: ").strip())
months = age*12
weeks = months*4
days = age*365
hours = days*24
minutes = hours*60
seconds = minutes*60
print("Your Live For: ")
print(f"{months} Months.")
print(f"{weeks} Weeks.")
print(f"{days} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")


# # ----------------------------------------
# # -----------  Control Flow  -------------
# # ----------- if, elif, else -------------
# # ----------- Make Decisions -------------
# # ----------------------------------------

uName = "Omer"
cName = "C++"
cPrice = 100
cDiscount = 30
print(f"Hello {uName} The Course \"{cName}\" Price is: {cPrice-cDiscount}") # Hello Omer The Course "C++" Price is: 70

uName = input("Enter your name: ").strip().capitalize()
uCountry = int(input("For Syria(1) \nFor Turkey(2) \nFor Egypt(3) \nFor kuwait(4) \nFor Qatar(5) \nFor somali(6) \nChoose your country:: "))
cName = "C++"
cPrice = 100
country = {
    1: "Syria",
    2: "Turkey",
    3: "Egypt",
    4: "kuwait",
    5: "Qatar",
    7: "Somali",
}
if uCountry==1:
    print(f"Hello {uName} In The \"{cName}\"")
    print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-60}")
elif uCountry==2:
    print(f"Hello {uName} In The \"{cName}\"")
    print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-40}")
elif uCountry==3:
    print(f"Hello {uName} In The \"{cName}\"")
    print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-60}")
elif uCountry==4:
    print(f"Hello {uName} In The \"{cName}\"")
    print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-10}")
elif uCountry==5:
    print(f"Hello {uName} In The \"{cName}\"")
    print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-10}")
elif uCountry==6:
    print(f"Hello {uName} In The \"{cName}\"")
    print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-80}")
else:
    print(f"{uName.capitalize()} since your country is not found, you cannot access the course")


# # -------------------------------------
# # -----------  Nested If  -------------
# # -------------------------------------

uName = input("Enter your name: ").strip().capitalize()
uCountry = int(input("For Syria(1) \nFor Turkey(2) \nFor Egypt(3) \nFor kuwait(4) \nFor Qatar(5) \nFor somali(6) \nChoose your country:: "))
is_student = int(input("Are your student (1, yes) (0, no): ").strip())
cName = "C++"
cPrice = 100
country = {
    1: "Syria",
    2: "Turkey",
    3: "Egypt",
    4: "kuwait",
    5: "Qatar",
    6: "Somali",
}

if uCountry==1:
    if is_student == 1:  
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-50}")
    elif is_student == 0:
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[1]}, The Course Price is: {cPrice-700}")

elif uCountry==2:
    if is_student == 1:  
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[2]}, The Course Price is: {cPrice-60}")
    elif is_student == 0:
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[2]}, The Course Price is: {cPrice-70}")

elif uCountry==3:
    if is_student == 1:  
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[3]}, The Course Price is: {cPrice-60}")
    elif is_student == 0:
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[3]}, The Course Price is: {cPrice-50}")

elif uCountry==4:
    if is_student == 1:  
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[4]}, The Course Price is: {cPrice-10}")
    elif is_student == 0:
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[4]}, The Course Price is: {cPrice}")

elif uCountry==5:
    if is_student == 1:
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[5]}, The Course Price is: {cPrice-10}")
    elif is_student == 0:
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[5]}, The Course Price is: {cPrice}")

elif uCountry==6:
    if is_student == 1: 
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[6]}, The Course Price is: {cPrice-70}")
    elif is_student == 0:
        print(f"Hello {uName} In The \"{cName}\"")
        print(f"Because You Are From {country[6]}, The Course Price is: {cPrice-50}")
else:
    print(f"{uName.capitalize()} since your country is not found, you cannot access the course")



# # --------------------------------------------------------
# # -----------  Ternary Conditional Operator  -------------
# # --------------------------------------------------------
omerName = input("Omer enter your name :) ").strip().capitalize()
aliName = input("Ali enter your name :) ").strip().capitalize()
omerAge = int(input("Omer, enter your age: ").strip())
aliAge = int(input("Ali, enter your age: ").strip())
print(f"{omerAge} greater than {aliName}" if omerAge>aliAge else f"{aliName} greater than {omerName}")


# # ---------------------------------------------------------------
# # -----------  Calculate Age Advanced and Training  -------------
# # ---------------------------------------------------------------

# Write Note
print("#"*70)
print(" You Can Write First Letter Or Full Name of The Time Unit.. ".center(70,"#"))
print("#"*70)

# Collect Age Data
age = input("Please write your age: ").strip()
# Collect Time Unit Data
unit = input("Please Choose Time Unite: Months, Weeks, Days: ").strip().lower()
# Get Time Units
months = int(age)*12
weeks = int(months)*4
days = int(age)*365

if unit == 'months' or unit == 'm':
        print("You Choosed The Unit Months.")
        print(f"You Lived {months:,} Months.")

elif unit == 'weeks' or unit == 'w':
        print("You Choosed The Unit Weeks.")
        print(f"You Lived {weeks:,} Weeks.")

elif unit == 'days' or unit == 'd':
        print("You Choosed The Unit Days.")
        print(f"You Lived {days:,} Days.")


countryOne = ["Syria", "Turkey", "Jordan", "Egypt"]
countryOneDiscount = 50

countryTwo = ["Kuwait", "Bahrain", "Qatar", "Ksa"]
countryTwoDiscount = 30

myCountry = input("Enter your country: ").capitalize().strip()

if myCountry in countryTwo:
    print(f"Hello you have a discount equal to ${countryTwoDiscount}")
elif myCountry in countryOne:
    print(f"Hello you have a discount equal to ${countryOneDiscount}")
else:
    print("You have not discount")








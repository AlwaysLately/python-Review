# -*- coding: utf-8 -*-

#2016.3.28
#python复习纪录

#lambda

f = lambda x,y : x * x + y * y
print f(5,10)

#list

classmates = ['ly','ws','zgq','hwl']

print len(classmates)

print classmates[0],classmates[-1]

classmates.append('ths')

print classmates

classmates.pop()
classmates.insert(0,'zy')

print classmates


#tuple

count = ('ly','ws','hwl')

print count[0]


#dict

information = {'ly':16, 'ws':38, 'hwl':29}

print  information['ly']

print information.get('ly',-1)

if 'ws' in information:
	information['zy'] = 23
for i,j in information.items():
	print (i,j)
	print (i,information.get(i))

information.pop('hwl')

print information.get('hwl', -1)


#a.sort() sorted(a) nlogn  a.reverse()和reversed(a)

a = [4,1,7,2]
print a.sort()
print sorted(a)


#python中装饰器，迭代器

def get_text(name):
	return "hello, {}".format(name)

def text_decorator(func):
	def wrapper(name):
		return "<p>{}</p>".format(func(name))
	return wrapper


#It's what it should be
my_text = text_decorator(get_text)

print my_text('ly')

#by using python syntax @

def text_decorator(func):
	def wrapper(name):
		return "<p>{}</p>".format(func(name))
	return wrapper

@text_decorator
def get_text(name):
	return "hello, {}".format(name)

print get_text('ly')



def p_decorate(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print my_person.get_fullname()



#yield关键字  列表生成器generator



















# Dictionary data type exploration
 
# Holds key value pairs
my_dict={1:1,2:2,3:3,4:4,5:5}

# Lists available methods for this data type
dir(my_dict)

# alternative of type() which gives its class name
my_dict.__class__ 

# Contains check for key values whether it is present
my_dict.__contains__ 

# Deleting the instance of the object
my_dict.__delattr__

# Deleting any 1 key of the dictionary
my_dict.__delitem__ 

# Gives the list of possible methods and functions
my_dict.__dir__

# Documentation related to the datatype
my_dict.__doc__ 

# Compare dictionary with other dictionary as its equal?
my_dict.__eq__(#mydictionary)

# 
my_dict.__format__

my_dict.__ge__
my_dict.__getattribute__
my_dict.__getitem__
my_dict.__gt__
my_dict.__hash__
my_dict.__init__ 
my_dict.__init_subclass__
my_dict.__iter__
my_dict.__le__ 
my_dict.__len__ 
my_dict.__lt__ 
my_dict.__ne__ 
my_dict.__new__ 
my_dict.__reduce__ 
my_dict.__reduce_ex__
my_dict.__repr__
my_dict.__setattr__
my_dict.__setitem__ 
my_dict.__sizeof__ 
my_dict.__str__
my_dict.__subclasshook__
my_dict.clear
my_dict.copy 
my_dict.fromkeys
my_dict.get
my_dict.items
my_dict.keys 
my_dict.pop 
my_dict.popitem
my_dict.setdefault
my_dict.update
my_dict.values

my_list=[1,2,3,4,5]

my_tuple=(1,2,3,4,5)

type(my_dict)
type(my_list)
type(my_tuple)

for k,v in my_dict:
    print (k,v)

for l in my_list:
    print (l)

for m in my_tuple:
    print (m)


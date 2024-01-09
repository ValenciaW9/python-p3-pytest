
#!/usr/bin/env python3

  from not_none_functions import return_not_none
  from boool_functions import test_return_true
  from string_functions import return_string, interpolate_string


def test_return_not_none():
    '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
assert return_not_none() is Not None 


def test_return_true():
        '''in bool_functions, function "return_true" returns True.'''
        assert return_true() == True
       assert return_true() == True

   
def test_interpolate_welcome():
   assert interpolate_welcome('Guido') == 'Welcome, Guido!'

def test_return_string():
    '''in string_functions, function "return_string()" returns a variable of type str.'''
    assert type(return_string()) == str


def test_interpolate_string():
    '''in string_functions, function "interpolate_string()" takes a string and inserts it into another sting 
    assert interpolate_string('Guido') == 'Hello, Guido!'


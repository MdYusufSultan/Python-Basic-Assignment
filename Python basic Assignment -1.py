#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
* (expression)
'hello'(values)
-87.8(value)
-(expression)
((expression))
+(expression)
6(value)


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')
-The variables are symbols that we can store data in program and strings are noting but it is a data. 


# In[ ]:


3.Describe three different data types.
- 1-Boolean-> it is used to reprsent logical value such as True or False.
  2-Integer-> it is used to represent whole number.
  3-Float-> it is used to represent number with decimal point. 


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')
- An expression is a combination of operators,variables and operands.
 the operands are go through with expression do operation and give a value


# In[ ]:


5. This assignment statements, like spam = 10.
get_ipython().set_next_input('What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')
- Expression can be assigned  and statement can only be declare


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1
-bacon contain integer value


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'
'spam' * 3
in both the case output will same 'spamspamspam'


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')
-variable name cannot start with the number


# In[ ]:


9. What three functions can be used to get the integer, floating-point number, or string
get_ipython().set_next_input('version of a value');get_ipython().run_line_magic('pinfo', 'value')
-For Integer->int()
 For Float->float()
 For String->str()   


# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten' + 99 +'burritos'
you can try to concartinate string with number that is not possible
if you want to fix it just treat number as a string
it will concartinate ('Ihave eaten''99''burritos')


#Testing and Debugging
'''Ways to use pdb debugger
1.From Command line- python -m pdb file_name.py
2. In file- import pdb'''

import pdb
def fact(a):
    fact=1
    for i in range (1,a-1):
        pdb.set_trace()
    print(i)
    fact=fact*i
    return fact
if __name__=="__main__":
    print("Factorial is:",fact(3))


import pdb
a=10
pdb.set_trace()
print(a)

'''Output- > c:\users\anirudh\desktop\python\my_cap_assignment\mine\testing_debugging.py(20)<module>()
-> print(a)
(Pdb) p a #HERE  p and a are user enetered..... to check the value of a variable enter p variable_name
10
(Pdb) p b
*** NameError: name 'b' is not defined'''

'''
Commands in pdb
1. p- to print variable value
2. n- to continue execution until next line is reached
3.l - to list the source code
4. b- List all break points
5. h- to list a;ll avaoilable commands----- h pdb
6. q-To quit the debugger
7. u- To go one step back
8. d- one step/ level down

Commands in breakpoint
break linenumber- Sets breakpoint at specified line
break- To list breakpoint set
clear-deletes breakpoint entirely
break functionname- Sets breakpoint to first line of function
disable-  breakpoint is disabled'''

import pdb
a=10
pdb.set_trace()
print(a)

'''Output-
> c:\users\anirudh\desktop\python\my_cap_assignment\mine\fjejfjsakasfkwfww.py(4)<module>()
-> print(a)
(Pdb) break 1
Breakpoint 1 at c:\users\anirudh\desktop\python\my_cap_assignment\mine\fjejfjsakasfkwfww.py:1
(Pdb) break 3
Breakpoint 2 at c:\users\anirudh\desktop\python\my_cap_assignment\mine\fjejfjsakasfkwfww.py:3
(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at c:\users\anirudh\desktop\python\my_cap_assignment\mine\fjejfjsakasfkwfww.py:1
2   breakpoint   keep yes   at c:\users\anirudh\desktop\python\my_cap_assignment\mine\fjejfjsakasfkwfww.py:3
(Pdb) clear
Clear all breaks? yes
Deleted breakpoint 1 at c:\users\anirudh\desktop\python\my_cap_assignment\mine\fjejfjsakasfkwfww.py:1
Deleted breakpoint 2 at c:\users\anirudh\desktop\python\my_cap_assignment\mine\fjejfjsakasfkwfww.py:3
(Pdb) l
  1  	import pdb
  2  	a=10
  3  	pdb.set_trace()
  4  ->	print(a)
[EOF]
(Pdb) n
10
--Return--
> c:\users\anirudh\desktop\python\my_cap_assignment\mine\fjejfjsakasfkwfww.py(4)<module>()->None
-> print(a)
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb'''





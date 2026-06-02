string methods
----------------------

1)case sensitive methods
---------------------------

uppercase()-->each and every line will get capital letters
lowercase()
capitalize()--> only first letter get capital
title()--> only first letter of each word get capital
swap()-->upper changes to lower /lower to upper

2) Allignment operations
--------------------------

center(width,fillchar)--> it gets in center of the line (s.center(28,'-'))
ljust()-->left allign the string (s.ljust(38,'*'))
rjust()-->right alligns the string
zfill()--> pads the str with zeros on the left

3)search and find methods
---------------------------
 find() -->left to right
 rfind()-->for right to last
 index()--> like find but raise an error
 r.index()--> like rfind, but raise an error
 count()--> counts how many it appears

 4)Replace and modify methods
 -----------------------------
 replace(old,new)
 translate()-->replace characters using numbers in a transition table(s.translate(s.maketrans('python','1234'))
 maketrans()-->it gives in a table
                                                                      
  5)splitting and joining methods
 ---------------------------------
 split()--> splits the string into a list
 rsplit()-->splits from right side
 splitlines()--> splits  at line breaks("/n")
 join()-->joins the elements with separator
 partition()-->splits into a 3-parts (tuple) at first
 rpartition()-->splits into 3- parts(tuple)at last

 encode()-->to convert strings into bytes
 decode()--> to convert bytres to strings

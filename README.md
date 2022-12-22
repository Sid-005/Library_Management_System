# Library_Management_System
Stores the files containing the source code for the library management system created for the purpose of my high-school year end project

PRE-REQUISITES:
1. Computer must have Python3 (versions Python 3.6 or later)
2. MySQL version 5.7 or later
3. Install the python - MySQL connector using pip install (refer to https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html)
4. Operating System: Windows 10 or later

This code is designed to be run on windows OS ONLY. Other operating systems shall yield undesirable errors caused by the importing of the ctypes module.

PROJECT DESCRIPTION:
Aims to build a basic library management system, using a GUI interface generated by the tkinter module in Python. 
Data is stored in a MySQL database, accessed using the mysql.connector module (refer to installation instructions attached in point 3 above)
Implements basic functions that performs the following tasks:
  - View all the transactions carried out within the library (books issued and returned in the past)
  - Search for records of transactions of particular books within the library
  - Add/Delete/Update the books found in the library
  - Allow user to issue/return books found in the library (displays appropriate error messages for error handling)
 Modules used:
    - ctypes
    - tkinter
    - mysql.connector
For ideal use of this system, it is recommended to connect it with a database of members or valid users, who are allowed to issue books from the library.

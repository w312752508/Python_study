import sys
import os
file_user = "user_list"
file_pass = "pass_list"

with open(file_user) as objec_user :
     for i in objec_user:
         with open(file_pass) as objec_pass :
             for j in objec_pass :
                 os.system("ssh i:j@ip  ")
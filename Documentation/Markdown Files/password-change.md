# Changing HLA password
To change the HLA password, we first must hash the password and then store it into our Python Script views.py. We are using a module called hashlib to encrypt our password. 

## What is hashing
Hashing changes a string into a inreversable encrypted code. This makes it a lot harder for people to know the password even if they have the source code! 

## How to create a new password
To create a new password, we need to run the password through a hash function. We run the password through this:

```Python
password="thepasswordyouwant"
print(str(hashlib.sha256(password.encode()).hexdigest()))
```
The script above will encrypt the password and print the result. Once you are finished encrypting the password. You can copy and paste the output into views.py on line 68.

```Python
# Change this line
if str(hashlib.sha256(password.encode()).hexdigest()) == '91aca2fdcc84a7c4171d103b5ff80b82bc1f4098a091b13d6398b224308a25fd':
```

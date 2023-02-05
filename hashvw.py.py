# !/usr/bin/env python3
# -*- coding: utf-8 -*- 
import hashlib
from sys import exit
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Hash Viewer'))


def hash_password(password, algorithm='sha256'):
    hash_object = hashlib.new(algorithm, password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

try:
    password = input("Enter the word or number: ")
except KeyboardInterrupt:
    exit()
    
print("HASH".center(50,"-"))    
print("sha256:", hash_password(password, 'sha256'))
print("sha384:", hash_password(password, 'sha384'))
print("sha512:", hash_password(password, 'sha512'))
print("md5:", hash_password(password, 'md5'))
print("sha1:", hash_password(password, 'sha1'))
print("sha224:", hash_password(password, 'sha224'))


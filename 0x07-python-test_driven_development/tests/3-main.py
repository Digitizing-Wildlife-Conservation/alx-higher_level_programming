#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Moses", "Mucahi")
say_my_name("Sam", "Ngéthe")
say_my_name("Bob")
try:
    say_my_name(12, "Ngéthe")
except Exception as e:
    print(e)

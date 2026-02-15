# Exercise 19: Etc Passwd To Dict

## Description

Write a function, passwd_to_dict, that reads from a Unix-style pass- word file, commonly stored as /etc/passwd, and returns a dict based on it. Each line is one user record, divided into colon-separated fields. The first field (index 0) is the username, and the third field (index 2) is the user’s unique ID number. The function passwd_to_dict should return a dict based on /etc/passwd in which the dict’s keys are usernames and the values are the users’ IDs.

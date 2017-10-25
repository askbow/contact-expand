#!/usr/bin/python
# Denis Borchev
# contactexpand.py - a contact list generator for Cisco Jabber

import csv



def genFull():
    # generates full list for all users
    contactsReader = csv.DictReader(open(r'contacts.csv'))
    userlist = list()
    for row in contactsReader:
        userlist.append((row['Contact ID'] , row['Contact Domain'],row['Nickname'],row['Group Name'] ))
    with open(r'output.csv', 'w', newline='') as csvfile:
        resultwriter = csv.writer(csvfile, dialect = 'excel')
        for row in userlist:
            print(row)
            for inrow in userlist:
                if not inrow[0] == row[0]: resultwriter.writerow([row[0],row[1],inrow[0],row[1],row[2],row[3]])
                #
def genNewUser(name=list()):
    # generates lists for selected users and adds them to everybody else's individual contact lists
    if name == list() : return genFull()
    contactsReader = csv.DictReader(open(r'contacts.csv'))
    userlist = list()
    for row in contactsReader:
        userlist.append((row['Contact ID'] , row['Contact Domain'],row['Nickname'],row['Group Name'] ))
    with open(r'output.csv', 'w', newline='') as csvfile:
        resultwriter = csv.writer(csvfile, dialect = 'excel')
        for row in userlist:
            print(row)
            for inrow in userlist:
                if not inrow[0] == row[0]: 
                    if inrow[0] in name: resultwriter.writerow([row[0],row[1],inrow[0],inrow[1],inrow[2],inrow[3]])
        for row in userlist:
            if row[0] in name: 
                for inrow in userlist:
                    if not inrow[0] == row[0]: resultwriter.writerow([row[0],row[1],inrow[0],inrow[1],inrow[2],inrow[3]])
        

if __name__ == '__main__':
    namelist = ['user1',
    'user2',
    'user3',] # list of users for whom to generate contacts
              # i.e. newcoming employees
              # if empty - generate full list for all users
    genNewUser(name=namelist)
    # EOF

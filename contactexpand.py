#!/usr/bin/python
# Denis Borchev
# contactexpand.py - a contact list generator for Cisco Jabber

import csv

def LoadContacts():
    userlist = list()
    with open(r'contacts.csv') as csvfile:
        contactsReader = csv.DictReader(csvfile)
        for row in contactsReader:
            userlist.append((row['Contact ID'] , row['Contact Domain'],row['Nickname'],row['Group Name'] ))
    return userlist

def genFull(resultwriter=None, userlist=None):
    # generates full list for all users
    for row in userlist:
            #
            for inrow in userlist:
                if not inrow[0] == row[0]: resultwriter.writerow([row[0],row[1],inrow[0],row[1],row[2],row[3]])
                #
def genNewUser(name=list(),resultwriter=None, userlist=None):
    # generates lists for selected users and adds them to everybody else's individual contact lists
    if name == list() : return genFull(resultwriter, userlist)
    #
     for row in userlist:
            #
            for inrow in userlist:
                if not inrow[0] == row[0]: 
                    if inrow[0] in name: resultwriter.writerow([row[0],row[1],inrow[0],inrow[1],inrow[2],inrow[3]])
            #
            if row[0] in name: 
                for inrow in userlist:
                    if not inrow[0] == row[0]: resultwriter.writerow([row[0],row[1],inrow[0],inrow[1],inrow[2],inrow[3]])
        

if __name__ == '__main__':
    namelist = ['user1',
    'user2',
    'user3',] # list of users for whom to generate contacts
              # i.e. newcoming employees
              # if empty - generate full list for all users
    userinput = LoadContacts()
    with open(r'output.csv', 'w', newline='') as csvfile:
        result = csv.writer(csvfile, dialect = 'excel')
        genNewUser(name=namelist, resultwriter=result, userlist=userinput)
    # EOF

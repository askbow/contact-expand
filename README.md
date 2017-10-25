CONTACT EXPAND is a simple Python script designed to create personal address books for contacts present in a CUCM address list. Takes contacts.csv as input and creates an output.csv which can be uploaded to CUCM. 

N.B.: CUCM=="Cisco Unified Communications Manager"

Moved from https://github.com/askbow/cloaked-octo-ironman/tree/master/contactexpand

New version is less fooling around and more doing the job:
- generate a full list (useful if restoring system operation after certail failure conditions / new setups)
- generate a partial list (useful when adding new users to the system, i.e. newly hired people)


Notes:

CUCM / presence / Cisco Jabber contact list addition mechanism is not entirely idempotent.
I.e. you will have duplicate contacts, if you add one several times.
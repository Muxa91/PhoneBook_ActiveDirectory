# -*- coding: utf-8 -*-
from ldap3 import Server, Connection, ALL
from operator import itemgetter
import userpass



server = Server(userpass.ip, get_info=ALL)
conn = Connection(server, read_only=True, user=userpass.user, password=userpass.password)
conn.bind()
# IpPhone
conn.search('dc=eskaro,dc=net', '(&(objectclass=person)(telephoneNumber=*))',attributes=['sn','givenName','title','telephoneNumber','mail'])

employees=[]
result=[]
def list():
    with open("phoneBook.txt", "w",encoding='utf-8') as file:
        for x in conn.entries:
            firsname =' ' if x['sn'] == None else x['sn'][0]
            givenName = ' ' if x['givenName'] == None else x['givenName'][0]
            title = ' ' if x['title'] == None else x['title'][0]
            IpPhone = ' ' if x['telephoneNumber'] == None else x['telephoneNumber'][0]
            mail = ' ' if x['mail'] == None else x['mail'][0]

            employees.append([firsname,givenName,IpPhone,title,mail])
            result=sorted(employees)

        for x in result:
            file.write(x[0] + " " + x[1] + ";" + x[2] + ";" + x[3] + ";"+x[4] + "|")




def person():
    x = open("phoneBook.txt", "r", encoding="UTF-8")
    list = x.read().split("|")
    for y in list:
        person = y.split(";")
        result.append(person)
    print(result)

if __name__ == "__main__":
    list()



# coding: utf-8

# In[ ]:

import argparse
import sys


# In[ ]:

parser=argparse.ArgumentParser()
parser._optionals.title = "Arguments"
parser.add_argument('-a',help="File Path for file a.  Required unless -stdInA is used", required=False,default="%#$")
parser.add_argument('-stdInA',help="Use stdin for A", action='store_true')
args = vars(parser.parse_args())


# In[ ]:

if len(sys.argv)==1:
    print("Please provide a file to format")
    sys.exit(1)


# In[ ]:

def processFile(FILENAME,useStdIn):
    if not useStdIn:
        header=""
        lines=[]
        for line in open(FILENAME,"r"):
            if line[0]=="#":
                header+=line.strip()+"\n"
            else:
                lines.append(line.strip().split())
    else:
        header=""
        lines=[]
        for line in sys.stdin:
            if line[0]=="#":
                header+=line.strip()+"\n"
            else:
                lines.append(line.strip().split())
    return header, [[x[0],int(x[1]),int(x[2]),x[3],int(x[4]),int(x[5]), x[6:]] for x in lines]


# In[ ]:

def formatContacts(contacts,delim):
    return [delim.join([str(y) for y in x[:-1]])+delim+delim.join(x[-1]) for x in contacts]


# In[ ]:

def flipContacts(contacts):
    i=0
    while i<len(contacts):
        contact=contacts[i]
        if contact[0] > contact[3]:
            contacts[i]=[contact[3],contact[4],contact[5],contact[0],contact[1],contact[2],contact[6]]
        elif contact[0]==contact[3]:
            if contact[1] > contact[4]:
                contacts[i]=[contact[3],contact[4],contact[5],contact[0],contact[1],contact[2],contact[6]]
            elif contact[1]==contact[4]:
                if contact[2] > contact[5]:
                    contacts[i]=[contact[3],contact[4],contact[5],contact[0],contact[1],contact[2],contact[6]]
        i+=1
    return contacts


# In[ ]:

header,A=processFile(args['a'],args['stdInA'])
    
res=flipContacts(A)
res=formatContacts(res,"\t")
if len(header)!=0:
    print(header)
print("\n".join(res))


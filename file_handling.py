f =open("file.txt","r") 
data = f.read()
print(data)
f.close()

with open ("file.txt ","r") as f :
    data = f.read()
    print( data)

str = " i am fine how are you hello  "
f=open( "myfile.txt","w")
f.write (str)
f.close 


# f =open("file.txt") 
# line = f.readlines()
# # print ( line , type(line ))
# while ( line !=""):
#     print ( line )
#     # line= f.readlines()
# f. close()

with open ( "myfile.txt") as f:
    content = f. read( )

    if "hello " in content:
        print ( " yes ")
    else:
        print ( " No " )
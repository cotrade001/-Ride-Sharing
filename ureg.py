#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="mypath")
cur = con.cursor()
print("""
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post" enctype="multipart/form-data">
        <input type="text" placeholder="Entername" name="name"><br>
        <input type="text" placeholder="Address" name="address"><br>
        <input type="email" placeholder="email" name="email"><br>
        <input type="password" placeholder="password" name="pass"><br>
        <input type="submit" name="submit">
    </form>
</body>
</html>
""")
form = cgi.FieldStorage()

name = form.getvalue("name")
address = form.getvalue("address")
email = form.getvalue("email")
password = form.getvalue("pass")
Submit = form.getvalue("submit")

if Submit != None:
    x = """insert into data(name,address,email,password) values('%s','%s','%s','%s')""" % (name, address, email, password)
    cur.execute(x)
    con.commit()
    print("""
    <script>
       alert("registered successfully")
    </script>
    """)

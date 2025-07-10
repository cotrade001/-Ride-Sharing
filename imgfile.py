#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql,cgi,cgitb,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="check_img")
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
        <input type="file" placeholder="Photo" name="photo"><br>
        <input type="submit" name="submit">
    </form>
</body>
</html>
""")

form = cgi.FieldStorage()

Name = form.getvalue("name")
Address = form.getvalue("address")
Email = form.getvalue("email")
Password = form.getvalue("pass")

Submit = form.getvalue("submit")

if Submit != None:
    Image =form['photo']
    fn = os.path.basename(Image.filename)
    open("images/" + fn,"wb").write(Image.file.read())

    x = """insert into img(name,address,email,password,image) values('%s','%s','%s','%s','%s')""" %(Name,Address,Email,Password,fn)
    cur.execute(x)
    con.commit()
    print("""
       <script>
           alert("Registered Successfully")
       </script>   
    """)
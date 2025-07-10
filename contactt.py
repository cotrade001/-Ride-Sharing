#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")

import pymysql
import cgi
import cgitb

# Enable debugging
cgitb.enable()

# Connect to MySQL Database
try:
    con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
    cur = con.cursor()
except pymysql.MySQLError as e:
    print(f"<h3 style='color:red;'>Database connection failed: {e}</h3>")
    exit()

# Get form data
form = cgi.FieldStorage()
name = form.getvalue("name")
email = form.getvalue("email")
subject = form.getvalue("subject")
message = form.getvalue("message")
submit = form.getvalue("submitc")

# Validate form data
if name and email and message:
    try:
        sql = "INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (name, email, subject, message))
        con.commit()
        message_status = "<h3 style='color:green;'>Thank you! Your message has been submitted successfully.</h3>"
    except pymysql.MySQLError as e:
        message_status = f"<h3 style='color:red;'>Error saving data: {e}</h3>"
    finally:
        cur.close()
        con.close()
else:
    message_status = "<h3 style='color:red;'>Error: Please fill all required fields.</h3>"

# HTML Content
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <link rel="stylesheet" href="nav.css">

    <style>
        .contact-section {{ padding: 60px 0; margin-top: 30px; }}
        .contact-form {{ background: #fff; padding: 30px; border-radius: 10px; }}
        .form-control {{ border-radius: 5px; }}
        .contact-info {{ padding: 30px; border-radius: 10px; text-align: center; }}
        .contact-info i {{ font-size: 30px; color: #007bff; margin-bottom: 10px; }}
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg fixed-top">
        <div class="container">
            <a class="navbar-brand" href="home.html">
                <img src="./img/ridd.png" alt="Logo" style="height:75px; width: 81px;">
            </a>

            <!-- Mobile Toggle Button -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>

            <!-- Navbar Links -->
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item"><a class="nav-link" href="home.html"><i class="fa-solid fa-house" style="margin-right: 10px;"></i>Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#"><i class="fa-solid fa-envelope" style="margin-right: 10px;"></i>Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Contact Section -->
    <div class="container contact-section">
        <div class="row">
            <!-- Contact Form -->
            <div class="col-md-7">
                <div class="contact-form">
                    <h3 class="mb-4">Get in Touch</h3>
                    {message_status}
                    <form action="contactt.py" method="POST" enctype="multipart/form-data">
                        <div class="mb-3">
                            <label for="name" class="form-label">Your Name</label>
                            <input type="text" class="form-control" name="name" placeholder="Enter your name" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">Your Email</label>
                            <input type="email" class="form-control" name="email" placeholder="Enter your email" required>
                        </div>
                        <div class="mb-3">
                            <label for="subject" class="form-label">Subject</label>
                            <input type="text" class="form-control" name="subject" placeholder="Enter subject">
                        </div>
                        <div class="mb-3">
                            <label for="message" class="form-label">Message</label>
                            <textarea class="form-control" name="message" rows="4" placeholder="Type your message here" required></textarea>
                        </div>
                        <input type="submit" name="submitc" class="btn btn-primary w-100" value="Send Message">
                    </form>
                </div>
            </div>

            <!-- Contact Info -->
            <div class="col-md-5">
                <div class="contact-info">
                    <h3>Contact Information</h3>
                    <p><i class="bi bi-geo-alt"></i> 436 NSR Main road Saibaba colony Coimbatore</p>
                    <p><i class="bi bi-envelope"></i> officialvimal01@gmail.com</p>
                    <p><i class="bi bi-telephone"></i> +919973788650</p>

                    <!-- Google Map Embed -->
                    <iframe src="https://www.google.com/maps/embed?..." width="100%" height="200" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
""")

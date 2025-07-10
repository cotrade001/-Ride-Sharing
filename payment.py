#!C:/Users/VIMAL GUPTA/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib, random, string, os, sys, json, razorpay

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="rideshare")
cur = con.cursor()


# Retrieve form data
form = cgi.FieldStorage()
cid = form.getvalue("cust_id")
booking_id = form.getvalue("book_id")




print("""
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<title>Ride share Payment</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>


<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');


* {
margin: 0;
padding: 0;
box-sizing: border-box;
}

body {
font-family: 'Poppins', sans-serif;
background: linear-gradient(135deg, #0f2027, #203a43, #ff0080, #00d4ff);
height: 100vh;
display: flex;
align-items: center;
justify-content: center;
}

.payment-container {
background: rgba(255, 255, 255, 0.2);
backdrop-filter: blur(15px);
border-radius: 20px;
padding: 30px;
width: 95%;
max-width: 500px;
box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
color: #fff;
animation: fadeIn 1s ease;
}

@keyframes fadeIn {
from {
opacity: 0;
transform: scale(0.95);
}

to {
opacity: 1;
transform: scale(1);
}
}

h2 {
text-align: center;
margin-bottom: 20px;
font-weight: 600;
color: #ff3d77;
}

.tabs {
display: flex;
justify-content: space-between;
margin-bottom: 25px;
background: rgba(255, 255, 255, 0.15);
border-radius: 10px;
flex-wrap: wrap;
}

.tab {
flex: 1 1 25%;
text-align: center;
padding: 12px;
cursor: pointer;
transition: 0.3s;
font-weight: bold;
border-radius: 10px;
color: #fff;
}

.tab:hover {
background: rgba(255, 255, 255, 0.3);
}

.tab.active {
background: #ff3d77;
color: #fff;
}

.form-group {
margin-bottom: 18px;
}

label {
display: block;
margin-bottom: 6px;
font-weight: 500;
}

input {
width: 100%;
padding: 10px;
border: none;
border-radius: 8px;
outline: none;
background: rgba(255, 255, 255, 0.9);
color: #333;
font-weight: 500;
}

.error {
color: #ff4d4d;
font-size: 13px;
}

.submit-btn {
width: 100%;
padding: 12px;
border: none;
border-radius: 10px;
background: #ff3d77;
color: #fff;
font-weight: bold;
font-size: 16px;
cursor: pointer;
transition: background 0.3s;
}

.submit-btn:hover {
background: #e6326b;
}

.method-section {
display: none;
animation: fadeIn 0.5s ease;
}

.method-section.active {
display: block;
}

p.cash-note {
text-align: center;
font-weight: 500;
font-size: 15px;
margin-top: 10px;
color: #fff;
}
</style>
</head>

<body>

<div class="payment-container">
<h2>💳 Ride Share Payment</h2>

<div class="tabs">
<div class="tab active" onclick="selectTab('card')">Card</div>
<div class="tab" onclick="selectTab('upi')">UPI</div>
<div class="tab" onclick="selectTab('netbanking')">NetBanking</div>
<div class="tab" onclick="selectTab('cash')">Cash</div>
</div>

<form onsubmit="return validateForm()" method="post" >
<!-- Card -->
<div class="method-section active" id="card">
<div class="form-group">
    <label>Card Number</label>
    <input type="text" name="card_number" id="card_number" placeholder="1234 5678 9012 3456">
    <span class="error" id="card_error"></span>
</div>
<div class="form-group">
    <label>Expiry Date</label>
    <input type="text" name="expiry_date" id="expiry_date" placeholder="MM/YY">
</div>
<div class="form-group">
    <label>CVV</label>
    <input type="password" name="cvv" id="cvv" placeholder="123">
</div>
</div>

<!-- UPI -->
<div class="method-section" id="upi">
<div class="form-group">
    <label>UPI ID</label>
    <input type="text" name="upi_id" id="upi_id" placeholder="name@upi">
    <span class="error" id="upi_error"></span>
</div>
</div>

<!-- Netbanking -->
<div class="method-section" id="netbanking">
<div class="form-group">
    <label>Bank Name</label>
    <input type="text" name="bank_name" id="bank_name" placeholder="e.g. SBI, HDFC">
</div>
<div class="form-group">
    <label>Account Number</label>
    <input type="text" name="account_number" id="account_number" placeholder="1234567890">
</div>
<div class="form-group">
    <label>IFSC Code</label>
    <input type="text" name="ifsc" id="ifsc" placeholder="SBIN0000001">
</div>
</div>

<!-- Cash -->
<div class="method-section" id="cash">
<p class="cash-note">You have selected <strong>Cash Payment</strong>.<br>
    Please pay the exact fare to the driver at the end of your ride.</p>
</div>

""")

q = """SELECT * 
       FROM booking 
       WHERE booking_id = %s AND custid = %s"""
cur.execute(q, (booking_id, cid))
result = cur.fetchone()

if result:
    passengers = int(result[9])
    priceseat = float(result[10])
    total_price = passengers * priceseat

    print(f"""
        <form method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label>Amount (₹){total_price}</label>
                <input type="hidden" name="seekid" value="{cid}">
                <input type="hidden" name="bookeid" value="{booking_id}">
                <input type="hidden" name="amount" value="{total_price}">
                <span class="error" id="amount_error"></span>
            </div>

            <input type="hidden" name="method" id="method" value="card">
            <input type="submit" name="subpay" class="submit-btn" value="Proceed to Pay">
        </form>
    """)


print("""

      
  </div>

  <script>
    function selectTab(method) {
      document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
      document.querySelector(`.tab[onclick="selectTab('${method}')"]`).classList.add('active');

      document.querySelectorAll('.method-section').forEach(section => section.classList.remove('active'));
      document.getElementById(method).classList.add('active');

      document.getElementById('method').value = method;
    }

    function validateForm() {
      const method = document.getElementById("method").value;
      let valid = true;
      document.querySelectorAll(".error").forEach(e => e.innerText = "");

      if (method === "card") {
        const card = document.getElementById("card_number").value.trim().replace(/\s/g, '');
        const cvv = document.getElementById("cvv").value.trim();
        if (!/^\d{16}$/.test(card)) {
          document.getElementById("card_error").innerText = "Enter 16-digit card number";
          valid = false;
        }
        if (!/^\d{3}$/.test(cvv)) {
          alert("Invalid CVV");
          valid = false;
        }
      } else if (method === "upi") {
        const upi = document.getElementById("upi_id").value.trim();
        if (!/^[\w.-]+@[\w]+$/.test(upi)) {
          document.getElementById("upi_error").innerText = "Invalid UPI ID";
          valid = false;
        }
      } else if (method === "netbanking") {
        const acc = document.getElementById("account_number").value.trim();
        const ifsc = document.getElementById("ifsc").value.trim();
        if (!/^\d{9,18}$/.test(acc)) {
          alert("Invalid Account Number");
          valid = false;
        }
        if (!/^[A-Z]{4}0[A-Z0-9]{6}$/.test(ifsc)) {
          alert("Invalid IFSC code");
          valid = false;
        }
      } else if (method === "cash") {
        // No specific validation required
      }

      const amount = document.getElementById("amount").value.trim();
      if (!/^\d+(\.\d{1,2})?$/.test(amount)) {
        document.getElementById("amount_error").innerText = "Enter valid amount";
        valid = false;
      }

      return valid;
    }
  </script>

</body>
</html>

 """)
# Extract common fields
if form.getvalue("subpay"):
    method = form.getvalue("method")
    amount = form.getvalue("amount")
    seekid = form.getvalue("seekid")
    bookid = form.getfirst("bookeid")

    card_number = expiry_date = cvv = None
    upi_id = None
    bank_name = account_number = ifsc = None

    if method == "card":
        card_number = form.getvalue("card_number")
        expiry_date = form.getvalue("expiry_date")
        cvv = form.getvalue("cvv")
    elif method == "upi":
        upi_id = form.getvalue("upi_id")
    elif method == "netbanking":
        bank_name = form.getvalue("bank_name")
        account_number = form.getvalue("account_number")
        ifsc = form.getvalue("ifsc")

    insert_query = """
        INSERT INTO payments (
            method, card_number, expiry_date, cvv,
            upi_id, bank_name, account_number, ifsc,
            amount, seekid, bookid
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        method, card_number, expiry_date, cvv,
        upi_id, bank_name, account_number, ifsc,
        amount, seekid, bookid
    )

    try:
        cur.execute(insert_query, values)
        con.commit()
        z = """UPDATE booking 
               SET status = %s, paymentmethod = %s, paymentstatus =%s 
               WHERE booking_id = %s AND custid = %s"""

        cur.execute(z, ('booked',  method, 'paid', bookid, cid))
        con.commit()

        # Show success and redirect
        print(f"""
            <script src=\"https://cdn.jsdelivr.net/npm/sweetalert2@11\"></script>
            <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css\"/>

            <script>
                Swal.fire({{
                    title: '🎉 <span style=\"color:#00f7ff; font-size: 24px;\">Payment Successful!</span>',
                    html: `
                        <div style=\"font-size: 18px; color: #ffffff; text-align: center;\">
                            <b>🚖 Your ride has been booked successfully!</b><br><br>
                            <span style=\"font-size: 16px;\">🏁 Your driver will be assigned shortly. Stay tuned! 🚗</span><br><br>
                            <span style=\"color: #ffc107; font-weight: bold;\">Thank you for choosing RideShare!</span>
                        </div>
                    `,
                    icon: 'success',
                    background: 'radial-gradient(circle, #1a1a2e 0%, #16213e 100%)',
                    color: '#ffffff',
                    confirmButtonText: '🚀 Go to Dashboard',
                    confirmButtonColor: '#ff005c',
                    showCancelButton: true,
                    cancelButtonText: '❌ Close',
                    cancelButtonColor: '#555',
                    timer: 8000,
                    timerProgressBar: true,
                    showClass: {{
                        popup: 'animate__animated animate__fadeInDown'
                    }},
                    hideClass: {{
                        popup: 'animate__animated animate__fadeOutUp'
                    }},
                    customClass: {{
                        popup: 'swal2-glow'
                    }}
                }}).then((result) => {{
                    if (result.isConfirmed) {{
                        window.location.href = \"userdashboard.py?cust_id={cid}\";
                    }}
                }});
            </script>

            <style>
                .swal2-glow {{
                    box-shadow: 0 0 30px 10px rgba(255, 0, 92, 0.8);
                    border-radius: 1rem;
                    padding: 20px;
                }}
            </style>
        """)


    except Exception as e:
          print(f"<p style='color: red;'>Error Processing Payment: {str(e)}</p>")
          con.rollback()  # Rollback on error

    finally:
          cur.close()
          con.close()

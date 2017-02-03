import webapp2
import re

user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_re = re.compile(r"^.{3,20}$")
email_re = re.compile("^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    if user_re.match(username) == None or not username:
        return False
    else:
        return True

def valid_password(password):
    if password_re.match(password) == None and not password:
        return False
    else:
        return True

def valid_email(email, username, password):
    if email:
        if email_re.match(email) == None:
            if valid_password(password) == True and valid_username(username) == True:
                return True
            if valid_password(password) == False or valid_username(username) == False:
                return False

page_header ="""
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type='text/css'>
        .error {
            color: red;
            }
    </style>
</head>
<body>"""

page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):

    def get(self):

        def build_page(signup_table):

            userElement = self.request.get("userError")
            passwordElement = self.request.get("passwordError")
            verifyElement = self.request.get("verifyError")
            emailElement = self.request.get("emailError")
            userValue = self.request.get("user")
            emailValue = self.request.get("email")

            username_input = "<tr><td>Username</td><td><input type='text' name='username' value=" + userValue + "> </input> &nbsp; <span class='error'>" + userElement + "</span></td></tr>"

            password_input = "<tr><td>Password</td><td><input type='password' name='password'> &nbsp; <span class='error'>" + passwordElement + "</span></td></tr>"

            verify_input = "<tr><td>Verify Password</td><td><input type='password' name='verify'> &nbsp; <span class='error'>" + verifyElement + "</span></td></tr>"

            email_input = "<tr><td>Email (optional)</td><td><input type='text' name='email' value=" + emailValue + "> &nbsp; <span class='error'>" + emailElement + "</span></td></tr>"

            inputs = username_input + password_input + verify_input + email_input

            submit = "<input type='submit'/>"

            tableform = "<table>" + inputs + "</table>"

            form = ("<form action='/signup' method='post'>" + tableform + submit + "</form>")

            header = "<h2>Signup</h2>"

            return header + form

        content = build_page("")

        self.response.write(page_header + content + page_footer)

class Signup(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""

        if valid_username(username) == False:
            username_error = "Please enter a valid username."
        if valid_password(password) == False:
            password_error = "Please enter a valid password."
        if verify == '':
            verify_error = "Please verify password."
        if verify != password:
            verify_error = "Passwords do not match."
        if valid_email(email, username, password) == False:
           email_error = "Please enter a valid email."

        if not username_error and not password_error and not verify_error and not email_error:
            self.response.write('<h2>Welcome ' + username + '!</h2>')
        else:
            self.redirect("/?userError=" + username_error + "&passwordError=" + password_error + "&verifyError=" + verify_error + "&emailError=" + email_error + "&user=" + username + "&email=" + email)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', Signup)
], debug=True)

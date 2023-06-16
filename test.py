from firebase import Firebase
import jwt
config = {
  "apiKey": "AIzaSyAn1bv1HgddTY8i2KJIUpSjbt2z5VeysIs",
  "authDomain": "iris-web-team.firebaseapp.com",
  "databaseURL": "https://iris-web-team-default-rtdb.firebaseio.com",
  "projectId": "iris-web-team",
  "storageBucket": "iris-web-team.appspot.com",
  "messagingSenderId": "923629246355",
  "appId": "1:923629246355:web:12e9f02d1b6272f39bfa66",
  "measurementId": "G-NJKHGW72RV"
  }

firebase = Firebase(config)
auth = firebase.auth()
# user_ = auth.sign_in_with_email_and_password("mbsaiaditya@gmail.com" ,"kakashi")
# print(user_)
token="eyJhbGciOiJSUzI1NiIsImtpZCI6IjY3YmFiYWFiYTEwNWFkZDZiM2ZiYjlmZjNmZjVmZTNkY2E0Y2VkYTEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaXJpcy13ZWItdGVhbSIsImF1ZCI6ImlyaXMtd2ViLXRlYW0iLCJhdXRoX3RpbWUiOjE2ODY3NDcxNzAsInVzZXJfaWQiOiJmeXh4Mjl1eTlXZmRsdWlSczlEVFBPb0VVYU0yIiwic3ViIjoiZnl4eDI5dXk5V2ZkbHVpUnM5RFRQT29FVWFNMiIsImlhdCI6MTY4Njc0NzE3MCwiZXhwIjoxNjg2NzUwNzcwLCJlbWFpbCI6ImhheW9jaXQ1MjRAYW53YXJiLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImhheW9jaXQ1MjRAYW53YXJiLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.DT0VEb3DUGEAHqJ2AqNF6N_khNjkh-5rdn0TIu-RC6zUNIVqWLMJ0iMfNUghNYpOSUN4wfRDYYvePRRm_6Yu_YJ2ljgAEfDOopAdaUlG4tKIBPOYnikmul1LY7GumWCpgBLaEOS7ACjM_Lsvoq2qICHD3EehUZl8ekqgVKT-G2gYY0-IdPZadSGrgBijxaTt73dPs4-dPzhSgu88EAwyYvQzStUks6VwxcaL1JKefGypJamEzzK86s-t9TcD1xBywJakITg4PcUy-KAHsQhfb6026fPPi6wUr4V6kPzul4nHQk83dPoyLOlZMtR15SzYomLrZrL8-Q_UA5qMwtAjCw"
# payload = jwt.decode(token, options={"verify_signature": False})
# print(payload)
user = auth.get_account_info(token)
print(user.get("users")[0].get("emailVerified"))

class User:
    username='admin'
    email=''
    city=''

    def __init__(self,email,city):
       self.email=email
       self.city=city

    def __str__(self):
        return f" {self.username} {self.email} {self.city}"

user= User('user@mail.com','pune')

#print(f"Username is {user.username} {user.email} {user.city}")
print(f"UserDetails {user}")

age=input('Enter your Age: ')

useAge=int(age)

if( useAge< 0):
    print('Enter correct age')
elif useAge <18:
    print('Not Allowed to vote')
elif useAge >=18 and useAge <70:
    print('allowed to vote')
else:
    print('senior citizen')

# array 
userNames=['Admin','Manager','QA']
for name in userNames:
    print(name)

projectTypes=['HRMS','IT','Banking','Finance']

dummy=[]

for project in projectTypes:
    if project =='Banking':
        continue
    else:
        print(f"Developing {project}")
dummy.append('Banking')
print(f"Developed : {dummy}")
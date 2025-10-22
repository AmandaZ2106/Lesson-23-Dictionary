student_data={'ID1':
              {'name':['Sara'],
               'class':['VI'],
               'age':['11']},
               'ID2':
               {'name':['David'],
                'class':['VII'],
                'age':['12']},
                'ID3':
                {'name':['Sara'],
               'class':['VI'],
               'age':['11']} }
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)
def st_info(name,*cr):
    if cr!=():
        print(f'''
        NAME:{name}
        Course:{cr[0]}
        ''')
    else:
        print(f'''
        NAME:{name}
        Course:B.tech
        ''')
a=input("Enter your name: ")
b=input("Enter your course: ")
st_info(a,b)
#st_info("rahul")

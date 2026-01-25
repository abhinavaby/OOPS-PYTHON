class student:
    collage_name="SJCET-PALAI"#class attribute
    name="name"
    def __init__(self,name,age):
        self.name=name
        self.age=age



s1=student("Arjun",18)#object attribute
print(s1.name,s1.age,s1.collage_name)
print(student.collage_name)#same result
print(s1.name)#object attribute>class attribute


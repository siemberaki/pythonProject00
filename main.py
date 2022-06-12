class  usa():
    def language(self):
        print("english and hindi")

    def capital(self):
        print("washnghton dc ")

class hindi():

    def language(self):
        print("hindi")

    def capital(self):
        print("mombhai" )

obj_usa=usa()
obj_hindi=hindi()


for counter in (obj_usa,obj_hindi):
    counter.language()
    counter.capital()






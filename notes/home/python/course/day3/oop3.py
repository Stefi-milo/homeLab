# methods = functions defined on classes
# method is a function defined in class that always accepts
# at least one parametr - the object on which the method is called
# this parameter is traditionaly named self:

class Human:
    firstname = '-'
    lastname = '-'

    def fullname(self):
        # in the method self is the object we are working on
        return self.firstname+' '+self.lastname

    # if method has additional parameters they are passed after the self
    def greeting(self,how='Hello'):
        print(how,self.fullname(),'!')

people = [ Human(),Human() ]
people[0].firstname = 'Adam'
people[1].firstname = 'Eva'

print()
for someone in people:
    print(f'{someone.fullname()=}')
    someone.greeting('A big hello')
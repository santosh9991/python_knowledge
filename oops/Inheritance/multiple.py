class A():
    def a_method(self):
        print "I am in A method"


class B():
    def b_method(self):
        print "I am in B method"

class C(A,B):
    a_method()
C()
    

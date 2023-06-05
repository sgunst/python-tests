def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

#inner functions
def parent():
    print("Printing from the parent() function")

    # inner functions DEFINED when parent function is CALLED
    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

def parent1(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

if __name__ == "__main__":
    print(greet_bob(say_hello))
    print(greet_bob(be_awesome))
    parent()
    print(parent1(10)())
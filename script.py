import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting='Hello, {}'.format(who_to_greet)
    return greeting


print(greet('python_project'))
print(greet('python_project'))
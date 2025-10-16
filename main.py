from time import sleep

def printl(text, slp):
    for char in text:
        print(char, end="", flush=True)
        sleep(slp)
    print()
  
# examples
def example():
    printl("example", 0.02)
    printl("example 2", 0.04)
    printl("example 3", 0.08)
  
# your main class
example()

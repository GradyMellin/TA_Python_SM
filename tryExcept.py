

def getInfo():
    var1 = input("\nPlease provide the first numaric value: ")
    var2 = input("\nPlease provide the second numaric value: ")
    return var1,var2

def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False 
        except ValueError as e:
            print("{}: \n\nYou did not provide a numaric value".format(e))
        except:
            print("\n\nOops, you provided an invalid input, program will close now")
    print("\n{} + {} = {}".format(var1,var2,var3))
        

    

if __name__ == "__main__":
    compute()

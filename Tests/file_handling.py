domain = input("Enter the domain name: ")

target = {
    "domain": domain,
    "status": "active"
}

with open('target.txt', 'a') as file:
    file.write("Domain: "+target["domain"] + "\n" + "Status: "+target["status"])
    print("Domain Info has been successfully saved to the file 'target.txt'!")

option = input("Do you want to see the file 'target.txt'? (y/n)")

try:
    if option == 'y':
        with open('target.txt', 'r') as file:
            content = file.read()
            print("Content of target.txt:")
            print(content)
    elif option == 'n':
        exit()
except ValueError:
    print("Value Error!")

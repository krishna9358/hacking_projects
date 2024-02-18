#made by Krishna Mohan
#!usr/bin/env python
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        #code to handle error
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        #code to handle erroe
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Mac Address successfully changed.")

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\W:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Sorry, I couldn't read the mac address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface) #after changing the value
if current_mac == options.new_mac:
    print("[+] Mac address was successfully changed to " +  current_mac)
else:
    print("[-] Mac address did not change")

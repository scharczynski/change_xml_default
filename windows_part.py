import pexpect
import sys
import numbers


def main():
    password = 'cheese'
    offset_value = sys.argv[1]

    try:
        offset_numeric = isinstance(float(offset_value), numbers.Number)
    except Exception as e:
        print "Non-numeric value provided, please try again with a numeric value"
        raise ValueError
    #child = pexpect.spawn('ssh root@192.168.7.2')
    child = pexpect.spawn('ssh steve@192.168.100.53')
    initial_connect = child.expect(
        ['password:', 'Are you sure you want to continue connecting', pexpect.TIMEOUT, pexpect.EOF], timeout=120)
    # print child.after
    if initial_connect == 0:
        child.sendline(password)
    elif initial_connect == 1:
        child.sendline("yes")
        child.sendline(password)
    child.expect(['Welcome to Ubuntu'])
    # print child.after
    #child.sendline('cd test/directory')
    #child.sendline('python change_xml_default.py')
    #child.sendline('python /all/opt/ht/mk5/scripts/change_xml_default.py ' + offset_value)
    child.sendline(
        'python /home/steve/workspace/misc/change_xml_default.py ' + offset_value)
    child.expect([offset_value, '75'])
    # print child.after
    check_changed = child.expect(
        ['True', 'False', pexpect.TIMEOUT, pexpect.EOF])
    if check_changed == 0:
        print "Successfully modified XML file"
    elif check_changed == 1:
        print "XML file was not modified"

    # print child.after
if __name__ == "__main__":
    main()

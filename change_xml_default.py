from xml_changer import change_element, verify_change
from subprocess import call
import time
import datetime
import sys


def main():
    #file_location = "/all/opt/ht/mk5/config/system.xml"
    file_location = "/home/steve/workspace/misc/system.xml"
    new_value = sys.argv[1]


    time_now = time.time()
    date_now = str(datetime.date.today())

    #call(['cp', '/all/opt/ht/mk5/config/system.xml', '/all/opt/ht/mk5/config/system_' + date_now + str(time_now) + '.xml'])
    call(['cp', '/home/steve/workspace/misc/system.xml',
        '/home/steve/workspace/misc/system_' + date_now + str(time_now) + '.xml'])
    # print '/home/steve/workspace/misc/system_' + date_now + str(time_now) +
    # '.xml'
    change_element(file_location, "channel",
                "r_stage_temp_actual", "scaleC", new_value)

    print verify_change(file_location, "channel", "r_stage_temp_actual", "scaleC", new_value)

# validate change?

#call(["systemctl", "restart", "mk5.service"])

if __name__ == "__main__":
    main()

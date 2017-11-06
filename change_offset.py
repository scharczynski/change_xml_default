from xml_changer import change_element, verify_change
from subprocess import call
import time
import datetime
import sys


def main():
    file_location = "/opt/ht/mk5/config/system.xml"
    new_value = sys.argv[1]
    time_now = time.time()
    date_now = str(datetime.date.today())

    call(['cp', '/opt/ht/mk5/config/system.xml',
          '/opt/ht/mk5/config/system_' + date_now + str(time_now) + '.xml'])

    change_element(file_location, "channel",
                   "r_adc1_ain7", "scaleC", new_value)
    change_success = verify_change(
        file_location, "channel", "r_adc1_ain7", "scaleC", new_value)

    print change_success

    call(["systemctl", "restart", "mk5.service"])

    return change_success


if __name__ == "__main__":
    main()

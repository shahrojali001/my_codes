"""Defination: convert the 12hr format to 24hr format. """
def time_format(time):
    """ convert the 12hr format to 24hr format."""
    if (time[-2:] == "AM" and time[:2] == "12" ):
        return "00"+time[2:8]
    elif(time[-2:]=="AM"):
        return time[0:8]
    elif(time[-2:]=="PM" and time[:2]=="12"):
        return time[0:8]
    else:
        return str(int(time[0:2])+12) + time[2:8]
if __name__=='__main__':
    TIME=input("Enter the time in 12hr(00:00:00 AM/PM) format:")
    result=time_format(TIME)
    print(f"The time in 24hr format is {result}")

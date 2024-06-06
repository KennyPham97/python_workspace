months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    outdated()

def outdated():
    while True:
        try:
            date = input("Date: ").strip()
            mm, dd, yyyy = date.split("/")
            if  1 <= int(mm) <= 12 and 1 <= int(dd) <= 31:
                print(yyyy, f"{int(mm):02}", f"{int(dd):02}", sep="-")
                break
        except:
            try:
                month, day, year = date.split(" ")
                if month in months and day.endswith(","):
                    month = months.index(month)+1
                    day = day.removesuffix(",")
                if 1 <= int(month) <= 12 and 1 <=int(day) <= 31:
                    print(year, f"{month:02}", f"{int(day):02}", sep="-")
                    break
            except:
                pass
            

main()

#line 26 and 27 are saying that if anything under the first try block errors out, then try this new code block underneath. 
#line 24 and 33 have to have the variable passed to the int function, or else the numbers "9" and "3" will print out to 90 and 30. Using the integers 9 and 3 however will then output 09 and 03 respectively. 
    
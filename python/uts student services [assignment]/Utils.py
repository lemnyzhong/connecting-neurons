class utils:
    def check(prompt):
        s = input(f"{prompt}: ")
        if s!="2022AUT":
            return False
        else:
            return True    

    def studentHeader():
        print("+----------------------+---------------------------+------------+------------+")
        print("| Student Name         | Email                     |  Phone     | Type       |")
        print("+----------------------+---------------------------+------------+------------+")

    def slipHeader():
        print("+--------------------+-------------+-------------+-------------+-------------+")
        print("| Student Name       |   Tuition   | Scholarship |     Net     |  Deduction  |")
        print("+--------------------+-------------+-------------+-------------+-------------+")

    def logHeader():
        print("+--------------+----------------+")
        print("|  TMS Record  |    RecordID    |")
        print("+--------------+----------------+")



if __name__ == '__main__':
    #utils = utils()
    utils.slipHeader()
    utils.studentHeader()
    utils.logHeader()
    print('Done')



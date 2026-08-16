import pandas as p
import mysql.connector as msql
import matplotlib.pyplot as plt
from mysql.connector import Error

try:
    conn = msql.connect(
        host='localhost',
        database="project",
        user='root',
        password='ishankandari.125@gmail.com'
    )

    if conn.is_connected():
        cursor = conn.cursor()
        print("Good")

except Error as e:
    print("Error while connecting to MySQL", e)

p.set_option('display.max_columns', None)

print("Welcome to Global Hospital!")
u = input("Please enter your username: ")
pa = input("Please enter your password: ")
print()

if u == "username" and pa == "password":
    print("Welcome to the admin page!\n")

    while True:
        print("Given Below are a list of options.")
        print("1. View All Records")
        print("2. Search Patient Record")
        print("3. Add Patient Record")
        print("4. Edit Patient Record")
        print("5. Remove Patient Record")
        print("6. Calculate Bill")
        print("7. Graph of Patient Progress")
        print("8. Exit Program\n")

        ch = input("Enter the number next to your choice: ")
        print()

        # EXIT
        if ch == "8":
            print("Exiting Program...")
            break

        # VIEW ALL
        elif ch == "1":
            sql = "select * from ptable"
            try:
                cursor.execute(sql)
                l = []

                for i in range(10):
                    result = cursor.fetchone()
                    l.append(result)

                df1 = p.DataFrame(l, columns=[
                    "Patient Id", "Name", "Gender", "Age", "DOA",
                    "Disease", "Treatment", "Patient Status",
                    "Room No.", "Doctor Name", "Due Date"
                ])

                print(df1)
                input("\nPress Any Key to close the window")

            except:
                conn.rollback()

        # SEARCH RECORD
        elif ch == "2":

            print("1. View single record")
            print("2. View first n records")
            print("3. View last n records")
            print("4. View records between IDs")

            c = input("Enter your choice: ")

            # SINGLE
            if c == "1":
                id = int(input("Enter Patient ID: "))

                sql = "select * from ptable where PatientID=%(ID)s"
                try:
                    cursor.execute(sql, {"ID": id})
                    result = cursor.fetchone()

                    s1 = p.Series(result, index=[
                        "Patient Id", "Name", "Gender", "Age", "DOA",
                        "Disease", "Treatment", "Patient Status",
                        "Room No.", "Doctor Name", "Due Date"
                    ])

                    print(s1)

                except Error as e:
                    print("Error:", e)

            # FIRST N
            elif c == "2":
                n1 = int(input("Enter number of records: "))
                sql = "select * from ptable where PatientID<=%(ID)s"

                try:
                    cursor.execute(sql, {"ID": n1})
                    result = cursor.fetchall()

                    df = p.DataFrame(result, columns=[
                        "Patient Id", "Name", "Gender", "Age", "DOA",
                        "Disease", "Treatment", "Patient Status",
                        "Room No.", "Doctor Name", "Due Date"
                    ])

                    print(df)

                except Error as e:
                    print("Error:", e)

        # ADD RECORD
        elif ch == "3":

            print("Enter Patient Details")

            pid = int(input("Patient ID: "))
            name = input("Name: ")
            g = input("Gender: ")
            a = int(input("Age: "))
            doa = input("DOA (YYYY-MM-DD): ")
            sick = input("Disease: ")
            method = input("Treatment Method: ")
            status = input("Status: ")
            rno = int(input("Room Number: "))
            docname = input("Doctor Name: ")
            duedate = input("Due Date (YYYY-MM-DD): ")

            sql = """
            insert into ptable 
            values(%(ID)s,%(N)s,%(G)s,%(A)s,%(D)s,%(S)s,
                   %(M)s,%(ST)s,%(R)s,%(DN)s,%(DD)s)
            """

            try:
                cursor.execute(sql, {
                    "ID": pid,
                    "N": name,
                    "G": g,
                    "A": a,
                    "D": doa,
                    "S": sick,
                    "M": method,
                    "ST": status,
                    "R": rno,
                    "DN": docname,
                    "DD": duedate
                })

                conn.commit()
                print("Record Inserted Successfully")

            except Error as e:
                print("Error:", e)

        # DELETE RECORD
        elif ch == "5":

            id = int(input("Enter Patient ID to delete: "))
            sql = "DELETE FROM ptable WHERE PatientID=%(ID)s"

            try:
                cursor.execute(sql, {"ID": id})
                conn.commit()
                print("Record Deleted Successfully")

            except Error as e:
                print("Error:", e)

        # CALCULATE BILL
        elif ch == "6":

            id = int(input("Enter Patient ID: "))

            rate = {
                "Dr. Pathan": 6500,
                "Dr. Prabhas": 7000,
                "Dr. Shupta": 7250,
                "Dr. Suresh": 7750,
                "Dr. Isha": 8000
            }

            sql = """
            select DocName, DateDiff(DueDate, DOA)
            from ptable where PatientID=%(ID)s
            """

            try:
                cursor.execute(sql, {"ID": id})
                result = cursor.fetchone()

                cost = result[1] * rate[result[0]]

                print("Doctor:", result[0])
                print("Total Cost:", cost)

            except Error as e:
                print("Error:", e)

        # GRAPH
        elif ch == "7":

            sql = "SELECT DocName, count(*) from ptable GROUP BY DocName"

            try:
                cursor.execute(sql)
                x = []
                y = []

                for i in range(5):
                    result = cursor.fetchone()
                    x.append(result[0])
                    y.append(result[1])

                plt.bar(x, y)
                plt.title("Patients per Doctor")
                plt.xlabel("Doctor Name")
                plt.ylabel("Number of Patients")
                plt.show()

            except Error as e:
                print("Error:", e)

        else:
            print("Please enter a correct option")

else:
    print("Incorrect username or password.")

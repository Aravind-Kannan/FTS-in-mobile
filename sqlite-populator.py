import gen_parser 
import random
import sqlite3

database_string = "cmp.db"


def main():
    conn = sqlite3.connect(database_string)
    cur = conn.cursor()

    name_list = gen_parser.line_parser("data-populate/names.txt")
    addr_list = gen_parser.dual_line_parser("data-populate/address.txt")
    print("Connected!")

    number_of_records = 10

    for i in range(number_of_records):
        name = random.choice(name_list)
        age = random.randint(18, 25)
        address = random.choice(addr_list)
        salary = random.randint(50, 100) * 10_000
        # print(name, age, address, salary)
        cur.execute("INSERT INTO COMPANY(name, age, address, salary) VALUES(?,?,?,?);", (name, age, address, salary))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()

import gen_parser 
import random
import sqlite3

database_string = "cmp.db"


def main():
    conn = sqlite3.connect(database_string)
    cur = conn.cursor()

    name_list = gen_parser.line_parser("names.txt")
    addr_list = gen_parser.dual_line_parser("address.txt")
    print("Connected!")

    for i in range(10_00_000):
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

import csv


def create_sql_file(field_file, sql_file="test.sql", tbl_name=("test", "订单")):
    with open(field_file, 'r', encoding="UTF-8") as f_reader, \
            open(sql_file, 'w') as f_writer:
        csv_file = csv.reader(f_reader)
        local_tbl_name = tbl_name[0]
        first_line = "CREATE TABLE {} (".format(local_tbl_name)
        new_line = ""
        for row in csv_file:
            row[2] = "COMMENT {}".format(row[2])
            print(row)
            line = " ".join(row)
            new_line = new_line + line + ", "
        total_line = first_line + new_line.strip(", ") + ") comment " + \
                     " \"{}\" ".format(
                         tbl_name[1]) + " PARTITIONED BY (`dt` string) ;"
        print(tbl_name[1])
        print(total_line)

        f_writer.write(total_line)


create_sql_file("tbl_fields_comments.csv", tbl_name=("order_analysis", "订单"))

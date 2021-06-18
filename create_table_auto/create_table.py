import csv

from loguru import logger


def create_sql_file(field_file, sql_file="all_sql.sql", tbl_name=("test", "订单")):
    with open(field_file, 'r', encoding="UTF-8") as f_reader, \
            open(sql_file, 'a') as f_writer:
        csv_file = csv.reader(f_reader)

        local_tbl_name = tbl_name[0]
        first_line = f"CREATE TABLE {local_tbl_name} ("
        new_line = ""
        for row in csv_file:
            logger.info(f"The row[2] is {row[2]}")

            if row[2] == "":
                row[2] = " "
            else:
                row[2] = f"COMMENT '{row[2]}' "
            logger.info(row)
            line = " ".join(row)
            new_line = new_line + line + ", "
        total_line = first_line + new_line.strip(", ") + ") comment " + \
                     " \"{}\" ".format(
                         tbl_name[1]) + " PARTITIONED BY (`dt` string) ;"
        logger.info(tbl_name[1])
        logger.info(total_line)

        f_writer.write(total_line)


create_sql_file("field.csv",
                tbl_name=("channel", "channel"))

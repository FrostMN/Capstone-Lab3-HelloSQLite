import HelloSQLite.utils.database as sql
import HelloSQLite.utils.logging as log
import HelloSQLite.utils.ui as ui


def main():
    sql.init_db()

    while True:
        ui.show_menu()
        action = ui.get_option()
        ui.do_action(action)

    # qry = "INSERT INTO jugglers (name, country, catches) VALUES('Test User', 'Canada', 50)"
    qry = "SELECT * FROM jugglers WHERE catches=50"
    print(sql.get_query_response(qry))


if __name__ == '__main__':
    log.start()
    main()

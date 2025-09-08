import sqlite3

def save(id,title,teacher,unit):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("insert into lessons (id,title,teacher,unit) values (?,?,?,?)",
                         [id,title,teacher,unit])

    connection.commit()
    connection.close()


def delete(id,title,teacher,unit):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("delete from lessons where id=?",[id])
    connection.commit()
    connection.close()


def edit(id,title,teacher,unit):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("update lessons set title = ?, teacher = ?, unit = ? where id = ?",)
    connection.commit()
    connection.close()




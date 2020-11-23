import sqlite3
import csv
con = sqlite3.connect(input())
cur = con.cursor()

bort, dmg = [x for x in input().split()]
dmg = int(dmg)

result = cur.execute(f"""SELECT p.broken_thing, p.damage, p.can_be_repaired, r.owner, r.size FROM Protocol p 
JOIN Rooms r ON r.id = p.id
JOIN Sides s ON r.rooms_id = s.id
WHERE s.title = '{bort}' AND p.damage >= '{dmg}'
ORDER BY p.damage""").fetchall()
con.close()
for i in result:
    print(i)

with open('damage.csv', 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=';', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    # Получение списка заголовков    
    for j in result:
        writer.writerow(j)

"""
destruction.db
left_side 20
"""
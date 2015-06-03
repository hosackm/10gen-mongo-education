import pymongo
from pprint import pprint


def main():
    conn = pymongo.MongoClient('mongodb://localhost')
    db = conn.students

    query = {
        'type': 'homework'
    }
    projection = [
        ('student_id', pymongo.ASCENDING),
        ('score', pymongo.ASCENDING)
    ]

    try:
        docs = db.grades.find(query).sort(projection)
        lows = [docs[i] for i in xrange(0, docs.count(), 2)]
        [db.grades.delete_one({'_id': l.get('_id')}) for l in lows]
    except Exception as e:
        print e


if __name__ == '__main__':
    main()

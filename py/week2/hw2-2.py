import pymongo
from pprint import pprint


def main():
    conn = pymongo.MongoClient('mongodb://localhost')
    db = conn.students

    dfilt = {
        'type': 'homework'
    }
    lsort = [
        ('student_id', pymongo.ASCENDING),
        ('score', pymongo.ASCENDING)
    ]

    try:
        docs = db.grades.find(dfilt).sort(lsort)
        evens = [docs[i] for i in xrange(0, docs.count(), 2)]
        [db.grades.delete_one({'_id': e.get('_id')}) for e in evens]
    except Exception as e:
        print e


if __name__ == "__main__":
    main()

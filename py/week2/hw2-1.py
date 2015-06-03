import pymongo


def main():
    conn = pymongo.MongoClient('mongodb://localhost')
    db = conn.students
    try:
        print db.grades.find(
            {'score': {'$gte': 65}}, {'score': 1, '_id': 0}).sort(
                [('score', pymongo.ASCENDING)]).limit(1)[0]
    except Exception as e:
        print e

if __name__ == '__main__':
    main()

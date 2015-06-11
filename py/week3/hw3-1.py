import pymongo
import operator


def drop_lowest(doc):
    non_hws = []
    hws = []
    for score in doc.get('scores', []):
        if score.get('type', '') == 'homework':
            hws.append(score)
        else:
            non_hws.append(score)

    hws = sorted(hws, key=operator.itemgetter('score'))[1:]

    return non_hws + hws


def main():
    db = pymongo.MongoClient('mongodb://localhost:27017').school
    student_collection = db.students
    students = student_collection.find({})

    for student in students:
        query = {'_id': student.get('_id')}
        new_scores = drop_lowest(student)
        student_collection.update(query, {'$set': {'scores': new_scores}})

if __name__ == '__main__':
    main()

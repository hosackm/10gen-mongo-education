use students;
db.grades.find({score: {$gte: 65}}, {student_id: 1, _id: 0}).sort({score: 1}).limit(1)

use students;

var lows = [];

var cur = db.grades.find({type: 'homework'}).sort({student_id: 1, score: 1});

for(var i = 0; i < 400; i+= 2) {
  lows[i/2] = cur[i];
}

lows.forEach(function (doc) {
  db.grades.remove(doc);
});
use weather;
db.data.find({'Wind Direction': {$gt: 180, $lt: 360}}, {State: 1, _id: 0}).sort({Temperature: 1}).limit(1);
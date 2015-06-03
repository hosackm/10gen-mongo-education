var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/weather', function (err, db){ 
  if(err) throw err;
  var query = {
    'Wind Direction': {$gt: 180, $lt: 360}
  };
  var projection = {
    _id: 0, State: 1
  };
  var options = {
    limit: 1, sort: {Temperature: 1}
  };

  db.collection('data').findOne(query, projection, options, function (err, doc) {
    if (err) throw err;
    console.log(doc);
    db.close();
  });
});

use movieDB

switched to db movieDB

db.users.insertMany([
{ _id: 1, name: "Rahul Sharma", email: "rahul@example.com", city: "Bangalore", plan:
"Premium" },
{ _id: 2, name: "Priya Singh", email: "priya@example.com", city: "Delhi", plan:
"Basic" },
{ _id: 3, name: "Aman Kumar", email: "aman@example.com", city: "Hyderabad", plan:
"Standard" }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': 1,
    '1': 2,
    '2': 3
  }
}


db.movies.insertMany([
{ _id: 101, title: "Inception", genre: "Sci-Fi", year: 2010, rating: 8.8 },
{ _id: 102, title: "3 Idiots", genre: "Comedy", year: 2009, rating: 8.4 },
{ _id: 103, title: "Bahubali", genre: "Action", year: 2015, rating: 8.1 },
{ _id: 104, title: "The Dark Knight", genre: "Action", year: 2008, rating: 9.0 },
{ _id: 105, title: "Dangal", genre: "Drama", year: 2016, rating: 8.5 }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': 101,
    '1': 102,
    '2': 103,
    '3': 104,
    '4': 105
  }
}


db.subscriptions.insertMany([
{ user_id: 1, start_date: ISODate("2025-01-01"), end_date: ISODate("2025-12-31"),
amount: 999 },
{ user_id: 2, start_date: ISODate("2025-02-01"), end_date: ISODate("2025-07-31"),
amount: 499 },
{ user_id: 3, start_date: ISODate("2025-01-15"), end_date: ISODate("2025-10-15"),
amount: 799 }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68c8fa069b24cdf8c769db79'),
    '1': ObjectId('68c8fa069b24cdf8c769db7a'),
    '2': ObjectId('68c8fa069b24cdf8c769db7b')
  }
}


db.watchHistory.insertMany([
{ user_id: 1, movie_id: 101, watch_date: ISODate("2025-02-10") },
{ user_id: 1, movie_id: 102, watch_date: ISODate("2025-02-12") },
{ user_id: 2, movie_id: 103, watch_date: ISODate("2025-02-11") },
{ user_id: 3, movie_id: 104, watch_date: ISODate("2025-02-13") },
{ user_id: 3, movie_id: 105, watch_date: ISODate("2025-02-14") }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68c8fa0f9b24cdf8c769db7c'),
    '1': ObjectId('68c8fa0f9b24cdf8c769db7d'),
    '2': ObjectId('68c8fa0f9b24cdf8c769db7e'),
    '3': ObjectId('68c8fa0f9b24cdf8c769db7f'),
    '4': ObjectId('68c8fa0f9b24cdf8c769db80')
  }
}


db.users.insertOne({
  _id: 4,
  name: "Neha Patel",
  email: "neha@example.com",
  city: "Mumbai",
  plan: "Standard"
});
{
  acknowledged: true,
  insertedId: 4
}


db.movies.updateOne(
  { title: "Bahubali" },
  { $set: { rating: 8.3 } }
);
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}


db.movies.deleteOne({ title: "3 Idiots" });
{
  acknowledged: true,
  deletedCount: 1
}


db.users.find({ plan: "Premium" });
{
  _id: 1,
  name: 'Rahul Sharma',
  email: 'rahul@example.com',
  city: 'Bangalore',
  plan: 'Premium'
}


db.users.createIndex({ email: 1 }, { unique: true });
email_1


db.movies.createIndex({ genre: 1, rating: -1 });
genre_1_rating_-1


db.users.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { email: 1 }, name: 'email_1', unique: true }
]


db.movies.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { genre: 1, rating: -1 }, name: 'genre_1_rating_-1' }
]


db.movies.find({ genre: "Action" }).sort({ rating: -1 });
{
  _id: 104,
  title: 'The Dark Knight',
  genre: 'Action',
  year: 2008,
  rating: 9
}
{
  _id: 103,
  title: 'Bahubali',
  genre: 'Action',
  year: 2015,
  rating: 8.3
}


db.movies.find({ year: 2000 });

db.movies.aggregate([
  { $group: { _id: "$genre", count: { $sum: 1 } } }
]);
{
  _id: 'Sci-Fi',
  count: 1
}
{
  _id: 'Action',
  count: 2
}
{
  _id: 'Drama',
  count: 1
}


db.movies.find().sort({ rating: -1 }).limit(2);
{
  _id: 104,
  title: 'The Dark Knight',
  genre: 'Action',
  year: 2008,
  rating: 9
}
{
  _id: 101,
  title: 'Inception',
  genre: 'Sci-Fi',
  year: 2010,
  rating: 8.8
}


db.subscriptions.aggregate([
  { $lookup: {
      from: "users",
      localField: "user_id",
      foreignField: "_id",
      as: "user"
  }},
  { $unwind: "$user" },
  { $group: { _id: "$user.plan", avgAmount: { $avg: "$amount" } } }
]);
{
  _id: 'Basic',
  avgAmount: 499
}
{
  _id: 'Standard',
  avgAmount: 799
}
{
  _id: 'Premium',
  avgAmount: 999
}


db.watchHistory.aggregate([
  { $group: { _id: "$movie_id", totalWatch: { $sum: 1 } } }
]);
{
  _id: 103,
  totalWatch: 1
}
{
  _id: 104,
  totalWatch: 1
}
{
  _id: 105,
  totalWatch: 1
}
{
  _id: 102,
  totalWatch: 1
}
{
  _id: 101,
  totalWatch: 1
}


db.users.aggregate([
  { $match: { plan: "Premium" } },
  { $group: { _id: "$city", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 1 }
]);
{
  _id: 'Bangalore',
  count: 1
}
db.watchHistory.aggregate([
  { $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "_id",
      as: "movie"
  }},
  { $unwind: "$movie" },
  { $group: { _id: "$movie.genre", totalWatch: { $sum: 1 } } },
  { $sort: { totalWatch: -1 } },
  { $limit: 1 }
]);
{
  _id: 'Action',
  totalWatch: 2
}


db.watchHistory.aggregate([
  { $lookup: {
      from: "users",
      localField: "user_id",
      foreignField: "_id",
      as: "user"
  }},
  { $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "_id",
      as: "movie"
  }},
  { $unwind: "$user" },
  { $unwind: "$movie" },
  { $project: {
      _id: 0,
      userName: "$user.name",
      movieTitle: "$movie.title",
      watch_date: 1
  }}
]);
{
  watch_date: 2025-02-10T00:00:00.000Z,
  userName: 'Rahul Sharma',
  movieTitle: 'Inception'
}
{
  watch_date: 2025-02-11T00:00:00.000Z,
  userName: 'Priya Singh',
  movieTitle: 'Bahubali'
}
{
  watch_date: 2025-02-13T00:00:00.000Z,
  userName: 'Aman Kumar',
  movieTitle: 'The Dark Knight'
}
{
  watch_date: 2025-02-14T00:00:00.000Z,
  userName: 'Aman Kumar',
  movieTitle: 'Dangal'
}


db.watchHistory.aggregate([
  { $lookup: {
      from: "users",
      localField: "user_id",
      foreignField: "_id",
      as: "user"
  }},
  { $unwind: "$user" },
  { $match: { "user.name": "Rahul Sharma" } },
  { $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "_id",
      as: "movie"
  }},
  { $unwind: "$movie" },
  { $project: { _id: 0, movieTitle: "$movie.title", watch_date: 1 } }
]);
{
  watch_date: 2025-02-10T00:00:00.000Z,
  movieTitle: 'Inception'
}


db.users.aggregate([
  { $lookup: {
      from: "subscriptions",
      localField: "_id",
      foreignField: "user_id",
      as: "subscription"
  }}
]);
{
  _id: 1,
  name: 'Rahul Sharma',
  email: 'rahul@example.com',
  city: 'Bangalore',
  plan: 'Premium',
  subscription: [
    {
      _id: ObjectId('68c8fa069b24cdf8c769db79'),
      user_id: 1,
      start_date: 2025-01-01T00:00:00.000Z,
      end_date: 2025-12-31T00:00:00.000Z,
      amount: 999
    }
  ]
}
{
  _id: 2,
  name: 'Priya Singh',
  email: 'priya@example.com',
  city: 'Delhi',
  plan: 'Basic',
  subscription: [
    {
      _id: ObjectId('68c8fa069b24cdf8c769db7a'),
      user_id: 2,
      start_date: 2025-02-01T00:00:00.000Z,
      end_date: 2025-07-31T00:00:00.000Z,
      amount: 499
    }
  ]
}
{
  _id: 3,
  name: 'Aman Kumar',
  email: 'aman@example.com',
  city: 'Hyderabad',
  plan: 'Standard',
  subscription: [
    {
      _id: ObjectId('68c8fa069b24cdf8c769db7b'),
      user_id: 3,
      start_date: 2025-01-15T00:00:00.000Z,
      end_date: 2025-10-15T00:00:00.000Z,
      amount: 799
    }
  ]
}
{
  _id: 4,
  name: 'Neha Patel',
  email: 'neha@example.com',
  city: 'Mumbai',
  plan: 'Standard',
  subscription: []
}


db.watchHistory.aggregate([
  { $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "_id",
      as: "movie"
  }},
  { $unwind: "$movie" },
  { $match: { "movie.year": { $gt: 2010 } } },
  { $lookup: {
      from: "users",
      localField: "user_id",
      foreignField: "_id",
      as: "user"
  }},
  { $unwind: "$user" },
  { $project: { _id: 0, userName: "$user.name", movieTitle: "$movie.title" } }
]);
{
  userName: 'Priya Singh',
  movieTitle: 'Bahubali'
}
{
  userName: 'Aman Kumar',
  movieTitle: 'Dangal'
}


db.movies.aggregate([
  { $lookup: {
      from: "watchHistory",
      localField: "_id",
      foreignField: "movie_id",
      as: "watchers"
  }},
  { $unwind: { path: "$watchers", preserveNullAndEmptyArrays: true } },
  { $lookup: {
      from: "users",
      localField: "watchers.user_id",
      foreignField: "_id",
      as: "userDetails"
  }},
  { $project: {
      _id: 0,
      movieTitle: "$title",
      users: "$userDetails.name"
  }}
]);
{
  movieTitle: 'Inception',
  users: [
    'Rahul Sharma'
  ]
}
{
  movieTitle: 'Bahubali',
  users: [
    'Priya Singh'
  ]
}
{
  movieTitle: 'The Dark Knight',
  users: [
    'Aman Kumar'
  ]
}
{
  movieTitle: 'Dangal',
  users: [
    'Aman Kumar'
  ]
}


db.watchHistory.aggregate([
  { $group: { _id: "$user_id", watchCount: { $sum: 1 } } },
  { $match: { watchCount: { $gt: 2 } } },
  { $lookup: {
      from: "users",
      localField: "_id",
      foreignField: "_id",
      as: "user"
  }},
  { $unwind: "$user" },
  { $project: { _id: 0, userName: "$user.name", watchCount: 1 } }
]);


db.subscriptions.aggregate([
  { $group: { _id: null, totalRevenue: { $sum: "$amount" } } }
]);
{
  _id: null,
  totalRevenue: 2297
}


db.subscriptions.aggregate([
  { $match: { end_date: { $gte: today, $lte: next30 } } },
  { $lookup: {
      from: "users",
      localField: "user_id",
      foreignField: "_id",
      as: "user"
  }},
  { $unwind: "$user" },
  { $project: { _id: 0, userName: "$user.name", end_date: 1 } }
]);
{
  end_date: 2025-10-15T00:00:00.000Z,
  userName: 'Aman Kumar'
}


db.watchHistory.aggregate([
  { $group: { _id: "$movie_id", totalWatch: { $sum: 1 } } },
  { $sort: { totalWatch: -1 } },
  { $limit: 1 },
  { $lookup: {
      from: "movies",
      localField: "_id",
      foreignField: "_id",
      as: "movie"
  }},
  { $unwind: "$movie" },
  { $project: { _id: 0, movieTitle: "$movie.title", totalWatch: 1 } }
]);
{
  totalWatch: 1,
  movieTitle: 'Inception'
}


db.watchHistory.aggregate([
  { $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "_id",
      as: "movie"
  }},
  { $unwind: "$movie" },
  { $group: { _id: "$movie.genre", totalWatch: { $sum: 1 } } },
  { $sort: { totalWatch: 1 } },
  { $limit: 1 }
]);
{
  _id: 'Sci-Fi',
  totalWatch: 1
}

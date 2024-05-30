// Shell Search Query Examples for Mongo DB

// Comparison Operators: "$eq" ( Matches values that are equal to a specified value.)
db.collection_name.find({ field: { $eq: value } }).pretty();
// // Comparison Operators: "$ne" ( Matches values that are  NOT equal to a specified value.)
db.collection_name.find({ field: { $ne: value } }).pretty();
// Comparison Operators: "$gt" ( Matches values that are GREATER THAN specified value.)
db.collection_name.find({ field: { $gt: value } }).pretty();
// Comparison Operators: "$lt" ( Matches values that LESS THAN  specified value.)
db.collection_name.find({ field: { $lt: value } }).pretty();
// Comparison Operators: "$type" (  Matches documents if a field is of the specified BSON type.)
db.collection_name.find({ field: { $type: "string" } }).pretty();




//  Some Find Queries

//Case-sensitive version of searching through collection 
- db["T01.01 16mm_Films"].find({ description: { $regex: "B&W" } }).pretty();

// If you want to search in multiple fields, you can use the $or operator: ( Case-INSENSITIVE Matching
db["T01.36 Posters"].find({$or: [
    { description: { $regex: "tank", $options: "i" } },
    { comments: { $regex: "And", $options:  "i" } }
  ]
}).pretty();



// An example of an aggregation query to search through the database using the "$Match" operator 


 // which Filters the documents to pass only those that match the specified condition.
db['16mm_Films'].aggregate([{ $match: { aircraftModel: "S-76" } }]).pretty();


// Documents Grouped by YearExtract the year from the date field and group documents by year.
db["T01.09_Flat_Documents"].aggregate([
  { $addFields: { year: { $substr: ["$date", 6, 4] } } },
  { $group: { _id: "$year", count: { $sum: 1 } } }
]).pretty();

// Group documents by aircraft model as well as using the "$Unwind operator to deconstruct array fields
db["T01.09 Flat_Documents"].aggregate([
  { $unwind: "$aircraftModel" },
  { $group: { _id: "$aircraftModel", count: { $sum: 1 } } }
]).pretty();



db.feedback.insertMany([
  {
    campaign_name: "Diwali Offer",
    product_id: 1,
    region: "North",
    feedback: "Great response, increased sales by 20%",
    rating: 4.5
  },
  {
    campaign_name: "Back to School",
    product_id: 3,
    region: "South",
    feedback: "Moderate response",
    rating: 3.2
  }
]);

db.feedback.createIndex({ product_id: 1 });
db.feedback.createIndex({ region: 1 });

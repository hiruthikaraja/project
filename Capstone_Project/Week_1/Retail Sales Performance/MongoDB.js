use retailDB

// Add revenue, cost, profit, discount_pct fields to each sale
db.sales.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "product_id",
      as: "product_info"
    }
  },
  { $unwind: "$product_info" },
  {
    $addFields: {
      revenue: { $multiply: ["$quantity", "$product_info.price"] },
      cost: { $multiply: ["$quantity", { $multiply: ["$product_info.price", 0.9] }] },
      profit: { $subtract: ["$revenue", "$cost"] },
      discount_pct: {
        $multiply: [
          { $divide: [{ $subtract: ["$product_info.price", { $divide: ["$cost", "$quantity"] }] }, "$product_info.price"] },
          100
        ]
      }
    }
  },
  { $out: "sales_cleaned" }
]);

// Summary by store
db.sales_cleaned.aggregate([
  {
    $group: {
      _id: "$store_id",
      total_revenue: { $sum: "$revenue" },
      total_profit: { $sum: "$profit" },
      total_transactions: { $sum: 1 }
    }
  },
  {
    $lookup: {
      from: "stores",
      localField: "_id",
      foreignField: "store_id",
      as: "store_info"
    }
  },
  { $unwind: "$store_info" },
  {
    $project: {
      store_id: "$_id",
      store_name: "$store_info.store_name",
      total_revenue: 1,
      total_profit: 1,
      total_transactions: 1
    }
  }
]);

// Summary by product
db.sales_cleaned.aggregate([
  {
    $group: {
      _id: "$product_id",
      total_revenue: { $sum: "$revenue" },
      total_profit: { $sum: "$profit" },
      total_units_sold: { $sum: "$quantity" }
    }
  },
  {
    $lookup: {
      from: "products",
      localField: "_id",
      foreignField: "product_id",
      as: "product_info"
    }
  },
  { $unwind: "$product_info" },
  {
    $project: {
      product_id: "$_id",
      product_name: "$product_info.product_name",
      total_units_sold: 1,
      total_revenue: 1,
      total_profit: 1
    }
  }
]);

// Create indexes
db.sales_cleaned.createIndex({ store_id: 1 })
db.sales_cleaned.createIndex({ product_id: 1 })
db.sales_cleaned.createIndex({ sale_date: 1 })
db.sales_cleaned.createIndex({ revenue: -1 })
db.sales_cleaned.createIndex({ profit: -1 })

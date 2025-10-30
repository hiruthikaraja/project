// ---------------------------------------------
// 1. SELECT DATABASE AND COLLECTION
// ---------------------------------------------

// Switch to (or create) the MongoDB database
use RetailFeedbackDB

// ---------------------------------------------
// 2. STORE UNSTRUCTURED FEEDBACK DATA
// ---------------------------------------------

// Insert sample customer and supplier feedback documents into a new collection
db.feedback.insertMany([
    {
        // Customer Feedback (Unstructured)
        type: "customer_review",
        product_id: "101",
        rating: 4,
        date: new Date("2023-10-28"),
        text: "The Wireless Mouse is great, but the scroll wheel feels a bit cheap. Shipping was fast.",
        reviewer_details: {
            customer_name: "Alice J.",
            email: "alice.j@example.com",
            source: "website"
        }
    },
    {
        // Supplier Feedback (Unstructured)
        type: "supplier_note",
        product_id: "102",
        date: new Date("2023-10-25"),
        text: "Delay expected for Q4 Coffee Maker shipment due to raw material shortage. Recommend increasing safety stock.",
        supplier_details: {
            supplier_id: "S002",
            contact_person: "Bob R.",
            urgency: "High"
        }
    },
    {
        // Another Customer Feedback
        type: "customer_review",
        product_id: "101",
        rating: 5,
        date: new Date("2023-10-29"),
        text: "Excellent product, exactly as described. Five stars!",
        reviewer_details: {
            customer_name: "Charlie M.",
            source: "app"
        }
    }
]);

// ---------------------------------------------
// 3. CREATE INDEX FOR QUICK SEARCH BY product_id
// ---------------------------------------------

// The index creation ensures fast lookup on the product_id field, which is essential
// for quickly linking unstructured feedback to structured product data.
db.feedback.createIndex({ product_id: 1 });

// ---------------------------------------------
// 4. READ/QUERY OPERATION (Demonstrate Index Use)
// ---------------------------------------------

// Find all feedback for a specific product
db.feedback.find({ product_id: "101" }).pretty();

// Find all customer reviews with a rating of 5
db.feedback.find({ type: "customer_review", rating: 5 }).pretty();

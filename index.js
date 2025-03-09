const express = require("express");

const app = express();
app.use(express.json()); // รองรับ JSON

// Webhook Endpoint
app.post("/webhook", (req, res) => {
  console.log("📩 Webhook Received:", req.body);
  res.json({ message: "✅ Webhook received!" });
});

// Export as Vercel Serverless Function
module.exports = app;

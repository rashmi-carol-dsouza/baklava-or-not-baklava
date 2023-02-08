import express from "express";
import cors from "cors";

const app = express();
const PORT = 5000;

app.use(
  cors({
    origin: "*",
  })
);

app.post("/photo", (req, res) => {
  const RANDOM_BOOL = Math.random() < 0.5;
  res.json({ is_baklava: RANDOM_BOOL });
});

app.listen(PORT, () => {
  console.log(`Mock server is running on port ${PORT}`);
});

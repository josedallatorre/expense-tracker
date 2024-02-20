const express = require('express')
const cors = require('cors')
const app = express()
//const next = require('next')
//const dev = process.env.NODE_ENV !== 'production'
//const hostname = 'localhost'
const port = 3000
// when using middleware `hostname` and `port` must be provided below
//const app = next({ dev, hostname, port })

app.use(cors());


app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get("/api/v1/users", (req, res)=>{
  const users = [
    {id: 1, name: "John"},
    {id: 2, name: "Joe"},
  ];
  return res.status(200).json({users});
});
//create a transaction
app.post("/transactions", async (req, res) => {
  try {
    const { item, price, record_time } = req.body;
    const newTrans = await pool.query(
      "INSERT INTO transactions (item, price, record_time) VALUES ($1, $2, $3) RETURNING *",
      [item, price, record_time]
    );
    res.json(newTrans.rows[0]);
  } catch (error) {
    console.log(error.message);
  }
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

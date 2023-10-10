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

app.get("/api/home", (req, res) => {
  res.json({ message: "Like this video!", people: ["Arpan", "Jack", "Barry"] });
});

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

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

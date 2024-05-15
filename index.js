const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

const app = express();
app.use(cors());

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'arduino_data'
});

db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log('Connected to database');
  
});

app.get('/getdata', (req, res) => {
  let sql = 'SELECT * FROM info_data ORDER BY updated_at DESC LIMIT 1';
  db.query(sql, (err, result) => {
    if (err) throw err;
    res.send(result);
   
  });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
  
});

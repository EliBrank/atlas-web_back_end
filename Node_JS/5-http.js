import * as http from 'node:http';
import countStudents from './3-read_file_async.js';

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });

  if (req.url === '/') {
    res.write('Hello Holberton School');
  } else if (req.url === '/students') {
    res.write('This is the list of our students');
    countStudents('database.csv');
  }

  res.end();
}).listen(1245);

export default app;

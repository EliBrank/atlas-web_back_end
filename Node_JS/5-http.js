import * as http from 'node:http';
import countStudents from './3-read_file_async.js';

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.write('Hello Holberton School');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      await countStudents('database.csv', (data) => {
        res.write(data);
      });
    } catch (error) {
      res.write(error.message);
    }
  }

  res.end();
}).listen(1245);

export default app;

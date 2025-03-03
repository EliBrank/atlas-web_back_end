import * as http from 'node:http';
import process from 'process';
import countStudents from './3-read_file_async.js';

const csvPath = process.argv[2];

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.write('Hello Holberton School');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      await countStudents(csvPath, (data) => {
        res.write(data);
      });
    } catch (error) {
      res.write(error.message);
    }
  }

  res.end();
}).listen(1245);

export default app;

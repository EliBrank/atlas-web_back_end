import express from 'express';
import process from 'process';
import countStudents from './3-read_file_async.js';

const app = express();
const csvPath = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.write('This is the list of our students\n');
  try {
    await countStudents(csvPath, (data) => {
      res.write(data);
    });
  } catch (error) {
    res.write(error.message);
  } finally {
    res.end();
  }
});

app.listen(1245);

export default app;

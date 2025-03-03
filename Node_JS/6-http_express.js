import * as express from 'express';

const app = express.default();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(1245);

export default app;

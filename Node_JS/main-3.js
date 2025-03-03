import countStudents from './3-read_file_async.js';

countStudents('nope.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  });

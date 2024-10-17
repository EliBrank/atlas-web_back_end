export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task3 = true;
    const task4 = false;
    console.log('test output:', task3, task4);
  }

  return [task, task2];
}

export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    const task3 = true;
    const task4 = false;
    console.log(task3 + task4);
  }

  return [task, task2];
}

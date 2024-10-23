export default function getListStudentIds(studentArray) {
  if (studentArray.constructor !== Array) {
    return [];
  }

  return studentArray.map((arrayElement) => arrayElement.id);
}

export default function getListStudentIds(studentArray) {
  if (!studentArray || studentArray.constructor !== Array) {
    return [];
  }

  return studentArray.map((arrayElement) => arrayElement.id);
}

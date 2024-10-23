export default function getStudentsIdSum(studentArray) {
  return studentArray.reduce((accumulator, student) => accumulator + student.id, 0);
}

export default function getStudentsByLocation(studentArray, city) {
  return studentArray.filter((arrayElement) => arrayElement.location === city);
}

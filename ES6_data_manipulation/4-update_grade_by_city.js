export default function updateGradeByCity(studentArray, city, newGrades) {
  return studentArray
    .filter((student) => student.location === city)
    .map((student) => {
      // gets grade associated with student
      let grade = newGrades.find((currentGrade) => currentGrade.studentId === student.id)?.grade;

      // checks if grade exists for student and is 0-100, assigned N/A otherwise
      if (!grade || !(grade >= 0 && grade <= 100)) {
        grade = 'N/A';
      }

      return { ...student, grade };
    });
}

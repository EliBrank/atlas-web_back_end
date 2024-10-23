export default function updateGradeByCity(studentArray, city, newGrades) {
  return studentArray
    .filter((student) => student.location === city)
    .map((student) => {
      // gets grade associated with student
      const gradeObj = newGrades.find((currentGrade) => currentGrade.studentId === student.id);
      let grade = gradeObj ? gradeObj.grade : undefined;

      // checks if grade exists for student and is 0-100, assigned N/A otherwise
      if (!grade || !(grade >= 0 && grade <= 100)) {
        grade = 'N/A';
      }

      return { ...student, grade };
    });
}

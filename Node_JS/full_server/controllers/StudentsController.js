class StudentsController {
  static getAllStudents(request, response) {
    try {
      // calls readDatabase from utils
      // displays:
      // 'This is the list of our students'
      // 'Number of students in ${FIELD}: ${6}. List: ${LISTOFFIRSTNAMES}
    } catch {
      // return a status 500 and the error message 'Cannot load the database'
    }
  }

  static getAllStudentsByMajor(request, response) {
    return (200, )
    // if different parameter passed:
    // server should return a 500 and the error 'Major parameter must be CS or SWE'
    // calls readDatabase from utils
    // List: LIST_OF_FIRSTNAMES_IN_THE_FIELD
    // if database not available:
    // return a status 500 and the error message 'Cannot load the database'
  }
}

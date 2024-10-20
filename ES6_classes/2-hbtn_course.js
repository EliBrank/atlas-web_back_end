export default class HolbertonCourse {

  constructor(name, length, students) {
    // setter is called for each of these assignments
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // Name
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    }
  }

  // Length
  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    }
  }

  // Students
  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (Array.isArray(newStudents) && newStudents.every(student => typeof student === 'string')) {
      this._students = newStudents;
    }
  }

}

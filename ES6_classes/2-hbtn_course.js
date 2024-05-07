export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }
  get name() {
    return this._name;
  }
  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    }
  }
  get length() {
    return this._length;
  }
  set length(length) {
    if (typeof length === 'number') {
      this._length = length;
    }
  }
  get students() {
    return this._students;
  }
  set students(students) {
    if (students instanceof Array) {
      this._students = students;
    }
  }
}

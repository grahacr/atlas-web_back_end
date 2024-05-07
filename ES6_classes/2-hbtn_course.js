export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') {
      this._name = name;
    }
    if (typeof length === 'number') {
      this._length = length;
    }
    if (students instanceof Array) {
      this._students = students;
    }
  };
  get name() {
    return this._name;
  }
  set name(name) {
    return this._name = name;
  }
  get length() {
    return this._length;
  }
  set length(length) {
    return this._length = length;
  }
  get students() {
    return this._students;
  }
  set students(students) {
    return this._students = students;
  }
}

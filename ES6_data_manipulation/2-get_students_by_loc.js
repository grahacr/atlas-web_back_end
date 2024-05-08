export default function getStudentsByLocation(students, city) {
  const studentLocation = students.filter(student => student.location === city)
  return studentLocation;
}
export default function getStudentIdsSum(students) {
  const sumIds = students.reduce((total, student) => total + student.id, 0);
  return sumIds;
}

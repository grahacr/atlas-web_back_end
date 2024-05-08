export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsInCity = students.filter((student) => student.location === city);
  const gradeUpdate = studentsInCity.map((student) => {
    const matchedGrade = newGrades.find((grade) => grade.studentId === student.id);
    if (matchedGrade) {
      return { ...student, grade: matchedGrade.grade };
    }
    return { ...student, grade: 'N/A' };
  });
  return gradeUpdate;
}

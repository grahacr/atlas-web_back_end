export default function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  const idOnly = array.map(item => item.id);
  return idOnly;
}

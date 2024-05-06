export default function concatArrays(array1, array2, string) {
  const concatArray = [...array1, ...array2];
  const resultArray = [...concatArray, ...string];
  return resultArray;
}

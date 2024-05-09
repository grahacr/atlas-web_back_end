export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8array = new Int8Array(buffer);
  if (position >= length) {
    throw new Error('Position outside range');
  }
  int8array[position] = value;
  return buffer;
}

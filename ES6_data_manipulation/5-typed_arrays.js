export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8array = new Int8Array(buffer);
  if (position >= 0 && position < length) {
    int8array[position] = value;
  } else {
    throw new Error('Position outside range');
  }
  return buffer;
}

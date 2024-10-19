export default function appendToEachArrayValue(array, appendString) {
  const arrayCopy = [...array];
  for (const [idx, value] of array.entries()) {
    arrayCopy[idx] = appendString + value;
  }

  return arrayCopy;
}

export default function appendToEachArrayValue(array, appendString) {
  const arrayCopy = [];
  for (const value of array.entries()) {
    arrayCopy.push(appendString + value);
  }

  return arrayCopy;
}

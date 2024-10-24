export default function cleanSet(set, startString) {
  if (startString === '' || !(typeof startString === 'string')) {
    return '';
  }

  const setArray = [];

  for (const value of set) {
    if (value.startsWith(startString) && typeof value === 'string') {
      // gets string for each element in set, adds to array with startString cut off
      setArray.push(value.slice(startString.length));
    }
  }

  return setArray.join('-');
}

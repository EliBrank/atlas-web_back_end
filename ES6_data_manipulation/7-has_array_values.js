export default function hasValuesFromArray(set, array) {
  // first convert array to set to eliminate potential duplicate checks
  const arraySet = new Set(array);

  // check if each unique value from array is contained in input set
  if ([...arraySet].every((value) => set.has(value))) {
    return true;
  }

  return false;
}

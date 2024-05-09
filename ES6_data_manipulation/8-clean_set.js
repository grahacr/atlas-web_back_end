export default function cleanSet(set, startString){
  let matches = '';
  if (typeof startString !== 'string' || startString.length === 0 || !startString) {
    return matches;
  }
  for (const value of set) {
    if (value.startsWith(startString)) {
      let restOfString = value.substring(startString.length);
      matches += (matches.length === 0 ? '' : '-') + restOfString;
    }
  }
  return matches;
}

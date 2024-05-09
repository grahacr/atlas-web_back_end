export default function cleanSet(set, startString){
  const matches = [];
  for (const value of set) {
    if (value.startsWith(startString)) {
      const restOfString = value.substring(startString.length);
      matches.push(restOfString);
    }
  }
  return matches.join('-');
}

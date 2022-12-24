/* 
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
Return your answer as a number.
*/
export function sumMix(x: any[]): number {
  return x.reduce(
    (accumulator, currentValue) => accumulator + Number(currentValue),
    0
  );
}

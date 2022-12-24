/* Given a non-empty array of integers, return the result of multiplying the values together in order. 
Example:
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
*/

export const grow = (arr: number[]): number =>
  arr.reduce((prev, current) => prev * current);

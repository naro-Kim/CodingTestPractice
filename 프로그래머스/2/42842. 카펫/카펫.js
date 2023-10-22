function solution(brown, yellow) {
  for (let width = 1; width <= yellow; width++) {
    if (yellow % width === 0) {
      const height = yellow / width;
      const brownArea = 2 * (width + height) + 4; // Brown area
      if (brownArea === brown) {
        return [height + 2, width + 2];
      }
    }
  }
}
function solution(participant, completion) {
  let map = new Map();
  participant.forEach((key) => map.set(key, (map.get(key) || 0) + 1)); // 중복 처리를 위해 +1
  completion.forEach((key) => map.set(key, (map.get(key) || 0) - 1));
  for (const [key, value] of map) {
    if (value) return key;
  }
}

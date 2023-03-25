function solution(genres, plays) {
  const dict = {};
  genres.forEach((key, index) => {
    dict[key] ? (dict[key] += plays[index]) : (dict[key] = plays[index]);
  });
  
  const sortedSongs = genres
    .map((key, index) => ({ genre: key, plays: plays[index], num: index }))
    
    .sort((a, b) => {
      if (a.genre !== b.genre) {
        return dict[b.genre] - dict[a.genre]; // 장르가 다른 경우, 장르를 키로 dict에 등록된 재생 수를 비교해 정렬한다.
      } else if (a.plays !== b.plays) {
        return b.plays - a.plays; // 재생 수가 다른 경우, 재생 수를 비교해 정렬한다.
      } else {
        return a.num - b.num; // 모두 같은 경우 고유 번호 순으로 정렬한다.
      }
    });
  
  const result = {};
    // 장르가 등록되어있지 않거나, 장르 당 수록 곡이 2개 이하일 때만 재생 수를 넣는다. 
  sortedSongs.forEach((song) => {
    if (!result[song.genre]) {
      result[song.genre] = [song.num];
    } else if (result[song.genre].length < 2) {
      result[song.genre].push(song.num);
    }
  });
  
  return Object.values(result).flat();
}

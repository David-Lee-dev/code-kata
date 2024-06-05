function findMissingParticipant(participant, completion) {
  participant.sort();
  completion.sort();

  for (let i = 0; i < completion.length; i++) {
    if (participant[i] !== completion[i]) {
      return participant[i];
    }
  }

  return participant[participant.length - 1];
}

// 테스트
console.log(
  findMissingParticipant(
    ["트리케라톱스", "티라노사우루스", "바리오닉스"],
    ["바리오닉스", "티라노사우루스"]
  )
); // '트리케라톱스'
console.log(
  findMissingParticipant(
    [
      "티라노사우루스",
      "파키케팔로사우루스",
      "티라노사우루스",
      "스테고사우루스",
    ],
    ["파키케팔로사우루스", "스테고사우루스", "티라노사우루스"]
  )
); // '티라노사우루스'

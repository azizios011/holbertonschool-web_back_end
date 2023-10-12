export default function taskBlock(trueOrFalse) {
  let task = false; // Use 'let' instead of 'var'
  let task2 = true; // Use 'let' instead of 'var'

  if (trueOrFalse) {
    task = true; // Reassign 'task' without redeclaring
    task2 = false; // Reassign 'task2' without redeclaring
  }

  return [task, task2];
}

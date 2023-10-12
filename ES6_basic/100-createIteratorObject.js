export default function* createIteratorObject(report) {
  for (const department in report.allEmployees) {
    if (report.allEmployees[department] instanceof Array) {
      for (const employee of report.allEmployees[department]) {
        yield employee;
      }
    }
  }
}

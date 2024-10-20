export default function createReportObject(employeesList) {
  const allEmployees = { ...employeesList };

  return {
    allEmployees,
    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };
}

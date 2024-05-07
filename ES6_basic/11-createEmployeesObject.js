export default function createEmployeesObject(departmentName, employees) {
  const employeeInfo = {
    [departmentName]: [...employees]
  };
  return employeeInfo;
}

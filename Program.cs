using System;
using System.Numerics;
using System.IO;

namespace laba
{
    class Program
    {
        class Employees
        {
            private int employeeId;
            private string lastName;
            private string firstName;
            private DateTime birthDate;
            private DateTime hireDate;
            private string address;

            public Employees(int employeeId, string lastName, string firstName, DateTime birthDate, DateTime hireDate, string address)
            {
                this.employeeId = employeeId;
                this.lastName = lastName;  
                this.firstName = firstName;
                this.birthDate = birthDate;
                this.hireDate = hireDate;
                this.address = address;
            }

            public int EmployeeId { get => employeeId; set => employeeId = value; }
            public string LastName { get => lastName; set => lastName = value; }
            public string FirstName { get => firstName; set => firstName = value; }
            public DateTime BirthDate { get => birthDate; set => birthDate = value; }
            public DateTime HireDate { get => hireDate; set => hireDate = value; }
            public string Address { get => address; set => address = value; }

            public override string ToString()
            {
                return $"{employeeId} {lastName} {firstName} {birthDate} {hireDate} {address}";
            }

            public static bool operator ==( Employees a, Employees b )
            {
                return a.employeeId == b.employeeId && a.lastName == b.lastName && a.firstName == b.firstName &&
                    a.birthDate == b.birthDate && a.hireDate == b.hireDate && a.address == b.address;
            }

            public static bool operator !=( Employees a, Employees b )
            {
                return !(a == b);
            }
        }

        class EmployeesList
        {
            private Employees[] M;

            public EmployeesList(Employees[] M)
            {
                this.M = M;
            }

            public int Count { get { return M.Length; } }

            public System.Collections.IEnumerator GetEnumerator()
            {
                for (int i = 0; i < Count; i++)
                    yield return M[i];
            }

            public bool Contains( Employees item )
            {
                for (int i = 0;i < Count; i++)
                    if (item == M[i])
                        return true;
                return false;
            }

            public Employees this[int index] {  get => M[index]; set => M[index] = value; } }
        

        static void Main(string[] args) 
        {
            StreamReader cin = new StreamReader("in.txt");

            Employees[] temp = new Employees[int.Parse(cin.ReadLine())];

            string line;
            string[] info;



            int i;

            i = 0;

            while ((line = cin.ReadLine()) != null)
            {
                info = line.Split(' ');

                IEnumerable<int> dateInfo =
                    from d in info[3].Split('/')
                    select int.Parse(d);

                IEnumerable<int> dateInfo2 =
                    from d in info[4].Split('/')
                    select int.Parse(d);

                temp[i] = new Employees(int.Parse(info[0]), info[1], info[2],
                    new DateTime(dateInfo[0], dateInfo[1], dateInfo[2]), 
                    new DateTime(dateInfo2[0], dateInfo2[1], dateInfo2[2]), info[5]);

                i++;
            }

            EmployeesList list = new EmployeesList(temp);

            cin.Close();
        }
    }
}
using ServiceStack.DataAnnotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Read_Write
{
    [Alias("Student")]
    class Student
    {
        public string id_s { get; set; }
        public string name { get; set; }
        public string Gender { get; set; }
        public string year { get; set; }
        public string phone { get; set; }
        public string Address { get; set; }
        public string Photo { get; set; }

    }
}

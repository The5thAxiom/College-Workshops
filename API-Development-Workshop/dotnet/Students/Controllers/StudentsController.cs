using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Students.Models;


namespace Students.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class StudentsController : ControllerBase
    {
        List<Student> allStudents = new List<Student>()
        {
            new Student() {Id = 1, FirstName = "Samridh", MiddleName = "Anand", LastName = "Paatni", Roll = "20BCE1550"},
            new Student() {Id = 2, FirstName = "Sanjeev", MiddleName = "Singh", LastName = "Rawat", Roll = "20BCE1234"}
        };

        // for getting all students
        [HttpGet("GetAllStudents")]
        public IActionResult GetAllStudents()
        {
            if (allStudents.Count == 0)
            {
                return NotFound("No Students");
            }
            return Ok(allStudents);
        }

        // for getting a particular student
        [HttpGet("GetStudent")]
        public IActionResult GetStudent(int id)
        {
            var obj = allStudents.SingleOrDefault(j => j.Id == id);
            return Ok(obj);
        }
    }
}

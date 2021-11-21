using System;
using System.Collections.Generic;
using System.Text;

namespace FinalProject_Template.Models
{
    public class Temperature
    {
        public int Id { get; set; }
        public float Humidity { get; set; }
        public float Celsius { get; set; }
        public float Fahrenheit { get; set; }
        public DateTime Time { get; set; }
    }
}

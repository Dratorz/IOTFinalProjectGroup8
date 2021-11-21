using System;
using System.Collections.Generic;
using System.Text;

namespace FinalProject_Template.Models
{
   public  class ListOfTemperatures
    {
        public List<Temperature> Search { get; set; }
        public List<Temperature> totalResults { get; set; }
        public string Response { get; set; }
    }
}

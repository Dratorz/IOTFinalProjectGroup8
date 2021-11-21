using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace FinalProject_Template.Services.Network
{
    public interface INetworkService
    {
        Task<TResult> GetAsync<TResult>(string url);
    }
}

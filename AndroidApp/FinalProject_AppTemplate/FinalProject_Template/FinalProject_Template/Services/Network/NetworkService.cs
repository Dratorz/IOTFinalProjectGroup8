using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace FinalProject_Template.Services.Network
{
    public class NetworkService : INetworkService
    {
        private HttpClient httpClient;

        public NetworkService()
        {
            httpClient = new HttpClient();
        }

        public async Task<TResult> GetAsync<TResult>(string url)
        {
            HttpResponseMessage response = await httpClient.GetAsync(url);

            string serialized = await response.Content.ReadAsStringAsync();
            var result = JsonConvert.DeserializeObject<TResult>(serialized);

            return result;
        }
    }
}

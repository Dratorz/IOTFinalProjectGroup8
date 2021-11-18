using FinalProject_Template.Views;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Xamarin.CommunityToolkit.ObjectModel;
using Xamarin.Forms;

namespace FinalProject_Template.ViewModels
{
    public class HomePageViewModel : ViewModelBase
    {
        public AsyncCommand ViewTable { get; }
        public AsyncCommand ViewStats { get; }

        public HomePageViewModel()
        {
            ViewTable = new AsyncCommand(ViewT);
            ViewStats = new AsyncCommand(ViewS);
        }

        private async Task ViewS()
        {
            var route = $"{nameof(ViewStatsPage)}";
            await Shell.Current.GoToAsync(route);
        }

        private async Task ViewT()
        {
            var route = $"{nameof(ViewTablePage)}";
            await Shell.Current.GoToAsync(route);
        }
    }
}

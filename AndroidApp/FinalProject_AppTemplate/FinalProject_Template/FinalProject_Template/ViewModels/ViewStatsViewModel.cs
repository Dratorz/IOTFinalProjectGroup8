using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Xamarin.CommunityToolkit.ObjectModel;
using Xamarin.Forms;

namespace FinalProject_Template.ViewModels
{
    public class ViewStatsViewModel : ViewModelBase
    {
        public AsyncCommand GoBackCommand { get; }
        public ViewStatsViewModel()
        {
            Title = "View Stats";

            GoBackCommand = new AsyncCommand(GoBack);
        }

        private async Task GoBack()
        {
            await Shell.Current.GoToAsync("..");
        }
    }
}

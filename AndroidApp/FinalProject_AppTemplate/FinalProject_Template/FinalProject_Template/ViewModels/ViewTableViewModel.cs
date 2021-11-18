using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Xamarin.CommunityToolkit.ObjectModel;
using Xamarin.Forms;

namespace FinalProject_Template.ViewModels
{
    public class ViewTableViewModel : ViewModelBase
    {
        public AsyncCommand GoBackCommand { get; }
        public ViewTableViewModel()
        {
            Title = "View Table";

            GoBackCommand = new AsyncCommand(GoBack);
        }

        private async Task GoBack()
        {
            await Shell.Current.GoToAsync("..");
        }
    }
}

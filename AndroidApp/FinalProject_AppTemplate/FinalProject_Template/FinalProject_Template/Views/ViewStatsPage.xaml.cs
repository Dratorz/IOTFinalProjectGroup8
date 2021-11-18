using FinalProject_Template.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace FinalProject_Template.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class ViewStatsPage : ContentPage
    {
        public ViewStatsPage()
        {
            InitializeComponent();
            BindingContext = new ViewStatsViewModel();
        }
    }
}
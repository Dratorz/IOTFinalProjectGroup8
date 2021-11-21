using FinalProject_Template.Services.Network;
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
    public partial class ViewTablePage : ContentPage
    {
        public ViewTablePage()
        {
            InitializeComponent();
            BindingContext = new ViewTableViewModel(new NetworkService());
        }
    }
}
using FinalProject_Template.ViewModels;
using FinalProject_Template.Views;
using System;
using System.Collections.Generic;
using Xamarin.Forms;

namespace FinalProject_Template
{
    public partial class AppShell : Xamarin.Forms.Shell
    {
        public AppShell()
        {
            InitializeComponent();
            Routing.RegisterRoute(nameof(ViewTablePage), typeof(ViewTablePage));
            Routing.RegisterRoute(nameof(ViewStatsPage), typeof(ViewStatsPage));
        }
    }
}

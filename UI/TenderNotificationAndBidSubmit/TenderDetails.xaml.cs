using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace TenderNotificationAndBidSubmit
{
    /// <summary>
    /// Interaction logic for TenderDetails.xaml
    /// </summary>
    public partial class TenderDetails : Window
    {
        public TenderDetails()
        {
            InitializeComponent();
        }

        public void FillTenderDetails(Dictionary<string,string> tenderDetails)
        {
            this.EventIDtxt.Text = tenderDetails["EventID"];
            this.TenderTitletxt.Text = tenderDetails["Title"];
            this.DeliveryDateIDtxt.Text = tenderDetails["DueDate"];
            this.TypeOfContracttxt.Text = tenderDetails["TypeOfContract"];
            this.Producttxt.Text = tenderDetails["Product"];
            this.DeliveryAttxt.Text = tenderDetails["DeliveryAt"];
            this.BaseCurrencytxt.Text = tenderDetails["BaseCurrency"];
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            BidInfo bidInfo = new BidInfo();
            bidInfo.ShowDialog();
        }
    }
}

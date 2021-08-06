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
    /// Interaction logic for BidInfo.xaml
    /// </summary>
    public partial class BidInfo : Window
    {
        public List<BidderDetails> bidInfos = new List<BidderDetails>();
        public BidInfo()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            BidderDetails bidderDetails = new BidderDetails();
            bidderDetails.CompanyArea = this.CompanyNametxt.Text;
            bidderDetails.RelevantExp = this.Exptxt.Text;
            bidderDetails.FinancialCap = this.FinancialCapabilitytxt.Text;
            bidderDetails.Appreciations = this.Appreciationstxt.Text;
            bidderDetails.PastPerformance = this.PastPerformancetxt.Text;
            bidderDetails.Methodology = this.Methodologytxt.Text;
            bidderDetails.OperationData = this.OperationDatatxt.Text;
            bidderDetails.Resource = this.Resourcestxt.Text;
            bidderDetails.ScopeOfWork = this.ScopeOfWorktxt.Text;
            bidderDetails.Price = this.Pricetxt.Text;
            bidInfos.Add(bidderDetails);

            this.Close();
        }
    }

    public class BidderDetails
    {
        public string CompanyArea { get; set; }
        public string RelevantExp { get; set; }
        public string FinancialCap { get; set; }
        public string Appreciations { get; set; }
        public string PastPerformance { get; set; }
        public string Methodology { get; set; }
        public string OperationData { get; set; }
        public string Resource { get; set; }
        public string ScopeOfWork { get; set; }
        public string Price { get; set; }
    }
}

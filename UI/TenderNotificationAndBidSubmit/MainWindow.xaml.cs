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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace TenderNotificationAndBidSubmit
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        List<Tender> tenders = new List<Tender>();
        List<CompleteTenderInfo> completeTenderInfos = new List<CompleteTenderInfo>();
        public MainWindow()
        {
            InitializeComponent();
            dataGrid1.ItemsSource = tenders = LoadBasicTenderData();
            LoadCompleteTenderInfo();
        }

        private List<Tender> LoadBasicTenderData()
        {
            List<Tender> authors = new List<Tender>();
            authors.Add(new Tender()
            {
                EventID = "101",
                Title = "Procurement of HSFG BOLTS & NUTS & Washer",
                DueDate = new DateTime(2020, 10, 03),
            });

            authors.Add(new Tender()
            {
                EventID = "201",
                Title = "Supply of Line Hardware Items",
                DueDate = new DateTime(2020, 10, 11)
            });

            authors.Add(new Tender()
            {
                EventID = "301",
                Title = "SUPPLY OF ELECTRICAL ACTUATORS AS PER ITEM DESCRIPTION",
                DueDate = new DateTime(2020, 10, 21)
            });
            //JOURNAL HEAD FULLY MACHINED
            authors.Add(new Tender()
            {
                EventID = "401",
                Title = "JOURNAL HEAD FULLY MACHINED",
                DueDate = new DateTime(2020, 10, 21)
            });

            return authors;
        }

        private void LoadCompleteTenderInfo()
        {

            completeTenderInfos.Add(new CompleteTenderInfo()
            {
                EventID = "101",
                Title = "Procurement of HSFG BOLTS & NUTS & Washer",
                DueDate = new DateTime(2020, 10, 03),
                Product = "Mechanical",
                TypeOfContract = "Goods",
                DeliveryAt = "Hyderabad",
                BaseCurrency = "Indian Rupee"
            });

            completeTenderInfos.Add(new CompleteTenderInfo()
            {
                EventID = "201",
                Title = "Supply of Line Hardware Items",
                DueDate = new DateTime(2020, 10, 11),
                Product = "Mechanical",
                TypeOfContract = "Goods",
                DeliveryAt = "Hyderabad",
                BaseCurrency = "Indian Rupee"
            });

            completeTenderInfos.Add(new CompleteTenderInfo()
            {
                EventID = "301",
                Title = "SUPPLY OF ELECTRICAL ACTUATORS AS PER ITEM DESCRIPTION",
                DueDate = new DateTime(2020, 10, 21),
                Product = "Electrical",
                TypeOfContract = "Goods",
                DeliveryAt = "Bangalore",
                BaseCurrency = "Indian Rupee"
            });
            //JOURNAL HEAD FULLY MACHINED
            completeTenderInfos.Add(new CompleteTenderInfo()
            {
                EventID = "401",
                Title = "JOURNAL HEAD FULLY MACHINED",
                DueDate = new DateTime(2020, 10, 21),
                Product = "Mechanical",
                TypeOfContract = "Goods",
                DeliveryAt = "Bombay",
                BaseCurrency = "Indian Rupee"
            });
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            TenderDetails tenderDetails = new TenderDetails();
            

            Dictionary<string, string> tenderInfo = new Dictionary<string, string>();
            if(tenders.Any(x=> x.EventID == tenderID.Text))
            {
                Tender tender = tenders.FirstOrDefault(x => x.EventID == tenderID.Text);
                tenderInfo.Add("EventID", tender.EventID);
                tenderInfo.Add("Title", tender.Title);
                tenderInfo.Add("DueDate", tender.DueDate.ToString());
            }
            if (completeTenderInfos.Any(x => x.EventID == tenderID.Text))
            {
                CompleteTenderInfo completeTender = completeTenderInfos.FirstOrDefault(x => x.EventID == tenderID.Text);
                tenderInfo.Add("Product", completeTender.Product);
                tenderInfo.Add("TypeOfContract", completeTender.TypeOfContract);
                tenderInfo.Add("DeliveryAt", completeTender.DeliveryAt);
                tenderInfo.Add("BaseCurrency", completeTender.BaseCurrency);
            }
            tenderDetails.FillTenderDetails(tenderInfo);
            tenderDetails.ShowDialog();
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            AdminLogin adminLogin = new AdminLogin();
            adminLogin.loginSucessfull += AdminLogin_loginSucessfull;

            adminLogin.ShowDialog();
        }

        private void AdminLogin_loginSucessfull(object sender, EventArgs e)
        {
            this.SubmitTenderEvaluation.Visibility = Visibility.Visible;
        }

        private void SubmitTenderEvaluation_Click(object sender, RoutedEventArgs e)
        {
            EvaluationProcess evaluationProcess = new EvaluationProcess();


            evaluationProcess.ShowDialog();
        }
    }

    public class Tender
    {
        public string EventID { get; set; }
        public string Title { get; set; }
        public DateTime DueDate { get; set; }
    }

    public class CompleteTenderInfo
    {
        public string EventID { get; set; }
        public string Title { get; set; }
        public DateTime DueDate { get; set; }
        public string Product { get; set; }
        public string TypeOfContract { get; set; }
        public string DeliveryAt { get; set; }
        public string BaseCurrency { get; set; }
        
    }
}

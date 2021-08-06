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
    /// Interaction logic for EvaluationProcess.xaml
    /// </summary>
    public partial class EvaluationProcess : Window
    {
        public EvaluationProcess()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            this.Bidder1Avg.Visibility = Visibility.Visible;
            this.Bidder2Avg.Visibility = Visibility.Visible;
            this.Bidder3Avg.Visibility = Visibility.Visible;

            this.b1evalu1.Text = "0.85";
            this.b1evalu2.Text = "0.75";
            this.b1evalu3.Text = "0.85";
            this.b1evalu4.Text = "0.75";
            this.b1evalu5.Text = "0.85";
            this.b1evalu6.Text = "0.75";
            this.b1evalu7.Text = "0.75";
            this.b1evalu8.Text = "1.125";
            this.b1evalu9.Text = "0.825";

            this.b2evalu1.Text = "0.85";
            this.b2evalu2.Text = "0.75";
            this.b2evalu3.Text = "0.85";
            this.b2evalu4.Text = "0.75";
            this.b2evalu5.Text = "0.55";
            this.b2evalu6.Text = "0.85";
            this.b2evalu7.Text = "0.75";
            this.b2evalu8.Text = "1.275";
            this.b2evalu9.Text = "1.125";


            this.b3evalu1.Text = "0.55";
            this.b3evalu2.Text = "0.85";
            this.b3evalu3.Text = "0.75";
            this.b3evalu4.Text = "0.55";
            this.b3evalu5.Text = "0.75";
            this.b3evalu6.Text = "0.75";
            this.b3evalu7.Text = "0.55";
            this.b3evalu8.Text = "1.125";
            this.b3evalu9.Text = "1.125";

            this.Bidder1Avg.Text = "7.5 ";
            this.Bidder2Avg.Text = "7.75";
            this.Bidder3Avg.Text = "7";
            this.ResultMessage.Visibility = Visibility.Visible;
        }

        private void ComboBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }
    }
}

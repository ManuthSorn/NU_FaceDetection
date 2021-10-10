using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;


namespace Read_Write
{
    public partial class Form1 : Form
    {
        
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'attendancedbDataSet.tbl_attendance' table. You can move, or remove it, as needed.
            this.tbl_attendanceTableAdapter.Fill(this.attendancedbDataSet.tbl_attendance);
            // TODO: This line of code loads data into the 'attendancedbDataSet.tbl_information' table. You can move, or remove it, as needed.
            this.tbl_informationTableAdapter1.Fill(this.attendancedbDataSet.tbl_information);
            // TODO: This line of code loads data into the 'attendancedb.tbl_information' table. You can move, or remove it, as needed.
        

            coboColumn.SelectedIndex = 1;

        }

        private void tb_search_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void tb_search_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode==Keys.Enter)
            {
                if (string.IsNullOrEmpty(tb_search.Text))
                {
                    tblinformationBindingSource1.Filter = string.Empty;
                }
                else
                {
                    tblinformationBindingSource1.Filter = string.Format("{0}='{1}'",coboColumn.Text, tb_search.Text);
                }
            }
        }

        private void tblinformationBindingSource1_CurrentChanged(object sender, EventArgs e)
        {

        }

        private void fKtblattendancetblinformationBindingSource_CurrentChanged(object sender, EventArgs e)
        {

        }

        private void btnBrowse_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog ofd = new OpenFileDialog() { Filter = "JPEG|*.jpg|*PNG|*.png", ValidateNames = true })
            {
                if (ofd.ShowDialog()==DialogResult.OK)
                {
                    pictureBox1.Image = Image.FromFile(ofd.FileName);
                    Student obj = tblinformationBindingSource.Current as Student;
                    if (obj != null)
                        obj.Photo = ofd.FileName;

                }
            }
        }

        void ClearInput()
        {
            tbID.Text = null;
            tbName.Text = null;
            comboGender.Text = null;
            tbPhone.Text = null;
            coboColumn.Text = null;
            tbAddress.Text = null;
            comboYear.Text = null;
            pictureBox1.Image = null;
        }
        SqlConnection cn = new SqlConnection("Data Source=MSI;Initial Catalog=attendancedb;User ID=sa;Password=1053");
        private void btnAdd_Click(object sender, EventArgs e)
        {
            cn.Open();
            int i = 0;

            SqlCommand cmd = new SqlCommand("INSERT INTO tbl_information(id_s, name, Gender,year, phone, Address, Photo) VALUES('" + tbID.Text + "','" + tbName.Text + "','" + comboGender.Text + "','" + comboYear.Text + "','" + tbPhone.Text + "','" + tbAddress.Text + "', @Photo)",cn);

            MemoryStream stream = new MemoryStream();

            pictureBox1.Image.Save(stream, System.Drawing.Imaging.ImageFormat.Jpeg);

            byte[] pic = stream.ToArray();
            cmd.Parameters.AddWithValue("@Photo", pic);

            i = cmd.ExecuteNonQuery();

            if (i>0)
            {
                //MessageBox.Show("Thank you" + i);

                ClearInput();
            }

            cn.Close();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void tabPage2_Click(object sender, EventArgs e)
        {

        }

        private void coboColumn_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void tb_search3_TextChanged(object sender, EventArgs e)
        {

        }

        private void tabPage1_Click(object sender, EventArgs e)
        {

        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
           
        }
    }
}

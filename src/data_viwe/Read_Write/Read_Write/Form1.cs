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
using System.Drawing.Imaging;

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
            // TODO: This line of code loads data into the 'attendancedbDataSet.tbl_information' table. You can move, or remove it, as needed.
            this.tbl_informationTableAdapter.Fill(this.attendancedbDataSet.tbl_information);
            // TODO: This line of code loads data into the 'attendancedbDataSet.tbl_attendance' table. You can move, or remove it, as needed.
            this.tbl_attendanceTableAdapter.Fill(this.attendancedbDataSet.tbl_attendance);
            // TODO: This line of code loads data into the 'attendancedbDataSet.tbl_attendance' table. You can move, or remove it, as needed.
            this.tbl_attendanceTableAdapter.Fill(this.attendancedbDataSet.tbl_attendance);
            // TODO: This line of code loads data into the 'attendancedbDataSet.tbl_information' table. You can move, or remove it, as needed.
            //this.tbl_informationTableAdapter1.Fill(this.attendancedbDataSet.tbl_information);
            // TODO: This line of code loads data into the 'attendancedb.tbl_information' table. You can move, or remove it, as needed.
        

            coboColumn.SelectedIndex = 1;

            Disp_data();
            Disp_data_inpu();

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
                    tblinformationBindingSource.Filter = string.Empty;
                }
                else
                {
                    tblinformationBindingSource.Filter = string.Format("{0}='{1}'",coboColumn.Text, tb_search.Text);
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
                if (ofd.ShowDialog() == DialogResult.OK)
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
            comboYear.Text = null;
            tbMajor.Text = null;
            tbAddress.Text = null;
            pictureBox1.Image = null; // Box Store Image
        }
        SqlConnection cn = new SqlConnection(@"Data Source=MSI;Initial Catalog=attendancedb;User ID=sa;Password=1053");


        private void btnAdd_Click(object sender, EventArgs e)
        {
            try
            {
                cn.Open();
                SqlCommand cmd = new SqlCommand("INSERT INTO tbl_information(id_s, name, Gender,year, phone, Address,Major, Photo) VALUES('" + tbID.Text + "','" + tbName.Text + "','" + comboGender.Text + "','" + comboYear.Text + "','" + tbPhone.Text + "','" + tbMajor.Text + "','" + tbAddress.Text + "', @Photo)", cn);
                MemoryStream stream = new MemoryStream();
                pictureBox1.Image.Save(stream, System.Drawing.Imaging.ImageFormat.Jpeg);
                byte[] pic = stream.ToArray();
                cmd.Parameters.AddWithValue("@Photo", pic);
                cmd.ExecuteNonQuery();
                ClearInput();
                cn.Close();
                Disp_data_inpu();
            }
            catch(Exception)
            {
                // MessageBox.Show("Don't forget input Photo");
                throw;
            }
        }


        public void Disp_data()
        {
            cn.Open();
            SqlCommand cmd = cn.CreateCommand();
            cmd.CommandType = CommandType.Text;
            cmd.CommandText = "select tbl_information.name AS [Student Name], tbl_attendance.id_f AS [Student ID],tbl_information.Major as Major,tbl_information.year as Year,tbl_information.Gender as Gender,tbl_information.Address as Address,tbl_information.Photo from tbl_information INNER JOIN tbl_attendance on tbl_information.id_s =tbl_attendance.id_f";
            cmd.ExecuteNonQuery();
            DataTable dt = new DataTable();
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            da.Fill(dt);
            dataGridView3.DataSource = dt;

            cn.Close();
        }

        // Display data that get from Input from page 1
        public void Disp_data_inpu()
        {
            cn.Open();
            SqlCommand cmd = cn.CreateCommand();
            cmd.CommandType = CommandType.Text;
            cmd.CommandText = "SELECT id_s as [Student ID],name as [Student Name],Gender,year as Year,phone as [Phone Number],Address,Major,Photo FROM tbl_information";
            cmd.ExecuteNonQuery();
            DataTable dt = new DataTable();
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            da.Fill(dt);
            dataGridView1.DataSource = dt;
            cn.Close();
        }


        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            tbID.Text = dataGridView1.Rows[e.RowIndex].Cells[0].Value.ToString();
            tbName.Text = dataGridView1.Rows[e.RowIndex].Cells[1].Value.ToString();
            comboGender.Text = dataGridView1.Rows[e.RowIndex].Cells[2].Value.ToString();
            comboYear.Text = dataGridView1.Rows[e.RowIndex].Cells[3].Value.ToString();
            tbPhone.Text = dataGridView1.Rows[e.RowIndex].Cells[4].Value.ToString();
            tbAddress.Text = dataGridView1.Rows[e.RowIndex].Cells[5].Value.ToString();
            tbMajor.Text = dataGridView1.Rows[e.RowIndex].Cells[6].Value.ToString();

            byte[] pic = (byte[])dataGridView1.Rows[e.RowIndex].Cells[7].Value; // Box Store Image
            MemoryStream ms = new MemoryStream(pic);
            pictureBox1.Image = Image.FromStream(ms);

        }

        private void btnEdit_Click(object sender, EventArgs e)
        {
            cn.Open();
            SqlCommand cmd = cn.CreateCommand();
            cmd = new SqlCommand("update tbl_information set id_s='" + tbID.Text + "', " + "name='" + tbName.Text + "', " + "Gender='" + comboGender.Text + "', " + "year='" + comboYear.Text + "', " + "phone='" + tbPhone.Text + "', " + "Address='" + tbAddress.Text + "', " + "Major='"+ tbMajor.Text +"'" + " WHERE ID=15'", cn);
            cmd.ExecuteNonQuery();
            MessageBox.Show("Done");
            cn.Close();
            Disp_data_inpu();
        }

        private void tabPage2_Click(object sender, EventArgs e)
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

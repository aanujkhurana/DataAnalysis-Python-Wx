
import wx
import wx.grid
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from App.ui.template_frame import MyFrame1 as MyFrame1
from App.logic.dataclean import df as df

from App.logic.DataTable import DataTable


class TableFrame(MyFrame1):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.table = DataTable(df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Show(True)
        self.Layout()

        # Bind the search button to search method
        self.Bind(wx.EVT_BUTTON, self.OnSearch, self.m_button1)

        # Create references to ComboBox, TextCtrl, and Filter button
        self.data_type_combo = self.m_comboBox1
        self.filter_input = self.m_comboText
        self.filter_button = self.m_button2
        self.Bind(wx.EVT_BUTTON, self.OnOffSearch, self.m_button_offence)

        # Bind the filter button to the filter method
        self.Bind(wx.EVT_BUTTON, self.OnFilter, self.filter_button)

        # Bind reset button to reset method
        self.Bind(wx.EVT_BUTTON, self.OnResetFilters, self.m_button3)

        # Bind buttons to generate and export the Matplotlib graph
        self.Bind(wx.EVT_BUTTON, self.OnGenerateGraph, self.m_button_graph)
        self.Bind(wx.EVT_BUTTON, self.OnExportGraph, self.m_button_export)
        self.canvas = None  # Store the FigureCanvas

        # generate report button
        self.Bind(wx.EVT_BUTTON, self.on_process_data, self.m_button_r)

        # generate Mobile Case Analysis button
        self.Bind(wx.EVT_BUTTON, self.on_mobilecase_analysis, self.m_button_mobilecase)

    # PentalyCase Page
    # search method for selected date range
    def OnSearch(self, event):
        # Get the selected start and end dates from the DatePickers
        start_date = self.m_datePicker_start.GetValue()
        end_date = self.m_datePicker_end.GetValue()

        # Convert the selected start and end dates to Pandas-compatible date strings
        start_date_str = start_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        end_date_str = end_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'

        # Filter the DataFrame based on the selected date range
        df_filtered = df[(df['OFFENCE_MONTH'] >= start_date_str) & (df['OFFENCE_MONTH'] <= end_date_str)]

        # Create a DataTable with the filtered data
        filtered_table = DataTable(df_filtered)

        # Clear the grid and set it to display the filtered data
        self.m_grid1.ClearGrid()
        self.m_grid1.SetTable(filtered_table, True)
        self.m_grid1.AutoSize()
        self.Layout()

    # filter method for generic filtering
    def OnFilter(self, event):
        # Get the selected data type from the ComboBox
        selected_data_type = self.data_type_combo.GetStringSelection()

        # Get the filter input value from the TextCtrl
        filter_value = self.filter_input.GetValue()

        # Initialize df_filtered with an empty DataFrame
        df_filtered = pd.DataFrame(columns=df.columns)

        # Check if "None" is selected in the ComboBox
        if selected_data_type != "None":
            # Filter the DataFrame based on the selected data type and input value
            if selected_data_type == 'CAMERA_TYPE':
                df_filtered = df[df['CAMERA_TYPE'] == filter_value]
            elif selected_data_type == 'SPEED_BAND':
                df_filtered = df[df['SPEED_BAND'] == filter_value]
            elif selected_data_type == 'SECTION_CLAUSE':
                df_filtered = df[df['SECTION_CLAUSE'] == filter_value]
            elif selected_data_type == 'LEGISLATION':
                df_filtered = df[df['LEGISLATION'] == filter_value]
            elif selected_data_type == 'LOCATION_CODE':
                filter_value_int = int(filter_value)
                df_filtered = df[df['LOCATION_CODE'] == filter_value_int]
            elif selected_data_type == 'OFFENCE_CODE':
                filter_value_int = int(filter_value)
                df_filtered = df[df['OFFENCE_CODE'] == filter_value_int]
            elif selected_data_type == 'LOCATION_DETAILS':
                df_filtered = df[df['LOCATION_DETAILS'] == filter_value]
            # Add more elif conditions for other data types as needed

        # Check if there is data to display after filtering
        if df_filtered.empty:
            wx.MessageBox("No data to display.", "No Data", wx.OK | wx.ICON_INFORMATION)
            return

        # Create a DataTable with the filtered data
        filtered_table = DataTable(df_filtered)

        # Clear the grid and set it to display the filtered data
        self.m_grid1.ClearGrid()
        self.m_grid1.SetTable(filtered_table, True)
        self.m_grid1.AutoSize()
        self.Layout()

    # reset all filters and date
    def OnResetFilters(self, event):
        self.table = DataTable(df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Show(True)
        self.Layout()

    #   offence description search
    def OnOffSearch(self, event):
        # Get the search query from the TextCtrl
        search_query = self.m_search_text.GetValue().strip().lower()
        # Convert to lowercase for case-insensitive search

        if not search_query:
            wx.MessageBox("Please enter a search query.", "Search Query Empty", wx.OK | wx.ICON_INFORMATION)
            return

        # Get the selected start and end dates from the DatePickers
        start_date = self.m_datePicker_start1.GetValue()
        end_date = self.m_datePicker_end1.GetValue()

        # Convert the selected start and end dates to Pandas-compatible date strings
        start_date_str = start_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        end_date_str = end_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'

        # Filter the DataFrame based on the selected date range
        df_filtered = df[(df['OFFENCE_MONTH'] >= start_date_str) & (df['OFFENCE_MONTH'] <= end_date_str)]

        # Perform the search on the "OFFENCE_DESC" column with case-insensitivity
        search_results = df_filtered[df_filtered['OFFENCE_DESC'].str.lower().str.contains(search_query, case=False)]

        if search_results.empty:
            wx.MessageBox("No matching records found.", "No Matches", wx.OK | wx.ICON_INFORMATION)
        else:
            # Create a new DataTable with the search results
            search_table = DataTable(search_results)

            # Clear the grid and set it to display the search results
            self.m_grid_offence.ClearGrid()
            self.m_grid_offence.SetTable(search_table, True)
            self.m_grid_offence.AutoSize()
            self.Layout()

    # ChartPage
    # export graph
    def OnExportGraph(self, event):
        # Check if there is a canvas to export
        if self.canvas is not None:
            # Open a file dialog to choose the export file path and format
            file_dialog = wx.FileDialog(self, "Save Graph As...",
                                        wildcard="PNG files (*.png)|*.png|PDF files (*.pdf)|*.pdf",
                                        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # User canceled the file dialog

            export_path = file_dialog.GetPath()
            file_dialog.Destroy()

            # Save the current figure to the chosen file path and format
            plt.savefig(export_path, bbox_inches='tight')
            wx.MessageBox(f"Graph saved to {export_path}", "Export Successful", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("No graph to export. Generate a graph first.", "Export Failed", wx.OK | wx.ICON_WARNING)

    # generate graphs options
    def OnGenerateGraph(self, event):
        # Get the selected graph type from the ComboBox
        selected_graph_type = self.m_comboBox_graph.GetStringSelection()

        if selected_graph_type == "HeatMap":
            # Generate a bar graph
            self.generate_heat_map()
        elif selected_graph_type == "CameraAnalysis":
            # Generate a line graph
            self.generate_cameraType_chart()
        elif selected_graph_type == "LocationAnalysis":
            # Generate a pie chart
            self.generate_location_analysis()
        elif selected_graph_type == 'SeasonalAnalysis':
            # Generate a Stack Plot
            self.generate_seasonal_analysis()
        elif selected_graph_type == 'PenaltyCasesAnalysis':
            # Generate a Stack Plot
            self.generate_pentalycase_analysis()
        else:
            wx.MessageBox("Please select a valid graph type.", "Invalid Selection", wx.OK | wx.ICON_WARNING)

    def generate_cameraType_chart(self):
        # clear
        self.clear_m_panel()
        # Get the selected start and end dates from the DatePickers
        start_date = self.m_datePicker_graph_start.GetValue()
        end_date = self.m_datePicker_graph_end.GetValue()
        # Convert the selected start and end dates to Pandas-compatible date strings
        start_date_str = start_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        end_date_str = end_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'

        # Filter the DataFrame based on the selected date range
        filtered_df = df[(df['OFFENCE_MONTH'] >= start_date_str) & (df['OFFENCE_MONTH'] <= end_date_str)]

        # Group by CAMERA_TYPE and calculate the count of penalties for each type
        camera_type_counts = filtered_df['CAMERA_TYPE'].value_counts()
        # Create a bar chart to visualize the distribution
        plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
        camera_type_counts.plot(kind='bar')
        plt.xlabel('Camera Type')
        plt.ylabel('Number of Penalties')
        plt.title('Distribution of Penalties by Camera Type')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Ensure labels are not cut off
        # Embed the Matplotlib chart in the m_panel
        self.canvas = FigureCanvas(self.m_panel, -1, plt.gcf())
        self.m_panel.Layout()

    def generate_heat_map(self):
        # clear
        self.clear_m_panel()
        # Get the selected start and end dates from the DatePickers
        start_date = self.m_datePicker_graph_start.GetValue()
        end_date = self.m_datePicker_graph_end.GetValue()
        # Convert the selected start and end dates to Pandas-compatible date strings
        start_date_str = start_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        end_date_str = end_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'

        # Filter the DataFrame based on the selected date range
        filtered_df = df[(df['OFFENCE_MONTH'] >= start_date_str) & (df['OFFENCE_MONTH'] <= end_date_str)]

        # correlation heatmap
        numeric_columns = filtered_df.select_dtypes(include=['number'])  # Select only numeric columns

        # Calculate the correlation matrix for numeric columns
        correlation_matrix = numeric_columns.corr()

        # Create a heatmap
        plt.figure(figsize=(7, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Embed the Matplotlib chart in the m_panel
        self.canvas = FigureCanvas(self.m_panel, -1, plt.gcf())
        self.m_panel.Layout()

    def generate_location_analysis(self):
        # clear
        self.clear_m_panel()
        # Get the selected start and end dates from the DatePickers
        start_date = self.m_datePicker_graph_start.GetValue()
        end_date = self.m_datePicker_graph_end.GetValue()
        # Convert the selected start and end dates to Pandas-compatible date strings
        start_date_str = start_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        end_date_str = end_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'

        # Filter the DataFrame based on the selected date range
        filtered_df = df[(df['OFFENCE_MONTH'] >= start_date_str) & (df['OFFENCE_MONTH'] <= end_date_str)]

        # Group by LOCATION_DETAILS and calculate the count of penalties for each location
        location_counts = filtered_df['LOCATION_DETAILS'].value_counts().reset_index()
        location_counts.columns = ['LOCATION_DETAILS', 'Number of Penalties']

        # Sort the locations by the number of penalties (descending order)
        location_counts = location_counts.sort_values(by='Number of Penalties', ascending=False)

        # Create a heatmap to visualize the distribution
        plt.figure(figsize=(12, 6))
        sns.heatmap(location_counts.head(20).set_index('LOCATION_DETAILS'), annot=True, cmap='YlGnBu', fmt='d')
        plt.xlabel('Number of Penalties')
        plt.ylabel('Location Details')
        plt.title('Distribution of Penalties by Location (Top 20)')
        plt.tight_layout()

        # Embed the Matplotlib chart in the m_panel
        self.canvas = FigureCanvas(self.m_panel, -1, plt.gcf())
        self.m_panel.Layout()

    def generate_seasonal_analysis(self):
        # clear
        self.clear_m_panel()
        # Get the selected start and end dates from the DatePickers
        start_date = self.m_datePicker_graph_start.GetValue()
        end_date = self.m_datePicker_graph_end.GetValue()
        # Convert the selected start and end dates to Pandas-compatible date strings
        start_date_str = start_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        end_date_str = end_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'

        # Filter the DataFrame based on the selected date range
        filtered_df = df[(df['OFFENCE_MONTH'] >= start_date_str) & (df['OFFENCE_MONTH'] <= end_date_str)]

        # Group by month and calculate the sum of penalty notices
        monthly_data = filtered_df.groupby(filtered_df['OFFENCE_MONTH'].dt.strftime('%m'))['TOTAL_NUMBER'].sum().reset_index()

        # Create a line plot for seasonal analysis
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_data['OFFENCE_MONTH'], monthly_data['TOTAL_NUMBER'], marker='o', linestyle='-')
        plt.title('Seasonal Analysis of Penalty Notices')
        plt.xlabel('Months')
        plt.ylabel('Total Penalty Notices Issued')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Embed the Matplotlib chart in the m_panel
        self.canvas = FigureCanvas(self.m_panel, -1, plt.gcf())
        self.m_panel.Layout()

    def generate_pentalycase_analysis(self):
        # Clear the m_panel before creating the new chart
        self.clear_m_panel()
        # Get the selected start and end dates from the DatePickers
        start_date = self.m_datePicker_graph_start.GetValue()
        end_date = self.m_datePicker_graph_end.GetValue()
        # Convert the selected start and end dates to Pandas-compatible date strings
        start_date_str = start_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        end_date_str = end_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        # Filter the DataFrame based on the selected date range
        df_filtered = df[(df['OFFENCE_MONTH'] >= start_date_str) & (df['OFFENCE_MONTH'] <= end_date_str)]
        # Group the data by financial year and calculate the total number of penalty notices issued in each year
        grouped_data = df_filtered.groupby('OFFENCE_FINYEAR')['TOTAL_NUMBER'].sum()
        # Create the bar chart
        plt.figure(figsize=(8, 6))  # Set the figure size (optional)
        # Plot the data
        plt.bar(grouped_data.index, grouped_data.values)
        # Customize the plot
        plt.title('Total Penalty Notices Issued by Financial Year (Bar Graph)')
        plt.xlabel('Financial Year')
        plt.ylabel('Total Number of Penalty Notices')
        plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
        # Embed the Matplotlib graph in the m_panel
        self.canvas = FigureCanvas(self.m_panel, -1, plt.gcf())
        self.m_panel.Layout()

    def clear_m_panel(self):
        # Clear the m_panel by destroying the previous FigureCanvas
        if self.canvas is not None:
            self.canvas.Destroy()

    #  report Generate Page
    def on_process_data(self, event):
        # Get the selected start and end dates from the DatePickers
        start_date = self.m_datePicker_rstart.GetValue()
        end_date = self.m_datePicker_rend.GetValue()
        start_date_str = start_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'
        end_date_str = end_date.Format("%Y-%m-%d")  # Format as 'YYYY-MM-DD'

        # Filter the DataFrame based on the selected date range
        df_filtered = df[(df['OFFENCE_MONTH'] >= start_date_str) & (df['OFFENCE_MONTH'] <= end_date_str)]

        # Function 1: Speed-Related Violations
        def speed_related_violations():
            speed_violations = df[df['SPEED_IND'] == 'Y']
            filtered_df = speed_violations[(speed_violations['OFFENCE_MONTH'] >= start_date_str) &
                                           (speed_violations['OFFENCE_MONTH'] <= end_date_str)]
            speed_band_counts = filtered_df['SPEED_BAND'].value_counts().reset_index()
            speed_band_counts.columns = ['Speed Band', 'Frequency']
            speed_band_counts = speed_band_counts.sort_values(by='Speed Band')
            return speed_band_counts

        # Function 2: Top Locations with Max Penalty Cases
        def top_locations_with_max_penalty_cases():
            filtered_df = df[(df['OFFENCE_MONTH'] >= start_date_str) &
                             (df['OFFENCE_MONTH'] <= end_date_str)]
            location_counts = filtered_df['LOCATION_DETAILS'].value_counts().reset_index()
            location_counts.columns = ['Location Details', 'Frequency']
            location_counts = location_counts.sort_values(by='Frequency', ascending=False)
            location_counts_top_N = location_counts.head(10)  # You can customize the number of top locations
            return location_counts_top_N

        def generate_pie_chart():
            # Clear the m_panel before creating the new chart
            self.clear_m_panel()
            # Group the data by financial year and calculate the total number of penalty notices issued in each year
            grouped_data = df_filtered.groupby('OFFENCE_FINYEAR')['TOTAL_NUMBER'].sum()
            # Create the pie chart
            plt.figure(figsize=(6, 6))  # Set the figure size (optional)
            # Plot the data
            plt.pie(grouped_data.values, labels=grouped_data.index, autopct='%1.1f%%', startangle=140)
            # Customize the plot
            plt.title('Distribution of Penalty Notices by Financial Year (Pie Chart)')
            # Embed the Matplotlib graph in the m_panel
            self.canvas = FigureCanvas(self.m_panel14, -1, plt.gcf())
            self.m_panel.Layout()

        def generate_bar_graph():
            # Clear the m_panel before creating the new chart
            self.clear_m_panel()
            # Group the data by financial year and calculate the total number of penalty notices issued in each year
            grouped_data = df_filtered.groupby('OFFENCE_FINYEAR')['TOTAL_NUMBER'].sum()
            # Create the bar chart
            plt.figure(figsize=(7, 5))  # Set the figure size (optional)
            # Plot the data
            plt.bar(grouped_data.index, grouped_data.values)
            # Customize the plot
            plt.title('Total Penalty Notices Issued by Financial Year (Bar Graph)')
            plt.xlabel('Financial Year')
            plt.ylabel('Total Number of Penalty Notices')
            plt.xticks(rotation=30)  # Rotate x-axis labels for better readability
            plt.tight_layout()
            # Embed the Matplotlib graph in the m_panel
            self.canvas = FigureCanvas(self.m_panel14, -1, plt.gcf())
            self.m_panel.Layout()

        def generate_line_graph():
            # Clear the m_panel before creating the new chart
            self.clear_m_panel()
            # Group the data by financial year and calculate the total number of penalty notices issued in each year
            grouped_data = df_filtered.groupby('OFFENCE_FINYEAR')['TOTAL_NUMBER'].sum()
            # Create the line chart
            plt.figure(figsize=(7, 5))  # Set the figure size (optional)
            # Plot the data
            plt.plot(grouped_data.index, grouped_data.values, marker='o', linestyle='-')
            # Customize the plot
            plt.title('Total Penalty Notices Issued by Financial Year (Line Graph)')
            plt.xlabel('Financial Year')
            plt.ylabel('Total Number of Penalty Notices')
            # Embed the Matplotlib graph in the m_panel
            self.canvas = FigureCanvas(self.m_panel14, -1, plt.gcf())
            self.m_panel.Layout()

        def generate_stack_plot():
            # Clear the m_panel before creating the new chart
            self.clear_m_panel()
            # Group the data by financial year and calculate the total number of penalty notices issued in each year
            grouped_data = df_filtered.groupby('OFFENCE_FINYEAR')['TOTAL_NUMBER'].sum()
            # Create a stack plot
            plt.figure(figsize=(7, 5))  # Set the figure size (optional)
            # Plot the stack plot using the grouped_data series
            plt.stackplot(grouped_data.index, grouped_data.values, labels=[grouped_data.name])
            # Customize the plot
            plt.title('Stack Plot of Penalty Notices by Financial Year')
            plt.xlabel('Financial Year')
            plt.ylabel('Total Number of Penalty Notices')
            plt.legend(loc='upper left', title='Years')

            # Embed the Matplotlib graph in the m_panel
            self.canvas = FigureCanvas(self.m_panel14, -1, plt.gcf())
            self.m_panel.Layout()

        selected_graph = self.m_comboBox_graph1.GetStringSelection()
        if selected_graph == "PieChart":
            generate_pie_chart()
        elif selected_graph == "BarGraph":
            generate_bar_graph()
        elif selected_graph == "LineGraph":
            generate_line_graph()
        elif selected_graph == "StackPlot":
            generate_stack_plot()

        # Call the functions
        speed_data = speed_related_violations()
        location_data = top_locations_with_max_penalty_cases()
        # Update the m_grid_r1 table with speed data
        self.update_grid(self.m_grid_r1, speed_data)
        # Update the m_grid_r2 table with location data
        self.update_grid(self.m_grid_r2, location_data)

    def update_grid(self, grid, data):
        # Clear the existing data in the grid
        grid.ClearGrid()

        # Check if the data has more rows or columns than the grid can display
        num_rows, num_cols = grid.GetNumberRows(), grid.GetNumberCols()
        data_rows, data_cols = data.shape[0], data.shape[1]

        # Resize the grid if needed
        if data_rows > num_rows:
            grid.AppendRows(data_rows - num_rows)
        if data_cols > num_cols:
            grid.AppendCols(data_cols - num_cols)

        # Set column labels based on DataFrame column names
        for j in range(data_cols):
            grid.SetColLabelValue(j, data.columns[j])

        # Populate the grid with data
        for i in range(data_rows):
            for j in range(data_cols):
                grid.SetCellValue(i, j, str(data.iat[i, j]))

    # mobileCases Analysis Page
    def on_mobilecase_analysis(self, event):
        # clear
        self.clear_m_panel()

        # Filter Mobile Phone Offenses
        mobile_phone_offenses = df[df['MOBILE_PHONE_IND'] == 'Y'].copy()

        # Convert 'OFFENCE_MONTH' to datetime type using .loc
        mobile_phone_offenses['OFFENCE_MONTH'] = pd.to_datetime(mobile_phone_offenses['OFFENCE_MONTH'])

        # Group data by month and count offenses
        mobile_phone_trend = mobile_phone_offenses.groupby(
            mobile_phone_offenses['OFFENCE_MONTH'].dt.to_period("M")).size().reset_index(name='Offense Count')

        # Convert 'OFFENCE_MONTH' back to string for plotting
        mobile_phone_trend['OFFENCE_MONTH'] = mobile_phone_trend['OFFENCE_MONTH'].dt.strftime('%Y-%m')
        # Create a Box Plot to visualize the mobile phone analysis offense code
        plt.figure(figsize=(12, 4))
        plt.plot(mobile_phone_trend['OFFENCE_MONTH'], mobile_phone_trend['Offense Count'], marker='o')
        plt.title('Mobile Phone Usage Offenses Over Time')
        plt.xlabel('Month')
        plt.ylabel('Number of Offenses')
        plt.xticks(rotation=0)
        plt.grid(True)
        # Embed the Matplotlib chart in the m_panel
        self.canvas = FigureCanvas(self.m_panel9, -1, plt.gcf())
        self.m_panel.Layout()

        def mobile_phone_usage_trend():
            # Filter Mobile Phone Offenses
            mobile_phone_offenses = df[df['MOBILE_PHONE_IND'] == 'Y'].copy()
            # Convert 'OFFENCE_MONTH' to datetime type using .loc
            mobile_phone_offenses['OFFENCE_MONTH'] = pd.to_datetime(mobile_phone_offenses['OFFENCE_MONTH'])
            # Group data by month and count offenses
            mobile_phone_trend = mobile_phone_offenses.groupby(
                mobile_phone_offenses['OFFENCE_MONTH'].dt.to_period("M")).size().reset_index(name='Offense Count')

            return mobile_phone_trend

        def mobile_phone_offense_code():
            # Filter Mobile Phone Offenses
            mobile_phone_offenses = df[df['MOBILE_PHONE_IND'] == 'Y'].copy()

            # Group by offense code and count offenses
            offense_code_counts = mobile_phone_offenses['OFFENCE_CODE'].value_counts().reset_index()
            offense_code_counts.columns = ['Offense Code', 'Offense Count']

            return offense_code_counts

        def mobile_phone_yearly_face_value():
            # Filter Mobile Phone Offenses
            mobile_phone_offenses = df[df['MOBILE_PHONE_IND'] == 'Y'].copy()

            # Extract year from 'OFFENCE_MONTH'
            mobile_phone_offenses['OFFENCE_YEAR'] = mobile_phone_offenses['OFFENCE_MONTH'].dt.year

            # Group data by year and offense code, then calculate the total face value
            yearly_face_value = mobile_phone_offenses.groupby(['OFFENCE_YEAR'])['FACE_VALUE'].sum().reset_index()

            return yearly_face_value

        mobile_usage = mobile_phone_usage_trend()
        mobileOffenceCode = mobile_phone_offense_code()
        mobileYearly = mobile_phone_yearly_face_value()

        self.txt_ctrl(self.m_textCtrl1, mobile_usage)

        self.txt_ctrl(self.m_textCtrl2, mobileOffenceCode)

        self.txt_ctrl(self.m_textCtrl3, mobileYearly)

    def txt_ctrl(self, txtCtrl, data):
        txtCtrl.Clear()
        txtCtrl.SetValue(str(data))

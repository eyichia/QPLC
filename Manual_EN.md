# QPLC Step Convert To CSV Manual

## 1. Software Introduction
**QPLC Step Convert To CSV** is a software designed to read internal Step data from a PLC (Programmable Logic Controller), visualize it, and export it.
This tool connects to the PLC over a network, reads specific register ranges, decodes raw step codes into human-readable actions and parameters, displays them in a Graphical User Interface (GUI), and allows exporting the complete step data to a CSV file (compatible with Excel).

- **Supported Models/Formats**: Mitsubishi (Network-type) PLCs used in equipment by **Chite Machinery** (C1J, C1K, C1M).
- **Language**: Supports Traditional Chinese, Simplified Chinese, and English
- **Developer**: Eric Chiang
- **Version**: v1.3.3

---

## 2. Operation Flow

1. **Launch Program**: Run "QPLC_StepConverter.exe".
2. **Select Model**:
   - Choose the corresponding equipment model from the dropdown list.
3. **Connection Settings**:
   - Verify the PLC's **IP Address** and **Port**.
   - Click the **[Connect PLC]** button.
4. **Read Step Data**:
   - Ensure the connection status shows "Connected."
   - Click the **[Read PLC]** button; the system will request all step data from the PLC.
5. **View Data**:
   - Once reading is complete, action names will appear in the step fields in the center of the UI.
   - Use the **Up/Down arrow buttons** or the input box to navigate through pages.
   - The list component will display the fully decoded information.
6. **Export Report**:
   - Click the **[Export CSV]** button.
   - Select the storage path and filename to save the converted step data to your computer.
7. **Import Report**:
   - Click the **[Import CSV]** button.
   - Select a report file to load and display the data on the screen.
8. **Write to PLC**:
   - Click the **[Write PLC]** button.
   - Select the report data you wish to upload and write it back to the PLC.
9. **Disconnect and Exit**:
   - Once operations are finished, click **[Disconnect PLC]** and close the program.

---

## 3. New Model Support

To request support for new PLC models or data formats, please contact the developer.
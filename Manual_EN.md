# QPLC Step Convert To CSV Manual

## 1. Software Introduction
**QPLC Step Convert To CSV** is a software designed to read internal Step data from a PLC (Programmable Logic Controller), visualize it, and export it.
This tool connects to the PLC over a network, reads specific register ranges, decodes raw step codes into human-readable actions and parameters, displays them in a Graphical User Interface (GUI), and allows exporting the complete step data to a CSV file (compatible with Excel).

- **Supported Models**: Dynamically scans the `Model` folder and loads them automatically (e.g., C1M, C1K, etc.)
- **Language**: Supports Traditional Chinese, Simplified Chinese, and English
- **Developer**: Eric Chiang
- **Version**: v1.1.2

---

## 2. Operation Flow

1. **Open Program**: Run `QPLC_StepConvertToCsv.exe`.
2. **Select Model**:
   - Choose the corresponding device model.
3. **Connection Settings**:
   - Verify the PLC's IP address and Port.
   - Click the **[Connection]** button.
4. **Read Steps**:
   - Ensure the connection status shows as connected.
   - Click the **[Read]** button, and the system will request all step data from the PLC.
5. **View Data**:
   - Once reading is complete, the center step fields of the UI will show the action names.
   - Use the Up/Down arrow buttons or input box to navigate and view different steps.
   - The list component on the screen will also display the fully decoded data.
6. **Export Report**:
   - Click the **[Export.csv]** button.
   - Select the save path and file name to save the converted step data to your computer.
7. **Disconnect and Exit**:
   - After completing your operations, click **[Disconnection]** and then close the program.

---

## 3. Adding Model Support

This software features a highly flexible architecture. If you want to support a new PLC model format, **there is absolutely no need to modify the main source code**.

**Steps:**
1. Prepare a JSON definition file that matches the existing format structure (e.g., `NewModel.json`).
2. Place this file into the `Model/` folder in the software directory.
3. Restart the software. The program will automatically scan the `Model/` folder and dynamically load the new model `NewModel` into the model selection dropdown menu.

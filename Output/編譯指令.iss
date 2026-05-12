[Setup]
AppName=QPLC Step Converter
AppVersion=1.1.3
DefaultDirName={autopf}\QPLC_Converter
DefaultGroupName=QPLC_Converter
OutputDir=D:\01Python\QPLC\Output
OutputBaseFilename=QPLC_Setup
SetupIconFile=D:\01Python\QPLC\Mystyle.ico
Compression=lzma
SolidCompression=yes

[Files]
; 1. 主執行檔
Source: "D:\01Python\QPLC\dist\QPLC_StepConvertToCsv.exe"; DestDir: "{app}"; Flags: ignoreversion

; 2. Model 資料夾
Source: "D:\01Python\QPLC\Model\*"; DestDir: "{app}\Model"; Flags: ignoreversion recursesubdirs createallsubdirs

; --- 在這裡新增 [Dirs] 區段 ---
[Dirs]
; 建立 Reports 資料夾並開放權限，讓程式可以自由讀寫 CSV
Name: "{app}\Reports"; Permissions: users-full

[Icons]
Name: "{group}\QPLC Step Converter"; Filename: "{app}\QPLC_StepConvertToCsv.exe"
Name: "{commondesktop}\QPLC Step Converter"; Filename: "{app}\QPLC_StepConvertToCsv.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
$ErrorActionPreference = 'Stop'
$reportRoot = 'C:\Users\Sudhanshu\Desktop\EF\Group_31\revised'
$reportWord = Join-Path $reportRoot 'Group_31_Term_Paper_Revised.docx'
$reportPdf = Join-Path $reportRoot 'Group_31_Term_Paper_Revised.pdf'
$wordApp = New-Object -ComObject Word.Application
$wordApp.Visible = $false
$wordApp.DisplayAlerts = 0
try {
    $paperDoc = $wordApp.Documents.Open($reportWord, $false, $false)
    $paperDoc.Fields.Update() | Out-Null
    $paperDoc.Repaginate()
    $paperDoc.Save()
    $paperDoc.ExportAsFixedFormat($reportPdf, 17)
    Write-Output ('Rendered pages: ' + $paperDoc.ComputeStatistics(2))
    $paperDoc.Close(0)
} finally {
    $wordApp.Quit()
}

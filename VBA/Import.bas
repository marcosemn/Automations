Attribute VB_Name = "Módulo1"
Sub import()
'The main objective of this sub is importing another xlsx into this workbook
Application.ScreenUpdating = False

Dim path As Variant
Application.DisplayAlerts = False

Range("A1").Select
Range(Selection, Selection.End(xlDown)).Select
Range(Selection, Selection.End(xlToRight)).Select
Selection.ClearContents

path = Range("K1").Value

If path = False Then
    Exit Sub
End If

Workbooks.Open path, , True

ActiveWorkbook.Sheets(1).Range("A1").CurrentRegion.Copy

ThisWorkbook.Sheets(1).Range("A1").PasteSpecial

ActiveWorkbook.Close False

Columns("A:G").Select
Columns("A:G").EntireColumn.AutoFit

Application.ScreenUpdating = True
Application.DisplayAlerts = True

MsgBox "Importado em " & Now()

End Sub

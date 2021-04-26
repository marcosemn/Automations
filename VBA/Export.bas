Attribute VB_Name = "Módulo3"
Sub export()
'the main objective of this sub is creating workbooks based in the worksheets we created
Dim vPlan As Worksheet
Dim wbk As Workbook
Dim wbkTemp As Workbook
Dim ArqExiste As String

Application.ScreenUpdating = False
Application.DisplayAlerts = False

Sheets("Base de Dados").Select

Set wbk = ActiveWorkbook

For Each vPlan In Sheets

    If vPlan.Name <> "Base de Dados" And vPlan.Name <> "Email" Then
    
        vPlan.Copy
        Set wbkTemp = ActiveWorkbook
        
        ArqExiste = Dir(wbk.path & "\PlanilhasTrovato\" & vPlan.Name & " - " & Format(Now, "yyyymmdd") & ".xlsx")
    
        If ArqExiste > "" Then
            Kill wbk.path & "\PlanilhasTrovato\" & vPlan.Name & " - " & Format(Now, "yyyymmdd") & ".xlsx"
        End If
    
    wbkTemp.SaveAs wbk.path & "\PlanilhasTrovato\" & vPlan.Name & " - " & Format(Now, "yyyymmdd")
    
    wbkTemp.Close
    
    Sheets(vPlan.Name).Select
    ActiveWindow.SelectedSheets.Delete
    
    End If
    
Next

Application.ScreenUpdating = True

MsgBox "Compilação concuída em " & Now

End Sub

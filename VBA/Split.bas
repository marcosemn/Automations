Attribute VB_Name = "Módulo2"
Sub split()
'The main objective of this sub is split the original dataframe into smaller parts.
'In this case, the separation was made according to the names of the stores (column C)
Application.ScreenUpdating = False

linha_fim = Range("A1").End(xlDown).Row
Range("C2:C" & linha_fim).Copy
Range("J1").PasteSpecial
Application.CutCopyMode = False
ActiveSheet.Range("$J$1:$J$" & linha_fim).RemoveDuplicates Columns:=1, Header:=xlNo
linha_fim = Range("J1").End(xlDown).Row

Set Rng = Range("$J$1:$J$" & linha_fim)

For Each loja In Rng

    Sheets("Base de Dados").Range("C3").AutoFilter
    ActiveSheet.Range("$A$1:$G$1048576").AutoFilter Field:=3, Criteria1:=loja
    Range("A1").Select
    Range(Selection, Selection.End(xlDown)).Select
    Range(Selection, Selection.End(xlToRight)).Select
    Selection.Copy
    Sheets.Add After:=ActiveSheet
    ActiveSheet.Name = loja
    ActiveSheet.Paste
    Columns("A:G").EntireColumn.AutoFit
    ActiveWindow.DisplayGridlines = False
    Columns("C:C").Select
    Selection.Delete Shift:=xlToLeft
    Sheets("Base de Dados").Select
    Range("A1").Select
    Selection.AutoFilter
    
Next

Sheets("Base de Dados").Range("J:J").Clear

Application.ScreenUpdating = True

MsgBox "Compilação concuída em " & Now()

End Sub

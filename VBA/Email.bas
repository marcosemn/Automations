Attribute VB_Name = "Módulo4"
Public wrkb As Workbook
Public wrks As Worksheet

Public IntervaloMailing As Range
Public Celula As Range

Public AppOutk As Outlook.Application
Public MailOutk As Outlook.MailItem

Public OApp As Object
Public OMail As Object
Public signature As String
Public Sub Mailing()

Set wrkb = ThisWorkbook
Set wrks = wrkb.Sheets("Email")

linha_fim = Range("A1").End(xlDown).Row
Set IntervaloMailing = wrks.Range("A2:A" & linha_fim)

With wrks
        .Select
        
        For Each Celula In IntervaloMailing
        
            Cria email
            
        Next
End With

End Sub

Sub CreateEmail()
'the main objective of this sub is sending email accoring to a list of contacts

Set AppOutk = New Outlook.Application
Set MailOutk = AppOutk.CreateItem(olMailItem)
Set OApp = CreateObject("Outlook.Application")
Set OMail = OApp.CreateItem(0)

With OMail
    .Display
End With

signature = OMail.body

With MailOutk
    .Display
    .To = wrks.Cells(Celula.Row, 3).Value
    .CC = wrks.Cells(Celula.Row, 4).Value
    .BCC = wrks.Cells(Celula.Row, 5).Value
    .Subject = wrks.Cells(Celula.Row, 6).Value
    .body = "wrks.Cells(Celula.Row,7).Value" & vbNewLine & signature
    .Attachments.Add wrks.Cells(Celula.Row, 8).Value
    '.Send
End With

Set OMail = Nothing
Set OApp = Nothing

End Sub


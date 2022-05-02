def main():
    sender = input("Podaj email: ")
    passwd = input("Podaj hasło: ")

    while True:

        from datetime import date
        import time
        import smtplib, ssl, funkcje
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        if str(time.strftime("%H:%M:%S")) == "19:20:20":
            recivers = []
            recivers = (funkcje.send_email())
            for sus in recivers:
                print(sus)
                rec = str(sus)
                subject = "Raport Dzienny"
                Miasto = 'Gdańsk'
                dzisiaj = date.today()
                data = dzisiaj.strftime("%d/%m/%Y")
                temp_min, temp_max = funkcje.pogoda()
                EUR, EUR_zmiana, kolor_EUR, USD, USD_zmiana, kolor_USD = funkcje.kursy()
                title1, opis1, link1, title2, opis2, link2, title3, opis3, link3, title4, opis4, link4, title5, opis5, link5, title6, opis6, link6 = funkcje.wiadomosci()

                html = '''
                    <html>
                    <head>

                    </head>

                    <body>

                        <table width="100%" align="center">
                            <tr>
                                <td align="center">
                                </td>

                                <td align="center">
                                    <h1>Raport Dnia</h1>
                                </td>

                                <td align="center">
                                    <h4 style="text-align:right;">''' + str(data) + '''</h4>
                                </td>

                            </tr>
                            <tr>
                                <td width="15%" valign="top">
                                    <h3>Kurs EUR/PLN (NBP): </h3>
                                    <h3 style="color:''' + str(kolor_EUR) + ''';">''' + str(EUR) + ''' (''' + str(EUR_zmiana) + ''')</h3>
                                    <br>
                                    <h3>Kurs USD/PLN (NBP): </h3>
                                    <h3 style="color:''' + str(kolor_USD) + ''';">''' + str(USD) + ''' (''' + str(USD_zmiana) + ''')</h3>
                                    </h3>

                                </td>
                                <td width="70%" valign="top">
                                    <h3><a href="''' + str(link1) + '''">''' + str(title1) + '''</a></h3>
                                    ''' + str(opis1) + '''
                                    <h3><a href="''' + str(link2) + '''">''' + str(title2) + '''</a></h3>
                                    ''' + str(opis2) + '''
                                    <h3><a href="''' + str(link3) + '''">''' + str(title3) + '''</a></h3>
                                    ''' + str(opis3) + '''
                                    <h3><a href="''' + str(link4) + '''">''' + str(title4) + '''</a></h3>
                                    ''' + str(opis4) + '''
                                    <h3><a href="''' + str(link5) + '''">''' + str(title5) + '''</a></h3>
                                    ''' + str(opis5) + '''
                                    <h3><a href="''' + str(link6) + '''">''' + str(title6) + '''</a></h3>
                                    ''' + str(opis6) + '''
                                </td>
                                <td width="15%" valign="top" align="center">
                                    <h3>Temperatura w ''' + str(Miasto) + ''':<br>
                                    ''' + str(temp_max) + ''' / ''' + str(temp_min) + '''
                                    </h3>
                                </td>
                            </tr>
                        </table>

                    </body>
                    </html>
                    '''

                message = MIMEMultipart()
                message['From'] = sender
                message['To'] = rec
                message['Subject'] = subject
                message.attach(MIMEText(html, "html"))
                message = message.as_string()

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender, passwd)
                    print("Zalogowano")
                    server.sendmail(sender, rec, message)
                    print("Wyslano")

if __name__ == "__main__":
    main()

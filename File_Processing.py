from reportlab.pdfgen import canvas
from reportlab.lib.colors import gold, black, transparent, grey, red,white
from reportlab.lib.units import mm
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import A4
import Config_Processing as cp


inici = 750
center = 480

def add_Title(c):
    c.drawImage("./images/logo-tecnocampus.jpg", 400, 700, width=200, height=20, mask=None, preserveAspectRatio=True)

    c.setLineWidth(.3)
    c.setFont('Helvetica-Bold', 24)

    c.drawString(90, center, "Migració de la infraestructura de")
    c.drawString(90, center-27, "seguretat perimetral per a" )
    c.drawString(90, center-(30*2), "TecnoCampus")

    c.setFont('Helvetica', 20)
    c.drawString(90, center-(30*5), "Gener 2019")

    bottom_t = c.beginText()

    c.setFont('Helvetica-Bold', 10)
    bottom_t.setTextOrigin(90, 100)
    bottom_t.\
        textLine("La informació continguda en aquest document pot ser de caràcter privilegiat y/o confidencial.")
    bottom_t. \
        textLine("Qualsevol disseminació, distribució o copia d’aquest document per qualsevol altre persona diferent")
    bottom_t. \
        textLine("als receptors "
                 "originals queda estrictament prohibida. Si ha rebut aquest document per error, sis plau ")
    bottom_t. \
        textLine("notifiquí immediatament al emissor i esborri qualsevol copia d’aquest document.")
    c.drawText(bottom_t)

    c.setFillColor(gold)
    c.rect(20, 20, 20, 800, fill=True, stroke=False)
    c.saveState()

def add_header(c):
    c.setFont('Helvetica', 12)
    c.setFillColor(grey)
    c.drawString(70, 800,"Migració de la infrastuctura de seguretat perimetral")
    c.drawImage("./images/logo-tecnocampus.jpg", 450, 800, width=100, height=20, mask=None, preserveAspectRatio=True)
    c.setFillColor(black)
    c.saveState()

def add_footer(c):
    c.setFillColor(grey)
    page_num = canvas.Canvas.getPageNumber(c)
    text = "Pàgina %s / 11" % page_num
    c.drawRightString(200 * mm, 10 * mm, text)
    c.setFillColor(black)
    c.saveState()

def add_index(c):
    c.showPage()
    add_header(c)
    add_footer(c)
    c.setFont('Helvetica-Bold', 18)
    c.drawString(70, inici, "Índex")
    c.setFont('Helvetica-Bold', 12)
    text = "1. INTRODUCCIÓ............................." \
           "................................................................................"
    c.drawString(70, inici - 27, text + "3")
    c.setFont('Helvetica', 12)

    text2 = "1.1. DESCRIPCIÓ.............................." \
            ".........................................................................3"

    c.drawString(90, inici - (27*2), text2)

    text2 = "1.2. OBJECTIUS....................." \
            "....................................................................................3"

    c.drawString(90, inici - (27 * 3), text2)

    text2 = "1.3. DESCRIPCIÓ GENERAL DE LES INFRAESTRUCTURES................................4"

    c.drawString(90, inici - (27 * 4), text2)

    c.setFont('Helvetica-Bold', 12)
    text = "2. CONFIGURACIÓ DEL DISPOSITIU............................................................................"
    c.drawString(70, inici - (27*5), text + "5")
    c.setFont('Helvetica', 12)

    text2 = "2.1. DISPOSITIU............................" \
            "............................................................................5"

    c.drawString(90, inici - (27 * 6), text2)

    text2 = "2.2. CREDENCIALS.................................." \
            ".................................................................5"

    c.drawString(90, inici - (27 * 7), text2)

    text2 = "2.3. GENERAL.............................." \
            ".............................................................................5"

    c.drawString(90, inici - (27 * 8), text2)

    text2 = "2.4. INTERFÍCIES......." \
            "...............................................................................................5"

    c.drawString(90, inici - (27 * 9), text2)

    text2 = "2.5. TAULA D'ENRUTAMENT........." \
            "...........................................................................6"

    c.drawString(90, inici - (27 * 10), text2)

    text2 = "2.6. OBJECTES ADRECES DEL FIREWALL............................................................6"

    c.drawString(90, inici - (27 * 11), text2)

    text2 = "2.7. OBJECTES" \
            " SERVEIS.........................................................................................7"

    c.drawString(90, inici - (27 * 12), text2)

    text2 = "2.8. NATS D'ENTRADA (VIRTUAL IPs).....................................................................9"

    c.drawString(90, inici - (27 * 13), text2)

    text2 = "2.9. POLÍTIQUES DE FIREWALL.............................................................................10"

    c.drawString(90, inici - (27 * 14), text2)

    text2 = "2.10. SERVEI ANTI" \
            "VIRUS.........................................................................................10"

    c.drawString(90, inici - (27 * 15), text2)

    text2 = "2.11. SERVEI DE " \
            "FILTRATGE WEB.........................................................................10"

    c.drawString(90, inici - (27 * 16), text2)

    text2 = "2.12. SERVEI " \
            "APPLICATION CONTROL..................................................................11"

    c.drawString(90, inici - (27 * 17), text2)

    text2 = "2.13. SERVEI INTRUSION PROTECTION................................................................11"

    c.drawString(90, inici - (27 * 18), text2)

    c.saveState()

def add_intro(c,name):

    c.showPage()
    add_header(c)
    add_footer(c)
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, inici, "1. Introducció")
    valor = inici-27
    c.drawString(70, valor, "1.1. Descripció")

    c.setFont('Helvetica', 11)
    c.setFillColor(black)
    #GETNAME
    ptext = "El present document descriu la configuració realitzada en el dispositiu Fortigate-%s de Fortinet" % name
    valor -= 27
    c.drawString(70, valor,ptext)
    ptext = "a la empresa Tecnocampus resultat de la substitució de un Firewall perimetral Cisco de "
    valor -= 20
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "l'organització."
    c.drawString(70, valor, ptext)

    valor -= 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "1.2. Objectius")

    valor -= 27
    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "El objectiu d’aquest document és la de formalitzar el traspàs d’informació al equip tècnic"
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "responsable del manteniment de les infraestructures instal·lades. Aquesta informació fa"
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "referencia al disseny, instal·lació i configuració dels dispositius i sistemes afectats per la"
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "implementació."
    c.drawString(70, valor, ptext)

    valor -= 27
    ptext = "La present documentació inclou:"
    c.drawString(70, valor, ptext)
    valor -= 27
    ptext = "           \u2022 Descripció general de les infraestructures instal·lades."
    c.drawString(70,valor, ptext)
    valor -= 27
    ptext = "           \u2022 Polítiques de filtratge de tràfic."
    c.drawString(70, valor, ptext)
    valor -= 27
    ptext = "           \u2022 Perfils de seguretat."
    c.drawString(70, valor, ptext)
    valor -= 27
    ptext = "           \u2022 Connexions Túnel."
    c.drawString(70, valor, ptext)

    c.saveState()

def add_draw(c,sec):
    c.showPage()

    add_footer(c)
    add_header(c)

    valor = inici - 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, inici, "1.3. Descripció general de les infraestructures")

    c.setFont('Helvetica', 11)
    c.setFillColor(black)
    ptext = "Actualment la infraestructura te la següent distribució:"
    c.drawString(70, valor, ptext)


    c.drawImage("./images/cloud.png", 120, 670, width=100, height=40, mask=transparent,
                preserveAspectRatio=False)
    c.drawString(145, 680, "INTERNET")
    c.drawImage("./images/cloud.png", 340, 670, width=100, height=40, mask=transparent,
                preserveAspectRatio=False)
    c.drawString(365, 680, "INTERNET")
    c.line(170, 680, 170, 600)
    c.line(380, 680, 380, 600)


    #pos x ,y width height
    c.rect(150, 600, 40, 40, fill=True, stroke=False)

    c.line(170, 600, 170, 525)
    c.line(170, 525, 250, 525)


    c.rect(360, 600, 40, 40, fill=True, stroke=False)

    c.line(380, 600, 380, 525)
    c.line(380, 525, 250, 525)


    c.rect(250, 500, 50, 50, fill=True, stroke=False)
    c.rect(150, 430, 100, 20, fill=True, stroke=False)

    c.line(170, 512, 250, 512)
    c.line(170, 440, 170, 512)

    c.rect(360, 430, 100, 20, fill=True, stroke=False)

    c.line(380, 512, 250, 512)
    c.line(380, 440, 380, 512)

    nl = 630;
    c.setFont('Helvetica', 8)
    c.setFillColor(red)
    ###IPS
    c.drawString(170, 590, sec[9])
    c.drawString(338, 590, sec[8])

    c.drawString(200, 527, sec[7])
    c.drawString(200, 515, sec[3])
    c.drawString(300, 527, sec[1])
    c.drawString(300, 515, sec[5])
    c.setFont('Helvetica',11)
    c.drawString(175, 420, sec[11])
    c.drawString(385, 420, sec[13])



    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ###STRINGS DEL
    c.drawString(70, nl, "Acces a Internet")
    c.drawString(70, nl - 27, "Backup + Wifi")
    c.drawString(400, nl, "Sortida")
    c.drawString(400, nl - 27, "Internet")
    c.drawString(400, nl - (27*2), "Principal")

    c.setFillColor(white)
    c.drawString(175, 438, sec[10])
    c.drawString(385, 438, sec[12])

    c.setFont('Helvetica', 6)
    c.setFillColor(black)
    c.drawString(225, 539, sec[6])
    c.drawString(225, 502, sec[2])
    c.drawString(312, 539, sec[0])
    c.drawString(312, 502, sec[4])


    c.setFont('Helvetica', 11)
    valor = 400
    ptext = "En aquest esquema es pot veure com el firewall disposa actualment de dos conexions a internet "
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "(Port1 i Port4) que es connecten a través de diferents routers."
    c.drawString(70, valor, ptext)
    valor -= 27
    ptext = "La infraestructura disposa de dos xarxes locals, la xarxa de servidors i la xarxa d'estacions de "
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "treball."
    c.drawString(70, valor, ptext)

    c.saveState()

def add_confi_1(c, name, firmware, port, res1, res2, res3, ip1, ip2, domini, dataset):
    c.showPage()
    add_header(c)
    add_footer(c)

    valor = inici - 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, inici, "2. Configuració del dispositiu")
    c.setFont('Helvetica', 11)
    c.setFillColor(black)
    ptext = "A continuació es detalla la configuració del dispositiu Fortigate-%s" % name
    c.drawString(70, valor, ptext)
    valor -= 27

    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "2.1. Dispositiu")

    valor -= 65

    data = [["Marca-Model", "Fortigate %s " % name],[ "OS/Firmware", "%s" % firmware], [ "S/N", ""]]
    width, height = A4
    table = Table(data)
    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
    ]))
    table.wrapOn(c, width, height)

    table.drawOn(c, 70, valor)

    valor -= 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "2.2. Credencials d'accés")

    valor -= 27
    c.setFont('Helvetica', 11)
    c.setFillColor(black)
    ptext = "Accés: https://10.132.4.254:%s" % port
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "Usuari: admin"
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "Password: dfAS34"
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "Restriccions d'accés: xarxes %s" % res1
    ptext += ", %s" % res2

    c.drawString(70, valor, ptext)
    valor -= 20
    c.drawString(70,valor,res3)

    valor -= 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "2.3. General")

    valor -= 27
    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "El dispositiu està configurat en mode NAT, és a dir, es separen vàries xarxes a nivell tres"
    c.drawString(70,valor,ptext)
    valor -= 20
    ptext = "d'enrutament."
    c.drawString(70,valor,ptext)
    valor -= 27
    ptext = "DNS:"
    c.drawString(80,valor,ptext)
    valor -= 27
    ptext = "           \u2022 Servidor Primari: %s" % ip1
    c.drawString(70,valor,ptext)
    valor -= 20
    ptext = "           \u2022 Servidor Secundari: %s" % ip2
    c.drawString(70,valor,ptext)
    valor -= 20
    ptext = "           \u2022 Nom del domini Local: %s" % domini
    c.drawString(70, valor, ptext)

    valor -= 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "2.4. Interfícies")

    valor -= 27
    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "El dispositiu instal·lat disposa d'una taula de polítiques de connexió per tal de definir el"
    c.drawString(70,valor,ptext)
    valor -= 20
    ptext = "comportament del mateix per cada una de les connexions tractades."
    c.drawString(70, valor, ptext)

    width, height = A4
    table = Table(dataset)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)

    table.drawOn(c, 70, 150)

    c.saveState()

def add_confi_2(c, num, ip1, ip2, dt1, dt2, dt3):
    c.showPage()

    add_footer(c)
    add_header(c)

    valor = inici - 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, inici, "2.5. Taula d' enrutament")

    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "S'ha definit %s default gw per permetre la sortida per les dues sortides a internet de la organització." %num
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "Per defecte el tràfic sortirà a través del GW %s (prioritat menor) i en cas de caiguda de la" % ip1
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "línia es redirigirà el tràfic a través del GW %s." %ip2
    c.drawString(70, valor, ptext)

    width, height = A4
    table = Table(dt1)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)
    valor -= 70
    table.drawOn(c, 70, valor)

    valor -= 20
    ptext = "S'ha definit una sèrie de Health-checks de ping a través de les interfícies wan per detectar"
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "la caiguda de les línies de comunicacions."
    c.drawString(70, valor, ptext)

    width, height = A4
    table = Table(dt2)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)
    valor -= 70
    table.drawOn(c, 70, valor)

    valor -= 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "2.6. Objectes Adreces del Firewall ")

    valor -= 27
    c.setFillColor(black)
    c.setFont('Helvetica',11)
    ptext = "El dispositiu actualment te vinculats determinats objectes (noms descriptius) a adreces IP per "
    c.drawString(70, valor,ptext)
    valor -= 20
    ptext = "tal de facilitar la seva utilització en el sistema."
    c.drawString(70, valor, ptext)

    table = Table(dt3)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)
    valor -= 200
    table.drawOn(c, 70, valor)

    valor -= 27
    ptext = "*[set type] = not exist (Subnet) / [set type] = iprange (range)"
    c.drawString(70, valor, ptext)

    c.saveState()

def add_confi_3(c,dt1):
    c.showPage()

    add_footer(c)
    add_header(c)

    valor = inici - 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, inici, "2.7. Objectes Serveis")

    c.setFillColor(black)
    c.setFont('Helvetica',11)
    ptext = "El dispositiu configurat disposa de serveis predeterminats per defecte establerts per FortiNet i"
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "addicionalment te introduïts serveis personalitzats. "
    c.drawString(70, valor, ptext)
    valor -= 20
    ptext = "Els serveis predeterminats són:"
    c.drawString(70,valor,ptext)

    width, height = A4
    table = Table(dt1)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 70, 70)

    c.saveState()

def add_confi_4(c, dt1):
    c.showPage()

    add_footer(c)
    add_header(c)

    width, height = A4
    table = Table(dt1)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 70, 70)

    c.saveState()

def add_confi_5(c, dt1, dt2):
    c.showPage()

    add_footer(c)
    add_header(c)

    width, height = A4
    table = Table(dt1)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 70, 250)

    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "Els serveis addicionals són:"
    c.drawString(70,250-20,ptext)

    table = Table(dt2)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 70, 160)

    c.saveState()

def add_confi_6(c,dt1,dt2,utm, utm2):
    c.showPage()

    add_footer(c)
    add_header(c)

    valor = inici - 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, inici, "2.8. NATs d'entrada (Virtual IPs)")

    c.setFillColor(black)
    c.setFont('Helvetica',11)
    ptext = "S'ha definit els següents NATs d'entrada (VIPs en nomenclatura Fortinet)"
    c.drawString(70, valor,ptext)

    width, height = A4
    table = Table(dt1)
    table.setStyle(TableStyle([
        ('TEXTFONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), gold),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 70, 650)
    table = Table(dt2)

    valor = 650 - 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70,valor , "2.9. Polítiques de Firewall")

    valor -= 27
    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "A continuació es mostren les polítiques de filtratge definides en el dispositiu Fortigate:"
    c.drawString(70, valor, ptext)

    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.10, black),
        ('BOX', (0, 0), (-1, -1), 0.25, black),
        ('BACKGROUND',(0,0),(-1,0),gold),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('TEXTFONT', (0, 0), (-1, -1), 'Times-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')


    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 25, 380)

    valor = 370 -27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "2.10. Servei Antivirus")

    valor -= 27
    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "El servei antivirus perimetral proveeix d'una base de dades automatitzada per assegurar la "
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "protecció davant de possible contingut de malware detectat a través de la navegació WEB."
    c.drawString(70, valor, ptext)

    valor -= 27
    ptext = "Actualment el dispositiu te com el perfil d'antivirus activat %s que detecta i neteja " % utm
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "malware i possibles connexions a xarxes de Botnets."
    c.drawString(70,valor,ptext)

    valor -= 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "2.11. Servei de Filtratge Web")

    valor -= 27
    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "El servei de filtratge de web, proveeix d'un servei de  filtratge de contingut web a través dels "
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "pprotocols de navegació."
    c.drawString(70, valor, ptext)

    valor -= 27
    ptext = "Actualment en el dispositiu s'ha definit el perfil %s que actualment únicament genera " % utm2
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "logs de tot el tràfic de navegació web."
    c.drawString(70, valor, ptext)

    c.saveState()

def add_confi_7(c,utm3,utm4,client,sSeverity1,os):
    c.showPage()

    add_footer(c)
    add_header(c)

    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, inici, "2.12. Servei Application control")

    valor = inici-27

    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "El servei de Application Control realitza un filtratge a nivell d'aplicació per tal de bloquejar o"
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "filtrar determinades comunicacions d'aplicacions."
    c.drawString(70, valor, ptext)

    valor -= 27
    ptext = "En el dispositiu s'ha activat el perfil %s i s'ha configurat per a generar logs de totes "% utm3
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "les aplicacions utilitzades i bloqueja totes les connexions d'aplicacions típiques de BotNets."
    c.drawString(70, valor, ptext)

    valor -= 27
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(70, valor, "2.13. Servei Intrusion Protection ")

    valor -= 27
    c.setFillColor(black)
    c.setFont('Helvetica', 11)
    ptext = "El Servei de Intrusion Protection permet detectar possibles atacs de xarxa contra la "
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "infraestructura de la organització."
    c.drawString(70, valor, ptext)

    valor -= 27
    ptext = "En el dispositiu s'ha activa el perfil %s en les polítiques de navegació web i s'han " % utm4
    c.drawString(70, valor, ptext)

    valor -= 20
    ptext = "activat el comportament per defecte (bloqueig en cas necessari o monitorzació) de les signatures "
    c.drawString(70, valor, ptext)
    valor -= 20

    sev = str.split(sSeverity1," ")

    ptext = "de tipus %s"%client
    ptext += ', de criticitat "%s" i '%sev[1]
    ptext += '"%s" que afectin a serveis' % sev[0]
    c.drawString(70, valor, ptext)

    ops = str.split(os," ")

    ptext = "de sistemes operatius %s" %ops[0]
    ptext += ", %s" %ops[1]
    ptext += " i %s." %ops[2]
    valor -= 20
    c.drawString(70, valor, ptext)
    c.saveState()

def __init__(file):

    temp = cp.ConfExport(file)

    name = temp.conf.name
    sec21 = temp.section21()
    sec22 = temp.section22()
    sec23 = temp.section23()
    sec24 = temp.section24()
    sec25 = temp.section25()
    sec26 = temp.section26()
    sec27 = temp.section27()
    sec28 = temp.section28()
    sec29 = temp.section29()
    sec210 = temp.section210()
    sec211 = temp.section211()
    sec212 = temp.section212()
    sec213 = temp.section213()
    secdraw = temp.draw()

    c = canvas.Canvas("Report_TCM.pdf")

    add_Title(c)
    add_index(c)
    # name,
    add_intro(c, name)

    # SEC DRAW
    add_draw(c,secdraw)

    ##DATASET SEC2.4
    dsConfig = [["Interficie", "Alias", "Address/FQDN", "DHCPRelay"],
                [sec24[0], sec24[1], sec24[2], sec24[3]],
                [sec24[4], sec24[5], sec24[6], sec24[7]],
                [sec24[8], sec24[9], sec24[10], sec24[11]],
                [sec24[12], sec24[13], sec24[14], sec24[15]]]

    add_confi_1(c, sec21[0], sec21[1], sec22[0],
                sec22[1],
                sec22[2],
                sec22[3],
                sec23[0],
                sec23[0],
                sec23[0],
                dsConfig)

    ##DATA SEC2.5
    ds125 = [["Xarxa Destí", "GW", "Interficie", "Prioritat"],
             ["0.0.0.0/0.0.0.0", sec25[3], sec25[4], sec25[5]],
             ["0.0.0.0/0.0.0.0", sec25[6], sec25[7], sec25[8]]]
    ds225 = [["Servidor desti", "GW", "Interficie", "Interval", "Failtime", "Recovery"],
             [sec25[9], sec25[10], sec25[11], sec25[12], sec25[13], sec25[14]],
             [sec25[15], sec25[16], sec25[17], sec25[18], sec25[19], sec25[20]]]
    ds126 = [["Name", "Category", "Address/FQDN", "Interface", "Type*"],
             [sec26[0], sec26[1], sec26[2], sec26[3], sec26[4]],
             [sec26[5], sec26[6], sec26[7], sec26[8], sec26[9]],
             [sec26[10], sec26[11], sec26[12], sec26[13], sec26[14]],
             [sec26[15], sec26[16], sec26[17], sec26[18], sec26[19]],
             [sec26[20], sec26[21], sec26[22], sec26[23], sec26[24]],
             [sec26[25], sec26[26], sec26[27], sec26[28], sec26[29]],
             [sec26[30], sec26[31], sec26[32], sec26[33], sec26[34]],
             [sec26[35], sec26[36], sec26[37], sec26[38], sec26[39]]]

    add_confi_2(c, sec25[0], sec25[1], sec25[2], ds125, ds225, ds126)

    ##DATASEC 2.7
    ds127 = [["Nom del servei", "Categoria", "Ports TCP", "Ports UDP", "Protocol"],
             [sec27[0], sec27[1], sec27[2], sec27[3], sec27[4]],
             [sec27[5], sec27[6], sec27[7], sec27[8], sec27[9]],
             [sec27[10], sec27[11], sec27[12], sec27[13], sec27[14]],
             [sec27[15], sec27[16], sec27[17], sec27[18], sec27[19]],
             [sec27[20], sec27[21], sec27[22], sec27[23], sec27[24]],
             [sec27[25], sec27[26], sec27[27], sec27[28], sec27[29]],
             [sec27[30], sec27[31], sec27[32], sec27[33], sec27[34]],
             [sec27[35], sec27[36], sec27[37], sec27[38], sec27[39]],
             [sec27[40], sec27[41], sec27[42], sec27[43], sec27[44]],
             [sec27[45], sec27[46], sec27[47], sec27[48], sec27[49]],
             [sec27[50], sec27[51], sec27[52], sec27[53], sec27[54]],
             [sec27[55], sec27[56], sec27[57], sec27[58], sec27[59]],
             [sec27[60], sec27[61], sec27[62], sec27[63], sec27[64]],
             [sec27[65], sec27[66], sec27[67], sec27[68], sec27[69]],
             [sec27[70], sec27[71], sec27[72], sec27[73], sec27[74]],
             [sec27[75], sec27[76], sec27[77], sec27[78], sec27[79]],
             [sec27[80], sec27[81], sec27[82], sec27[83], sec27[84]],
             [sec27[85], sec27[86], sec27[87], sec27[88], sec27[89]],
             [sec27[90], sec27[91], sec27[92], sec27[93], sec27[94]],
             [sec27[95], sec27[96], sec27[97], sec27[98], sec27[99]],
             [sec27[100], sec27[101], sec27[102], sec27[103], sec27[104]],
             [sec27[105], sec27[106], sec27[107], sec27[108], sec27[109]],
             [sec27[110], sec27[111], sec27[112], sec27[113], sec27[114]],
             [sec27[115], sec27[116], sec27[117], sec27[118], sec27[119]],
             [sec27[120], sec27[121], sec27[122], sec27[123], sec27[124]],
             [sec27[125], sec27[126], sec27[127], sec27[128], sec27[129]],
             [sec27[130], sec27[131], sec27[132], sec27[133], sec27[134]],
             [sec27[135], sec27[136], sec27[137], sec27[138], sec27[139]],
             [sec27[140], sec27[141], sec27[142], sec27[143], sec27[144]],
             [sec27[145], sec27[146], sec27[147], sec27[148], sec27[149]]
             ]
    ds227 = [["Nom del servei", "Categoria", "Ports TCP", "Ports UDP", "Protocol"],
             [sec27[150], sec27[151], sec27[152], sec27[153], sec27[154]],
             [sec27[155], sec27[156], sec27[157], sec27[158], sec27[159]],
             [sec27[160], sec27[161], sec27[162], sec27[163], sec27[164]],
             [sec27[165], sec27[166], sec27[167], sec27[168], sec27[169]],
             [sec27[170], sec27[171], sec27[172], sec27[173], sec27[174]],
             [sec27[175], sec27[176], sec27[177], sec27[178], sec27[179]],
             [sec27[180], sec27[181], sec27[182], sec27[183], sec27[184]],
             [sec27[185], sec27[186], sec27[187], sec27[188], sec27[189]],
             [sec27[190], sec27[191], sec27[192], sec27[193], sec27[194]],
             [sec27[195], sec27[196], sec27[197], sec27[198], sec27[199]],
             [sec27[200], sec27[201], sec27[202], sec27[203], sec27[204]],
             [sec27[205], sec27[206], sec27[207], sec27[208], sec27[209]],
             [sec27[210], sec27[211], sec27[212], sec27[213], sec27[214]],
             [sec27[215], sec27[216], sec27[217], sec27[218], sec27[219]],
             [sec27[220], sec27[221], sec27[222], sec27[223], sec27[224]],
             [sec27[225], sec27[226], sec27[227], sec27[228], sec27[229]],
             [sec27[230], sec27[231], sec27[232], sec27[233], sec27[234]],
             [sec27[235], sec27[236], sec27[237], sec27[238], sec27[239]],
             [sec27[240], sec27[241], sec27[242], sec27[243], sec27[244]],
             [sec27[245], sec27[246], sec27[247], sec27[248], sec27[249]],
             [sec27[250], sec27[251], sec27[252], sec27[253], sec27[254]],
             [sec27[255], sec27[256], sec27[257], sec27[258], sec27[259]],
             [sec27[260], sec27[261], sec27[262], sec27[263], sec27[264]],
             [sec27[265], sec27[266], sec27[267], sec27[268], sec27[269]],
             [sec27[270], sec27[271], sec27[272], sec27[273], sec27[274]],
             [sec27[275], sec27[276], sec27[277], sec27[278], sec27[279]],
             [sec27[280], sec27[281], sec27[282], sec27[283], sec27[284]],
             [sec27[285], sec27[286], sec27[287], sec27[288], sec27[289]],
             [sec27[290], sec27[291], sec27[292], sec27[293], sec27[294]],
             [sec27[295], sec27[296], sec27[297], sec27[298], sec27[299]],
             [sec27[300], sec27[301], sec27[302], sec27[303], sec27[304]],
             [sec27[305], sec27[306], sec27[307], sec27[308], sec27[309]],
             [sec27[310], sec27[311], sec27[312], sec27[313], sec27[314]],
             [sec27[315], sec27[316], sec27[317], sec27[318], sec27[319]],
             ]
    ds327 = [["Nom del servei", "Categoria", "Ports TCP", "Ports UDP", "Protocol"],
             [sec27[320], sec27[321], sec27[322], sec27[323], sec27[324]],
             [sec27[325], sec27[326], sec27[327], sec27[328], sec27[329]],
             [sec27[330], sec27[331], sec27[332], sec27[333], sec27[334]],
             [sec27[335], sec27[336], sec27[337], sec27[338], sec27[339]],
             [sec27[340], sec27[341], sec27[342], sec27[343], sec27[344]],
             [sec27[345], sec27[346], sec27[347], sec27[348], sec27[349]],
             [sec27[350], sec27[351], sec27[352], sec27[353], sec27[354]],
             [sec27[355], sec27[356], sec27[357], sec27[358], sec27[359]],
             [sec27[360], sec27[361], sec27[362], sec27[363], sec27[364]],
             [sec27[365], sec27[366], sec27[367], sec27[368], sec27[369]],
             [sec27[370], sec27[371], sec27[372], sec27[373], sec27[374]],
             [sec27[375], sec27[376], sec27[377], sec27[378], sec27[379]],
             [sec27[380], sec27[381], sec27[382], sec27[383], sec27[384]],
             [sec27[385], sec27[386], sec27[387], sec27[388], sec27[389]],
             [sec27[390], sec27[391], sec27[392], sec27[393], sec27[394]],
             [sec27[395], sec27[396], sec27[397], sec27[398], sec27[399]],
             [sec27[400], sec27[401], sec27[402], sec27[403], sec27[404]],
             [sec27[405], sec27[406], sec27[407], sec27[408], sec27[409]],
             [sec27[410], sec27[411], sec27[412], sec27[413], sec27[414]],
             [sec27[415], sec27[416], sec27[417], sec27[418], sec27[419]],
             [sec27[420], sec27[421], sec27[422], sec27[423], sec27[424]],
             [sec27[425], sec27[426], sec27[427], sec27[428], sec27[429]],
             [sec27[430], sec27[431], sec27[432], sec27[433], sec27[434]]
             ]

    ds427 = [["Nom del servei", "Categoria", "Ports TCP", "Ports UDP", "Protocol"],
             [sec27[435], sec27[436], sec27[437], sec27[438], sec27[439]],
             [sec27[440], sec27[441], sec27[442], sec27[443], sec27[444]]
             ]

    add_confi_3(c, ds127)
    add_confi_4(c, ds227)
    add_confi_5(c, ds327, ds427)

    ##DATASEC 2.8, 2.9,2.10,2.11

    ds128 = [["Name", "External IP Address/Range", "External Service Port", "Mapped IP\nAddress/Range", "Map to Port"],
             [sec28[0], sec28[1], sec28[2], sec28[3], sec27[8]],
             [sec28[5], sec28[6], sec28[7], sec28[8], sec28[9]]
             ]

    ds129 = [["ID", "From", "To", "Source", "Destinatio", "Service", "Action", "AV", "Web Filter", "App Control", "IPS",
              "SSL INSPECT", "LOG", "NAT"],
             [sec29[0], sec29[1], sec29[2], sec29[3], sec29[4], sec29[5], sec29[6], sec29[7], sec29[8], sec29[9],
              sec29[10],
              sec29[11], sec29[12], sec29[13]],
             [sec29[14], sec29[15], sec29[16], sec29[17], sec29[18], sec29[19], sec29[20], sec29[21], sec29[22],
              sec29[23],
              sec29[24], sec29[25], sec29[26], sec29[27]],
             [sec29[28], sec29[29], sec29[30], sec29[31], sec29[32], sec29[33], sec29[34], sec29[35], sec29[36],
              sec29[37],
              sec29[38], sec29[39], sec29[40], sec29[41]],
             [sec29[42], sec29[43], sec29[44], sec29[45], sec29[46], sec29[47], sec29[48], sec29[49], sec29[50],
              sec29[51],
              sec29[52], sec29[53], sec29[54], sec29[55]],
             [sec29[56], sec29[57], sec29[58], sec29[59], sec29[60], sec29[61], sec29[62], sec29[63], sec29[64],
              sec29[65],
              sec29[66], sec29[67], sec29[68], sec29[69]],
             [sec29[70], sec29[71], sec29[72], sec29[73], sec29[74], sec29[75], sec29[76], sec29[77], sec29[78],
              sec29[79],
              sec29[80], sec29[81], sec29[82], sec29[83]],
             [sec29[84], sec29[85], sec29[86], sec29[87], sec29[88], sec29[89], sec29[90], sec29[91], sec29[92],
              sec29[93],
              sec29[94], sec29[95], sec29[96], sec29[97]],
             [sec29[98], sec29[99], sec29[100], sec29[101], sec29[102], sec29[103], sec29[104], sec29[105], sec29[106],
              sec29[107], sec29[108], sec29[109], sec29[110], sec29[111]],
             [sec29[112], sec29[113], sec29[114], sec29[115], sec29[116], sec29[117], sec29[118], sec29[119],
              sec29[120],
              sec29[121], sec29[122], sec29[123], sec29[124], sec29[125]],
             ["", "Any", "Any", "ALL", "ALL", "ALL", "DENY"]]

    add_confi_6(c, ds128, ds129, sec210[0], sec211[0])

    ##DATASEC 2.12, 2.13
    add_confi_7(c, sec212[0], sec213[0], sec213[1], sec213[2], sec213[3])

    c.save()


try:
    nfile = input('Please enter the config file you want to read: ')
    __init__(nfile)
    print("Succesfull file creation.")
except:
    print('Error file not found')



